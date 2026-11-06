# Contrapunctus Rework 2B3-Moves: 5D Movement Phase Rule Space & Neurocognitive Dynamic Rule Transmutation

## Overview
`rework2b3-moves/contrapunctus-3.html` implements a major paradigm shift in the Contrapunctus cellular automaton composition engine:
Transitioning from **static tone filtering** ("which notes are allowed in abstract?") to an endogenous **Movement Phase Rule Space governed by Neurocognitive Dynamic Rule Transmutation** ("how recent board situations, multi-step expectations, and auditory scene dynamics influence the next possible contrapuntal movements by dynamically transmuting the rule manifolds").

---

## Core Innovations & Subsystems

### 1. 5D Movement Phase Rule Space (`MOVE_AXES`)
The movement rule space maps Voice-Leading Movement Phase across a 5D discrete hypercube lattice $\mathcal{M} = \psi \times \mu_m \times \gamma_m \times \sigma_m \times \phi_m$ (3 × 5 × 3 × 2 × 3 = 270 cells):
- **$\psi$ (Departure Context / Direction, 3 values):**
  - `0`: Avoid / foreign departure
  - `1`: Scale tone / passing motion
  - `2`: Harmonic target departure (root, guide tone, color tension)
- **$\mu_m$ (Movement Step Class, 5 values):**
  - `0`: Hold / unison repetition ($0\text{ st}$)
  - `1`: Half-step motion ($1\text{ st}$)
  - `2`: Whole-step motion ($2\text{ st}$)
  - `3`: Small leap / skip ($3\text{--}4\text{ st}$)
  - `4`: Large leap ($>4\text{ st}$) requiring resolution/recovery
- **$\gamma_m$ (Relative Voice Motion, 3 values):**
  - `0`: Similar motion
  - `1`: Oblique motion (one voice holds, other moves)
  - `2`: Contrary motion (classical ideal)
- **$\sigma_m$ (Metric Beat Accent, 2 values):**
  - `0`: Structural metric downbeat (accented)
  - `1`: Passing metric offbeat (unaccented)
- **$\phi_m$ (Target Fit Class, 3 values):**
  - `0`: Avoid / foreign tone
  - `1`: Scale tone / passing tone
  - `2`: Harmonic target (root, 3rd/7th guide tone, 9th/11th/13th color tension)

### 2. 4D Temporal Rule Space (`TIME_AXES`)
The temporal rule space captures rhythmic duration and subdivision $\mathcal{T} = m_\text{pos} \times m_\text{sub} \times d_\text{dur} \times s_\text{sync}$ (4 × 3 × 3 × 2 = 72 cells):
- **$m_\text{pos}$ (Metric Bar Position, 4 values):** Quarter-bar division ($1\text{st}, 2\text{nd}, 3\text{rd}, 4\text{th}$ beat).
- **$m_\text{sub}$ (Subdivision Level, 3 values):** On-beat (0), eighth subdivision (1), sixteenth subdivision (2).
- **$d_\text{dur}$ (Duration Class, 3 values):** Staccato short (0), normal sustained (1), legato extended (2).
- **$s_\text{sync}$ (Syncopation State, 2 values):** Straight (0) vs syncopated offbeat onset (1).

### 3. Neurocognitive Predictive Coding & Dynamic Rule Transmutation (`CognitiveStateTracker`)
Rather than relying on static filters or ad-hoc sorting fudge factors, the composition engine models the cognitive listening and expectation process across multiple steps:
- **Melodic Expectation Gradients ($E_v$):** Implements Narmour's Implication-Realization model. Small stepwise motions ($1\text{--}2\text{ st}$) build directional continuation momentum ($E_v \to \pm 1$), while large leaps ($>4\text{ st}$) trigger reversal expectations ($E_v \to \mp 0.8$).
- **Trans-Step Gap-Fill Debt ($G_v$):** When a voice takes a large leap, a multi-step gap-fill obligation $G_v$ is registered with a required reverse direction and remaining semitone debt. Subsequent steps prioritize stepwise filling of the octave/fifth gap.
- **Trans-Step Dissonance Resolution Obligations ($O_v$):** Dissonant passing or suspension tones obligate stepwise resolution to a consonant interval on the subsequent beat.
- **Rule Transmutation Operator (`transmuteRuleSpace`):** On every decision step, the base Movement and Voice rule spaces are dynamically transformed ($T_M, T_V$). Allowed cell manifolds expand or contract in response to $E_v, G_v, O_v$, making expectation fulfillment and gap resolution intrinsic to the rule space rather than an external check.

