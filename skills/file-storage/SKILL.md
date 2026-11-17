---
name: file-storage
description: Production-grade object storage integration using Cloudflare R2 (or AWS S3). Covers S3-compatible client setup, presigned upload URLs (direct client-to-storage without proxying through backend), MIME type validation, file size limits, public CDN delivery, and secure deletion.
---

# Cloudflare R2 & S3-Compatible File Storage Skill

This skill governs zero-egress, high-performance object storage for user uploads (avatars, documents, invoices, media).

---

## 1. Core Architectural Invariant: Presigned Direct Uploads

**NEVER proxy multi-megabyte file uploads through your Next.js / serverless backend.**
- Proxying file bytes through serverless functions triggers payload size limits (Vercel has a 4.5MB server action limit) and wastes server compute.
- **The Pattern**:
  1. Frontend asks backend for a secure presigned upload URL: `POST /api/storage/upload-url` with `{ filename, contentType, size }`.
  2. Backend validates auth, user permissions, MIME whitelist, and file size.
  3. Backend generates a 60-second S3 `PutObjectCommand` presigned URL via `@aws-sdk/s3-request-presigner`.
  4. Frontend uploads directly to Cloudflare R2 via `PUT <presigned-url>` with a progress bar.
  5. Frontend saves the resulting public/private asset key to the database.

---

## 2. Dependencies
Install the standard AWS S3 SDK (works seamlessly with Cloudflare R2):
```bash
npm install @aws-sdk/client-s3 @aws-sdk/s3-request-presigner
```

---

## 3. Environment Configuration
Store in `.env.local` / `.env`:
```env
# Cloudflare R2 Credentials
R2_ACCOUNT_ID="your_cloudflare_account_id"
R2_ACCESS_KEY_ID="your_r2_access_key_id"
R2_SECRET_ACCESS_KEY="your_r2_secret_access_key"
R2_BUCKET_NAME="client-assets"
R2_PUBLIC_DOMAIN="https://assets.yourdomain.com" # Or Cloudflare r2.dev domain
```

---

## 4. S3 / R2 Client Setup (`lib/storage.ts`)

```typescript
import { S3Client, PutObjectCommand, DeleteObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

export const s3Client = new S3Client({
  region: "auto",
  endpoint: `https://${process.env.R2_ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID!,
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY!,
  },
});

const ALLOWED_MIME_TYPES = new Set([
  "image/jpeg",
  "image/png",
  "image/webp",
  "image/gif",
  "application/pdf",
  "text/csv",
]);

const MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024; // 10 MB default limit

export async function createPresignedUploadUrl({
  filename,
  contentType,
  sizeBytes,
  userId,
}: {
  filename: string;
  contentType: string;
  sizeBytes: number;
  userId: string;
}) {
  if (!ALLOWED_MIME_TYPES.has(contentType)) {
    throw new Error(`Unsupported file type: ${contentType}`);
  }

  if (sizeBytes > MAX_FILE_SIZE_BYTES) {
    throw new Error(`File size exceeds 10MB limit`);
  }

  // Sanitize filename & create unique key with path isolation
  const extension = filename.split(".").pop()?.toLowerCase() || "bin";
  const uniqueKey = `users/${userId}/${crypto.randomUUID()}.${extension}`;

  const command = new PutObjectCommand({
    Bucket: process.env.R2_BUCKET_NAME!,
    Key: uniqueKey,
    ContentType: contentType,
  });

  const uploadUrl = await getSignedUrl(s3Client, command, { expiresIn: 60 });

  return {
    uploadUrl,
    key: uniqueKey,
    publicUrl: `${process.env.R2_PUBLIC_DOMAIN}/${uniqueKey}`,
  };
}

export async function deleteStoredFile(key: string) {
  const command = new DeleteObjectCommand({
    Bucket: process.env.R2_BUCKET_NAME!,
    Key: key,
  });
  return s3Client.send(command);
}
```

---

## 5. Security & Isolation Rules
1. **Never Make Buckets Publicly Writable**: Bucket policies must only allow public read (if hosting public images) or strict presigned access.
2. **User Path Isolation**: Always prefix storage keys with the authenticated tenant or user ID (`tenants/<tenantId>/avatars/...`). Never let user A overwrite user B's filename.
3. **MIME Verification**: Validate content-type headers on both the presigned signature generation and frontend file picker.
