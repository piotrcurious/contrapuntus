# Contrapunctus

A deterministic counterpoint automaton, cellular composition engine, and multi-dimensional rule-space framework built with WebGL, Web Audio API, and HTML5 Canvas.

## Rework 2B3-Moves Architecture (`rework2b3-moves/contrapunctus-3.html`)

`rework2b3-moves/contrapunctus-3.html` implements an endogenous 5D Movement Phase Rule Space architecture:
- **5D Movement Phase Rule Space (`MOVE_AXES`):** 270-cell discrete lattice ($\psi \times \mu_m \times \gamma_m \times \sigma_m \times \phi_m$) governing movement transitions based on recent board situations.
- **4D Temporal Metric Space (`TIME_AXES`):** Metric beat positions, subdivisions, duration classes, and syncopations.
- **Non-Linear $L_p$ Norm Cost Surface ($p=3.0$):** $L_p$ norm with cross-axis coupling penalties preventing single-axis failures from unlocking in early $\lambda$ sublevel sets.
- **Multi-Step Lookahead Pathfinding (`evaluateLookaheadMove`):** Prunes dead ends, unresolvable non-chord tones, and unrecovered leaps at step $t+1$.
- **Strict Structural Beat Vertical Consonance:** Enforces consonant vertical intervals ($3\text{rds}, 5\text{ths}, 6\text{ths}, 8\text{ves}$) above bass on structural downbeats.
- **Supervisory Macro-Governance:** Formal phrase arcs (exposition, development, climax, resolution), guide-tone resolution chains ($3 \leftrightarrow 7$), and dynamic $\lambda_M$ modulation.
- **Algebraic Rule Rings & Fiber Bundle Orbifold Geometry:** Composable ring operators over $\mathbb{F}_2^N$ and cross-space pullback tensor intersections.
- **Secondary Composition Toolkit (Dynamic Context Hierarchy):** Dynamic 3-tier tie-breaking arbitration (`mode: 'contextual'`) replacing static scalar weights and rigid lexicographical cascades.
- **Melody Figure Attractor Spline Target Lane (`SEQ.splineLane`):** Interactive Catmull-Rom cubic spline lane with velocity alignment, adjustable point weights ($0.25$ to $1.00$), and presets (`arch`, `wave`, `clear`).
- **Real-Time Visual Telemetry Suite:**
  - *Candidate Decision Inspector (`tieDecisionCanvas`):* Multi-colored stacked breakdown of competing transition scores with click-to-pin.
  - *Neurocognitive Movement Telemetry (`cogTrackerCanvas`):* Directional momentum ($E_v$), gap-fill debt gauges ($G_v$), dissonance obligations ($O_v$), and Bayesian surprise histograms.
  - *2D Contrapuntal Tangent Phase Portrait (`movePhaseCanvas`):* Velocity vector flow plane ($\Delta p_0 \times \Delta p_2$) mapping contrary, oblique, and similar motion with live scrubbing.
  - *Score Movement Phase Badges (`#btnShowMovement`):* Displays live $(\psi, \mu_m, \gamma_m, \sigma_m, \phi_m)$ movement vector badges on notes.
- **Visual Dashboards:** Complete suite of 10 interactive canvas visualizers including 3D Rule Hypercubes, Fiber Bundle Closures, 2D Phase Space Trajectories, Decision Inspectors, Cognitive Telemetry, Piano Roll Scores, Multi-Voice Sequencer Lanes, Envelope Editors, and Basin Maps.
- **Zero External Dependencies & Bundling:** All fonts, stylesheets, scripts, audio synthesis engines, and WebGL painters are 100% self-contained with no external network requests. Run `python3 scripts/bundle.py` to package or verify standalone offline bundles.
