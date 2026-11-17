---
name: redhat-appsec-hardening
description: Elite Red-Hat defensive application security auditing, threat modeling, and surgical vulnerability remediation. Audits entire architecture, function-to-function trust boundaries, IDOR/BOLA gaps, Server Action auth leaks, cryptographic webhook verifications, data exfiltration, rate limiting, and HTTP security headers. Produces an audit scorecard and applies surgical fixes.
user-invocable: true
argument-hint: "[target-path] or 'audit' or 'fix'"
license: MIT
---

# Red-Hat AppSec Hardening & Vulnerability Remediation

This skill transforms your coding agent into an elite defensive security engineer and penetration tester. It systematically threat-models the application, discovers subtle architectural and implementation vulnerabilities (including AI-generated security gaps), applies surgical zero-bloat fixes, and produces a production-ready security scorecard.

---

## 1. When to Use This Skill
- When preparing to deploy or ship a client application or production product.
- When the user asks: *"Audit security", "Audit entire codebase for flaws", "Find security gaps in APIs/webhooks", "Harden this application", "Is this safe to ship?"*.
- Before merging sensitive features (Auth, Payments, Multi-Tenant Workspaces, Webhooks, Data Ingestion).

---

## 2. Niche-Aware Threat Modeling (Stage 1)
Security cannot be one-size-fits-all. The agent must first identify the **product niche and active trust boundaries**:

