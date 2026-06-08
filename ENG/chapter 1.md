# Chapter 1: Axiomatics and Rigorous Formalism of TSM: Emergent Time, Crystalline 0-Matrix, and Elastodynamics of the 3-Brane

Before the full mathematical apparatus describing continuum dynamics and wave phenomena is introduced, it is necessary to rigorously define the fundamental parameter with respect to which this dynamics occurs. The Topological Sheet Geometrodynamics (TSM) model completely rejects the concept of empty spacetime and absolute, Newtonian time. As outlined in Chapter 0, the foundation of reality is the 0-Matrix – a dense, chaotic substrate of trapped 0-particles.

## 1.1. The Fundamental Evolutionary Parameter $\tau$ as a Measure of Global, Averaged 0-Particle Activity

If the 0-Matrix in its fundamental state is pure chaos, devoid of any cyclical, regular structures, introducing an absolute parameter would seem like smuggling in Newtonian time. However, from a chaotic, stationary set of fluctuations, the concept of an "evolutionary step" can be derived, emerging from the very dynamics of the 0-particles. The key lies in the statistics of a vast number of identical 0-particles and the resulting laws of averaging.

**The 0-Matrix as a Chaotic Gas of Identical Oscillators**
In the Zero State (perfect symmetry, no topological structures), all spheres of oscillation (defined in Chapter 0) have an identical volume, and each 0-particle possesses the same elementary mass and momentum. The motion of an individual 0-particle is completely chaotic. However, because this ensemble is stationary and homogeneous in a statistical sense, there exists a well-defined average frequency of impacts for a single 0-particle in this state:

$$f_0 \equiv \langle f_{\text{osc}} \rangle_{\text{Zero State}}$$

This quantity arises directly from microscopic parameters and the size of the oscillation sphere. It is not imposed from the outside – it is a statistical property of the ensemble.

**Global Evolutionary Parameter $\tau$**
Let $N_{\text{total}}(\tau)$ denote the total number of elementary impacts, summed over all 0-particles in the observable universe, from some arbitrarily chosen reference state. There exists an extensive, monotonically increasing state function:

$$\tau = \frac{N_{\text{total}}}{\mathcal{N}_0 \cdot f_0}$$

where $\mathcal{N}_0$ is the total number of 0-particles. Thus defined, $\tau$:

* **Emerges from microscopy:** It is a normalized measure of the total number of elementary events.
* **Requires no synchronization:** It relies on counting events, and chaos cancels out in the thermodynamic limit, yielding a smooth macroscopic quantity.
* **Is not directly observable:** No local observer has access to the sum of all impacts.

In any infinitesimal interval $d\tau$, each 0-particle performs an average of $f_0 \, d\tau$ impacts (in the unperturbed state).

**Averaging as a Bridge to the Continuum**
On scales well below the Planck scale, chaotic fluctuations undergo self-averaging. The local mean impact density per unit $\tau$ defines a scalar field:

$$\rho_{\text{imp}}(\mathbf{x}, \tau) = \lim_{V \to \text{meso}} \frac{1}{V} \sum_{i \in V} \frac{dN_i}{d\tau}$$

In the Zero State, $\rho_{\text{imp}} = \text{const} \cdot f_0$. In the presence of deformations (compression, torsion), the local mean frequency deviates from $f_0$. This local, averaged frequency enters the wave equation and the equations of continuum dynamics as a deterministic envelope.

**Measured Time $t$ versus Parameter $\tau$**
A single clock (e.g., an atom) does not measure global $\tau$, but rather counts the cycles of its own oscillator. Its instantaneous frequency $f_{\text{lok}}(\mathbf{x}, \tau)$ depends on the local state of stress and velocity of motion. The measured time increment is:

$$dt = \frac{f_0}{f_{\text{lok}}(\mathbf{x}, \tau)} \, d\tau$$

In an unperturbed region, $dt = d\tau$. Any deviation of $f_{\text{lok}}$ from $f_0$ causes time dilation. Time is thus a statistical cosmic clock woven from billions of independent "ticks," and order emerges phenomenally from chaos, much like temperature.

## 1.2. Medium and Space: The Crystalline 0-Matrix and the Isotropic 3-Brane

