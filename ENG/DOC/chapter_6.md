<!-- ver:2.0.0 -->
# Chapter 6: Gravity as Orthogonal Tension. The 4D Dimension, Plasmoids, and Nonlinear Continuum Dynamics

In Topological 0-Matrix (Substrate) Mechanics (TSM), we reject the geometric abstraction that attributes gravity to the pure curvature of non-material spacetime. Gravity is defined here as an actual orthogonal tension (transverse tension) of the elastic 3-brane directed toward the fourth spatial dimension ($x^4$). This chapter presents the complete mathematical formalism describing the behavior of the substrate in both the linear regime and under extreme nonlinear astrophysical conditions, replacing the apparatus of General Relativity (GR) with the classical elastodynamics of continuous media.

## 6.1. Ontology of Gravity and the Linear Limit (Laplace's Equation)

Our observable Universe functions as an isotropic, three-dimensional membrane (3-brane) formed from densely packed 0-particles. According to the mode distribution introduced in Chapter 2, the polarization components directed orthogonally to the brane represent local deflections of the substrate.

When the local coupling of electromagnetic and torsional fields forms a stable topological knot (fermion) with a specific energy density, the 3-brane responds to this concentration by forcing a displacement along the $x^4$ axis. This physical stress gradient of the substrate outside the knot is perceived by test objects as a gravitational field.

For weak and medium energy densities (the Newtonian limit), the membrane tends to minimize its surface area and equalize stresses, behaving like an ideally thin, taut elastic membrane. The static equilibrium equation for an isotropic membrane subjected to a transverse point load $q(r)$ reduces to the three-dimensional Laplace equation:

$$\nabla^2 w(\mathbf{r}) = 0, \quad \text{for } r > 0$$

where $w(\mathbf{r})$ denotes the magnitude of the deflection (displacement) of the membrane along the $x^4$ axis at point $\mathbf{r} = (x^1, x^2, x^3)$. Assuming ideal spherical symmetry of the system, the Laplace operator in spherical coordinates reduces to the form:

$$\frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{dw}{dr} \right) = 0$$

Integrating this equation twice yields the explicit solution for the deflection profile as a function of distance $r$ from the center of the knot:

$$w(r) = \frac{C}{r} + C_2$$

Applying the boundary condition at infinity $w(r \to \infty) = 0$, the integration constant $C_2$ vanishes. The constant $C$ is directly proportional to the total energy of the knot (mass $M$) and inversely proportional to the surface tension of the brane $T_b$: $C = - \frac{G M}{T_b}$. The gravitational force $\mathbf{F}_g$ acting on a test particle of mass $m$ inside the brane is the direct gradient of the potential energy $V_g(r)$, rigidly defined through the work done against the tension of the substrate as $V_g(r) = T_b m w(r)$. Hence:

$$\mathbf{F}_g = - \nabla V_g(r) = - T_b m \nabla w(r) = - \frac{G M m}{r^2} \hat{\mathbf{r}}$$

In this manner, Newton's inverse-square law is derived not from the postulate of exchanging hypothetical particles (gravitons), but as a direct geometric projection of the transverse, three-dimensional deflection profile of the elastic continuum.

## 6.2. Formalized Elastodynamics of the 3-Brane: Nonlinear Deflection in $\mathbb{R}^4$

To correctly describe the drastic deflection of the three-dimensional continuum of the substrate in the orthogonal direction (the $x^4$ dimension), classical linear elasticity theory must be replaced by the rigorous formalism of large deformations. In the TSM model, the 3-brane is not a two-dimensional shell, but a fully fledged three-dimensional isotropic space embedded in $\mathbb{R}^4$.

**1. The Green-St. Venant Strain Tensor for the 3-Brane**
Let $\mathbf{x} = (x^1, x^2, x^3)$ denote the coordinates inside the flat 3-brane, $u_a(\mathbf{x})$ the intra-brane displacement vector, and $w(\mathbf{x})$ the scalar deflection of the membrane in the direction of the fourth dimension $x^4$. The rigorous measure of geometric deformation that accounts for the coupling of dimensions is the finite Green-St. Venant strain tensor $E_{ab}$ (where indices $a, b \in \{1, 2, 3\}$):

