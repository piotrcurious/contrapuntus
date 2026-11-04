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

## Interactive Controls & UI
- **4-Space Selector (`#selSpace`):** Toggle active editing across `CHORD`, `VOICE`, `MOVE`, and `TIME` spaces.
- **Density & Profile Sliders (`#sLamM`, `#sLamT`, `#profM`, `#profT`):** Adjust rule space threshold densities and preset profile weightings in real-time.
- **Live 3D & 2D Lattice Projections:** Real-time visual feedback of active rule space cells, multi-space trajectory paths, and dynamic rule-space transmutations.