Having defined the evolutionary parameter, we can formally describe space. Fundamental space is a 4-dimensional differentiable manifold $\mathcal{M}^4$. It is not a vacuum, but a "pressure vessel" entirely filled with colliding 0-particles.

**Jamming Network**
Due to the finiteness of the Universe and extreme packing, 0-particles do not form a free gas, but undergo geometric jamming (the jamming phenomenon). Each 0-particle becomes trapped in its own sphere of interaction (Wigner-Seitz cell). This creates a rigorous, crystalline spatial lattice in 4D, which acquires a full stiffness tensor and the ability to propagate transverse waves. The mechanical state of this medium is described by a symmetric stress tensor $\sigma_{ab}$, where the trace of the tensor is denoted as $\Sigma$. In the absolute Zero State, the stress is $\sigma_{ab}=0$.

**Isotropic 3-Brane**
As mentioned in Chapter 0 (Chladni figures analogy), permanent pressure waves force self-organization. Our physical Universe is an isotropic, three-dimensional membrane (3-brane) suspended deep within the 4th dimension. Due to the averaging of crystalline directions at the macroscopic level, the 3-brane behaves like a perfectly continuous, isotropic nonlinear elastic medium.

## 1.3. Nonlinear Kinematics: Emergence of the Metric $g_{ab}$ from Strain

In TSM, the spatial metric $g_{ab}$ is not a primary entity of abstract geometry. It is a physical projection of the strain state of the 0-Matrix. In the Zero State, the medium is described by a flat Euclidean metric $\delta_{ab}$. Introducing a physical vector displacement field of the substrate $\phi^a(\mathbf{x})$, the observable (Riemannian) metric emerges rigorously from the nonlinear displacement gradients:

$$g_{ab} = \delta_{ab} + \nabla_a \phi_b + \nabla_b \phi_a + \delta_{cd} \nabla_a \phi^c \nabla_b \phi^d$$

The curvature of space and the resulting grawitation are the mechanical stretching of local 0-particle cells, creating a stress gradient toward the 4th dimension.

## 1.4. Wave Dynamics of the 0-Matrix and Field Equations

The mechanics of the 0-Matrix are governed by a generalized Lagrangian formalism. The Lagrangian density $\mathcal{L}$ of the isotropic 3-brane is defined by its total elastic energy, utilizing the elastic modulus tensor $K^{abcd}$:

$$\mathcal{L} = \frac{1}{2} K^{abcd} \epsilon_{ab} \epsilon_{cd} + \mathcal{O}(\epsilon^3)$$

The derivative of the Lagrangian with respect to the strain tensor $\epsilon_{ab}$ uniquely determines the stress tensor:

$$\sigma^{ab} = \frac{\partial \mathcal{L}}{\partial \epsilon_{ab}} = K^{abcd} \epsilon_{cd}$$

Small field deformations in the 3-brane satisfy the wave equation:

$$\nabla^2 \phi - \frac{1}{c_{\text{lok}}^2} \frac{\partial^2 \phi}{\partial \tau^2} = \mathcal{S}(\mathbf{x}, \tau)$$

where $c_{\text{lok}}$ is the local wave propagation velocity, and $\mathcal{S}$ is the source function (the presence of permanent deformations). Geometric curvature is a direct reflex of the background stress tensor, coupled via the elastic material constants of the 0-Matrix.

## 1.5. Dual Regime of Elastodynamics: Elastic Waves vs. Nonlinear Topological Locking

The introduction of a mechanism for instantaneous stress relaxation through Kinetic Repulsion Spheres (described in Chapter 0) generates a fundamental dynamic problem: how can a stable, permanent material structure (particle) form and maintain itself in a perfectly elastic medium that, by definition, instantaneously dissipates any excess pressure? If the relaxation time approaches a minimum, the local density gradient should smooth out at the speed $c_{\text{lok}}$ long before the lattice has time to undergo plastic restructuring.

The solution to this apparent paradox requires a rigorous separation of the 0-Matrix dynamics into two complementary regimes, demarcated by a critical packing fraction threshold $\phi_{\text{lock}}$ (the topological freezing threshold).

**Regime I: Linear Acoustic Relaxation ($\phi < \phi_{\text{lock}}$)**
As long as the local compression of the lattice does not exceed the critical geometric stability threshold of the Wigner-Seitz cages, the 0-Matrix behaves like an ideal, linear elastic continuum. In this state:

* Strains are conservative. Kinetic Repulsion Spheres deform (e.g., flatten), but the 0-particles rigorously maintain the matrix of their current neighbors. No change in the local topology of the lattice occurs.
* The excess effective pressure $P_{\text{eff}}$, resulting from the increase in collision frequency $f_{\text{osc}}$, is transferred symmetrically outward on the principle of a boundary cascade. The medium relaxes energy through the propagation of longitudinal and transverse elastic waves at the speed $c_{\text{lok}}$. The dissipation of disturbing phenomena is instantaneous and complete.

**Regime II: Nonlinear Topological Locking ($\phi \ge \phi_{\text{lock}}$)**
The situation changes drastically when, due to an extreme concentration of energy (e.g., the collision of large-scale pressure waves in 4D space), the system is compressed beyond the plasticity limit $\phi_{\text{lock}}$.

* Kinetic cages are crushed to such an extent that maintaining the previous neighborhood matrix becomes geometrically impossible. Hyper-fast oscillators ($v_k \gg c_{\text{lok}}$) are forced into topological neighbor-switching.
* As a result of this geometric twisting of the structure, collision momentum vectors can no longer be transmitted outward (centrifugally). They begin to cross at non-standard angles, looping into a self-sustaining, cyclical kinematic vortex.
* Kinetic self-confinement ensues: the incredible speed of the 0-particles, which in Regime I guaranteed the instantaneous dissipation of energy, now guarantees its instantaneous and permanent closure. Particles strike each other inside the entanglement so rapidly that any attempt to return to a linear geometric state is immediately blocked by the oncoming momentum of an adjacent particle trapped in the loop.

In this regime, the 0-Matrix loses its capacity to release topological stresses. A nonlinear entanglement (soliton) is formed. It gains stability because untangling this knot would require passing through a state of extreme compression again, which creates a powerful energy barrier. The paradox is resolved: the medium perfectly propagates elastic waves in its linear limit, but permanently traps energy in the topological limit, giving rise to quantized matter.

## 1.6. The Axiom of Matter: Quantized Topological Knots and the Rigorous Separation of Mass and Charge

Under the influence of extreme nonlinear compression, where the local packing fraction of the 0-Matrix exceeds the critical topological freezing threshold ($\phi(\mathbf{x}) \ge \phi_{\text{lock}}$), linear fluctuations lose their capacity for wave relaxation. The momentum vectors of hyper-fast oscillators are forced to geometrically change their neighborhood matrix and loop. In a 4-dimensional continuum, they form remarkably stable standing waves (solitons), which are essentially permanent topological knots that macroscopic physics identifies as fermions.

**Mathematical Genesis of Matter Quantization**
The quantized nature of elementary particles is not an ad hoc assumption in TSM, but a strict requirement of the apparatus of algebraic topology. The state of deformation (twisting) of the kinetic cages is described by a vector field of substrate orientation $\mathbf{n}(\mathbf{x})$ (where $|\mathbf{n}| = 1$). For the knot to maintain stability, the field $\mathbf{n}$ far from the core of the entanglement must smoothly asymptotically approach the unperturbed, homogeneous background state. This boundary constraint forces the parameter space to close onto a sphere.

Rigorous topological theorems prove that the integral of the density of such spatial twisting (the mapping from physical space to the orientation space) can take only integer values. This phenomenon defines an invariant winding number (topological charge) $\mathcal{W} \in \mathbb{Z}$. A knot possessing a charge $\mathcal{W} = 1$ cannot smoothly "radiate away" a fraction of its twist (e.g., pass to a state $\mathcal{W} = 0.5$), because this would require a global, macroscopic rupture of the crystalline lattice continuity. The threshold $\phi_{\text{lock}}$ acts as the ignition mechanism for confinement, but it is the hard rules of spherical geometry that enforce the indivisible quantization of the formed soliton defect.

Thanks to this foundation, TSM rigorously separates the concepts of mass and charge:

