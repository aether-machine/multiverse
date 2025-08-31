# The Universe as a Diode Junction — Technical Draft

## Abstract
We outline a toy framework that treats spacetime as a biased transmission medium and models universes as coupled oscillatory subsystems. Using Stuart–Landau limit-cycle oscillators connected by asymmetric couplings, we demonstrate that cross-rail coupling can produce robust phase-and-amplitude locking (mutual reinforcement). The model supports the shorthand: the observable universe behaves like a diode junction within a larger meta-circuit. We present the model, simulation results, interpretation, and testable predictions.

---

## 1. Introduction & motivation
Conventional frameworks take spacetime as a neutral background; here we posit a transmission bias (a preferred mode of propagation). Particles and macroscopic structures are condensations of resistance to that bias. Black holes act as rectifiers; stars act as sources. The double-slit experiment and interferometric visibility suggest coherence is a primary state variable. The purpose of this note is to make the first quantitative step: a toy dynamical model for **mutual reinforcement of coherence** across three coupled bias-rails.

---

## 2. Minimal model
We model each rail (Light `L`, Our `O`, Dark `D`) as a complex Stuart–Landau oscillator $$\(z_i(t)\in\mathbb{C}\)$$ with self-dynamics and linear coupling:

$$\[
\dot z_i = (\lambda_i + i\omega_i - |z_i|^2)\,z_i + \sum_{j\neq i} C_{ij}\, z_j,
\qquad i \in \{L,O,D\}.
\]$$

- $$\(\lambda_i\)$$ : net local drive (growth/damping).  
- $$\(\omega_i\)$$ : natural frequency (phase bias).  
- $$\(C_{ij}\)$$ : complex/real coupling from rail $$\(j\)$$ into $$\(i\)$$. Asymmetry in $$\(C\)$$ encodes rectification/diode-like behavior.

We define a global coherence metric:

$$\[
\mathcal{R}(t) = \frac{\left|\sum_i w_i z_i(t)\right|}{\sum_i w_i |z_i(t)|},\qquad 0\le \mathcal{R}\le 1.
\]$$

$$\(\mathcal{R}\approx 1\)$$ indicates strong common-mode amplitude/phase alignment.

---

## 3. Linear stability & locking onset
Linearize near $$\(z\approx 0\): \(\dot{\mathbf z} \approx M \mathbf z\)$$ with $$\(M_{ii}=\lambda_i+i\omega_i\), \(M_{ij}=C_{ij}\)$$. Mutual reinforcement onset occurs when $$\(M\)$$ has an eigenvalue with positive real part. The corresponding eigenvector gives the modal amplitude/phase ratio across rails.

---

## 4. Rectification & gating
Diode-like behavior can be modeled by asymmetric couplings and simple gating functions:

$$\[
C_{ij} = c_{ij}\, f(|z_j|,|z_i|),
\quad f(x,y) = \frac{1}{1+\exp[-\alpha(x-y-V_{th})]},
\]$$

so coupling turns on when upstream amplitude exceeds a threshold relative to downstream.

---

## 5. Simulation (toy example)
We integrate the system with a robust time-stepping scheme (RK4) and show a representative run where `Our` has slightly positive self-drive and asymmetric couplings produce a rapidly growing common mode. See `sim/run_simulation.py` for parameters and figure generation.

**Observations**:
- Small random perturbations are amplified into a coherent global mode.
- Phase locking is rapid compared to amplitude saturation.
- Rectifying asymmetry biases amplitude distribution but still allows locking if couplings overcome detuning.

---

## 6. Interpretation
- **Universe as diode:** The macrostate of a universe is a diode junction in a meta-circuit: it rectifies an external bias into local DC-like constants.  
- **Life-signal:** Mutual locking provides a robust mechanism for a cross-rail "life-signal" to persist in the presence of noise and parameter mismatch.  
- **Black holes:** modelled as strong rectifiers, implementing highly asymmetric couplings.  
- **Cosmogenesis:** a global polarity flip or large-scale gating event corresponds to a phase change of the meta-circuit.

---

## 7. Predictions & falsifiability
- Interferometric visibility laws apply identically once normalized by $$\(\lambda\)$$ and coherence length: testable across photons/electrons.  
- Coupled-signal models predict enhanced environmental cross-coherence near strong rectifiers (e.g., near astrophysical anomalies, megalithic sites if coupling exists).  
- Engineered three-way coupling in synthetic oscillators (electrical, optical, cold-atom) yields measurable locking thresholds consistent with eigenvalue tests.

---

## 8. Limitations & next steps
- Mapping model parameters to physical observables is nontrivial; the current note is a mathematical skeleton.  
- Extend to continuum models (field-theoretic coherence density), include noise, and compute spectral signatures.  
- Design lab-scale analogues (coupled laser cavities, coupled superconducting resonators) to test cross-rail locking.

---

## 9. Appendix — suggested experiments
1. Electron biprism interferometry vs optical Mach–Zehnder with matched δ/λ and controlled decoherence.  
2. Three-oscillator laboratory analogue (RF cavities or lasers) with asymmetric couplings and gating thresholds to reproduce diode-like switching.

---

## References
(Experimental and theoretical references to be added; this is an exploratory note.)

