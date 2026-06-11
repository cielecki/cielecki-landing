# cielecki.com Homepage Redesign: HNWI AI Coaching

## Context

Maciej wants to offer AI coaching for high-net-worth individuals (post-exit founders, executives with established wealth). The current cielecki.com is a personal brand portfolio site. We're restructuring the homepage so coaching is the hero offering and the personal brand (10Clouds, AIConsole, blog) serves as credibility proof.

**Key decisions**: English-first, psychology-led positioning ("You built it. You sold it. Now what?"), transparent pricing (2500 zł/h), case studies framed as "systems I built for myself", Cal.com for booking with Stripe payments.

---

## Files to Modify

| File | Action |
|------|--------|
| `cielecki-landing-astro/src/pages/index.astro` | REWRITE — all sections |
| `cielecki-landing-astro/src/layouts/BaseLayout.astro` | UPDATE — meta title/description |
| `cielecki-landing-astro/src/styles/main.css` | MINOR — add featured pricing card style |

No new dependencies. No changes to `tailwind.config.mjs`, blog, or images.

---

## New Section Structure (top to bottom)

### Nav (MODIFY)
- Links: Coaching, Process, Proof, Writing, Book a Call (button)
- "MC" logo stays
- CTA button links to Google Calendar booking URL

### 1. Hero (REWRITE)
- Badge: "AI Coaching for Founders"
- Headline: **"You built it. You sold it. Now what?"** — "Now what?" in italic terracotta with hand-underline
- Subheadline: 1-2 sentences positioning the service (psychology + AI tools)
- Primary CTA: "Book a Discovery Call" → Google Calendar
- Secondary CTA: "See How It Works" → `#process`
- Portrait stays (right column)

### 2. Problem Agitation (NEW)
- 3 `.glass` cards in `md:grid-cols-3`:
  1. **"The Paradox of Success"** — motivation void after achieving everything
  2. **"Information Overload, Zero Clarity"** — too many options, no signal
  3. **"AI Hype vs. AI Reality"** — nobody shows how AI changes YOUR life
- Reuse existing card pattern from About trait cards

### 3. Solution / What I Do (NEW)
- 2-column layout (text left, photo right)
- Direct Maciej-voice copy: "I sit with you, understand what's actually going on, and we build systems together."
- Not a program, not a course — 1-on-1, built for your life

### 4. Process (NEW, id="process")
- 3 numbered steps with icons:
  1. **Discovery Call** (free, 30 min) — "You talk, I listen"
  2. **Strategic Sessions** (2500 zł/h) — deep work, mapping, building
  3. **Custom Tools** (case by case) — bespoke AI systems

### 5. Pricing (NEW, id="pricing")
- 3 `.glass` cards side by side:
  - Discovery Call: Free | 30 min | "Book Now"
  - Strategic Session: 2,500 zł/h | Deep 1-on-1 | "Book Now" (featured card, terracotta accent)
  - Custom Tools: Case by case | Built for your life | "Let's Talk"

### 6. Case Studies (NEW)
- Header: "Systems I Built for Myself"
- Bento grid (reuse Work section pattern):
  - Net Worth Optimizer
  - Gamified Finances
  - AI Strategy Research
  - Multi-Person Workflow
- Authentic framing, no fake clients

### 7. Credibility / Proof (REWRITE, id="proof")
- Stats bar: 15+ years, 150+ team, 80hrs/week AI
- Quote: "I see a world where individuals have the same computational power as corporations"
- Compact grid: 10Clouds (with photo), AIConsole (with GitHub link), LinkedIn
- Life Navigator: REMOVED

### 8. Writing / Blog (KEEP, id="writing")
- Same as current, just renumber to `08`

### 9. Final CTA (REWRITE of Contact)
- Large headline: "Ready to Build Your Next Chapter?"
- Big "Book a Discovery Call" button
- Secondary: LinkedIn, X, email links (de-emphasized)
- Avatar + background image treatment

### Footer (MODIFY)
- New tagline: "AI Coaching for Founders & Executives"
- Social links stay

---

## Booking & Payments — Cal.com + Stripe

**Tool**: Cal.com (free plan) with Stripe integration for paid sessions.

**Setup steps** (before or after page build):
1. Create Cal.com account at cal.com
2. Connect Stripe account in Cal.com settings
3. Create two event types:
   - **Discovery Call** — free, 30 min, no payment required
   - **Strategic Session** — 2500 PLN prepaid via Stripe, 60 min
4. Get shareable booking URLs for each event type

**On the page**: Two separate CTAs link to different Cal.com event types:
- "Book a Discovery Call" → Cal.com free event link
- "Book a Strategic Session" → Cal.com paid event link (Stripe checkout inline)

```typescript
// index.astro frontmatter
const DISCOVERY_URL = 'https://cal.com/maciej-cielecki/discovery'; // placeholder
const SESSION_URL = 'https://cal.com/maciej-cielecki/strategic-session'; // placeholder
```

---

## CTA Placement (4 locations)

1. **Hero** — "Book a Discovery Call" → `DISCOVERY_URL`
2. **Process section** — Step 1 links to discovery, Step 2 links to strategic session
3. **Pricing cards** — Discovery "Book Now" → `DISCOVERY_URL`, Strategic Session "Book Now" → `SESSION_URL`, Custom Tools "Let's Talk" → mailto
4. **Final CTA** — "Book a Discovery Call" → `DISCOVERY_URL`

---

## Technical Notes

- All new sections reuse existing Tailwind utilities: `.glass`, `.reveal`, `.hand-underline`, `.blob`
- Existing color palette (cream/terracotta/sage/charcoal) + fonts (Newsreader/Space Grotesk) unchanged
- One new CSS class: `.pricing-featured` — terracotta border/glow for the middle pricing card
- Update `<title>` to: "Maciej Cielecki — AI Coaching for Founders & Executives"
- Update `<meta name="description">` to reflect coaching positioning
- Mobile: all sections use established responsive patterns (single col → grid)
- Zero new JS, zero new dependencies
- Cal.com URLs stored as frontmatter constants — easy to swap once accounts are set up

---

## Verification

1. `cd cielecki-landing-astro && npm run dev` — check localhost:4321
2. Visual check all sections render correctly on desktop and mobile
3. Verify all booking CTAs link to correct placeholder URLs
4. Verify blog section still loads posts
5. Verify no broken images (Life Navigator image removed, others kept)
6. `npm run build` — ensure clean static build
7. Check meta title/description in page source
8. After Cal.com setup: test full flow — click CTA → Cal.com booking → Stripe payment → confirmation