* **Electric Charge (3D Projection):** It is the directly measured flux of the knot's phase-twist vector projected onto the plane of our 3-brane. Since a closed twist must always close to a full phase rotation (constituting a geometric multiple of $2\pi$), the charge undergoes absolute quantization to values of $\pm 1e$, regardless of the internal complexity of the knot in the higher dimension.
* **Rest Mass (4D Embedding):** It is defined as the macroscopic equivalent of the elastic energy stored within the strained structure of the knot. It corresponds directly to the depth to which the formed entanglement orthogonally bulges the 3-brane into the fourth dimension. This conclusively explains mass asymmetry: a complex, multiple topological braid (proton) forces a much deeper 4D deformation and generates an incomparably stronger background stress gradient than a simple twist (electron), despite possessing an identical charge projection of $\pm 1e$.

**Fluid Motion and Asymptotic Extinction of Discrete Barriers**
The propagation of matter through space (e.g., the free motion of an electron) does not consist of pushing 0-particles through the medium, but rather of the lossless, wave-like transfer of the topological entanglement state itself through successive Kinetic Repulsion Spheres.

The spatial size of the knot core ($L$) drastically exceeds the microscopic size of an individual Wigner-Seitz cage ($a$). This fundamental scale asymmetry causes the periodic resistance potential of the crystalline lattice to undergo spatial averaging. This leads to an exponential extinction of the discrete Peierls-Nabarro energy barrier, which determines the minimum force required to move a defect in a solid:

$$E_{PN} \propto \exp\left(-\pi \frac{L}{a}\right) \approx 0$$

As a result, a topological knot formed in this manner slides inside the 0-Matrix in an ideally fluid manner, without energy dissipation, which rigorously and effortlessly realizes Newton's First Law of Motion. The radiation of energy in the form of transverse waves (photons) occurs exclusively during knot deformations resulting from collisions or rapid acceleration.

## 1.7. Derivation of Relativistic Kinematics from Hydrodynamics

Lorentz transformations and the $E=mc^2$ principle are a rigorous consequence of hydrodynamic drag during the motion of standing waves.

**Length Contraction:**
For a knot moving along the $x$-axis with velocity $v$, we introduce the co-moving coordinate $u = x - v\tau$. Transforming the homogeneous wave equation requires rescaling the $x$-axis to preserve the isotropic form of the soliton:

$$x' = \frac{u}{\sqrt{1 - \frac{v^2}{c_{\text{lok}}^2}}} = \gamma (x - v\tau)$$

The shape of the knot undergoes mechanical compression by a factor of $\gamma$ under the influence of the medium's drag.

**Energy and Momentum:**
The kinetic and potential stress energy of the knot integrates to:

$$E(v) = \gamma \cdot E_0, \qquad m(v) = \gamma m_0$$

Vector momentum is $p(v) = \gamma m_0 v$. The force required for acceleration reveals the phenomenon of asymptotic wave resistance:

$$F = \frac{dp}{dt} = m_0 \gamma^3 \cdot a$$

As $v \to c_{\text{lok}}$, $\gamma \to \infty$. Wave resistance becomes infinite. (An exception is orthogonal motion along the $x_4$ axis, which does not force the propagation of a forward wave on the 3D plane).

## 1.8. Variable Wave Propagation (Local $c$) and Fundamental Constants

The speed $c$ is not a universal constant. It results from the nonlinear phenomenon of acoustoelasticity. In a medium subjected to tension ($\Sigma$), the local velocity of transverse waves is modulated by nonlinear stiffness (Murnaghan constants):

$$c_{\text{lok}}^2 = \frac{\mu}{\rho_0} \left( 1 + \mathcal{A} \Sigma \right) \quad \text{and electrodynamic notation:} \quad c_{\text{lok}} = \frac{1}{\sqrt{\epsilon_{\text{eff}} \mu_0}}$$

The permittivity of the medium $\epsilon_{\text{eff}}$ depends on gradients induced by gravity or magnetic fields: $\epsilon_{\text{eff}} = \epsilon_0 (1 + \kappa B^2 + \lambda \frac{\Phi}{c_0^2} + \dots)$.

In TSM, the hitherto dimensionless parameters of the Universe become material constants of the 4-dimensional continuum:

* $c_0$ – transverse relaxation velocity in the relaxed Zero State.
* $\kappa$, $\zeta$, $\lambda$ – constants of elasto-dynamic coupling (magnetic, oscillatory, gravitational).
* $\chi$ – topological constant determining the baseline tension of the knots.
* $G_{\text{eff}}$ – local gravitational constant, depending on the global degree of background relaxation.
