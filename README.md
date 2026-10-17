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
- **Visual Dashboards:** 7 interactive canvas visualizers including 3D Rule Hypercubes, Phase Space Trajectories, Piano Roll Scores, Multi-Voice Sequencer Lanes, Envelope Editors, and Basin Maps.