### 4. Non-Linear $L_p$ Metric Tensor Cost Surfaces & Coupling
Cell costs in Movement Space are evaluated via a non-linear $p$-norm ($p=3.0$) with cross-axis penalty coupling:
$$C(c) = \left( \sum_{i} w_i |x_i - x_i^\text{ideal}|^p + \text{coupling}(c) \right)^{1/p}$$
- Leaps into dissonant unaccented targets incur exponential compound penalties.
- Accented structural contrary motion into guide tones achieves minimal cost.

### 5. Multi-Step Lookahead Simulation (`evaluateLookaheadMove`)
Candidate moves in `pickNote` and `pickEnhancedBassNote` evaluate a step $t+1$ lookahead projection:
- Simulates subsequent step $t+1$ under incoming chord changes.
- Identifies dead-end paths that would force inevitable parallel octaves/fifths or voice collisions.
- Integrates path lookahead cost into the unified candidate evaluation:
  $$C_\text{total} = C_\text{flow} + C_M + 0.8 C_V + 0.4 C_T + C_\text{lookahead}$$

### 6. Strict Vertical Consonance Option A & Extended Jazz/Modal Vocabulary
- **Option A Consonance:** Structural beats require strict vertical consonance against the bass (3rds, 5ths, 6ths, 8ves, and consonant color extensions 9ths/#11ths), yielding 0.0% unconditioned vertical dissonances.
- **Circle of Fifths Progression:** Repairs algebraic rule ring product operators to ensure natural, functional harmonic movement across modal interchange and secondary dominants (`Imaj7 -> IVmaj7 -> ii7 -> V7`).
- **Melodic Arch Balance:** Combines Huron's pitch proximity model with Narmour's implication-realization to produce singable, smooth contrapuntal contours (over 80% steps/thirds).

---

## 7. Secondary Composition Toolkit: Dynamic Context Hierarchy (`mode: 'contextual'`)
Rather than relying on static scalar weights or rigid lexicographical cascades, the composition engine features a **3-Tier Contextual Dynamic Hierarchy**:
- **Macro-Harmonic Arbitration (`chordNext` & `tieBreak`):**
  Dynamically scales motion penalties, voice leading parsimony, fifths bonuses, and cadential goal attraction based on the active phrase stage (exposition vs development vs resolution) and cadential proximity.
  $$S(c) = -w_\text{motion} \cdot P_\text{motion} - w_\text{voice} \cdot D_\text{vl} + w_\text{voice} \cdot B_\text{common} + w_\text{fifths} \cdot B_\text{fall} + w_\text{goal} \cdot B_\text{goal} \pm w_\text{cost} \cdot C_\text{rule}$$
- **Micro-Contrapuntal Arbitration (`pickNote` & `pickEnhancedBassNote`):**
  Integrates lookahead dead-end safety, cadence attraction, cognitive debt recovery (`\mu_m = 4`), anti-stagnation, and relative contrary motion over raw pitch proximity.
- **Interactive Control Sliders:** Dedicated sliders for Motion Penalty, Voice Leading, Rule Cost, Circle of 5ths, Cadence Urgency (`wGoal`), Cognitive Debt Bias (`wDebt`), Contrary Motion Affinity (`wContrary`), and Anti-Stagnation Drive (`wStagnation`).

---

## 8. Real-Time Telemetry & Visual Inspection Dashboards
The Secondary Composition Toolkit integrates three dedicated interactive canvas visualizers with real-time bidirectional synchronization:

1. **Candidate Decision Inspector (`#tieDecisionCanvas`, `drawTieDecisionInspector`):**
   - Renders a multi-colored stacked score breakdown bar chart for all candidate chord transitions at the active segment.
   - Shows exact positive components (Cadential Goal, Fifths/Resolution, Common Tones, Rule Cost) vs negative penalties (Repetition, Voice Leading Distance).
   - Interactive mouse hover tooltips display exact mathematical terms; clicking any candidate pins/unpins that transition.
2. **Neurocognitive Movement Telemetry Dashboard (`#cogTrackerCanvas`, `drawCognitiveDashboard`):**
   - Plots filled continuous momentum curves for Soprano ($E_0$) and Bass ($E_2$) alongside leap gap-fill debt gauges ($G_v$) and dissonance obligations ($O_v$).
   - Displays a background histogram of Bayesian information surprise in bits ($- \log_2 P(pc)$).
   - Clicking anywhere along the canvas seeks the active step.
3. **2D Contrapuntal Tangent Phase Portrait (`#movePhaseCanvas`, `drawMovePhasePortrait`):**
   - Visualizes melodic velocity $\Delta p_0$ versus bass velocity $\Delta p_2$ across the 4 phase quadrants:
     - Quadrants II & IV: **Contrary Motion ($\gamma = 2$)** with green flow styling.
     - Quadrants I & III: **Similar Motion ($\gamma = 0$)** with red cautionary styling.
     - Axes: **Oblique Motion ($\gamma = 1$)** with cyan styling.
   - Features directional velocity arrows and interactive scrubbing to inspect any step's vector in the score.

---

## 9. Melody Figure Attractor Spline Target Lane (`SEQ.splineLane`, `STATE.melodySpline`)
The sequencer includes a dedicated **Spline Target Lane** allowing composers to paint continuous target pitch contours and velocity profiles:
- **Catmull-Rom Cubic Interpolation (`evaluateMelodySpline`):**
  Derives continuous target pitch $p^*(s)$, instantaneous velocity $v^*(s) = \frac{d p^*}{d s}$, and interpolated guidance weight $w^*(s)$ across all steps.
- **Adjustable Control Point Weights ($0.25$ to $1.00$):**
  - **Low Weight ($w \approx 0.25$):** Functions as gentle melodic contour guidance.
  - **High Weight ($w \to 1.00$):** Strictly commands note destination, pulling candidates to exact target pitches.
- **Velocity Alignment Guidance:**
  Candidate notes moving counter to the spline target velocity ($\Delta p \cdot v^* < 0$) receive weighted kinetic friction penalties in `pickNote`.
- **Interactive Painting & Presets:**
  - Click to add or move control points.
  - Shift-click to cycle weights ($0.25 \to 0.50 \to 0.75 \to 1.00$).
  - Alt-click / Right-click to delete points.
  - Sequencer toolbar presets: `arch`, `wave`, and `clear spline`.

---

## Interactive Controls & UI
- **4-Space Selector (`#btnSetChord`, `#btnSetVoice`, `#btnSetMove`, `#btnSetTime`):** Toggle active editing across `CHORD`, `VOICE`, `MOVE`, and `TIME` spaces.
- **Movement Phase Badges (`#btnShowMovement`):** Toggle live $(\psi, \mu_m, \gamma_m, \sigma_m, \phi_m)$ movement vector badges on note onsets in the piano-roll score.
- **Density & Profile Sliders (`#sLamM`, `#sLamT`, `#profM`, `#profT`):** Adjust rule space threshold densities and preset profile weightings in real-time.
- **Full State Serialization (`serializeState` / `restoreState`):** Persists all 4 rule spaces, tie-breaking rules, cognitive tracker parameters, supervisory settings, and melody spline profiles with complete validation.