| Application Niche | Primary Threat Vectors to Audit | Secondary Vectors |
| :--- | :--- | :--- |
| **SaaS / Multi-Tenant Portals** | **BOLA / IDOR** (Tenant A accessing Tenant B's data), Privilege Escalation, Broken Access Control | Session fixation, invite token leakage |
| **E-Commerce & Billing** | **Webhook Replay / Spoofing**, Price Tampering in Client Payloads, Race Conditions on Stock | Carding abuse, order ID enumeration |
| **Lead Generation & Public Forms** | **SSRF**, Email Header Injection, Unauthenticated Form Flooding, Spambots | Rate-limit exhaustion, CRM poison |
| **Internal Dashboards / Portals** | **Broken Authentication**, Over-Privileged API Keys, Stack Trace / Credential Leaks | CSRF, Stored XSS in admin fields |

---

## 3. The 7 Critical AppSec Vulnerability Audits (Stage 2)

### Audit 1: Broken Object-Level Authorization (BOLA / IDOR)
**The Vulnerability**: Querying data by a raw ID from request parameters without verifying tenant or user ownership.
```typescript
// ❌ VULNERABLE: Any logged-in user can change `id` in the URL to read another user's invoice
export async function GET(req: Request, { params }: { params: { id: string } }) {
  const invoice = await db.query.invoices.findFirst({ where: eq(invoices.id, params.id) });
  return Response.json(invoice);
}

// ✅ HARDENED: Always filter by the authenticated user's organization/ID
export async function GET(req: Request, { params }: { params: { id: string } }) {
  const session = await auth.getSession();
  if (!session) return new Response("Unauthorized", { status: 401 });

  const invoice = await db.query.invoices.findFirst({
    where: and(eq(invoices.id, params.id), eq(invoices.orgId, session.user.orgId)),
  });
  if (!invoice) return new Response("Not Found", { status: 404 });
  return Response.json(invoice);
}
```

### Audit 2: Next.js Server Action Auth Bypasses
**The Vulnerability**: Assuming a Server Action is private because it lives inside an authenticated page component. Server Actions generate public HTTP endpoints.
```typescript
// ❌ VULNERABLE: Callable by anyone with curl/POST, no session check inside the action
export async function deleteProjectAction(projectId: string) {
  "use server";
  await db.delete(projects).where(eq(projects.id, projectId));
}

// ✅ HARDENED: Explicit session validation & input schema validation inside the action
export async function deleteProjectAction(rawInput: unknown) {
  "use server";
  const session = await auth.getSession();
  if (!session?.user) throw new Error("Unauthorized");

  const { projectId } = z.object({ projectId: z.string().uuid() }).parse(rawInput);
  await db.delete(projects).where(and(eq(projects.id, projectId), eq(projects.ownerId, session.user.id)));
}
```

### Audit 3: Cryptographic Webhook Verification (HMAC)
**The Vulnerability**: Parsing webhook payloads as JSON directly without verifying signatures against the raw unparsed request buffer.
```typescript
// ❌ VULNERABLE: Attackers can forge POST /api/webhooks/stripe to unlock free subscriptions
export async function POST(req: Request) {
  const data = await req.json();
  if (data.type === "checkout.session.completed") { /* unlock */ }
}

// ✅ HARDENED: Cryptographic signature verification with raw body
export async function POST(req: Request) {
  const rawBody = await req.text();
  const signature = req.headers.get("stripe-signature") || "";
  let event;
  try {
    event = stripe.webhooks.constructEvent(rawBody, signature, process.env.STRIPE_WEBHOOK_SECRET!);
  } catch (err) {
    return new Response("Invalid Signature", { status: 400 });
  }
  // Process verified event...
}
```

### Audit 4: Data Exfiltration & Over-Fetching
**The Vulnerability**: Returning full database models (`SELECT *`) to frontend responses, leaking sensitive fields (password hashes, provider tokens, internal notes).
```typescript
// ❌ VULNERABLE: Leaks password_hash or internal tenant secrets in network tab
const user = await db.query.users.findFirst({ where: eq(users.id, id) });
return Response.json(user);

// ✅ HARDENED: Whitelisted explicit field projection
const user = await db.query.users.findFirst({
  where: eq(users.id, id),
  columns: { id: true, name: true, email: true, image: true },
});
return Response.json(user);
```

### Audit 5: Input Injection & Parameter Pollution
**The Vulnerability**: Trusting query parameters or POST bodies without runtime type and length boundaries.
- Every endpoint receiving input MUST parse through strict runtime schemas (Zod).
- String inputs must enforce maximum lengths (`z.string().max(255)`) to prevent ReDoS (Regular Expression Denial of Service) and buffer exhaustion.

### Audit 6: Rate Limiting on Abuse-Prone Endpoints
**The Vulnerability**: Unrestricted endpoints allowing credential stuffing, OTP brute-forcing, or email spamming.
- Enforce IP-based or session-based rate limits on: `/api/auth/*`, `/api/contact`, `/api/reset-password`, `/api/checkout`.

### Audit 7: HTTP Security Headers & Transport Hardening
**The Vulnerability**: Missing defensive HTTP headers, leaving apps exposed to clickjacking, MIME-sniffing, or insecure HTTP downgrades.
Ensure headers are configured in `next.config.js`, middleware, or reverse proxy:
```javascript
const securityHeaders = [
  { key: "X-Frame-Options", value: "DENY" },
  { key: "X-Content-Type-Options", value: "nosniff" },
  { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
  { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
];
```

---

## 4. The 5-Stage Execution Protocol (Stage 3 & 4)

When invoked, the agent MUST follow these steps sequentially:

1. **Step 1: Inventory Trust Boundaries**:
   - Grep for all API route handlers (`app/api/**/route.ts`, `pages/api/**/*.ts`).
   - Grep for all Server Actions (`"use server"`).
   - Grep for all Webhook handlers.
2. **Step 2: Threat Analysis**:
   - Check every route for missing auth, IDOR, raw un-validated inputs, and over-fetching.
3. **Step 3: Surgical Remediation (Shortest Working Diff)**:
   - Apply fixes directly at the boundary.
   - Do not refactor adjacent business logic.
4. **Step 4: Regressive Compilation**:
   - Run `craft-check` and compiler/linter checks to ensure 0 build errors.
5. **Step 5: Output the Security Scorecard**:
   - Present findings clearly with risk levels (Critical, High, Medium, Low).

---

## 5. Standard Security Scorecard Format

```markdown
==========================================================
          RED-HAT DEFENSIVE SECURITY SCORECARD
==========================================================
Overall Security Score: 98 / 100 [PRODUCTION READY]

[CRITICAL / HIGH FINDINGS]
- FIXED: BOLA/IDOR vulnerability in `/api/invoices/[id]/route.ts`. Added tenant ID filter.
- FIXED: Unprotected Server Action `updateUserRoleAction`. Added session verification.

[HARDENED BOUNDARIES VERIFIED]
✔ Auth & Session Verification: 100% of mutation handlers protected.
✔ Input Validation: All routes bound to runtime Zod schemas.
✔ Webhook Cryptography: Stripe & Resend signatures validated against raw body.
✔ Data Exfiltration: Explicit column projection enforced (0 password/token leaks).
✔ Security Headers: HSTS, X-Frame-Options (DENY), nosniff active.
✔ Rate Limiting: Active on all public auth/form endpoints.

VERDICT: APPROVED FOR PRODUCTION SHIPPING.
==========================================================
```
