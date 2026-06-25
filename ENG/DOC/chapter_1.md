---
title: "Topological 0-Matrix \\raisebox{-0.3ex}{\\small (Substrate)} Mechanics (TSM)"
subtitle: "Chapter 1: Elasto-mechanics of the 0-Matrix: Emergence of Time, Metric, and Relativistic Kinematics"
author: "Piotr R. Szopiński (Peter R. [sho-peen-skee]) \\\ \\vspace{0.2cm} \\large Wrocław, 2026"
format:
  pdf:
    documentclass: scrartcl
    toc: true
    number-sections: true
    number-depth: 4          # ile poziomów numerować
    classoption: oneside       # Wyłącza asymetrię stron parzystych/nieparzystych
    geometry:
      - top=2.5cm              # Równy margines górny
      - bottom=2.5cm           # Równy margines dolny
      - left=2.5cm             # Równy margines lewy
      - right=2.5cm            # Równy margines prawy
    lang: en
    include-in-header:
       text: |
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{} % Wyczyszczenie domyślnych nagłówków i stopek
        \renewcommand{\headrulewidth}{0pt} % Usunięcie linii poziomej w nagłówku
        \renewcommand{\footrulewidth}{0.5pt} % Opcjonalnie: cienka linia nad stopką
        
        % Konfiguracja stopki:
        % [L] - lewa strona, [C] - środek, [R] - prawa strona
        \fancyfoot[L]{%
          {\small Piotr R. Szopiński (Peter R. [sho-peen-skee])} \\
          {\footnotesize Published under CC BY 4.0 Int.}
        }
    keep-tex: true
    header-includes:
      - \usepackage{chngcntr}
      - \counterwithin{equation}{subsection}
      - \renewcommand{\theequation}{\thesubsection.\arabic{equation}}
      # Poniżej zmiany rozmiaru:
      - \addtokomafont{title}{\huge\bfseries}
      - \addtokomafont{subtitle}{\Large\mdseries\itshape}
---
<!-- ver:4.7.1-->
# Elasto-mechanics of the 0-Matrix: Emergence of Time, Metric, and Relativistic Kinematics {#sec:rom-tsm}

## Introduction and Conceptual Framework {#sub-wprowadzenie}

This chapter constitutes the formal core of the Topological Substrate Mechanics (TSM) theory, implementing a rigorous mathematical and physical apparatus for its conceptual foundations. While previous considerations established the ontological necessity of a sub-Planckian underlying medium, focus here is concentrated on the mathematical reconstruction of macroscopic physical laws from a dynamic geometric network—the 0-Matrix. The TSM paradigm categorically rejects the notion of empty spacetime as a fundamental physical background. Instead, through the rigorous apparatus of discrete elasto-mechanics, it demonstrates that macroscopic time, the effective gravitational metric $g_{ab}$, and relativistic transformations are not primary attributes of reality, but rather secondary (emergent) phenomena arising from the averaged states of stress, strain, and topological configurations of the jammed 4D substrate.

The formalized argument aimed at reconstructing the macroscopic continuum reflects a strict reductionist sequence, divided into four key stages:

1. **Substrate architecture and the genesis of time:** The chapter opens with an analysis of the microstructure of the 0-Matrix, based on the oscillation spheres of 0-particles. The mechanism of their geometric, global jamming, which forms an isotropic 3-brane, is presented. Only on this physical substrate, through the mathematical formalism of averaging stochastic fluctuations, is the Effective Substrate Density defined. Macroscopic time is derived here not as a continuum, but as a canonical measure of the succession of successive network states.
2. **Wave elastodynamics and the speed of light:** Instead of postulating the constancy of the speed of light as an overriding axiom, the formalism derives it directly from the material properties of the substrate. The speed $c$ is defined as the propagation velocity of transverse shear disturbances in the mechanically jammed 4D structure, and its local variability ($c_{\perp}$) is linked to the material constants of the network.
3. **Emergence of geometry and relativistic kinematics:** In the realm of non-linear kinematics, the chapter proves that the effective macroscopic metric $g_{ab}$ is a mathematical description of the local strains of the Substrate. Consequently, relativistic time dilation gains a purely mechanical interpretation as an isotropic crowding (densification) of the substrate. This allows for a full derivation of relativistic transformations directly from the laws governing the elasto-mechanics of a degenerate crystal lattice, without appealing to the postulates of Special Relativity.
4. **Field equations and the axiom of matter:** In the domain of wave dynamics, the chapter assimilates the mathematical solutions of General Relativity, yet without its ontological assumptions—the field equations here become a description of the stress states of the network in a dual elastodynamic regime (elastic waves versus non-linear jamming). The culmination of this description is the definition of the axiom of matter: particles are formalized as stable solitonic configurations (local zones of topological jamming). This allows for a rigorous, geometric separation of mass (as a local density defect of the substrate) from electric charge (as its topological twist).

## Microstructure of the 0-Matrix and the State of Global Jamming {#sec-1-2}

The starting point for Topological Substrate Mechanics (TSM) is the complete rejection of the notion of a primary, continuous spacetime as a fundamental physical background. The sole objective ontological reality is the 0-Matrix—a degenerate, vibrating crystal lattice. All relativistic phenomena and interactions manifested at the macroscopic scale do not constitute features of space itself, but are the emergent result of stress states, deformations, and wave dynamics of this primary, hidden structure.

### Lattice Geometry: 0-Particles in Oscillation Spheres as the Foundation of the Substrate {#sec-1-2-1}

In contrast to classical ether models, the microstructure of the 0-Matrix exhibits a rigorous, quasi-crystalline lattice order, functioning in its ground state as a rigid, elastic topological glass in the four-dimensional Euclidean space of the Substrate. At the fundamental level, a single 0-particle is an indivisible object of constant volume $V_{00}$, topologically confined within its assigned lattice node. Its volume satisfies the condition of the sub-Planckian scale:

$$0 < V_{00} \ll V_{\text{Planck}}$$ {#eq-wz1-1}

* *In the notational convention of the entire chapter, a double subscript `00` denotes a microscopic quantity internal to a single 0-particle and independent of its environment (e.g., $V_{00}$, $m_{00}$, $v_{00}$)—in contrast to a single subscript `0`, which is reserved for quantities determined by the collective context of the network, whether at the level of cell geometry ($R_0$) or macroscopic fields of the Zero State ($\phi_0$, $\rho_0$, $T_0$, $P_0$).*

In the low- and intermediate-energy regime, individual elements of the substrate are devoid of translational freedom, which precludes phenomena such as macroscopic flow through the medium. A 0-particle can execute motions exclusively within a strictly bounded space, defined as a configuration cell (oscillation sphere). Formally, if $\mathbf{X}_i$ denotes the static equilibrium position of the $i$-th node in 4D, then the instantaneous displacement of the 0-particle $\mathbf{u}_i$ is subject to a rigorous geometric constraint:

$$|\mathbf{u}_i| = |\mathbf{x}_i - \mathbf{X}_i| \le R_0$$ {#eq-wz1-2}

where $R_0$ represents the radius of the sphere in the state of full relaxation of the 0-Matrix. The boundary of this sphere is not a potential barrier in the quantum sense, but a hard topological constraint resulting from the maximal geometric packing and physical proximity of other zones in the degenerate lattice.

For complete clarity of the model, TSM mechanics introduces at this point a rigorous distinction between the **absolutely hard core of the 0-particle** and its **sphere of oscillation (interactions)**:

* **The core** constitutes a physical, impenetrable, and fundamentally indivisible body of volume $V_{00}$. It possesses no internal structure, and its volume does not undergo any compression even under conditions of extreme pressure. It also possesses an invariant mass $m_{00}$ and speed $v_{00}=\text{const}$. These fundamental microscopic properties are identical for all 0-particles and independent of the macroscopic state of the substrate. The volume $V_{00}$, mass $m_{00}$, and speed $v_{00}$ are a **primary axiom** of the TSM model: they do not emerge from the lattice geometry or collision dynamics, but represent an ontologically primary quantity defining the energy scale of the 0-Matrix, analogously to the elementary charge in electrodynamics.
* **The oscillation sphere**, in turn, defines the volume of the configuration cell in the full 4D space, $V_0 = \frac{\pi^2}{2}R_0^4$ (the volume of a 4-ball), which constitutes the effective unit volume per single lattice node in the relaxed state, within which the core executes its chaotic kinetics.

The cores of neighboring 0-particles in the linear regime of the substrate never undergo direct, static contact. The approach of the cores encounters an asymptotically increasing force barrier, which is an emergent consequence of their own confinement and ultra-fast, elastic collisions within the densely packed crystal lattice. The sphere of interaction is thus in essence a kinetic barrier, rather than a force field in the classical sense.

#### Cell Microdynamics: The Sinai Billiards Mechanism {#sec-1-2-1-1}

The geometry of the configuration cell determines the unique character of the internal motion of the 0-particle. Its walls are not formed by a smooth, empty cavity, but by the convex interaction spheres of neighboring 0-particles. Motion within a region bounded by such convex dispersing obstacles is classified as Sinai billiards (a mathematical model of the Lorentz gas). The physical consistency of the billiard model requires satisfying the geometric condition $r_{00}<R_0$, where $r_{00}$ denotes the radius of the 0-particle core, related to its volume by $V_{00}=\frac{\pi^2}{2}r_{00}^4$ (the volume of a 4-ball). The ratio $r_{00}/R_0$ microscopically determines both the mean free path $\ell$ and the 4-dimensional scattering cross-section $S_{4D}$—parameters that remain phenomenologically open in the subsequent derivation (@sec-1-3-3), but whose physical scale is thereby bounded from below by $r_{00}>0$ and from above by $r_{00}<R_0<l_P$.

Unlike billiards with smooth walls (e.g., integrable motion in an empty sphere bypassing the center), a dispersing billiard of this type exhibits a strong mixing property and full ergodicity. Regardless of the initial condition, the spatial distribution of the particle's presence converges exponentially fast to a uniform equilibrium distribution over the entire available cell volume. This motion is strictly deterministic, yet stochastically unpredictable for a macroscopic observer due to the sub-Planckian spatial scale.

#### Emergence of the Macroscopic Spherical Shield {#sec-1-2-1-2}

The key factor transforming this microdynamics into stable macroscopic structures is the asymmetry of timescales. The oscillation frequency of the 0-particle, expressed in virtual seconds, exceeds macroscopically distinguishable units of time by dozens of orders of magnitude. The time required to achieve complete spatial mixing from the perspective of emergent time is practically zero.

Thus, the 0-particle does not "traverse" its sphere in observable time; it fills it with its physical presence almost instantaneously. From the outside, this ultra-fast oscillation manifests as a dynamic, impenetrable shield of perfect spherical symmetry. This establishes a strict division between the chaotic internal dynamics and the averaged macroscopic phenomena, where the local density of the substrate is a derivative of the concentration of these spheres.

#### Critical Regime and the Critical Displacement Clause {#sec-1-2-1-3}

The state of fundamental confinement changes exclusively under critical conditions—under the influence of extreme external pressure or strong topological twisting. When local shear stresses exceed a critical plasticity threshold, the Critical Displacement Clause is activated.

Since the asymptotic force barrier prohibits physical contact of the cores, this process is strictly collective. Displacement is realized as a coupled, synchronous shift of a cluster of 0-particles in the form of a solitonic wave, utilizing rarefaction regions to compensate for the pressure. The lattice elements physically change position (gaining a new neighborhood topology) without violating the minimum interparticle distance. The moment the stresses drop below the threshold, the 0-particles immediately regain their interaction spheres and return to the state of confined micro-oscillations, concluding the rearrangement process.

### Global Jamming Mechanism and the Emergence of the Isotropic 3-Brane {#sec-1-2-2}

The base state of the 0-Matrix, enabling the existence of the observable world, is the state of **global jamming** (*structural jamming*). Upon reaching a critical packing density $\phi \ge \phi_c$, the independent degrees of freedom of the 0-particles become mutually locked by topological contact forces in four spatial dimensions.

As a result of this isotropic jamming, non-linear interactions lead to the emergence of a stable, three-dimensional hypersurface—an isotropic 3-brane (a region of local deflection induced by a disturbance in the Zero State). To an internal observer, the 3-brane appears as a three-dimensional metric. The macroscopic stress tensor of the network in the state of pure jamming takes the form:

$$T_{IJ}^{(0)} = -P_0 \delta_{IJ}$$ {#eq-sek1-1-tens-zaklesz}

where:

* $I,J \in \{1,2,3,4\}$—spatial indices in the full, 4-dimensional Euclidean space of the Substrate,
* $\delta_{IJ}$—the Kronecker delta, reflecting the perfect isotropy of the jammed state (the absence of a preferred direction of stress),
* $P_0$—the isotropic jamming pressure in the 4D space, treated in this chapter as a **reference parameter of the Zero State**, on equal footing with $\phi_0$, $T_0$ from (@sec-1-2-3), and $\rho_0$ from (@sec-1-3-2). Like these quantities, $P_0$ is not derived here from a deeper microscopic theory, but is taken as a phenomenological property of the ground state of the 0-Matrix at the jamming threshold $\phi\ge\phi_c$—in accordance with the practice of jamming physics, where the threshold pressure is an empirical quantity of the system rather than one analytically derived.

The perfect symmetry of the tensor masks the discrete nature of the matrix from measuring instruments.

## Emergence of Macroscopic Time from Sub-Planckian Dynamics {#sec-1-2a}

### The Boundary of Cognition and the Elimination of Stochastic Fluctuations {#sec-1-2a-1}

In the ground state, the 0-Matrix is characterized by permanent, microscopic oscillations of the substrate particles around equilibrium positions. This phenomenon, described at the microscale as Sinai billiards (@sec-1-2-1-1), generates an incoherent background noise defined as the fundamental temperature of the Substrate ($T_{\text{sub}}$). In accordance with the principle of empirical rigor, the TSM model categorically rejects any attempt to define macroscopic time through these primary, chaotic oscillations.

All wave effects and local frequency variations occurring directly on individual lattice elements are sub-Planckian in nature—occurring below the boundary of the Planck scale ($\sim 10^{-35}$ m)—and are stochastically unpredictable. Any attempt to define them operationally from a macroscopic standpoint is devoid of measurable meaning. For this reason, the TSM model foregoes postulating microscopic kinematic dependencies of individual 0-particles, transferring the entire weight of the formalism to the macroscopic elasto-mechanical averaging of the degenerate crystal lattice.

### Mathematical Formalism of Averaging—Effective Substrate Density {#sec-1-2a-2}

The key parameter linking the discrete dynamics of the network with the observable macroscopic reality is the fundamental packing density of the 0-particles, defined as a continuous field in the full, 4-dimensional space of the Substrate: $\phi(\mathbf{X}) = \phi(x^1, x^2, x^3, x^4)$. The macroscopic averaging operator smooths out local, discontinuous density anomalies around individual lattice cells using a convolution with a window function $W$ with a cutoff scale equal to the Planck scale ($\Lambda_{\text{Planck}}$):

$$\langle\phi(\mathbf{X})\rangle_{\text{macro}} = \int_{\mathbb{R}^4} \phi(\mathbf{X}') \, W(\mathbf{X} - \mathbf{X}', \Lambda_{\text{Planck}}) \, d^4\mathbf{X}'$$ {#eq-1-2-1}

where:

* $\mathbf{X} = (x^1, x^2, x^3, x^4)$—the position 4-vector in the Euclidean space of the 0-Matrix,
* $\phi(\mathbf{X}')$—the raw, microscopic local density of the substrate in the full 4D space,
* $W$—a normalized, 4-dimensional transition function (filtering window) that eliminates sub-Planckian noise,
* $\Lambda_{\text{Planck}}$—the spatial cutoff scale.

Since all physical measuring instruments (clocks, detectors) are formed topological nodes confined within the jammed 3-brane, the only experimentally accessible value is $\langle\phi(\mathbf{X})\rangle_{\text{macro}}$ restricted to this hypersurface. In the unperturbed state, the brane occupies the hypersurface $x^4 = 0$, whereas in the presence of local deformations and stresses, it is deflected to the position $x^4 = w(\mathbf{x})$. The observable macroscopic packing density at a projected point of the three-dimensional space $\mathbf{x} = (x^1, x^2, x^3)$ is therefore expressed by the projection:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} \equiv \left.\langle\phi(\mathbf{X})\rangle_{\text{macro}}\right|_{x^4 = w(\mathbf{x})}$$ {#eq-1-2-2}

To preserve full information about the state of the 4D medium within the deflected hypersurface, we assume that the window function $W$ is mathematically separable with respect to the brane components and the orthogonal dimension: $W(\mathbf{X}-\mathbf{X}', \Lambda_{\text{Planck}}) = W_3(\mathbf{x}-\mathbf{x}', \Lambda_{\text{Planck}}) \cdot W_4(x^4 - \xi, \Lambda_{\text{Planck}})$. This allows us to define the effective 3D surface density as an integral weighted by the function $W_4$ along the orthogonal axis $\xi$ (corresponding to the coordinate $x^4$):

$$\phi_{\text{eff}}(\mathbf{x}') \equiv \int_{-\infty}^{+\infty} \phi(\mathbf{x}', \xi) \, W_4\!\left(w(\mathbf{x}') - \xi, \, \Lambda_{\text{Planck}}\right) d\xi$$ {#eq-1-2-3}

Since the characteristic thickness of the 3-brane in the orthogonal direction is of the order of the Planck scale, and the function $W_4$ rigorously eliminates contributions from outside this range, the integration is asymptotically localized in the Planckian neighborhood of the brane. Measurable results remain independent of the state of the deep structures of the 0-Matrix outside this zone. The final, operational form of the effective macroscopic density on the 3-brane takes the form of a three-dimensional convolution:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} = \int_{\mathbb{R}^3} \phi_{\text{eff}}(\mathbf{x}') \, W_3(\mathbf{x} - \mathbf{x}', \Lambda_{\text{Planck}}) \, d^3\mathbf{x}'$$ {#eq-1-2-4}

**Note on gravitational-temporal consistency:** The dependence of the effective density $\phi_{\text{eff}}$ on the brane deflection function $w(\mathbf{x})$ through the argument of the kernel $W_4$ provides a direct, mechanistic justification for the phenomenon of gravitational time dilation. A topological node (a massive object) inducing a deflection $w > 0$ locally shifts the sampling point of the function $W_4$ into a region of the substrate with higher structural pressure. This increases the value of $\langle\phi(\mathbf{x})\rangle_{\text{macro}}$ and consequently slows down the rate of local proper time in accordance with the canonical relation.

### Canonical Definition of Macroscopic Time as a Measure of the Succession of Network States {#sec-1-2-3}

In TSM mechanics, time is neither a primary, independent dimension nor an autonomous arena for the evolution of systems. Time measured macroscopically by any measuring instruments—which themselves constitute macroscopic structures composed of a network of topological nodes—is solely an operational parameter of the succession of structural changes. Its rate of passage remains strictly and inversely proportional to the effective elasto-mechanical density of the substrate.

The increment of local proper time $dt$ is expressed by the canonical equation:

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi(\mathbf{x})\rangle_{\text{macro}}}$$ {#eq-1-2-5}

where:

* $dt$—the increment of local proper time, expressed in measurement units (seconds).
* $dN$—the pure number of observed topological events. This is a fundamental indicator of system activity, defined as the sum of realized full phase cycles (e.g., spin rotations or solitonic oscillations).
* $T_0$—the calibration constant (translation coefficient). It does not hold the status of a fundamental entity; it is a metrological "translator" allowing for the mapping of the objective number of cycles ($dN$) to standard units of time adopted in macroscopic physics.
* $\phi_0$—the baseline, isotropic packing density of the 0-Matrix in the Zero State (flat space).
* $\langle\phi(\mathbf{x})\rangle_{\text{macro}}$—the averaged, local density of the substrate in the region occupied by the system.

The mechanism of time dilation follows directly from the kinematics of the structural jamming state (*structural jamming*). A local increase in the density of the substrate cells ($\langle\phi(\mathbf{x})\rangle_{\text{macro}} > \phi_0$) generates a proportionally higher elasto-mechanical resistance of the network. Tighter geometric packing drastically constrains the vibrational freedom of the confined 0-particles, which slows down energy transfer, signal propagation, and all internal relaxation processes of the physical system.

For a constant number of microscopic cycles $dN$, the increment of proper time $dt$ decreases. From the perspective of an external reference observer, the local second undergoes physical stretching (becomes longer), because the mathematical apparatus of TSM rigorously links the rate of succession of network states to the denominator of the time interval operator.

## Lattice Elastodynamics and the Microscopic Origin of the Speed of Light {#sec-1-3}

To eliminate the methodological objection of introducing the wave speed barrier $c$ as an *ad hoc* assumption, the Topological Substrate Mechanics (TSM) model derives the constant speed of light (identified as the transverse shear wave velocity $c_{\perp} \equiv c$) as an emergent quantity. This derivation is executed in two stages: first, through a rigorous description of the elasto-dynamic continuum incorporating the topological jamming state, and subsequently by coupling it with the sub-Planckian kinetics of 0-particles.

### Propagation of Shear Perturbations and Longitudinal Wave Blocking in the 4D Substrate {#sec-1-3-1}

Let us consider the ground state of the Substrate prior to brane formation. In classical elasticity theory, two primary types of waves can propagate through a continuous medium: longitudinal waves (compressions/rarefactions, governed by the bulk modulus) and transverse waves (shear, torsional, governed by the shear modulus).

As a 4-dimensional, isotropic elastic medium with a colossal collision density, the 0-Matrix is governed by the generalized Navier-Cauchy equations for displacements $\mathbf{u}(x^1, x^2, x^3, x^4)$. Here and throughout the remainder of this chapter, we adopt the following notational convention: Latin indices from the middle of the alphabet ($i,j,k,\dots$) and uppercase Latin indices ($I,J$, introduced in @sec-1-2-2) interchangeably denote the coordinates of the full, 4-dimensional Euclidean space of the Substrate and span the range $\{1,2,3,4\}$; whereas indices $a,b,c,d$, utilized from @sec-1-4 onward, are strictly reserved for the 3-dimensional hypersurface of the 3-brane ($\{1,2,3\}$). We introduce the 4-dimensional Cauchy-Green strain tensor $\epsilon_{ij}$ in the form:

$$\epsilon_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x^j} + \frac{\partial u_j}{\partial x^i} + \frac{\partial u_k}{\partial x^i} \frac{\partial u_k}{\partial x^j} \right)$$ {#eq-sek131-4wym-tensor-odkszt}

Assuming a linear elastic regime (wherein non-linear quadratic gradients are negligible prior to exceeding the topological locking threshold), the elastic energy density $\mathcal{U}$ is given by the classical Lamé formula extended to 4 dimensions (utilizing the Einstein summation convention for repeated indices):

$$\mathcal{U} = \frac{1}{2} \lambda (\epsilon_{kk})^2 + \mu \epsilon_{ij} \epsilon_{ij}$$ {#eq-sek131-gest-energ-sprezU}

Where $\lambda$ and $\mu$ are the macroscopic Lamé coefficients characterizing, respectively, the bulk elasticity (resistance to compression) and shear elasticity (resistance to shear) of the Substrate.

The equation of motion for a volume element of the matrix framework within the flat background time $t_{\text{flat}}$ can be expressed in vector form, where the differential operators $\nabla$, $\nabla \cdot$, and $\nabla^2$ operate in the full space $\mathbb{R}^4$, and $\rho_{\text{eff}}$ denotes the effective macroscopic wave density:

$$(\lambda + \mu) \nabla (\nabla \cdot \mathbf{u}) + \mu \nabla^2 \mathbf{u} = \rho_{\text{eff}} \frac{\partial^2 \mathbf{u}}{\partial t_{\text{flat}}^2}$$ {#eq-sek131-rown-ruchu-elemVosn}

At this juncture, the core mechanics of the TSM model manifest. In the geometric jamming state, the interaction spheres of the 0-particles become densely packed (while the particle cores themselves retain their free sub-Planckian dynamics). Consequently, the medium becomes **locally incompressible** with respect to macroscopic interactions. Any attempt to induce a longitudinal wave encounters an asymptotically infinite resistance, which is mathematically expressed by the first Lamé parameter tending to infinity ($\lambda \to \infty$) concurrent with the vanishing divergence of the displacement ($\nabla \cdot \mathbf{u} \to 0$).

In accordance with the generalized Helmholtz theorem in multidimensional spaces, we decompose the displacement field into an irrotational (longitudinal) component $\mathbf{u}_\parallel$ and a solenoidal (transverse) component $\mathbf{u}_\perp$:

$$\mathbf{u} = \mathbf{u}_\parallel + \mathbf{u}_\perp, \quad \text{where} \quad \frac{\partial u_j^\parallel}{\partial x^i} - \frac{\partial u_i^\parallel}{\partial x^j} = 0 \quad \text{and} \quad \frac{\partial u_i^\perp}{\partial x^i} = 0$$ {#eq-sek131-pole-wekt}

The condition of local incompressibility of the Substrate entirely eliminates longitudinal waves from the physical macroscopic spectrum. The Navier-Cauchy equation reduces exclusively to the transverse component $\mathbf{u}_\perp$, representing local shear (rotation of the interaction spheres):

$$\mu \nabla^2 \mathbf{u}_\perp = \rho_{\text{eff}} \frac{\partial^2 \mathbf{u}_\perp}{\partial t_{\text{flat}}^2} \implies \nabla^2 \mathbf{u}_\perp - \frac{\rho_{\text{eff}}}{\mu} \frac{\partial^2 \mathbf{u}_\perp}{\partial t_{\text{flat}}^2} = 0$$ {#eq-sek131-redukc-rownNC}

From this, we extract the propagation velocity of the transverse (shear) wave:

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_{\text{eff}}}}$$ {#eq-sek131-propag-fali-poprzecznej}

Since the 3-brane is defined as a macroscopic twist confined along the fourth dimension ($x^4$), all interactions within our world are transverse waves of this structure. Considering, without loss of generality, a wave vector oriented in the $(x^1, x^4)$ plane, namely $\mathbf{k} = (k_1, 0, 0, k_4)$, we obtain the dispersion relation $\omega^2 = c_{\perp}^2 (k_1^2 + k_4^2)$. The maximum velocity of the projection of the transverse wave onto the observable 3D space occurs for the confined component $k_4 = 0$ and defines the absolute speed limit of physical phenomena. The velocity $c_{\perp}$ is therefore identical to the macroscopic speed of light $c$ in vacuum.

### Dynamic Relaxational Resistance and Microscopic Grounding of Parameters {#sec-1-3-2}

The wave equation for $c_{\perp}$ describes the behavior of the continuum at the macroscale; however, the shear modulus $\mu$ and the effective wave density $\rho_{\text{eff}}$ are not fundamental constants. They emerge from the microscopic kinetics of the Sinai billiard. The key to coupling the absolute sub-Planckian velocity $v_\text{00}$ with the macroscopic constant $c_{\perp}$ lies in a colossal disparity of geometric scales.

Let us introduce here the lattice constant of the Substrate $a$ — the distance between the equilibrium positions of adjacent nodes $\mathbf{X}_i$. This quantity is not an independent parameter of the model, but follows directly from the geometry of the oscillation spheres introduced in [@sec-1-2-1]; in the state of full relaxation of the jammed lattice, neighboring interaction spheres of radius $R_0$ touch tangentially, defining the boundary contact of configuration cells [@sec-1-2-1-1]. For an isotropic lattice with identical oscillation spheres, the inter-node distance is therefore equal to the sum of the radii of two adjacent cells:

$$a = 2R_0$$ {#eq-sek1-3-stala-sieci}

which confirms the consistency of the scale: since $a < 1.6 \times 10^{-35}$ m (sub-Planckian scale), it follows that $R_0 < 0.8 \times 10^{-35}$ m.

Let us define the dimensionless ratio $\xi$ between the lattice constant of the Substrate $a$ and the wavelength of the measurable macroscopic perturbation $\lambda_\text{fala}$:

$$\xi = \frac{a}{\lambda_\text{fala}} \ll 1$$ {#eq-sek1-3-bezw-stos-sieci-al}

| Type of Radiation | Exemplary $\lambda_\text{fala}$ | Upper Bound $\xi \leq l_P/\lambda_\text{fala}$ |
| --- | --- | --- |
| Radio | $\sim 1$ m | $\lesssim 2 \times 10^{-35}$ |
| Visible | $\sim 5 \times 10^{-7}$ m | $\lesssim 3 \times 10^{-29}$ |
| X-ray | $\sim 10^{-10}$ m | $\lesssim 2 \times 10^{-25}$ |

:Table 1 {#tbl-1-3-2}

Irrespective of the spectral band, the parameter $\xi$ strictly satisfies $\xi \ll 1$. A single cell does not instantaneously experience the macroscopic wave deflection as a unidirectional phenomenon.

The baseline static background density $\rho_0$ follows directly from the mass of a single core $m_{00}$ and the volume of the interaction sphere in the relaxed state $V_0$: $\rho_0 = m_{00} / V_0$. According to Axiom II, in the isotropic state, the kinetic energy of 0-particles moving with velocity $v_\text{00}$ is distributed uniformly across 4 degrees of freedom. From the equipartition of momentum, it follows that the shear modulus $\mu$ depends directly on the variance of the orthogonal velocity:

$$\mu = \rho_0 \langle v_{\text{00}\perp}^2 \rangle = \rho_0 \frac{v_{\text{00}}^2}{4}$$ {#eq-sek1-3-mod-sprez}

As a macroscopic wave propagates through the lattice, neighboring 0-particles do not collide head-on, but rather cascade-deform the geometry of their interaction spheres, transmitting a torsional impulse. These ultra-fast oscillations across 4 axes manifest a resistance characterized by gyroscopic inertia. The wave front encounters resistance arising from the necessity of cascading momentum redistribution.

We define the macroscopic geometric inertia amplification parameter $\Gamma_{4D}$, representing the number of sub-Planckian micro-collision cycles required to execute a macroscopic, fully conservative momentum transfer (cf. [@sec-1-3-3]).

### Derivation of $\Gamma_{4D}$ from Core Random Walk {#sec-1-3-3}

To avoid defining the inertia amplification parameter $\Gamma_{4D}$ operationally through the velocity $c_\perp$ itself (which would result in circular reasoning), we derive it solely from the lattice geometry and microscopic collision statistics.

We define the fundamental parameters of the system in $d=4$: the number density of 0-particles $n$ (nodes per unit 4-volume), the effective lattice constant $a \equiv n^{-1/4}$ (consistent with the identity $a=2R_0$ derived in @sec-1-3-2 from the tangency condition of the oscillation spheres), the 4-dimensional scattering cross-section $S_{4D}$, and the mean free path $\ell$ of a free core moving within the locked spheres. At this stage, the nature of the cross-section $S_{4D}$ must be rigorously defined. In 4-dimensional space, the cross-section is not a two-dimensional surface area, but rather a three-dimensional impact hyper-surface (the effective volume of a collision 3-sphere), possessing the geometric dimension $[L^3]$. Taking into account the number density of the matrix framework $n \equiv a^{-4}$ with dimension $[L^{-4}]$, the mean free path $\ell$ from classical kinetic theory generalized to 4 dimensions takes the form:

$$\ell = \frac{1}{\sqrt{2}\, n\, S_{4D}}$$ {#eq-1-3-3-wz1}

The dimensionality of the denominator reduces to $[L^{-1}]$, which correctly endows the mean free path $\ell$ with the physical dimension of length $[L^1]$. This guarantees absolute consistency of the dimensional analysis in subsequent steps.

Substituting $n=a^{-4}$:

$$a^4 = \sqrt{2}\,\ell\,S_{4D} \implies a^2 = \sqrt[4]{2}\sqrt{\ell\,S_{4D}}$$ {#eq-1-3-3-wz2}

Due to the condition of local incompressibility of the Substrate, the macroscopic momentum transfer of the transverse wave requires a cascading redistribution of energy within the lattice cell. The motion of the core inside the sphere exhibits the character of a random walk: after $N$ collisions of length $\ell$, the mean squared displacement is $\langle r^2\rangle=N\ell^2$. According to the same principle of equipartition over 4 degrees of freedom that yielded $\mu=\rho_0v^2/4$ in @sec-1-3-2, the progression along a single transverse axis is:

$$\langle x_{\perp}^2\rangle = \frac14 N\ell^2$$ {#eq01-3-3-wz3}

We define $\Gamma_{4D}\equiv N$ as the number of micro-collisions required to transfer the impulse across the distance of a single interaction sphere $a$. Imposing the boundary condition $\langle x_\perp^2\rangle=a^2$:

$$\Gamma_{4D} = 4\left(\frac{a}{\ell}\right)^2 = 4\sqrt[4]{2}\,\frac{\sqrt{S_{4D}}}{\ell^{3/2}}$$ {#eq-1-3-gamma4d}

Owing to the previously established dimension of $[L^3]$ for the quantity $S_{4D}$, the square root in the numerator takes the form $[L^{1.5}]$, which perfectly cancels with the denominator $\ell^{3/2}$. This renders the geometric inertia amplification parameter $\Gamma_{4D}$ a strictly dimensionless quantity.

This quantity is now a function solely of the lattice geometry ($a$) and collision statistics ($\ell$, $S_{4D}$) — without reference to $c_\perp$ or $v_\text{00}$. This implies that the effective inertial density "seen" by the propagating wave increases with the square of the confined, gyroscopic background resistance relative to the pristine mass density $\rho_0$. To formally prove this dependence and avoid arbitrarily postulating the macroscopic density value, it must be derived directly from the kinetic energy balance and the kinematic amplification mechanism.

When a macroscopic shear wave propagates through the 0-Matrix, it induces a macroscopic transverse displacement velocity $\dot{u}_{\text{macro}}$ on the volume element of the Substrate. However, because the impulse must physically traverse a tortuous path consisting of $N = \Gamma_{4D}$ micro-collisions (the random walk of the core), the actual, induced microscopic velocity of impulse transmission between 0-particles ($\dot{u}_{\text{mikro}}$) is proportionally higher. The factor $\Gamma_{4D}$ acts here as an effective propagation delay:

$$\dot{u}_{\text{mikro}} = \Gamma_{4D} \cdot \dot{u}_{\text{macro}}$$ {#eq-1-3-3-wz5-a}

In the macroscopic continuum, the kinetic energy density of the wave is described using the sought-after, homogeneous effective density $\rho_{\text{eff}}^{(0)}$ in the equilibrium state:

$$E_k = \frac{1}{2} \rho_{\text{eff}}^{(0)} (\dot{u}_{\text{macro}})^2$$ {#eq-1-3-3-wz5-b}

On the other hand, at the fundamental microscopic level, this same kinetic energy is stored in the actual motion of the cores with the baseline background mass density $\rho_0$:

$$E_k = \frac{1}{2} \rho_0 (\dot{u}_{\text{mikro}})^2$$ {#eq-1-3-3-wz5-c}

Substituting the kinematic amplification relation into the microscopic energy balance, we obtain:

$$E_k = \frac{1}{2} \rho_0 (\Gamma_{4D} \cdot \dot{u}_{\text{macro}})^2 = \frac{1}{2} (\rho_0 \Gamma_{4D}^2) (\dot{u}_{\text{macro}})^2$$

 {#eq-1-3-3-wz5-d}

Comparing this result directly with the macroscopic formulation yields the rigorous, analytical form of the equilibrium inertial density governing the unperturbed jammed state of the 0-Matrix:

$$\rho_{\text{eff}}^{(0)} = \rho_0 \cdot \Gamma_{4D}^2$$ {#eq-1-3-3-wz5}

It is precisely $\rho_{\text{eff}}^{(0)}$, rather than the raw microscopic density $\rho_0=m_{00}/V_0$, that is the quantity directly inserted into the Helmholtz relation $c_\perp=\sqrt{\mu/\rho_{\text{eff}}^{(0)}}$ in §1.3.4 and into the equation of motion of the Substrate (@eq-1-5-6) in @sec-1-5-1 as the reference value around which the field $\rho_{\text{eff}}(\mathbf{x})$—introduced there for the description of local gravitational perturbations—fluctuates.

### Derivation of $c_{\perp}$ and its Physical Interpretation {#sec-1-3-4}

Substituting the independently derived $\mu=\rho_0v_\text{00}^2/4$ (@sec-1-3-2) and $\rho_{\text{eff}}^{(0)}=\rho_0\Gamma_{4D}^2$ (@eq-1-3-3-wz5, @sec-1-3-3) into the Helmholtz reduction $c_\perp=\sqrt{\mu/\rho_{\text{eff}}^{(0)}}$:

$$c_{\perp} = \sqrt{\frac{\rho_0\frac{v_\text{00}^2}{4}}{\rho_0\Gamma_{4D}^2}} = \frac{v_\text{00}}{2\Gamma_{4D}} = \frac{v_\text{00}}{8}\left(\frac{\ell}{a}\right)^2 = \frac{v_{00}}{8\sqrt[4]{2}}\,\frac{\ell^{3/2}}{\sqrt{S_{4D}}}$$ {#eq-1-3-c-perp-final}

where the final form arises from the explicit geometric expression for $\Gamma_{4D}=4\sqrt[4]{2}\,\sqrt{S_{4D}}/\ell^{3/2}$ (@eq-1-3-gamma4d).

In contrast to the purely definitional relation $\Gamma_{4D}\equiv v_\text{00}/(2c_\perp)$, the above derivation grounds $c_\perp$ solely upon the lattice geometry ($a$) and microscopic collision statistics ($\ell$, $S_{4D}$), thereby eliminating any circular reasoning. This equation is not a tautology, but a fundamental physical bridge of the TSM framework: it demonstrates that the macroscopically observable speed of light (identified in this regime with $c_\perp$) is not an independent, abstract universal constant, but an explicit function of the intrinsic kinetic velocity of the 0-particles ($v_{00}$) alongside the geometric parameters and cross-section of the jammed lattice.

The result conveys a clear physical meaning: in the jamming state ($\ell\ll a$, where the core undergoes numerous micro-collisions before the impulse reaches the adjacent cell), the fraction $(\ell/a)^2$ is extremely small, severely suppressing the pristine sub-Planckian velocity $v_\text{00}\gg c_\perp$ down to the measurable value $c_\perp$.

In this manner, the transition from the discrete description (the dynamics of 0-particles) to the continuous description (the elastodynamic continuum of the 3-brane) is mathematically closed without the introduction of phenomenological fitting parameters. This relation unambiguously demonstrates that the invariance of $c$ for a macroscopic observer is a direct consequence of thermodynamic stability and the constancy of the packing density of the 0-Matrix in its Zero State. Local fluctuations in the density of the Substrate will therefore modify the effective local stiffness tensor, which manifests macroscopically as a metric curvature, *i.e.*, a gravitational field.

### Conservative Nature of Wave Propagation and Absence of Energy Dissipation {#sec-1-3-5}

Defining the geometric inertia amplification parameter $\Gamma_{4D}$ raises a fundamental question: how, in a medium dominated by cascading collision processes, does the energetic stability of the wave escape immediate dissipation into heat? The TSM model eliminates dissipation via two ontological conditions:

1. **Absence of a structural sub-level:** The collisions of 0-particles are hard, indivisible, and absolutely elastic. Since no "interior" of a 0-particle exists, there is no mechanism for energy to thermalize into lower dimensions or internal friction.
2. **Purely reactive nature of lattice impedance:** The lattice cells act as a geometric energy accumulator. They absorb macroscopic momentum at the leading edge of the wave, returning it fully and losslessly at the trailing edge.

The net energy balance of momentum transfer across one full wave cycle is exactly zero. Consequently, the redshift observed in cosmology is not a result of photon friction against the Substrate (distinguishing TSM from "tired light" models), but stems from the cosmological evolution of the averaged substrate density $\langle\phi\rangle_\text{macro}$—via the mechanism outlined preliminarily in Chapter 0.4 and detailed further in Chapter 6. Furthermore, a local variation in $\langle\phi\rangle_\text{macro}$ modifies the rate of canonical time (@eq-1-2-5), which the observer registers as a shift in wave frequency.

### Status of the Longitudinal Wave: Superluminal 4D Density Waves and Time Fluctuations {#sec-1-3-6}

The Helmholtz decomposition reveals the existence of a second mode—the longitudinal (dilatational) wave, whose velocity is:

$$c_{\parallel} = \sqrt{\frac{\lambda + 2\mu}{\rho_{\text{eff}}}}$$ {#eq-1-3-predk-fali-podluz}

The status of the parameter $\lambda$ must be further clarified with respect to the strict incompressibility condition adopted in §1.3.1. There, the idealization $\lambda\to\infty$ (concurrent with $\nabla\cdot\mathbf{u}\to0$) formally eliminates the longitudinal wave from the macroscopic spectrum—*i.e.*, that which is observed at the level of the 3-brane by electromagnetic detectors. In the present subsection, we do not consider this strict limit, but rather a residual, formally very large yet finite bulk resistance ($\lambda\gg\mu$, $\lambda<\infty$)—corresponding to a non-zero, albeit extremely small, residual compressibility of the Substrate at the sub-Planckian scale. Consequently, $c_\parallel$ remains finite, although $c_\parallel\gg c_\perp$, which justifies the designation "superluminal" without introducing a formal divergence. The physical manifestation of this wave confined to the 3-brane consists of transient spatial oscillations of the substrate packing fraction ($\phi$). In accordance with the canonical equation of time, a local variation in density directly determines the rate of physical processes. Longitudinal waves propagating within the 0-Matrix are thus sub-Planckian **time dilation waves**, invisible to EM detectors, yet generating the quantum noise background. The relationship between this residual $\lambda$ and the strict $\lambda\to\infty$ limit from §1.3.1—specifically the microscopic origin of the scale at which the bulk resistance ceases to be treated as infinite—is left as an open quantitative problem of this chapter.

## Nonlinear Kinematics and the Emergence of Effective Macroscopic Geometry {#sec-1-4}

In TSM mechanics, the spatial metric $g_{ab}$ is not a primal entity of abstract geometry; it constitutes solely a physical and mathematical projection of the elasto-mechanical strain state of the Substrate. We completely eliminate the notion of a unifying spacetime—in the macroscopic description, we deal exclusively with the averaged spatial geometry of the 3-brane, onto which the dynamic stresses of the degenerate 4D crystalline lattice are projected.

### Emergence of the Effective Metric $g_{ab}$ from Local Strains of the Substrate {#sec-1-4-1}

In a flat, unperturbed 3-brane (at a large distance from topological nodes), the medium is characterized by a flat Euclidean metric $\delta_{ab}$. We introduce a physical vector displacement field of the substrate framework $\mathbf{u}(\mathbf{x})$, which describes the local strain of a lattice volume element from its equilibrium position. The macroscopically observable Riemannian metric emerges rigorously from the nonlinear gradients of this displacement (indices $a,b,c,d\in\{1,2,3\}$ according to the convention of §1.3.1, restricted to the hypersurface of the 3-brane):

$$g_{ab} = \delta_{ab} + \nabla_a u_b + \nabla_b u_a + \delta_{cd} \nabla_a u_c \nabla_b u_d$$ {#eq-1-4-1}

where:

* $g_{ab}$ – the metric tensor constituting the observable geometry of space,
* $\delta_{ab}$ – the flat Euclidean metric of the unperturbed background lattice,
* $\mathbf{u}$ – the vector of physical displacement of the Substrate framework,
* $\nabla$ – the covariant derivative operator defined in the background metric $\delta_{ab}$.

Any spatial curvature and the resulting gravitational phenomena are thus a direct consequence of the mechanical tensioning of the system of 0-particle cells. This generates a macroscopic gradient of the effective packing density $\phi$ directed toward the fourth, orthogonal spatial dimension $x^4$.

### Nonlinear Wave Kinematics and the Physical Contraction of Space {#sec-1-4-2}

Relativistic coordinate transformations and the observed phenomenon of time dilation are a direct consequence of the manner in which solitonic nodes (field nodes) interact with the dense, deformable continuum of the 0-Matrix during motion. In high-velocity states, the forced piling-up of the Substrate framework and the resulting modification of the local density of oscillatory states lead to a change in the geometry of the node's oscillations, which is macroscopically interpreted as an extension of the duration of internal processes.

#### Velocity Construction and Length Contraction {#sec-1-4-2-1}

To maintain conceptual rigor, we define two complementary representations of macroscopic velocity:

1. Background coordinate velocity ($v$): expresses the change in position relative to the static reference lattice:

$$v = \frac{dx}{dt_{\text{flat}}}$$ {#eq-1-4-3-vtla}
2. Proper velocity of the node ($q$): measured by the dilated local time:

$$q = \frac{dx}{dt}$$ {#eq-1-4-3-vwezla}

The transformational relationship between them follows directly from the framework piling-up mechanism ($dt = dt_{\text{flat}} / \gamma$):

$$q = \frac{dx}{\frac{dt_{\text{flat}}}{\gamma}} = \gamma \cdot v = \frac{v}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$  {#eq-1-4-3-wz1}

As the coordinate velocity approaches the transverse shear limit of the substrate framework ($v_\text{00} \to c_{\perp}$), the rising topological inertia causes the factor $\gamma \to \infty$, while the proper velocity $q \to \infty$. This distinction naturally eliminates the paradox of infinite kinematic velocity in absolute terms.

The motion of a node generates an elastic compression front ahead of the object. By introducing the co-moving coordinate $u = x - vt_{\text{flat}}$, the transformation of the homogeneous wave equation to preserve the shape invariance of the soliton forces a rescaling of the spatial axis along the momentum vector:

$$x' = \frac{u}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} = \gamma (x - vt_{\text{flat}})$$ {#eq-1-4-6}

Under the influence of this unilateral elasto-mechanical resistance, the shape of each solitonic node undergoes actual mechanical compression, which macroscopically manifests as length contraction in the direction of motion:

$$L' = L / \gamma.$$ {#eq-1-4-6a}

### Kinematic Time Dilation as an Isotropic Piling-Up of the Substrate {#sec-1-4-3}

The motion of a macroscopic structure (a node) does not consist in pushing matter through the medium, but in the propagation of the topological deformation itself through the degenerate, vibrating crystalline lattice of the substrate framework. At the fundamental level, 0-particles do not undergo physical translation behind the moving body; rather, the shape of their interaction spheres undergoes a cascading, wave-like deformation along with the motion of the solitonic impulse. This is a lossless propagation of a collective pattern of node-solitons through the jammed Substrate. Matter behaves like a porous topological mesh through which the strain state of the lattice propagates without resistance.

During the motion of this system at coordinate velocity $v$, microscopic, local piling-up occurs on each individual, geometrically bent sphere. Since these effects occur at the sub-Planckian scale, their individual occurrence does not introduce local directional anisotropy. However, at the macroscopic scale, within the envelope of the moving system, a constructive, isotropic accumulation of these micro-strains takes place.

The mechanism of this piling-up follows directly from the principle of conservation of the 0-particle core volume ($V_{00}=\text{const}$, @sec-1-2-1) in combination with the spatial contraction of the solitonic structure in the direction of motion. As demonstrated independently in @sec-1-4-2-1 from the requirement of soliton shape invariance with respect to the homogeneous wave equation of the substrate framework, a moving node undergoes a shortening of its spatial extent along the direction of motion by a factor of $1/\gamma$: $L'=L/\gamma$ (@eq-1-4-6a). Since the number of 0-particles $N$ forming the soliton structure and the volume of their individual, indivisible cores $V_{00}$ remain unchanged (absolute core rigidity, @sec-1-2-1-1), the reduction in spatial volume occupied by the same number of particles forces a proportional increase in the local packing density:

$$\langle\phi(v)\rangle_{\text{macro}} = \phi_0\cdot\frac{V}{V'} = \frac{\phi_0}{\sqrt{1 - \dfrac{v^2}{c_{\perp}^2}}} = \phi_0\cdot\gamma$$ {#eq-1-4-2}

The parameter $\phi_0$ in the above relation denotes the sub-Planckian packing of 0-particles in the 0-Matrix at the microscopic level (Level I). The soliton as a physical object, however, is a topological defect of a higher order of organization (Level II): it is built of $N_\text{str}$ topological zones, each of which involves $M$ 0-particles, together forming a mesoscopic structure with its own effective compression modulus $K_\text{eff}$. For simple elementary particles, $N_\text{str}$ is small (e.g., for base hopfions, $N_\text{str}=1$), for composite particles—atomic nuclei, multiquark hadrons—$N_\text{str}$ can range from tens to thousands, proportionally to the rest mass (§1.6).

This hierarchy of levels is crucial for interpreting the limiting behavior of formula (@eq-1-4-2). The static packing limit of 0-particles $\phi_\text{max}^\text{stat}$—determined by the geometry of hard hyperspherical cores in 4D and governing the thresholds $\phi_c$ and $\phi_\text{lock}$ in @sec-1-5-2—applies exclusively to Level I and describes equilibrium lattice reshuffling. Kinematic compression of the continuous substrate by a moving soliton, on the other hand, operates on Level II zones, which are not hard spheres but topological structures—hopfions and their local variants. Moreover, the transit time of a soliton through a single lattice node is shorter than the structural relaxation time $T_0$, so the lattice reacts exclusively elastically, without Level I topological reshuffling. In this dynamic regime, the effective compression limit is not determined by the geometric ceiling $\phi_\text{max}^\text{stat}$, but by the elastic energy:

$$U_\text{comp}(v) \approx \frac{1}{2}K_\text{eff}\left(\frac{\phi_0\gamma - \phi_0}{\phi_0}\right)^2 \cdot V_\text{sol} \xrightarrow{v \to c_\perp} \infty$$  {#eq-1-4-2b}

The divergence of $U_\text{comp}$ as $v\to c_\perp$ means that the velocity barrier $v_\text{lock} = c_\perp$ is an asymptotic energy barrier—not a geometric ceiling of core packing. Regardless of the degree of complexity of the soliton ($N_\text{str}$, rest mass $m_0$), no finite input of energy allows reaching $v=c_\perp$. This result is internally consistent with the divergence of kinetic energy $E=\gamma m_0 c_\perp^2$ from §1.4.4—both descriptions express the same physical impossibility from two complementary perspectives: energetic and geometric-topological.

Owing to the fact that the piling-up (@eq-1-4-2) takes the form of a homogeneous scalar field within the envelope of the moving object:

1. All microscopic oscillators and clocks inside this body experience an identical deceleration of relaxation processes (according to the canonical dilation formula from §1.2.3), which completely eliminates any directional gradient and explains the negative results of the Michelson-Morley and Kennedy-Thorndike experiments.
2. The Lorentz factor $\gamma$ is rigorously derived from the nonlinear elasticity and wave resistance of the 0-Matrix, without the necessity of introducing postulates about the constancy of the speed of light as an abstract axiom.

#### Gravitational Dilation—Relationship with the Potential $\Phi$ {#sec-1-4-3-1}

The strain of the 3-brane into the fourth spatial dimension, induced by the presence of passive topological nodes (mass), causes a radial gradient of the substrate framework packing density around the source. In the weak gravitational field regime, we assume a linear dependence of the effective density on the modulus of the local gravitational potential $\Phi(\mathbf{x})$:

$$\phi(\mathbf{x}) \approx \phi_0 \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right)$$  {#eq-1-4-3}

Substituting this dependence into the canonical definition of time, the ratio of the increment of local proper time $dt$ to the unperturbed flat background time $dt_\text{flat}$ takes the form:

$$\frac{dt}{dt_{\text{flat}}} = \frac{\phi_0}{\phi(\mathbf{x})} \approx \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right)^{-1} \approx 1 - \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}$$ {#eq-1-4-4}

This equation provides an empirically correct approximation of gravitational dilation, identical to the results of the Pound-Rebki experiment and the relativistic corrections applied in satellite navigation systems. It must be emphasized that the linear expansion (@eq-1-4-3) holds exclusively in the weak-field regime, where $|\Phi|/c_\perp^2\ll 1$; in the strong-field regime (the vicinity of ultra-dense plasmoids replacing singularities), a nonlinear treatment of the dependence $\phi(\mathbf{x})$ is required, which remains an open problem for subsequent chapters.

### Energy, Momentum, and Relativistic Mass {#sec-1-4-4}

The elastic deformation energy of a node (the base equivalent of which is the rest mass $m_0$) proportionally vibrates with the superimposed load of the substrate framework density. Since a piling-up of the density field $\langle\phi(v)\rangle_{\text{macro}} = \phi_0\gamma$ occurs for a moving system, relativistic mass—understood as the instantaneous, effective topological inertia of the solitonic node—scales as:

$$m = \gamma m_0 = \frac{m_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$  {#eq-1-4-7}

The momentum carried by the translating deformation takes a form conjugate to the proper velocity $q$:

$$p = m_0 \frac{dx}{dt} = m_0 q = \gamma m_0 v$$ {#eq-1-4-8}

Differentiating the momentum with respect to the flat background time ($t_{\text{flat}}$), we obtain the dynamic force equation, which reveals the mechanism of asymptotic lattice resistance:

$$F = \frac{dp}{dt_{\text{flat}}} = \frac{d}{dt_{\text{flat}}}(\gamma m_0 v) = m_0 \gamma^3 \frac{d^2 x}{dt_{\text{flat}}^2} = m_0 \gamma^3 a$$ {#eq-1-4-9}

*(The above step assumes one-dimensional motion along the direction of soliton propagation, in accordance with the convention of the entirety of @sec-1-4-4 - @sec-1-4-5; for a force component perpendicular to $v$, the scaling factor would be $\gamma^1$, not $\gamma^3$.)*

To demonstrate mass-energy equivalence directly from continuum mechanics, let us define the increment of macroscopic kinetic energy ($E_k$) as the work performed by the force $F$ while accelerating the node from rest ($v=0$) to velocity $v$ over a distance $x$:

$$E_k = \int_0^x F \, dx' = \int_0^t F v \, dt_{\text{flat}}'$$ {#eq-1-4-10}

Substituting the elasto-mechanical force equation (@eq-1-4-9) into the integral, we transform the variable of integration from time to coordinate velocity:

$$E_k = \int_0^v \left( m_0 \gamma^3 \frac{dv'}{dt_{\text{flat}}'} \right) v \, dt_{\text{flat}}' = m_0 \int_0^v \gamma^3 v' \, dv'$$ {#eq-1-4-11}

Expanding the Lorentz factor $\gamma$ explicitly, we obtain an integral solved via rigorous substitution:

$$E_k = m_0 \int_0^v \frac{v'}{\left(1 - \frac{v'^2}{c_{\perp}^2}\right)^{3/2}} \, dv'$$ {#eq-1-4-12}

The result of this integration is the direct dependence of kinetic energy on the compressional configuration of the lattice:

$$E_k = \left[ \frac{m_0 c_{\perp}^2}{\sqrt{1 - \frac{v'^2}{c_{\perp}^2}}} \right]_0^v = \frac{m_0 c_{\perp}^2}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} - m_0 c_{\perp}^2 = \gamma m_0 c_{\perp}^2 - m_0 c_{\perp}^2$$ {#eq-1-4-13}

According to the axioms of TSM, a state converging to rest ($v=0$, i.e., $\gamma=1$) does not imply zero energy of the continuum. Every solitonic node, in order to exist at all within the dense crystalline lattice, requires a permanent, local tensioning of the interaction spheres of the 0-particles. The energy of this rest tension constitutes the intrinsic structural energy of the Substrate: $E_0 = m_0 c_{\perp}^2$.

Defining the total relativistic energy of the system ($E$) as the sum of the kinetic energy (the work introduced into the lattice) and the rest energy (the intrinsic geometry of the node), we obtain a full derivation of the Einstein relation:

$$E = E_k + E_0 = (\gamma m_0 c_{\perp}^2 - m_0 c_{\perp}^2) + m_0 c_{\perp}^2 = \gamma m_0 c_{\perp}^2$$  {#eq-1-4-14}

Taking into account the relativistic scaling of inertial mass defined in @eq-1-4-7, the above equation reduces to the final, sought-after form of the mass-energy equivalence of the continuum:

$$E = m c_{\perp}^2$$ {#eq-1-4-15}

As the coordinate velocity approaches the transverse shear limit ($v \to c_{\perp}$), the work required for further compression of the wave front tends to infinity. From the mathematical coupling of the total energy equations (@eq-1-4-14) and the standing wave momentum (@eq-1-4-8), an invariant dispersion relation of lattice inertia emerges, confirming the lossless character of propagation.

Direct substitution of $E=\gamma m_0 c_\perp^2$ and $p=\gamma m_0 v$ yields:


$$E^2-(pc_\perp)^2=\gamma^2 m_0^2 c_\perp^2(c_\perp^2-v^2)=\gamma^2 m_0^2 c_\perp^4\left(1-\frac{v^2}{c_\perp^2}\right)=m_0^2c_\perp^4$$ {#eq-1-4-16przed}

from which immediately:

$$E^2 = (pc_{\perp})^2 + (m_0 c_{\perp}^2)^2$$ {#eq-1-4-16}

### Material Constants of the Substrate Framework and the Local Variability of Wave Propagation ($c_{\perp}$) {#sec-1-4-5}

The speed of light is not a universal constant; it follows directly from the nonlinear acoustoelastic phenomenon of the dense continuum. In a region subjected to mechanical stress ($\Sigma$), the local velocity of transverse waves $c_{\perp,\text{lok}}$ is modulated by nonlinear stiffness (Murnaghan constant $\mathcal{A}$):

$$c_{\perp,\text{lok}}^2 = \frac{\mu}{\rho_{\text{eff}}^{(0)}} \left( 1 + \mathcal{A} \Sigma \right) = c_{\perp}^2 \left( 1 + \mathcal{A} \Sigma \right)$$ {#eq-zmiennosc-c}

The acoustoelastic constant $\mathcal{A}$ has the dimension of the inverse of stress $[\text{Pa}^{-1}]$, ensuring the dimensionless nature of the term $\mathcal{A}\Sigma$; its relation to the third-order dimensionless Murnaghan constants is realized through normalization to the shear modulus: $\mathcal{A} = \tilde{\mathcal{A}}/\mu$, where $\tilde{\mathcal{A}}$ is a dimensionless material constant. The explicit form of this relationship remains phenomenologically open.

To pass from a general mechanical stress $\Sigma$ to specific physical sources (magnetic field, gravitational potential), we identify $\Sigma$ with the appropriate stress tensor originating from the given interaction:

**Magnetic field contribution.** The Maxwell stress generated by the field $B$ in the medium is $\Sigma_B = B^2/(2\mu_\text{em})$, where $\mu_\text{em}$ denotes the magnetic permeability of vacuum (a symbol distinguished from the Lamé shear modulus $\mu$ used throughout the chapter). Substituting into (@eq-zmiennosc-c):

$$c_{\perp,\text{lok}}^2 \approx c_{\perp}^2\left(1 + \mathcal{A}\frac{B^2}{2\mu_{\text{em}}}\right)$$ 
 {#eq-1-4-5-wz1}

**Gravitational potential contribution.** From the density relation of @sec-1-4-3 (@eq-1-4-2), $\phi(\mathbf{x})\approx\phi_0(1+|\Phi|/c_\perp^2)$, and the density bridge $\rho_{\text{eff}}=\rho_0\cdot\phi/\phi_0$ introduced and formally justified in @sec-1-5-1 (@eq-1-5-5b), we obtain $\rho_{\text{eff}}(\mathbf{x})\approx\rho_0(1+|\Phi|/c_\perp^2)$. Since $c_{\perp,\text{lok}}^2=\mu/\rho_{\text{eff}}$, a first-order expansion yields:

$$c_{\perp,\text{lok}}^2 \approx \frac{\mu}{\rho_0}\left(1 - \frac{|\Phi|}{c_\perp^2}\right)$$ {#eq-1-4-5-wz2}

We adopt here the standard sign convention for the gravitational potential: $\Phi\le0$ for an attractive field, whence $|\Phi|=-\Phi$. Combining both contributions and moving to electrodynamic notation ($c_{\perp,\text{lok}}=1/\sqrt{\epsilon_{\text{eff}}\mu_0}$, where $\epsilon_{\text{eff}}\propto 1/c_{\perp,\text{lok}}^2$), we obtain the effective permeability expressed directly in terms of the signed variable $\Phi$ (rather than $|\Phi|$):

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 - \kappa B^2 + \beta_\Phi \frac{\Phi}{c_{\perp}^2} + \dots\right)$$  {#eq-1-4-5-wz3}

with the magnetic coupling constant explicitly expressed through the Murnaghan constant:

$$\kappa = \frac{\mathcal{A}}{2\mu_\text{em}}$$ {#eq-1-4-5-wz4}

The gravitational coefficient is $\beta_\Phi=-1$: since $|\Phi|/c_\perp^2=-\Phi/c_\perp^2$ under the adopted convention $\Phi\le0$, substituting $|\Phi|\to-\Phi$ into the formula for $\epsilon_{\text{eff}}$ directly yields a coefficient of $-1$ for the variable $\Phi$. This value therefore follows from the linear density relation $\rho_{\text{eff}}(\Phi)$ (and not from the acoustoelastic mechanism $\mathcal{A}\Sigma$) and, in the current formulation of the model, is a constant independent of $\mathcal{A}$. A full reduction of both constants to a common source $\mathcal{A}$ would require demonstrating that the density gradient induced by $\Phi$ is physically equivalent to a Murnaghan stress—which remains an open research problem of this chapter.

As can be seen, in the TSM model, the hitherto dimensionless physical constants lose their abstract status, becoming mechanothermodynamic parameters and material constants of the 4-dimensional continuum, explicitly reducible to a single, common constant of elastic nonlinearity $\mathcal{A}$.

### Final Conclusions and Synthesis of TSM Kinematics {#sec-1-4-6}

The derivation of nonlinear macroscopic kinematics within the framework of Topological Substrate Mechanics allows for the formulation of four key conclusions that redefine the relativistic paradigm:

1. **Ontological reduction of spacetime:** TSM proves that Minkowski spacetime is not an independent, primal physical arena. The four-dimensional relativistic formalism is solely a mathematical effect, emerging from the fact that macroscopic time is an operational parameter of the succession of changes (dependent on the local substrate framework density $\phi$), and measured space is a physically bent and tensioned 3-brane.
2. **Mechanistic meaning of the constancy of the speed of light:** The constancy of the speed of light ($c_{\perp}$) in vacuum ceases to be an unconditional, axiomatic kinematic postulate. It becomes a physical material constant of the degenerate 0-Matrix lattice—the limiting velocity of propagation of transverse acoustic (shear) waves in an elastic topological glass.
3. **Physicality of contraction and dilation:** Lorentz length contraction ($L'=L/\gamma$) and kinematic time dilation are not perspective illusions resulting from the abstract geometry of reference frames. They are real, elasto-mechanical deformations. The motion of a solitonic structure generates a physical piling-up of the substrate framework around the nodes, which increases the relaxation resistance of the lattice and objectively slows down all internal periodic processes (clocks) of the moving body.
4. **Unity of gravitation and inertia:** Through the identity of the denominators in the kinematic (@eq-1-4-2) and gravitational (@eq-1-4-4) dilation relations, TSM unifies both phenomena at the microscopic level. Regardless of whether the local increase in the substrate framework density $\langle\phi\rangle_{\text{macro}}$ is induced by the bending of the brane into the fourth dimension by a central mass (gravitation) or by the constructive piling-up of the wave front by the proper motion of the soliton (kinematics), the temporal effect is identical because the measuring apparatus reacts exclusively to the net, absolute packing of the 0-Matrix cells.

## Wave Dynamics of the Substrate and the Dual Regime of Elasto-Dynamics {#sec-1-5}

Substrate mechanics is governed by a generalized Lagrangian formalism, assimilating the mathematical solutions of General Relativity, but without its relativistic ontological assumptions. Space and its dynamics are not a geometric abstraction, but a consequence of the physical states of the crystalline lattice of the 0-Matrix.

### Matrix Framework Field Equations as a Description of Lattice Stress States {#sec-1-5-1}

The Lagrangian density $\mathcal{L}$ of an isotropic 3-brane is the difference between the kinetic energy density and the elastic potential energy density. Utilizing the elasticity modulus tensor $K^{abcd}$, we model the continuum in the low-strain regime using the expansion:

$$\mathcal{L} = \frac{1}{2}\rho_{\text{eff}} \, \delta_{ab} \frac{\partial u^a}{\partial t_{\text{flat}}} \frac{\partial u^b}{\partial t_{\text{flat}}} - \frac{1}{2}K^{abcd}\epsilon_{ab}\epsilon_{cd} + \mathcal{O}(\epsilon^3)$$ {#eq-1-5-1}

where the first term describes the kinetic energy density of the displacement field, and the second term represents the elastic potential energy density $\mathcal{U}$. The small-strain tensor $\epsilon_{ab}$ is determined directly from the gradients of the matrix framework displacement field $u$:

$$\epsilon_{ab} = \frac{1}{2}(\partial_a u_b + \partial_b u_a)$$ {#eq-1-5-2}

The macroscopic properties contained within the tensor $K^{abcd}$ and the stress tensor $\sigma^{ab}$ determined by them result directly from the elasto-mechanical state of the confined, sub-Planckian 0-particles and their repulsion spheres. For an ideally isotropic crystalline lattice, the elasticity modulus tensor reduces to two independent Lamé constants ($\lambda$ and $\mu$):

$$K^{abcd} = \lambda \delta^{ab}\delta^{cd} + \mu (\delta^{ac}\delta^{bd} + \delta^{ad}\delta^{bc})$$  {#eq-1-5-3}

where $\delta^{ab}$ denotes the flat, Euclidean background metric of the Substrate. In the constitutive approach, the matrix framework stress tensor $\sigma^{ab}$ is defined directly by the derivative of the elastic energy density $\mathcal{U}$ with respect to the strain tensor (which, assuming the absence of an explicit dependence of the kinetic energy on spatial strains in the linear regime, corresponds to the relation $-\partial \mathcal{L} / \partial \epsilon_{ab}$):

$$\sigma^{ab} = \frac{\partial \mathcal{U}}{\partial \epsilon_{ab}} = K^{abcd} \epsilon_{cd} = \lambda \delta^{ab} \epsilon^c_c + 2\mu \epsilon^{ab}$$ {#eq-1-5-4}

The field $\phi(\mathbf{x})$, introduced phenomenologically in @sec-1-2a-2 as the convolution of the microscopic lattice packing fraction with a filter window $W$ (@eq-1-2-1), is identified in the elastic continuum limit with the field defined directly by the local volumetric dilation of the medium, assuming the linear relation $\phi(\mathbf{x}) = \phi_0(1 - \epsilon^c_c)$. This identification—analogous to the standard relation between microscopic number density and macroscopic displacement divergence in the classical theory of elasticity for granular media—constitutes a constitutive assumption of the TSM model, rather than a theorem derived directly from the microdynamics of the Sinai billiard (@sec-1-2-1-1); its rigorous proof remains an open research problem of this chapter, on par with the derivation of $c_\perp$ (@sec-1-4-5) and the radial structure of the soliton (@sec-1-6-1).

*Note on threshold hierarchy:* In TSM, a strict ordering holds: $\phi_0 \le \phi_c < \phi_\text{lock}$. The threshold $\phi_c$ determines the global jamming state of the lattice, which serves as the physical background; the threshold $\phi_\text{lock}$ is the local criterion for the formation of stable topological nodes (matter) and always exceeds $\phi_c$. The quantitative relationship between these thresholds—and their dependence on spatial dimensionality and core geometry—remains an open quantitative problem of the model.

Thus, we define the local macroscopic matrix framework density $\phi$ as a function of the local degree of densification or rarefaction of the lattice cells, which mathematically corresponds to the trace of the strain tensor (volumetric dilation $\epsilon^c_c = \nabla \cdot \mathbf{u}$):

$$\phi = \phi_0 (1 - \epsilon^c_c) = \phi_0 (1 - \nabla \cdot \mathbf{u})$$  {#eq-1-5-5}

*Note:* Expression (@eq-1-5-5) assumes that $\epsilon^c_c$ is small but finite—in accordance with the explanation in @sec-1-3-6, where the idealization $\lambda\to\infty$ from @sec-1-3-1 represents an approximation of the macroscopic spectrum, not a strict limit. Residual, finite compressibility ($\lambda\gg\mu$, $\lambda<\infty$) at the sub-Planckian scale allows $\epsilon^c_c$ to take small, non-zero values, which generate the observable gradients of $\phi$ responsible for the gravitational field.

where $\phi_0$ is the undistorted, baseline, **dimensionless** packing density of the 0-Matrix in equilibrium. Since the equation of motion of the Substrate requires an inertial coefficient with the dimensions of mass density (rather than a dimensionless packing fraction), we relate $\phi$ to the homogeneous inertial density $\rho_{\text{eff}}^{(0)}$ derived microscopically in §1.3.3 (@eq-1-3-3-wz5) via a simple proportion:

$$\rho_{\text{eff}}(\mathbf{x}) = \rho_{\text{eff}}^{(0)} \cdot \frac{\phi(\mathbf{x})}{\phi_0}$$ {#eq-1-5-5b}

which in equilibrium ($\phi=\phi_0$) reduces to $\rho_{\text{eff}}=\rho_{\text{eff}}^{(0)}$, in agreement with the microkinetic definition from §1.3.3. It should be emphasized that $\rho_{\text{eff}}^{(0)}\neq\rho_0$: the raw mass density of the cores $\rho_0=m_{00}/V_0$ (§1.3.2) is a purely material quantity, whereas $\rho_{\text{eff}}^{(0)}=\rho_0\Gamma_{4D}^2$ additionally accounts for the gyroscopic resistance of cascading momentum redistribution in the jammed lattice—and it is precisely this latter quantity that correctly reproduces the measured value of $c_\perp$.

Applying Hamilton's principle of least action ($\delta \int \mathcal{L} \, d^4x = 0$) with respect to the Substrate displacement field $u_i$, we obtain the dynamic equation of motion of the 4-dimensional matrix framework (the continuum equivalent of the Navier-Cauchy equation):

$$\rho_{\text{eff}} \frac{\partial^2 u^i}{\partial t_{\text{flat}}^2} = \nabla_j \sigma^{ij} = (\lambda + \mu) \nabla^i (\nabla \cdot \mathbf{u}) + \mu \nabla^2 u^i$$  {#eq-1-5-6}

In accordance with the mechanics of crystalline media, the displacement field $u^a$ can be uniquely decomposed (Helmholtz decomposition) into an irrotational component (longitudinal waves) and a solenoidal component (transverse shear waves): $\mathbf{u} = \nabla \varphi_H + \nabla \times \mathbf{\Psi}$, where $\varphi_H$ is the scalar potential of the decomposition (a symbol distinguished from the gravitational potential $\Phi$ in @sec-1-4-3-1). Substituting this decomposition into the equation of motion (@eq-1-5-6) for the transverse component $\mathbf{\Psi}$ (where $\nabla \cdot \mathbf{\Psi} = 0$), we obtain a pure, homogeneous wave equation:

$$\nabla^2 \mathbf{\Psi} - \frac{\rho_{\text{eff}}}{\mu} \frac{\partial^2 \mathbf{\Psi}}{\partial t_{\text{flat}}^2} = 0$$  {#eq-1-5-7}

The above substitution rigorously defines the transverse shear wave velocity as a fundamental material constant of the lattice: $c_{\perp} = \sqrt{\mu / \rho_{\text{eff}}}$—consistent with the definition already derived microscopically in §1.3.1–1.3.4.
In the general case, in the presence of permanent lattice distortions (nodes), any function of the transverse strain field components $\psi \in \mathbf{\Psi}$ satisfies an inhomogeneous wave equation:

$$\nabla^2 \psi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \psi}{\partial t_{\text{flat}}^2} = \mathcal{S}(\mathbf{x}, t_{\text{flat}})$$ {#eq-1-5-8}

where $\mathcal{S}(\mathbf{x}, t_{\text{flat}})$ is the source function representing the density of non-linear topological distortions.

This relation is not an independent postulate, but rather the linear limit of the full, non-linear deformation metric introduced in §1.4.1 (@eq-1-4-1). Neglecting the quadratic term $\delta_{cd}\nabla_a u_c\nabla_b u_d$ (justified in the small-strain regime, $|\nabla u|\ll1$, identical to the linearity assumption adopted in (@eq-1-5-1)), the metric reduces to:

$$g_{ab} \approx \delta_{ab} + 2\epsilon_{ab}$$ {#eq-1-5-9}

In the regime of local incompressibility already established in §1.3.1 ($\lambda\to\infty$, $\nabla\cdot\mathbf{u}=\epsilon^c_c\to0$), the constitutive law (@eq-1-5-4) simplifies to $\sigma_{ab}=2\mu\epsilon_{ab}$, whence $\epsilon_{ab}=\sigma_{ab}/(2\mu)$. Substituting:

$$g_{ab} = \delta_{ab} + \frac{1}{\mu}\sigma_{ab}$$  {#eq-1-5-9a}

The above reproduces the form of the linear constitutive coupling of TSM

$$g_{ab} = \delta_{ab} - \chi\sigma_{ab}$$ {#eq-1-5-9b}

with the macroscopic elastic compliance of the Substrate uniquely expressed by the shear modulus: $\chi \equiv -1/\mu$. *(The sign of the coefficient $\chi$ depends on the adopted stress sign convention for $\sigma_{ab}$—in this text, the convention $T^{(0)}_{IJ}=-P_0\delta_{IJ}$ from @sec-1-2-2 implies that compressive stress is negative; within this convention, $\chi=-1/\mu$ yields the physically correct direction: compression increases $g_{ab}$. If you adopt the inverse sign convention for $\sigma_{ab}$ in §1.3, verify the sign consistency here.)* In this manner, gravity emerges as a linear approximation of the very same stress field described in its full, non-linear form by @eq-1-4-1—eliminating the need to curve the primordial ontology of space itself.

### Elastic Waves vs. Non-linear Topological Locking {#sec-1-5-2}

In an ideally elastic medium that dissipates excesses of local pressure losslessly and symmetrically, the formation of any stable, localized material structures (particles) would be impossible. To prevent instantaneous relaxation and energy dispersion, TSM mechanics separates the dynamics of the Substrate into two complementary physical regimes, sharply demarcated by a critical geometric freezing threshold termed the **topological locking density $\phi_{\text{lock}}$**.

#### **Regime I: Linear Acoustic Relaxation ($\phi < \phi_{\text{lock}}$)** {#sec-1-5-2-1}

As long as the local lattice compression does not exceed the geometric stability threshold of the Wigner-Seitz cages ($\epsilon^c_c > \epsilon_{\text{crit}}$), the Substrate behaves as an ideal, linear elastic continuum. Cell deformations are conservative in nature—repulsion spheres undergo transient deformation, but the 0-particles strictly maintain the intact matrix of their original neighbors. The excess local pressure is transferred isotropically outward, and the medium effectively relaxes energy through the propagation of classical transverse waves at the invariant material velocity $c_{\perp}$. In this regime, the background remains a massless physical vacuum.

#### **Regime II: Non-linear Topological Locking ($\phi \ge \phi_{\text{lock}}$)** {#sec-1-5-2-2}

The situation changes dramatically when the local arrangement of cells is compressed beyond the limit of geometric plasticity ($\epsilon^c_c \le \epsilon_{\text{crit}}$). The kinetic Wigner-Seitz cages then undergo critical distortion. In Regime II, individual, uncorrelated hops of 0-particles are forbidden; the sole form of neighborhood modification is the collective shift described in [@sec-1-2-1-3], which leads to a rearrangement of the 0-Matrix topology.

The non-linear shortening of cell axes within the zone of extreme compression activates higher-order terms $\mathcal{O}(\epsilon^3)$ in the Lagrangian (@eq-1-5-1), forcing a permanent rotation of the principal directions of elastic stress. Instead of sequential outward momentum transfer (wave relaxation), the stress lines close in upon themselves, forming a spatially locked structure:

1. **A kinetic and geometric confinement of the freedom of the 0-particles' interaction spheres occurs.**
2. **The stress fields loop into a self-sustaining, rotational entanglement, i.e., a microscopic soliton vortex.** This state is mathematically described by a non-zero mechanical vorticity tensor $\Omega_{ab} = \frac{1}{2}(\nabla_a u_b - \nabla_b u_a)$, whose closed circulation becomes a topological invariant of the entire system.
3. **The Substrate within this specific region completely loses its capacity to release accumulated energy via the ordinary emission of acoustic waves $c_{\perp}$.**

A non-linear topological node is formed, acquiring independent structural stability. Unraveling or destroying it would require a re-supply of energy sufficient to overcome the state of limiting compression, establishing a massive, quantized energy barrier. In this manner, the non-linear mechanics of crystalline distortions directly gives rise to stable, quantized macroscopic matter.

### Summary of the Dynamic Dualism of the Substrate {#sec-1-5-3}

The introduction of the generalized elasto-dynamics formalism allows for an unambiguous formulation of the mechanical definition of space and matter in TSM. The entirety of the dynamic states of the 0-Matrix can be framed within a rigorous, complementary structure:

| Parameter / Feature | Regime I: Linear Acoustic Relaxation | Regime II: Non-linear Topological Locking |
| --- | --- | --- |
| **Transition criterion** | $\phi < \phi_{\text{lock}}$ \ (equivalently: $\epsilon^c_c > \epsilon_{\text{crit}}$, where $\epsilon_{\text{crit}} \equiv 1 - \phi_\text{lock}/\phi_0 < 0$) | $\phi \ge \phi_{\text{lock}}$ \ (equivalently: $\epsilon^c_c \le \epsilon_{\text{crit}}$, where $\epsilon_{\text{crit}} \equiv 1 - \phi_\text{lock}/\phi_0 < 0$) |
| **Lattice cage state** | Low, conservative elastic strains. | Critical, plastic distortion of Wigner-Seitz cages. |
| **Behavior of 0-particles** | Vibrations within cages; preservation of the full matrix of original neighbors. | Absolute confinement; permanent rotation of the principal directions of elastic stresses. |
| **Energy transfer** | Free, isotropic emission of transverse waves at the material velocity $c_{\perp}$. | Impossibility of linear emission; looping of stress lines into a rotational entanglement. |
| **Mathematical invariant** | Homogeneous hyperbolic equation: \ $\nabla^2 \mathbf{\Psi} - \frac{1}{c_{\perp}^2}\frac{\partial^2\mathbf{\Psi}}{\partial t^2} = 0$ | Non-zero mechanical vorticity tensor $\Omega_{ab} \neq 0$, whose closed spatial circulation is a quantized topological invariant. |
| **Emergent physical status** | **Massless physical vacuum** (background for electromagnetic wave propagation). | **Stable, quantized macroscopic matter** (elementary particles as nodes). |

## The Axiom of Matter: Mathematical Structure of Defects, Inertia, and Spin {#sec-1-6}

Under the influence of extreme non-linear compression ($\phi(\mathbf{x}) \ge \phi_{\text{lock}}$), linear acoustic fluctuations lose the capability of wave relaxation, and the lattice cells are forced into geometric looping. In the 4-dimensional continuum of the Substrate, stable standing waves (solitons) are formed, which are in essence permanent topological nodes that macroscopic physics identifies as fermions. These nodes are fully 4-dimensional entities—their structure extends also into the fourth spatial dimension ($x^4$), which is of substantive significance for the emergence of gravity and nuclear interactions.

### Mathematical Structure of the Topological Charge and Soliton Profile {#sec-1-6-1}

To endow the concept of "topological twisting" with a rigorous mathematical meaning, the phase deformation field of the matrix framework in the vicinity of the defect must be represented as a continuous smooth mapping from the physical space $\mathbb{R}^3$ (compactified by a point at infinity, which topologically yields the sphere $S^3$) into the space of internal phase states $SU(2) \cong S^3$. Let $\mathbf{U}(\mathbf{x})$ be a unitary matrix field defined as:

$$\mathbf{U}(\mathbf{x}) = \pi_0(\mathbf{x})\mathbb{I} + i \sum_{a=1}^3 \pi_a(\mathbf{x})\sigma_a$$ {#eq-1-6-wz1}

where $\sigma_a$ are the Pauli matrices, $\mathbb{I}$ is the identity matrix, and the quaternionic components of the field $\pi_\mu(\mathbf{x})$ satisfy the geometric normalization condition $\sum_{\mu=0}^3 \pi_\mu^2 = 1$.

The topological charge $\mathcal{W}$, constituting a candidate for a conserved quantum number of the particle (corresponding to the baryon number in standard Skyrme theory; its identification with the electric charge is a postulate of the TSM model requiring further justification in Chapter 3), is an invariant representing the degree of the mapping (the homotopy index $\pi_3(S^3)$) and is given by an explicit integral formula:

$$\mathcal{W} = \frac{1}{24\pi^2} \int_{\mathbb{R}^3} d^3x \, \epsilon^{ijk} \text{Tr}\left[ (\mathbf{U}^{-1}\partial_i \mathbf{U}) (\mathbf{U}^{-1}\partial_j \mathbf{U}) (\mathbf{U}^{-1}\partial_k \mathbf{U}) \right]$$ {#eq-1-6-wz2-w}

where $\epsilon^{ijk}$ is the completely antisymmetric Levi-Civita tensor in three dimensions, and $\partial_i \equiv \partial/\partial x^i$. The invariant $\mathcal{W}$ takes exclusively integer values ($\mathcal{W} \in \mathbb{Z}$), which constitutes a purely geometric, first principle of the absolute quantization of the elementary charge in the TSM model.

Derrick's classical theorem postulates that three-dimensional solitons in linear field theories are unstable and spontaneously collapse to a point. In the TSM model, this problem is resolved geometrically: an attempt to further contract the soliton induces an asymptotic increase in shear stress energy. This results from the fact that the local deformation density approaches the structural jamming threshold $\phi_{\text{lock}}$, at which the effective stiffness modulus tends to infinity. This geometric locking arrests the collapse, stabilizing a finite rest size $L$ of the soliton core.

The dynamics of spatial stabilization follow directly from the balance between the long-range elastic energy and the non-linear periodic potential of the lattice. In the full three-dimensional description, to preserve the spherical symmetry of an isolated static defect, the so-called hedgehog ansatz (*Hedgehog ansatz*) is introduced, which is a particular, radially symmetric solution of the aforementioned general form of the field—corresponding to the substitution $\pi_0(\mathbf{x})=\cos\theta(r)$ and $\pi_a(\mathbf{x})=\hat{x}_a\sin\theta(r)$, which automatically satisfies the normalization condition $\sum_\mu\pi_\mu^2=1$. The unitary matrix field then assumes an explicit radial form:

$$\mathbf{U}(\mathbf{x}) = \cos\theta(r)\mathbb{I} + i (\hat{\mathbf{x}} \cdot \boldsymbol{\sigma}) \sin\theta(r)$$  {#eq-1-6-wz3}

where $r = |\mathbf{x}|$ represents the distance from the center of the defect, $\hat{\mathbf{x}} = \mathbf{x}/r$ is the radial unit vector, and $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ denotes the vector of Pauli matrices. The phase profile $\theta(r)$ determines the spatial structure of the soliton core, and the total rest mass $m_0$ follows directly from the volumetric integration of the three-dimensional elastic energy density $\rho_{E}(\mathbf{x})$ in spherical coordinates:

$$m_0 = \int_{\mathbb{R}^3} \rho_{E}(\mathbf{x}) \, d^3x = 4\pi \int_{0}^{\infty} \rho_{E}(r) r^2 \, dr$$  {#eq-1-6-wz4-mspocz}

The rigorous differential equation for the radial profile $\theta(r)$, arising from the full spherical Laplacian in $\mathbb{R}^3$, contains an additional curvature term $\frac{2}{r}\theta'(r)$, which is absent in the one-dimensional reduction considered below. For this reason, the formula for $m_0$ above, although formally rigorous, generally requires a numerical or approximate solution $\theta(r)$ of this full radial equation, rather than a direct substitution of the profile $\theta(x)$ obtained in the one-dimensional reduction.

To obtain analytical, closed-form solutions for the phase transition profiles and to analyze the behavior of a defect moving along a specific axis, a dimensional reduction to a one-dimensional formulation is performed, considering a cross-section along the wave propagation trajectory. The profile $\theta(x)$ and its corresponding density $\rho_E(x)$, derived below in this reduced formulation, are subsequently applied in the mass integral $m_0$ as an approximation valid within the soliton core region away from the curvature singularity at $r=0$—where the radial curvature is negligible relative to the phase gradient. The rigorous closure of the full, three-dimensional radial profile $\theta(r)$ remains an open mathematical problem of this chapter, analogous to the others identified above (the derivation of $c_\perp$ in the variable regime, §1.4.5; the relationship of $\phi_{\text{eff}}(\mathbf{x})$ to microdynamics, §1.5.1).

In this formulation, the spatial evolution of the local phase twist angle $\theta(x)$ is described by a non-linear differential equation of the Sine-Gordon type:

$$\frac{\partial^2 \theta}{\partial x^2} - \frac{\rho_{\text{eff}}}{\mu}\frac{\partial^2 \theta}{\partial t_{\text{flat}}^2} = \frac{1}{L^2} \sin(\theta)$$ {#eq-1-6-wz5-kat-skret}

For a static soliton ($\partial_t \theta = 0$) carrying an elementary topological charge $\mathcal{W}=1$, the analytical solution determining the phase transition profile in the matrix framework is a kink structure:

$$\theta(x) = 4 \arctan\left( \exp\left( \frac{x - x_0}{L} \right) \right)$$  {#eq-1-6-wz6-kinku}

The elastic energy density $\rho_{E}(x)$ locked inside this defect assumes the rigorous form:

$$\rho_{E}(x) = \frac{\mu}{2} \left( \frac{\partial \theta}{\partial x} \right)^2 + \frac{\mu}{L^2} (1 - \cos\theta) = \frac{4\mu}{L^2} \text{sech}^2\left(\frac{x - x_0}{L}\right)$$  {#eq-1-6-wz7-esprez}

The Substrate architecture rigorously separates two fundamental features of the defect:

* **Electric charge:** A topologically quantized invariant $\mathcal{W}$, depending solely on the closure of a full phase rotation in space and the topological invariance of the mapping.
* **Rest mass:** The integrated potential energy of the local elastic stresses of the matrix framework. A more complex, denser topological entanglement generates stronger gradients of the phase field, forcing a larger amount of energy $m_0$ to be stored in the core, despite the possibility of carrying the same elementary topological charge.

### Elastodynamic Resistance as the Source of Inertia {#sec-1-6-2}

As the soliton moves through the discrete structure of the 0-Matrix, the translational continuity of the background is broken by the misfit potential of the crystalline lattice. The activation energy of this barrier (the Peierls-Nabarro potential) is described by the function:

$$U_{\text{PN}}(b) = U_0 \cos\left( \frac{2\pi b}{a} \right)$$ {#eq-1-6-wz8-enaktyw}

where $b$ determines the displacement of the soliton center relative to the nearest lattice node with constant $a$. The barrier amplitude $U_0$ decreases exponentially with an increasing ratio $L/a$.

**Recall:**

The motion of a soliton does not consist in the physical translation of elements through the medium, but rather in the sequential, lossless transfer of the strain state (wave) from one lattice cell to the neighboring one. Since the node core size $L$ (femtometer scale) exceeds the distance between the Substrate elements $a$ (sub-Planckian scale) by many orders of magnitude, the barrier amplitude $U_0$ tends asymptotically to zero. This ensures a macroscopically smooth phenomenal motion.

Resistance appears exclusively when attempting to alter the state of motion—the necessity of a local, phonic reorganization of the momenta of the vibrating elements of the crystalline Substrate during the acceleration of the deformation wave generates a hydrodynamic drag of the medium, observed in the macroscale as **inertia**.

### Explanation of the Geometric-Wave Method {#sec-1-6-3}

The introduction of the degree of mapping integral of the topological charge removes the heuristic nature of the description of particles. From a mathematical perspective, this invariant guarantees that the field profile cannot undergo continuous deformation to the vacuum state ($\mathbf{U}=\mathbb{I}$) without rupturing the continuity of the Substrate, thereby ensuring the absolute stability of matter. The Sine-Gordon wave equation and the energy density in turn provide a direct analytical bridge to the interpretation of rest mass as the stored elastic energy of the background, explicitly linking the integral description in $\mathbb{R}^3$ with reduced models of one-dimensional trajectories.

### Geometric Origin of Spin 1/2 and the Ontology of Antimatter {#sec-1-6-4}

The confinement of a soliton in a continuous, elastic medium imposes specific boundary conditions on its rotation. A defect described by a unitary matrix field $\mathbf{U}(\mathbf{x}) \in SU(2)$ requires a rotation in physical space by an angle of $4\pi$ ($720^\circ$) for the three-dimensional strain lines of the surrounding background to spontaneously return to a state of zero stress (to untangle). The rotation configuration space for this type of topological object is doubly covered by the spinor group, which makes spin 1/2 a direct mechanical consequence of the topology of the continuous Substrate.

The TSM model also redefines the ontology of antimatter, eliminating the concept of negative energy or motion backward in time:

* **Chiral symmetry:** For every node with a positive topological charge $\mathcal{W} = +1$, there exists a mirror configuration with reversed phase field chirality, for which $\mathcal{W} = -1$.
* **Antimatter mass:** Since the elastic energy density $\rho_{E}(x)$ depends on the square of the spatial derivatives of the field, both configurations (particle and antiparticle) generate an identical, positive contribution to the rest mass $m_0$.
* **Annihilation:** The collision of a particle with an antiparticle constitutes a process of topological annihilation. The vector twists sum to a net zero charge ($\mathcal{W}_{\text{net}} = 0$), leading to a violent untangling of local defects and the residual-free release of the stored elastic energy in the form of pure transverse waves of the matrix framework (photons).