---
name: resend-email
description: Production transactional email delivery using Resend and React Email. Covers API key setup, domain DNS verification (DKIM/SPF), responsive email templates coded in React/Tailwind, dynamic data hydration, deliverability best practices, and webhook bounce handling.
---

# Transactional Email with Resend & React Email

This skill governs transactional email delivery (auth verification, password resets, client invoices, alerts) with modern React components.

---

## 1. Why Resend + React Email Wins for Freelance
- **Zero Raw HTML/Tables Headaches**: Code emails like regular modern React components with `@react-email/components` and Tailwind CSS.
- **Generous Free Tier**: **3,000 emails/month free** (100 emails/day), with instant pay-as-you-go scaling when clients grow.
- **Top-Tier Deliverability**: Built-in automated DKIM, SPF, and DMARC verification via Cloudflare/custom DNS.

---

## 2. Dependencies
```bash
npm install resend @react-email/components
```

---

## 3. Environment Configuration
Store in `.env.local` / `.env`:
```env
RESEND_API_KEY="re_123456789_abcdefg"
EMAIL_FROM="Your App <notifications@yourdomain.com>"
```

---

## 4. Email Client Wrapper (`lib/email.ts`)

```typescript
import { Resend } from "resend";
import * as React from "react";

export const resend = new Resend(process.env.RESEND_API_KEY);

interface SendEmailParams {
  to: string | string[];
  subject: string;
  react: React.ReactElement;
  replyTo?: string;
}

export async function sendTransactionalEmail({
  to,
  subject,
  react,
  replyTo,
}: SendEmailParams) {
  try {
    const { data, error } = await resend.emails.send({
      from: process.env.EMAIL_FROM || "onboarding@resend.dev",
      to,
      subject,
      react,
      replyTo,
    });

    if (error) {
      console.error("[Email Error]:", error);
      throw new Error(`Failed to send email: ${error.message}`);
    }

    return data;
  } catch (err: any) {
    console.error("[Email Send Exception]:", err);
    throw err;
  }
}
```

---

## 5. Reusable React Email Template (`emails/VerifyEmail.tsx`)

```tsx
import {
  Html,
  Head,
  Body,
  Container,
  Section,
  Text,
  Button,
  Heading,
  Tailwind,
} from "@react-email/components";
import * as React from "react";

interface VerifyEmailProps {
  userName: string;
  actionUrl: string;
  appName?: string;
}

export function VerifyEmail({
  userName,
  actionUrl,
  appName = "Antigravity App",
}: VerifyEmailProps) {
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-neutral-50 font-sans text-neutral-800">
          <Container className="mx-auto my-10 max-w-lg rounded-xl border border-neutral-200 bg-white p-8 shadow-sm">
            <Heading className="mb-4 text-xl font-bold text-neutral-900">
              Confirm your email address
            </Heading>
            <Text className="mb-6 text-sm leading-relaxed text-neutral-600">
              Hi {userName}, welcome to {appName}. Please click the button below
              to verify your email and activate your account.
            </Text>
            <Section className="my-6 text-center">
              <Button
                className="rounded-lg bg-neutral-950 px-6 py-3 text-sm font-semibold text-white no-underline hover:bg-neutral-800"
                href={actionUrl}
              >
                Verify Email Address
              </Button>
            </Section>
            <Text className="text-xs text-neutral-400">
              If you didn't create an account, you can safely ignore this email.
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
}
```

---

## 6. Deliverability & Production Rules
1. **Never Send from Generic Gmail**: Always configure a custom client domain (e.g., `notifications@clientbrand.com`). Resend provides 3 DNS records (DKIM, SPF, MX) to paste into Cloudflare/Route53.
2. **Never Put Passwords or Sensitive Tokens in Subject Lines**.
3. **Set Expiration on Auth Links**: Verification/reset links sent via email must expire within 15–30 minutes.
