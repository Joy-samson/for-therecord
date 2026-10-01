---
name: Private Archival Pressing
colors:
  surface: '#fff8f4'
  surface-dim: '#dfd9d5'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f2ee'
  surface-container: '#f3ede9'
  surface-container-high: '#ede7e3'
  surface-container-highest: '#e8e1dd'
  on-surface: '#1d1b19'
  on-surface-variant: '#524343'
  inverse-surface: '#33302e'
  inverse-on-surface: '#f6efec'
  outline: '#857373'
  outline-variant: '#d7c1c2'
  surface-tint: '#8c4c50'
  primary: '#552026'
  on-primary: '#ffffff'
  primary-container: '#71363b'
  on-primary-container: '#f2a1a6'
  inverse-primary: '#ffb2b6'
  secondary: '#715b2f'
  on-secondary: '#ffffff'
  secondary-container: '#fbdca4'
  on-secondary-container: '#765f33'
  tertiary: '#502429'
  on-tertiary: '#ffffff'
  tertiary-container: '#6b3a3f'
  on-tertiary-container: '#e9a6ab'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdadb'
  primary-fixed-dim: '#ffb2b6'
  on-primary-fixed: '#390a11'
  on-primary-fixed-variant: '#6f353a'
  secondary-fixed: '#fedea7'
  secondary-fixed-dim: '#e0c38d'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#58441a'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#f9b5ba'
  on-tertiary-fixed: '#350e14'
  on-tertiary-fixed-variant: '#69383d'
  background: '#fff8f4'
  on-background: '#1d1b19'
  surface-variant: '#e8e1dd'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '500'
    lineHeight: 44px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 26px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: DM Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: DM Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: DM Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: DM Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.08em
  label-sm:
    fontFamily: DM Sans
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.14em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  margin: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system expresses an intimate, tactile, and editorial gift experience structured around the physical metaphor of a custom vinyl pressing, liner notes, and private memory archiving. The emotional tone is deliberate, warm, quiet, and profoundly personal—evoking the weight of tangible artifacts, faded print ephemera, hand-stamped cardstock, and preserved audio masters.

Drawing heavily from modern tactile skeuomorphism and literary editorial design, the interface eschews the sterile gloss of contemporary software in favor of paper grain, gentle deckled edges, physical micro-details (brass rivets, archival tape, label notches), and deliberate typography. It prioritizes emotional resonance and unhurried pacing over aggressive utility, functioning as an enduring bespoke keepsake.

## Colors

The palette is anchored in archival paper goods, letterpress inks, oxidised metal, and cured phonograph vinyl:

- **Primary (`#71363B`) & Deep Burgundy (`#54272C`):** Used for focal interactive states, primary actions, heavy editorial typographic headers, and sleeve accents.
- **Secondary / Muted Gold Brass (`#A58B5A`):** Applied to archival catalog indices, stamped badges, physical fastener metaphors, audio playback scrub heads, and subtle metallic rules.
- **Tertiary / Faded Burgundy (`#8A4A4E`):** Reserved for secondary buttons, quiet tags, and subdued hover/active variations.
- **Neutral / Deep Ink (`#171513`) & Dark Brown (`#35271F`):** Provides deep, warm contrast for body text, vinyl record grooves, outer jackets, and foundational dark backdrops.
- **Surfaces (Warm Paper `#F1E7D3` & Aged Paper `#E4D4B8`):** Supply canvas warmth and physical depth. Background layers sit on Aged Paper, while individual interactive cards, slips, and liner sheets layer forward in Warm Paper.

## Typography

The type system creates an archival editorial hierarchy by juxtaposing literary presence with catalog precision:

- **Playfair Display:** Drives headlines, track titles, chapter markers, and reflective quotes. Its high stroke contrast and traditional serifs ground the project in physical publishing.
- **DM Sans:** Acts as the clean, modern archival workhorse. It ensures track descriptions, timestamps, technical audio specs, and liner notes remain effortlessly legible at all scales.
- **Archival Metadata Treatment:** Use `label-sm` in all caps with wide tracking (`0.14em`) for stamps like `RZ-000`, `SIDE A`, `33⅓ RPM`, and `MASTER TAPE`.
- **Handwritten Accents:** For occasional marginalia, dates, and personal annotations, apply an organic handwriting script (such as Caveat or Kalam) sparingly at modest scale, angled slightly ($-1.5^\circ$ to $2^\circ$) across card margins and photographic tape overlays.