$$E_{ab} = \frac{1}{2} (\partial_a u_b + \partial_b u_a + \partial_a w \partial_b w)$$

This equation rigorously defines the fact that any physical "pushing" of the substrate into the $x^4$ dimension (represented by the gradient $\partial_a w$) automatically and nonlinearly stretches the 3-brane within its own spatial dimensions.

**2. Three-Dimensional Compatibility Equations and the Generalized Monge-Ampère Operator**
In a three-dimensional 3-brane, introducing a scalar Airy stress function (appropriate for 2D) is mathematically insufficient. To guarantee the continuity of the medium (the absence of physical ruptures in the 0-Matrix), the strain tensor $E_{ab}$ must strictly satisfy the three-dimensional Saint-Venant compatibility equations.

Using the three-dimensional Levi-Civita symbol $\epsilon^{acd}$, this condition is written strictly as:

$$\epsilon^{acd} \epsilon^{bef} \partial_c \partial_e E_{df} = 0$$

Substituting our definition of the nonlinear tensor $E_{ab}$ into this equation, the derivatives of the intra-brane displacements ($u_a$) identically vanish. Only the nonlinear coupling term remains, which defines the strict, three-dimensional analogue of the Monge-Ampère bracket for the 3-brane, represented by the torsion source tensor $S^{ab}[w]$:

$$S^{ab}[w] = - \frac{1}{2} \epsilon^{acd} \epsilon^{bef} \partial_c \partial_e w \partial_d \partial_f w$$

**3. The Beltrami Stress Tensor and the Full Coupled System**
To satisfy the internal equilibrium condition $\partial_b \sigma^{ab} = 0$, instead of a scalar function, we introduce a symmetric Beltrami stress function tensor $\Phi_{cd}$ in the three-dimensional 0-Matrix, from which the macroscopic intra-brane stress field is generated:

$$\sigma^{ab} = \epsilon^{acd} \epsilon^{bef} \partial_c \partial_e \Phi_{df}$$

Integrating the above derivations, we obtain the final, rigorous, three-dimensional analogue of the Föppl-von Kármán equations describing the gravitational tension of the 3-brane:

$$D \nabla^4 w = \sigma^{ab} \partial_a \partial_b w + q(\mathbf{r})$$

$$\epsilon^{acd} \epsilon^{bef} \partial_c \partial_e (\mathbb{C}^{-1}_{dfpq} \sigma^{pq}) = S^{ab}[w]$$

Where $\nabla^4 = (\partial_1^2 + \partial_2^2 + \partial_3^2)^2$ is the three-dimensional biharmonic operator, $\mathbb{C}^{-1}$ is the elastic compliance tensor of the 0-Matrix, and $q(\mathbf{r})$ is the orthogonal load generated by the knot. The flexural rigidity of the 3-brane volume $D$ is an explicit material parameter structurally defined as:

$$D = \frac{E h^3}{12(1-\nu^2)}$$

where $E$ represents the Young's modulus of the pure substrate, and $\nu$ is the Poisson's ratio.

In order to maintain full covariance and computational feasibility, the elastic compliance tensor $\mathbb{C}^{-1}_{dfpq}$ for the isotropic 0-Matrix is explicitly determined by projection onto the metric tensor of the gravitational background $g_{df}$, which reduces the left side of the compatibility equation to the form:

$$\mathbb{C}^{-1}_{dfpq} \sigma^{pq} = \frac{1+\nu}{E} \sigma_{df} - \frac{\nu}{E} \sigma^c_c g_{df}$$

where $\sigma^c_c = \text{Tr}(\sigma)$ represents the trace of the stress tensor (the hydrostatic pressure of the substrate).

In turn, the $J_2$ invariant, which governs the nonlinear stiffening of the effective shear modulus $\mu_{\text{eff}}$, is defined as the second invariant of the stress deviator tensor $s^{ab}$:

$$J_2 = \frac{1}{2} s_{ab} s^{ab}$$

where the deviator tensor $s^{ab}$ represents pure shear stresses, isolated from the volumetric pressure, defined as:

$$s^{ab} = \sigma^{ab} - \frac{1}{3} \sigma^c_c g^{ab}$$

