---
name: redhat-appsec-hardening
description: Elite Red-Hat defensive application security auditing, multi-agent offensive exploitation, threat modeling, and surgical vulnerability remediation. Combines white-box source analysis, autonomous dynamic red-team exploitation (Strix/HTTP simulation), IDOR/BOLA verification, Server Action hardening, cryptographic webhook validation, and zero-downtime surgical patching.
user-invocable: true
argument-hint: "[target-path] or 'audit' or 'red-team' or 'harden'"
license: MIT
---

# Red-Hat AppSec Hardening & Multi-Agent Exploitation Engine

This skill transforms your AI agent into an elite Red-Hat Application Security Engineer and Penetration Tester (Google Information Security / Microsoft MSRC bar). It combines deep **white-box architecture review**, **autonomous multi-subagent offensive exploitation**, and **surgical zero-bloat remediation** to ship impenetrable client applications.

---

## 1. When to Use This Skill
- When user asks: *"Audit security", "Pentest this application", "Find vulnerabilities in codebase/APIs", "Deploy security swarm", "Harden this project", "Is this ready to ship?"*.
- Before shipping any production application or client deliverable.
- Whenever authentication, payments, multi-tenancy, webhooks, or file uploads are implemented.

---

## 2. Niche-Aware Threat Modeling Matrix (Automated Detection)

The agent automatically inspects project dependencies, schemas, and routes to determine the threat surface:

| Product Niche | Primary Threat Surface | Attack Vectors Tested |
| :--- | :--- | :--- |
| **B2B SaaS / Multi-Tenant** | Tenant Boundaries, Workspace RBAC | **BOLA / IDOR**, Privilege Escalation, Cross-tenant data leaks |
| **FinTech & E-Commerce** | Checkout, Subscriptions, Webhooks | **Webhook Forgery**, Client price tampering, Race conditions, Refund fraud |
| **AI Agents & LLM Apps** | Tool calling, Prompts, Embeddings | **Prompt Injection**, SSRF via agent fetch tools, Insecure tool output |
| **Healthcare / HIPAA / PII** | Patient data, Forms, Audit logs | **Data Exfiltration**, Unencrypted storage, URL token leakage |
| **Public Marketplaces / Lead Gen**| Contact forms, Listings, Uploads | **SSRF**, File upload malware, ReDoS, Spam flooding, Stored XSS |

---

## 3. The 12 Comprehensive Enterprise Security Audits

### Domain 1: Broken Object-Level Authorization (BOLA / IDOR)
- **Check**: Every query by an entity ID (`id`, `orderId`, `docId`) MUST enforce tenant/user ownership in the `WHERE` clause.
- **Pattern**: `where: and(eq(table.id, id), eq(table.tenantId, session.tenantId))`

### Domain 2: Next.js Server Action & RPC Public Exposure
- **Check**: Server Actions are public HTTP POST endpoints. Every action MUST execute `const session = await auth.getSession(); if (!session) throw new Error("Unauthorized");` on line 1.

### Domain 3: Cryptographic Webhook HMAC Signatures
- **Check**: Stripe, Resend, Twilio, and GitHub webhooks MUST verify signatures using the **raw unparsed request text**, NEVER parsed JSON.

### Domain 4: Data Exfiltration & Over-Fetching
- **Check**: Forbid `SELECT *` on user/tenant tables. Enforce explicit column projection (whitelist only `id`, `name`, `email`; never return `password_hash`, `stripeCustomerId`, or auth tokens to client).

### Domain 5: Strict Runtime Schema Validation (Zod)
- **Check**: Every route handler, server action, and webhook MUST parse inputs through strict Zod schemas with maximum string lengths to prevent ReDoS and memory exhaustion.

### Domain 6: SSRF (Server-Side Request Forgery) Defense
- **Check**: Any backend `fetch()` or webhook dispatcher taking user-supplied URLs must block internal IPs (`127.0.0.1`, `localhost`, `169.254.169.254` cloud metadata).

### Domain 7: Rate Limiting & Abuse Prevention
- **Check**: Public auth routes (`/api/auth/*`), contact forms, and reset-password routes MUST enforce sliding-window IP/user rate limiting (e.g. 5 attempts/minute).