## Layout & Spacing

The layout is built around a centralized fixed-column spine that expands organically on wider monitors to simulate an open gatefold vinyl sleeve and accompanying booklet:

- **Grid Architecture:** Desktop views utilize a symmetrical 12-column layout (max width 1120px) flanked by wide paper borders. Tablet transitions to an 8-column layout, and mobile consolidates into a 4-column flow with tight 16px margins to retain intimate, book-like pacing.
- **Vertical Rhythm:** Generous vertical intervals (`space-xl` and above) simulate the spacing of custom letterpress printing, discouraging compressed visual clutter.
- **Gatefold Viewports:** Side-by-side elements on desktop (e.g., vinyl jacket on the left, tracklist and lyric slips on the right) collapse to a stacked, sequential tactile feed on mobile screens.

## Elevation & Depth

Depth in this system represents physical sheets resting on one another rather than arbitrary mathematical z-index planes:

- **Paper Stack Shadows:** Multiple paper layers use low-opacity, warm-tinted ambient shadows (`rgba(53, 39, 31, 0.08)` to `rgba(23, 21, 19, 0.16)`) combined with tight contact borders (`0 1px 2px rgba(23, 21, 19, 0.08)`) to suggest heavy 300gsm cotton stock.
- **Sleeve Inset & Vinyl Recess:** Grooves and internal sleeve pockets employ inner shadows (`inset 0 2px 4px rgba(23, 21, 19, 0.25)`) and dark ring gradients simulating pressed PVC lacquer.
- **Fasteners & Tape:** Washi-tape and photo-corner treatments cast delicate micro-shadows (`0 1px 3px rgba(0, 0, 0, 0.12)`) on top of photo prints, grounding them firmly to the paper substrate.

## Shapes

The interface embraces the crisp geometry of physical paper stationery:

- **Soft Base Curvature:** Buttons, paper cards, and polaroid panels use minimal softening (`0.25rem`) to maintain the feel of die-cut cardstock rather than synthetic modern UI pills.
- **Vinyl & Eyelet Circularity:** Complete circles (`border-radius: 9999px`) are reserved exclusively for vinyl discs, center paper runout labels, brass rivets, and audio playback transport toggles.
- **Deckled Accents:** Occasional bottom edges on hero slips use micro-perforations or subtle organic cut masks to evoke torn letterhead paper.

## Components

### Buttons
- **Primary:** Solid Burgundy (`#71363B`) background, Aged Paper (`#E4D4B8`) text, `roundedness: 1`, padded with `space-sm` vertical and `space-lg` horizontal. On hover, transitions subtly to Deep Burgundy (`#54272C`) with a microscopic press translation (`translateY(1px)`).
- **Secondary / Archival Outline:** 1px border of Muted Gold/Brass (`#A58B5A`), transparent background, typography in Ink (`#171513`). Subtle paper-tint hover fill.

### Cards & Liner Slips
- **Foundation:** Layered Warm Paper (`#F1E7D3`) rectangles over Aged Paper (`#E4D4B8`) backdrop. Borders feature 1px solid `rgba(165, 139, 90, 0.25)` or low-opacity ink rules.
- **Photo Insert Elements:** Tilted slightly ($-0.8^\circ$ to $+1^\circ$), framed by thick off-white borders, fastened visually by translucent, matte paper tape strips across the upper edge.

### Chips & Archival Badges
- **Style:** Compact, monospace or uppercase tracked text (`label-sm`), bounded by thin hairline borders in Faded Burgundy or Brass.
- **Variants:** "SIDE A / SIDE B", "RZ-000", "STEREO", and "MASTER TAPE". Displayed with stamp-like authenticity, occasionally encased in small debossed cartouches.

### Audio Player & Vinyl Carrier
- **Turntable / Sleeve Container:** Dark Brown (`#35271F`) vinyl jacket pocket with a textured circular cutout exposing the inner vinyl runout label.
- **Tracklist Rows:** Editorial typography with track numbers rendered in Playfair Display italics, track names in DM Sans, and duration right-aligned with dot leaders connecting title to timestamp.

### Inputs & Text Areas
- **Form Controls:** Understated single bottom border (`1.5px solid #A58B5A`) resembling ruled ledger paper rather than boxed fields. Typography matches body ink. Focus state deepens border to Primary Burgundy.