The parameter $h$ appearing in the definition of the flexural rigidity $D$ gains a profound interpretation in the three-dimensional formalism of $\mathbb{R}^4$: it is not the thickness of a physical shell, but rather the width of the energy localization function of the 3-brane in the orthogonal direction $x^4$. This scale is closely linked to the packing density of 0-particles within the Wigner-Seitz cell and corresponds to the Planck scale $l_{\text{P}}$.

The nonlinear coupling imposes an asymptotic stiffening of the background. As local pressures increase, when the second invariant of the stress deviator ($J_2$) approaches a critical value $J_{2,\text{crit}}$, the effective transverse elasticity modulus $\mu_{\text{eff}}$ grows nonlinearly according to the relation:

$$\mu_{\text{eff}}(J_2) = \frac{\mu_0}{1 - \left(\frac{J_2}{J_{2,\text{crit}}}\right)^2}$$

As $J_2 \to J_{2,\text{crit}}$, the material resistance of the 0-Matrix approaches infinity ($\mu_{\text{eff}} \to \infty$). This implies that the continuum exerts absolute resistance against further extension, forcing the existence of a minimum radius of curvature $R_{\text{min}}$ for any concentration of energy. A mathematical singularity of type $1/r$ with an infinite gravitational density is physically impossible in TSM.

## 6.3. Topological Plasmoids instead of Black Holes

The consequence of the breakdown of singularities is a redefinition of compact objects. The concept of a "Black Hole" as a geometric hole in spacetime is replaced by the concept of a **Topological Plasmoid**. A plasmoid is a finite, stable, and ultra-dense physical object in which 0-particles under the influence of extreme gravitational pressures have reached a state of absolute structural jamming (*jamming*). This state does not result from the internal, isolated jamming of the motion of individual 0-particles, but is a mechanical effect of the drastic spatial restriction of their interaction spheres within an extremely compressed network.

* **The Event Horizon as a Phase Boundary:** The horizon is not a mathematical curtain of no return, but a physical boundary of the substrate's phase transition. Outside this edge, the 0-Matrix retains its full elastic properties, allowing the free propagation of waves. Inside the boundary, due to extreme packing, the substrate transitions into a state of a rigid quasicrystalline system. Light (a transverse wave) entering this zone does not fall into a singularity, but undergoes immediate, complete dispersion on extreme stress gradients and conversion into lattice vibrations of the Plasmoid.
* **The Mechanism of Galactic Jets:** Since the Plasmoid is a dynamic, compressed knot, stress fluctuations constantly occur within it. When the local internal pressure exceeds the strength of the topological lock, the 0-Matrix violently releases the excess accumulated potential energy. This release occurs in a highly anisotropic manner—via the ejection of compressed matter and longitudinal modes along the axis of least mechanical resistance (the rotation axis of the system), which telescopes register as galactic jets.

## 6.4. Galactic Dynamics: Torsional Dragging and the Elimination of Dark Matter

The introduction of the Plasmoid as a rotating physical knot with a gigantic angular momentum allows us to resolve key dynamic anomalies at macroscopic scales without the need to introduce exotic Dark Matter particles.

### 6.4.1. Torsional Dragging and Flat Stellar Rotation Curves

In classical astrophysics, the linear velocity of stars on the peripheries of galaxies should decrease with distance $r$ according to Keplerian dynamics ($v \propto 1/\sqrt{r}$). However, observations show that the rotation curve stabilizes at a constant level ($v \approx \text{const}$).

In TSM, this phenomenon is a direct consequence of Torsional Dragging (the hydro-elastodynamic analogue of the Lense-Thirring effect). The central Plasmoid, rotating at immense speed, literally "screws in" the surrounding 0-Matrix due to the extreme topological viscosity of the system, generating a macroscopic rotational shear field $\bar{\beta}$. This field propagates deep into the 3-brane, and its direct kinematic manifestation is the local angular velocity profile of the substrate $\Omega(r)$. Stars located on the outskirts of the galaxy are not held solely by the radial force of transverse tension $\mathbf{F}_g = -\nabla w$, but move inside a rotating vortex of the substrate itself. The net linear velocity of a star $v_{\text{total}}$ is a superposition of its local orbital velocity and the drift velocity of the entraining background.

