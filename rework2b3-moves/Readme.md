# Contrapunctus Rework 2B3-Moves: 5D Movement Phase Rule Space Architecture

## Overview
`rework2b3-moves/contrapunctus-3.html` implements a major paradigm shift in the Contrapunctus cellular automaton composition engine:
Transitioning from **static tone filtering** ("which notes are allowed in abstract?") to an endogenous **Movement Phase Rule Space** ("how recent board situations influence the next possible contrapuntal movements").

---

## Core Innovations & Subsystems

### 1. 5D Movement Phase Rule Space (`MOVE_AXES`)
The movement rule space maps Voice-Leading Movement Phase across a 5D discrete lattice containing 270 cells ($3 \times 5 \times 3 \times 2 \times 3$):

$$\mathcal{M} = \psi \times \mu_m \times \gamma_m \times \sigma_m \times \phi_m$$

- **$\psi$ (Departure Context):** `0`: NCT/Chromatic, `1`: Diatonic Extension, `2`: Chord/Guide Tone.
- **$\mu_m$ (Movement Step Class):** `0`: Hold ($0\text{st}$), `1`: Step ($1\text{--}2\text{st}$), `2`: Small Leap ($3\text{--}4\text{st}$), `3`: Large Leap ($\ge 5\text{st}$), `4`: Resolution/Recovery.
- **$\gamma_m$ (Relative Voice Motion):** `0`: Similar, `1`: Oblique, `2`: Contrary.
- **$\sigma_m$ (Metric Accent):** `0`: Structural Beat ($1, 3, 5, 7$), `1`: Passing Off-Beat ($2, 4, 6, 8$).
- **$\phi_m$ (Target Fit Class):** `0`: Foreign/Chromatic, `1`: Diatonic Extension, `2`: Essential Harmonic Chord/Guide Tone.

### 2. Non-Linear $L_p$ Norm Cost Surface ($p=3.0$) & Cross-Axis Coupling
Rule space costs (`cellCost`) utilize a non-linear $L_p$ p-norm ($p=3.0$) combined with cross-axis coupling penalties:

$$C(\mathbf{c}) = \left( \sum_{i} \Big( w_i \cdot (1 - \text{aff}[c_i]) \Big)^p \right)^{1/p} + P_{\text{coupling}}(\mathbf{c})$$

This prevents single-axis failures (e.g. leaping from a non-chord tone or landing on a downbeat dissonance) from leaking into early $\lambda$ sublevel sets, guaranteeing that only well-balanced, species-compliant moves unlock first.

### 3. Multi-Step Lookahead Pathfinding (`evaluateLookaheadMove`) & Dead-End Pruning
Voice walks (`runVoiceWalk`, `pickNote`, `pickEnhancedBassNote`) incorporate a multi-step lookahead engine that simulates step $t+1$ for every candidate move at step $t$:
- **Dead-End Pruning:** Candidates at step $t$ that lead to 0 legal moves or species counterpoint singularities at step $t+1$ are discarded.
- **Temporal Resolution Enforcement:** Passing/neighbor non-chord tones ($\phi_m < 2$) at step $t$ are discarded unless step $t+1$ has a valid stepwise resolution to a chord tone ($\phi_{m, t+1} \ge 2$).
- **Leap Recovery Enforcement:** Large leaps ($\ge 5\text{st}$) at step $t$ are discarded unless step $t+1$ has a valid stepwise recovery in the opposite direction.

### 4. Strict Structural Beat Vertical Consonance Rules
On structural downbeats ($\sigma_m = 0$):
- **Bass Voice:** Required to land on essential chord tones or roots ($\phi_m \ge 2$).
- **Upper Voices:** Required to form consonant vertical intervals above the bass ($3\text{rds}, 5\text{ths}, 6\text{ths}, 8\text{ves}$) unless prepared as a suspension ($\psi = 2$). Second, fourth (above bass), seventh, and tritone dissonances on downbeats are strictly prohibited.

### 5. Supervisory Macro-Governance Engine (`evaluateSupervisorySpace`)
Supervises macro-phrase trajectories over exposition, development, climax, and resolution stages:
- **Paradigms:** `Classical`, `Jazz`, `Hybrid`.
- **Guide-Tone & Enclosure Guidance:** Enforces 3rd $\leftrightarrow$ 7th voice-leading resolution vectors and chromatic enclosures.
- **Dynamic Parameter Modulation:** Dynamically modulates legal rule fractions ($\lambda_C, \lambda_V, \lambda_M$) along the phrase arc.

### 6. Topological Fiber Bundle & Voice-Leading Orbifold Intersections
Implements formal cross-space fiber bundle projections and voice-leading orbifold geodesic distance metrics ($D_\text{orb}$):

$$\pi_{\mathcal{M} \to \mathcal{V}}: \mathcal{M}(\psi, \mu_m, \gamma_m, \sigma_m, \phi_m) \longrightarrow \mathcal{V}(\kappa, \mu, \phi, \sigma, \gamma)$$
$$\pi_{\mathcal{V} \to \mathcal{C}}: \mathcal{V}(\kappa, \mu, \phi, \sigma, \gamma) \longrightarrow \mathcal{C}(d, \tau, \rho, \eta)$$

Computes pullback Kronecker tensor intersections in real-time, rendered as 3D geodesic trajectory vectors and fiber bundle density overlays on `#latticeCanvas` and `#ringCanvas`.

### 7. Algebraic Rule Rings (`evaluateAlgebraicRuleRing`)
Combines rule generators ($R_\text{cpt}, R_\text{modal}, R_\text{saddle}, R_\text{topo}$) via composable ring operators over $\mathbb{F}_2^N$:
- **Cadential Intersection ($\land$)**
- **Harmonic Symmetry Union ($\lor$)**
- **Non-Commutative Product ($\circ$)**
- **Fusion Synthesis ($\odot$)**

---

## Visualization Dashboards
- **`#latticeCanvas` (Three.js / WebGL / 2D Canvas Fallback):** 3D Rule Hypercube, Cost Cuts, Fiber Trajectories, Hover & Link Highlights.
- **`#ringCanvas`:** Live Algebraic Ring Closures & Fiber Bundle Pullback Density Bars.
- **`#supCanvas`:** Macro Energy Arc, Formal Phrase Stages, and Dynamic $\lambda_M$ Curves.
- **`#rollCanvas` & `#seqCanvas`:** Piano Roll Score and Multi-Voice Sequencer Lanes.
- **`#envCanvas` & `#basinCanvas`:** Interactive ADSR Envelope Editor and Starting State Basin Map.