### Domain 8: HTTP Defense-in-Depth Headers
- **Check**: Configure strict headers in reverse proxy or `next.config.js`:
  - `X-Frame-Options: DENY` (Anti-Clickjacking)
  - `X-Content-Type-Options: nosniff` (Anti-MIME sniffing)
  - `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Permissions-Policy: camera=(), microphone=(), geolocation=()`

### Domain 9: Secrets, Keys & Token Hygiene
- **Check**: Scan codebase for hardcoded `sk_live_`, `ghp_`, private keys, or exposed `.env` variables in client-side bundles (`NEXT_PUBLIC_` misuse).

### Domain 10: Supply Chain & Dependency CVEs
- **Check**: Audit `package.json` / `requirements.txt` for known high/critical CVEs and unpinned risky dependencies.

### Domain 11: CORS & Origin Validation
- **Check**: Forbid `Access-Control-Allow-Origin: *` when credentials are supported. Origin must match trusted tenant domains.

### Domain 12: Race Conditions & State-Mutation Concurrency
- **Check**: Balance updates, inventory decrements, and coupon claims MUST use atomic database transactions (`tx.update(...).where(...)`) with locking, not client-driven increments.

---

## 4. Multi-Agent Red-Team Orchestration Swarm

Upon user request or approval, the coordinator agent launches **3 specialized autonomous subagents**:

```
                       [COORDINATOR AGENT]
                 Identifies Niche & Threat Model
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
  [SUBAGENT 1]            [SUBAGENT 2]            [SUBAGENT 3]
  Static White-Box        Offensive Red-Team      Surgical Blue-Team
  Auditor (AST & Code)    Attacker (PoC Exploit)  Patcher (Ponytail Diff)
```

1. **Subagent 1 (White-Box Code Auditor)**:
   - Greps every API endpoint, Server Action, and database query.
   - Traces data flow from request parameters to SQL/ORM execution.
   - Compiles list of suspected trust-boundary gaps.

2. **Subagent 2 (Offensive Red-Team Attacker)**:
   - Runs simulated exploit payloads against target endpoints (tampering tenant IDs, crafting unauthenticated POSTs, injecting boundary test strings).
   - Confirms true positives: produces a verified Proof-of-Concept (PoC) for every confirmed hole. Discards false alarms.

3. **Subagent 3 (Surgical Blue-Team Remediation Specialist)**:
   - Takes verified PoCs from Subagent 2.
   - Applies the **shortest working diff** (Ponytail invariant) to patch each hole.
   - Re-runs tests and `craft-check` to prove zero functional regressions.

---

## 5. Standard Enterprise Security Scorecard

```markdown
==========================================================
        RED-HAT DEFENSIVE APPSEC SCORECARD
==========================================================
Overall Security Score: 98 / 100 [ENTERPRISE SHIP-READY]

[EXPLOIT PROOFS & SURGICAL PATCHES]
- IDOR (Critical): Tenant B could read Tenant A invoices via `/api/invoices/[id]`.
  -> PATCH: Injected `and(eq(invoices.id, id), eq(invoices.orgId, session.user.orgId))`.
- AUTH LEAK (High): Server Action `promoteAdmin` callable unauthenticated.
  -> PATCH: Added session role validation gate at entry.
- WEBHOOK (Critical): Stripe webhook parsed unverified JSON.
  -> PATCH: Wired `stripe.webhooks.constructEvent` with raw request buffer.

[VERIFIED ENTERPRISE DOMAINS]
✔ 1. Multi-Tenant IDOR: 100% of queries filtered by tenant boundary.
✔ 2. Server Action Auth: Zero publicly callable mutation holes.
✔ 3. Webhook Cryptography: Raw body HMAC verification enforced.
✔ 4. Data Over-Fetching: Explicit column whitelisting active.
✔ 5. Runtime Schemas: Zod parsing on 100% of incoming payloads.
✔ 6. SSRF Protection: Private/metadata IP ranges blocked.
✔ 7. Rate Limiting: Sliding-window active on auth & forms.
✔ 8. Transport Headers: HSTS, DENY, nosniff active.
✔ 9. Secret Hygiene: 0 hardcoded keys detected.
✔ 10. Dependency Health: 0 critical/high CVEs.
✔ 11. CORS Boundary: Wildcards eliminated.
✔ 12. Concurrency Safety: Atomic DB transactions on mutations.

VERDICT: APPROVED FOR PRODUCTION SHIPPING.
==========================================================
```