To explicitly derive the drift velocity component $v_{\text{drift}}(\bar{\beta})$, we consider the momentum balance equation for the spherical component (longitudinal $\theta$) under steady-state conditions. The central Plasmoid, rotating with angular velocity $\Omega_0$ at the critical radius $R_{\text{min}}$, imposes an angular velocity field on the substrate $\Omega(r)$. The transmission equation of angular momentum through the visco-elastic structure of the 0-Matrix takes the form:

$$\frac{d}{dr} \left( r^3 \mu_{\text{eff}}(r) \frac{d\Omega(r)}{dr} \right) = 0$$

Where $\mu_{\text{eff}}(r)$ is the radial profile of the nonlinear shear modulus, induced by the gravitational deflection of the dense center. In the near zone, where nonlinear stresses dominate, the profile $\mu_{\text{eff}}(r)$ exhibits a power-law decay, forcing a slow decay of the background angular velocity. The solution to this equation defines the background drift field as:

$$v_{\text{drift}}(r) = r \Omega(r) = r \left( \Omega_0 - \int_{R_{\text{min}}}^{r} \frac{C_{\text{torsion}}}{x^3 \mu_{\text{eff}}(x)} dx \right)$$

Where $C_{\text{torsion}}$ is an integration constant dependent on the angular momentum of the Plasmoid. On the peripheries of the galaxy, this function perfectly compensates for the Keplerian drop in the orbital velocity of test knots ($v_{\text{orb}} \propto 1/\sqrt{r}$), forcing the asymptotic stabilization of the net linear velocity of stars ($v_{\text{total}} = v_{\text{orb}} + v_{\text{drift}} \approx \text{const}$). The spatial decay of the nonlinear rotational field $\bar{\beta}$ in the elastic membrane ideally cancels out the deficit of classical radial attraction, completely eliminating the need to introduce hypothetical Dark Matter particles.

### 6.4.2. Behavior of Stars Near the Galactic Center (S2 Orbit)

The nonlinear regime of TSM finds direct confirmation in the trajectories of stars orbiting in the immediate vicinity of the central Plasmoid Sgr A*, such as the star S2. As the star approaches pericenter, the system leaves the linear Laplace limit and enters the zone described by the Föppl-von Kármán equations.

Due to the nonlinear stiffening of the substrate ($\mu_{\text{eff}} \to \infty$), the actual gravitational potential becomes deeper, and the attractive force gains an additional elastic term $\delta \mathbf{F}(\mu_{\text{eff}})$, deviating from the pure $1/r^2$ dependence. The explicit form of the net gravitational force vector in this nonlinear region is given by:

$$\mathbf{F}_{\text{TSM}}(r) = - \left( \frac{G M m}{r^2} + \frac{\mathcal{A}_{\text{nielin}}(J_2)}{r^4} \right) \hat{\mathbf{r}}$$

where $\mathcal{A}_{\text{nielin}}$ is a nonlinear elastic coupling coefficient determined directly from the local gradient of the $J_2$ invariant and the evolution of the $\mu_{\text{eff}}$ modulus. According to classical mechanics, any higher power-law correction to the Newtonian potential violates Bertrand's theorem, forcing rapid apsidal precession of the orbit. The rosette motion of the S2 star and the precession of its perihelion are natural consequences in TSM of the nonlinear material resistance of the stressed network, rather than a purely relativistic metric correction.

## 6.5. Alternative to Expansion: Redshift as Distance-Dependent Wave Dispersion (Consistency with Postulate 0.7)

This section categorically abolishes the concept of the "expansion of space" and the associated Dark Energy hypothesis. According to Postulate 0.7, the Universe never passed through a primordial singularity, nor is it in a state of global, post-explosive relaxation of stresses. The cosmic 0-Matrix as a whole is a closed system of constant 4D volume, remaining in a state of macroscopic equilibrium of dynamic pressures.

Since the physical distances between network nodes are stationary on average at the cosmological scale, the observed redshift of the spectral lines of distant galaxies must be interpreted as a purely material phenomenon—the distance-dependent dispersion of transverse waves within a visco-elastic continuum.

