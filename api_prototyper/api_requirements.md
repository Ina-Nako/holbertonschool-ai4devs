# API Requirements – iCan (Inclusive Audiobook Platform API)

## Domain Overview
iCan is an inclusive audiobook platform for blind users, people with dyslexia, and busy learners. It provides audiobook discovery, playback (human-narrated and AI-generated/TTS), “Quick Listen” summaries, offline downloads, cross-device sync, and in-player bookmarking and voice notes. It also supports creator uploads, moderation, and subscription/purchase entitlements.

## Target Users
- **Client app developers (Web/iOS/Android)**: build discovery, player, library, offline, and accessibility-first experiences.
- **End users (listeners)**: browse, play, download, and track progress across devices.
- **Authors/Creators**: upload and manage audiobook content, metadata, and view engagement/royalty analytics.
- **Admins/Moderators**: review submissions, handle moderation queues, and manage users/content.
- **Analysts/Operators**: monitor platform KPIs, usage, and operational health.

## Core Operations (12)
1. **Sign up / Sign in / Token refresh**: create accounts (email/social), authenticate, and issue/refresh access tokens.
2. **Browse catalog & search**: list categories, search by title/author/topic, and filter by language/duration/format.
3. **Get audiobook details**: retrieve metadata (synopsis, narrator/voice options), availability, and accessibility flags.
4. **Get streaming entitlement / DRM license**: verify purchase/subscription and issue a time-limited playback license or signed URL.
5. **Playback progress sync**: create/update “continue listening” position per device and sync across devices.
6. **Playback settings**: store per-user settings (speed, pitch, voice type) and retrieve defaults on new devices.
7. **Bookmarks & voice notes**: create/list/update/delete bookmarks and voice notes tied to a timestamp in the audio.
8. **Offline downloads**: request download authorization, list active downloads, and revoke downloads when entitlements expire.
9. **Quick Listen summaries**: request a summary audio/version and retrieve summary metadata (estimated listen time).
10. **Recommendations**: retrieve personalized recommendations based on listening history and preferences.
11. **Subscription & purchases**: list plans, manage subscription state, and check entitlements (payment processing via PCI-compliant provider).
12. **Creator workflow + moderation**: creators create titles, upload audio assets/chapters, submit for review; admins approve/reject and publish/unpublish.

## Data Validation Rules
### Accounts & Identity
- **Email format**: must be valid RFC-like email syntax; must be unique per account.
- **Password policy** (if password auth is used): minimum length 10, must not be in common-password denylist.
- **Age/consent**: if applicable, require user consent flags for GDPR/terms before enabling playback.

### Catalog & Content Metadata
- **Title constraints**: title length 1–200 characters; synopsis length 0–5000 characters.
- **Language codes**: use ISO 639-1/639-3 codes; reject unknown codes.
- **Duration**: must be a positive integer in seconds; chapter durations must sum (within tolerance) to total duration.
- **Identifiers**: if ISBN/ASIN is provided, it must match expected format; a given identifier must be unique per edition.

### Audio Assets & Uploads
- **Allowed formats**: accept only approved audio formats (e.g., AAC/MP3/M4B/WAV as configured) and reject executable/content-mismatched files.
- **File size limits**: enforce per-file and per-title limits; large uploads must use multipart/resumable uploads.
- **Virus/malware scan required**: uploaded assets must pass scanning before review/publish.

### Playback, Progress, and Notes
- **Progress bounds**: position must be between 0 and (duration + tolerance); never negative.
- **Monotonic updates**: progress updates should not move backwards unless explicitly flagged as a user seek event.
- **Playback speed**: must be between 0.5× and 3.0×.
- **Pitch**: must be within a safe configured range (e.g., -12 to +12 semitones or equivalent unit).
- **Bookmarks**: timestamp must be within track duration; optional label 0–120 characters.
- **Voice notes**: transcription text (if stored) 0–2000 characters; audio note length cap (e.g., 2 minutes).

### Entitlements, Downloads, and DRM
- **Entitlement required**: download/DRM license endpoints must verify an active entitlement (purchase, subscription, or free-tier access).
- **License TTL**: issued licenses must have a maximum TTL (e.g., 15 minutes) and be non-reusable outside allowed device limits.
- **Device limits**: offline downloads limited per user/plan (e.g., N devices); reject when limit exceeded.

### Moderation & Publishing
- **Status transitions**: creator content state must follow valid transitions (e.g., `draft -> submitted -> approved -> published` or `submitted -> rejected`).
- **Admin-only actions**: only admins can approve/reject/publish/unpublish.

## Non-Functional Requirements
### Performance & Latency
- **Catalog read endpoints** (browse/search/details): p95 < 200ms.
- **Progress sync endpoints**: p95 < 150ms.
- **DRM/license endpoints**: p95 < 300ms.
- **Upload and export/analytics**: asynchronous jobs for large payloads; return job ids and allow polling.

### Authentication & Authorization
- **Authentication**: OAuth2/OIDC with JWT access tokens; refresh tokens for mobile/web.
- **Authorization**: RBAC with roles such as `listener`, `creator`, `admin`.
- **Least privilege**: scopes per endpoint (e.g., `library:read`, `playback:write`, `creator:upload`, `admin:moderate`).

### Rate Limiting
- **Per-user limits**: default 120 requests/minute/user with burst up to 240.
- **Search limits**: tighter limits to prevent scraping (e.g., 30 requests/minute/user).
- **DRM/license limits**: very tight limits (e.g., 10 requests/minute/user/device) with anomaly detection.
- **429 responses**: include `Retry-After` and a stable error schema.

### Reliability & Availability
- **Uptime SLA**: 99.9% monthly.
- **Scale**: support up to 500K concurrent users.
- **Idempotency**: idempotency keys for create operations (bookmarks, notes, purchases webhooks ingestion, creator submissions).
- **Pagination**: cursor-based pagination for all list endpoints.

### Security, Privacy, and Compliance
- **Transport security**: HTTPS required; HSTS enabled.
- **Encryption**: encrypt PII and sensitive tokens at rest; rotate keys.
- **GDPR**: support data export and deletion requests; minimize stored personal data.
- **Accessibility**: platform must meet WCAG 2.1 AA for user-facing surfaces; API must expose needed accessibility metadata.
- **DRM**: protect audiobook content with signed URLs/licenses and enforce entitlements.
- **Payments**: PCI-DSS compliant payment processing via a certified provider; store only tokenized payment references.

### Observability
- **Logs + tracing**: request id correlation; trace playback license issuance and upload workflows.
- **Metrics**: search latency, license issuance rate, progress sync lag, moderation queue time.

### Compatibility & API Hygiene
- **Versioning**: version all endpoints (e.g., `/v1/...`).
- **Consistent errors**: standardized error format with machine-readable codes.