### 6.5.1. Mechanism of Viscous Loss of Wave Momentum

No real medium possessing a discrete, granular structure (a network of 0-particles) is a perfectly lossless environment for the propagation of wave perturbations over extreme distances. The transmission of shear strain (the propagation of a photon represented by the $\beta$ mode) between successive Wigner-Seitz cells involves a microscopic, visco-elastic resistance of the substrate.

As the wave packet traverses a distance $r$, its energy $E$ (and consequently its frequency $\nu$) undergoes a slow, systematic dissipation due to the finite material compliance of the background. The progression of this process is described by the differential structural damping equation:

$$\frac{dE}{dr} = - \zeta E$$

where $\zeta$ is the spatial damping constant, determined by the internal bulk viscosity and shear modulus of the 0-Matrix. Integrating this equation along the optical path of the photon from the distant source to the observer yields an exponential dependence:

$$\nu_{\text{obs}} = \nu_{\text{em}} \exp(-\zeta r)$$

For local distances (on the scale of several tens of megaparsecs), where the total damping is small ($\zeta r \ll 1$), expanding the exponential function into a Taylor series to the first non-zero term gives a linear relation:

$$\frac{\nu_{\text{em}} - \nu_{\text{obs}}}{\nu_{\text{obs}}} = \exp(\zeta r) - 1 \approx \zeta r$$

Defining the standard redshift parameter $z = \frac{\lambda_{\text{obs}} - \lambda_{\text{em}}}{\lambda_{\text{em}}} = \frac{\nu_{\text{em}} - \nu_{\text{obs}}}{\nu_{\text{obs}}}$, we obtain the direct dependence:

$$z \approx \zeta r$$

Hubble's classical law is thus completely stripped of its kinematic foundation (there is no recession of galaxies). The Hubble constant $H_0$ becomes a strictly material parameter, describing the unit damping capacity of transverse waves by the 0-Matrix: $H_0 = \zeta c_{\perp}$, where $c_{\perp}$ is the critical propagation velocity within the brane.

### 6.5.2. Refutation of Dark Energy and Inter-Mode Wave Conversion

The exponential nature of the damping $\exp(-\zeta r)$ becomes the key to explaining the luminosity anomalies of Type Ia Supernovae without introducing Dark Energy. Light traveling from objects located at extreme cosmological distances (billions of light-years) enters the nonlinear regime of exponential damping. The energy drop of photons occurs faster there than the linear extrapolation of the Newton-Hubble law, causing supernovae to reach terrestrial detectors fainter and more strongly redshifted. Standard cosmology, misinterpreting this fact as a kinematic acceleration, is forced to postulate dark energy. In TSM, this is a pure effect of the nonlinear resistance of the medium.

To make this model consistent and robust against classical objections raised against "tired light" theories (such as the blurring of images of distant stars due to scattering), TSM introduces the mechanism of **nonlinear inter-mode conversion**. The energy lost by the transverse wave (the shear mode $\beta$) is not dissipated into chaotic thermal vibrations of particles (which would cause distortions of the wave front), but is instead—via nonlinear network couplings—transformed into an orthogonal, longitudinal compression mode ($\alpha$).

In this way, the energy "lost" by light directly feeds the background pressure component in the fourth dimension, sustaining the continuous fluctuations and creation of new deformations described in Postulate 0.7. The system closes its energy cycle, remaining macroscopically static and eternal.

## 6.6. Physical Nature of the Constant $c$ and Stress Waves (LIGO)

In Topological 0-Matrix (Substrate) Mechanics, the constant $c$ loses its mystical status as an inviolable geometric barrier of spacetime itself. It is reduced to the role of the **critical propagation velocity of transverse waves ($c_{\perp}$)** within the elastic continuum of the 3-brane.

### 6.6.1. Mechanical Origin of Relativistic Effects

This velocity is rigidly defined by the mechanical parameters of the substrate—its local shear stiffness modulus $\mu$ and its mass inertial density $\rho$:

$$c_{\perp} = \sqrt{\frac{\mu}{\rho}}$$

Each elementary particle (being a local topological knot) maintains its internal structural coherence due to the continuous exchange of stress information between its constituent 0-particles. When a knot is accelerated to velocities close to $c_{\perp}$ inside the 3-brane, it begins to catch up with the front of its own stress wave. The medium ahead of the moving knot undergoes nonlinear compression and stiffening, creating a structural equivalent of a Mach cone.

The classical relativistic effects observed as a result—the apparent asymptotic increase in inertial mass and time dilation—do not stem from changes in abstract spacetime, but are **pure hydro-elastodynamic phenomena**. The particle encounters powerful wave resistance from the medium, and the internal oscillatory processes within the knot slow down due to the elongation of stress propagation paths in the compressed substrate.

### 6.6.2. Superluminality in 4D and Interferometric Registrations

Because the velocity limit to the value $c_{\perp}$ results directly from the density and shear stiffness within the three-dimensional brane, this limit **does not apply in the orthogonal direction ($x^4$)**. The $x^4$ dimension (the surrounding *Bulk*) exhibits the characteristics of a superfluid condensate of 0-particles, devoid of a dense network of fermionic knots, which allows for the propagation of longitudinal modes ($\alpha$) and the movement of structures at velocities significantly exceeding $c_{\perp}$. What we register in 3D as a relativistic particle is merely the projection (shadow) of a higher, four-dimensional dynamic process.

In this view, interferometric experiments such as LIGO do not record the "rippling of empty geometry itself," but rather actual, powerful stress-wave fronts of transverse stresses propagating through the substrate at the material velocity $c_{\perp}$. These waves are generated during rapid, nonlinear structural reorganizations—for example, during the merger of two Topological Plasmoids, when their locked phase zones collide, generating macroscopic "stress booms" in the elastic background of the Universe.

## 6.7. Summary of Chapter 6

* **Ontology of Gravity as Elastic Tension:** Gravity is stripped of its relativistic geometric abstraction and defined as an actual, mechanical deformation and transverse tension of the three-dimensional substrate (3-brane) directed orthogonally toward the fourth spatial dimension ($x^4$). Einstein's equations are thus replaced by the classical elastodynamics of continuous media.
* **Transition to the Nonlinear Regime (Föppl-von Kármán):** While weak gravitational fields (the Newtonian limit) are correctly described by the linear Laplace equation ($\nabla^2 w = 0$), near extremely dense knots, the deflection of the membrane becomes so powerful that it requires the application of the nonlinear Föppl-von Kármán equations. The coupling of bending with intra-brane stretching causes an asymptotic increase in the effective stiffness of the substrate ($\mu_{\text{eff}}$), which effectively blocks gravitational collapse.
* **Elimination of Singularities in Favor of Plasmoids:** TSM categorically rejects the existence of points of infinite density (black holes). In the centers of galaxies and collapsed neutron stars, under the influence of gigantic pressure, Topological Plasmoids are formed—stable structures of finite radius in a state of maximum mechanical structural jamming (*structural jamming*) of the Wigner-Seitz cells.
* **Demystification of the Speed of Light ($c$):** The speed $c$ ceases to be an universal constant of geometry itself and becomes the material speed of sound for transverse (shear) waves inside the 3-brane. The asymptotic wave resistance when approaching $c$ (classical relativistic mass increase) is a purely hydrodynamic effect—a topological knot moving in the substrate catches up with its own tension wave, creating a structural equivalent of an acoustic Mach cone.
* **Superluminality in the Orthogonal Dimension ($x^4$):** Since the velocity limitation to $c_{\perp}$ results directly from the shear stiffness of the three-dimensional substrate, this limit does not apply in the perpendicular direction. The surrounding *Bulk* space ($x^4$) exhibits characteristics of a superfluid condensate devoid of fermionic knots, allowing the propagation of longitudinal modes ($\alpha$) and the movement of structures at superluminal velocities ($v > c_{\perp}$).
* **The Nature of Gravitational Waves in the LIGO Interpretation:** Interferometric experiments do not record oscillations of empty spacetime, but rather powerful, macroscopic stress-wave fronts of transverse stresses propagating in the substrate at the material velocity $c_{\perp}$ due to violent processes of knot reorganization (e.g., the merging of Plasmoids). This is subject to potential falsification through the study of anomalous hydrodynamic drag and nonlinear orbital deviations of tight binary systems.