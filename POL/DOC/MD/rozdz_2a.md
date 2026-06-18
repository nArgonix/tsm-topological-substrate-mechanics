<!-- ver:3.2.0 -->

# Rozdział 2: Struktura materii – od elastodynamiki 4D do sformalizowanego modelu Faddeeva‑Skyrme’a i reguły Koidego

Zdefiniowanie globalnych parametrów ewolucyjnych oraz makroskopowych właściwości kontinuum (Rozdział 1) pozwala na przejście do kluczowego zagadnienia Mechaniki Substratu Topologicznego (TSM): w jaki sposób z kinetycznego tła ultra‑szybkich drgań 0‑cząstek wyłania się sztywny ośrodek, a w nim – skwantowane, trwałe formy materii. TSM całkowicie odrzuca dualizm korpuskularno‑falowy w jego tradycyjnym, abstrakcyjnym ujęciu. Cząstki elementarne nie są punktami; są lokalnymi, nieliniowymi defektami topologicznymi (solitonami) samej struktury 0‑Matrycy, uwięzionymi w mechanizmie dylatacji temporalnej.

---

## 2.0. Czas lokalny w formalizmie dynamiki Substratu – osadzenie

Zgodnie z Aksjomatem II, pierwotne mikro‑oscylacje 0‑cząstek nie mierzą upływu czasu, lecz stanowią źródło energii tła. Fundamentem dynamiki makroskopowej jest **lokalny czas własny** $t$, wyłaniający się z gęstości upakowania i częstotliwości zderzeń. Przyrost czasu własnego w punkcie $\mathbf{x}$ wyraża się równaniem:

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi\rangle_{\text{macro}}} \tag{2.0.1}$$ 

Gdzie:
- $dt$ – przyrost lokalnego czasu własnego $[\text{s}]$,
- $dN$ – liczba cykli makroskopowego procesu okresowego (np. oscylacji atomowych),
- $T_0$ – okres referencyjny w niezaburzonej, stacjonarnej osnowie $[\text{s}]$,
- $\phi_0$ – podstawowa gęstość upakowania 0‑Matrycy w Stanie Zero,
- $\langle\phi\rangle_{\text{macro}}$ – uśredniona hydrodynamicznie gęstość osnowy w obszarze pomiarowym.

W obszarach o ekstremalnie wysokiej gęstości, takich jak rdzenie stabilnych solitonów ($\phi \to \phi_{\text{max}}$), przyrost $dt$ dąży do zera. Ta silna dylatacja temporalna „zamraża” strukturę wewnętrzną węzła, chroniąc uformowany splot przed dekoherencją termiczną podłoża (szumem $T_{\text{sub}}$), co jest kluczem do stabilności cząstek.

---

## 2.1. Mikroskopowy mechanizm skończonej ściśliwości i rygorystyczny formalizm elasto‑dynamiczny w $\mathbb{R}^4$

Osnowa, mimo globalnego zakleszczenia, posiada skończoną podatność sprężystą wynikającą z dynamiki sfer oddziaływań. To pozwala na opis rzeczywistości przy użyciu 4‑wymiarowej elastodynamiki.

### 2.1.1. Stan globalnego zakleszczenia i skończona sztywność objętościowa

Zgodnie z Rozdziałem 0.3, cała 4‑wymiarowa 0‑Matryca od początku znajduje się w stanie **globalnego zakleszczenia (jamming)** – ułamek upakowania przekracza wartość krytyczną $\phi_c$ w całej objętości bańki. Nie istniała pierwotna faza chaotyczna – osnowa od początku jest sztywnym, sprężystym szkłem topologicznym, zdolnym do przenoszenia naprężeń we wszystkich czterech wymiarach. Pierwotne 0-cząstki nie poruszają się swobodnie jak gaz, lecz wykonują szybkie oscylacje wewnątrz ustalonych, ściśle ograniczonych sfer swojego kinetycznego wpływu.

W odróżnieniu od modeli zakładających nieskończoną sztywność, TSM definiuje stan osnowy jako ośrodek o wysokiej, lecz skończonej ściśliwości. Ułamek upakowania $\phi$ oscyluje wokół wartości referencyjnej $\phi_0$ (w obszarach niezakłóconych) i może lokalnie wzrastać aż do granicy $\phi_{\text{max}}$ (kontaktu jąder 0‑cząstek). To implikuje, że sfery oddziaływań posiadają mierzalną, elastomechaniczną podatność.

W konsekwencji, dynamiczny opis 0‑Matrycy musi uwzględniać dwa parametry materiałowe: moduł sprężystości objętościowej $K$ (odpowiedzialny za reakcję na zmianę gęstości) oraz moduł sprężystości poprzecznej $\mu$ (odpowiedzialny za reakcję na ścinanie). Te stałe materiałowe determinują istnienie dwóch odrębnych klas wzbudzeń falowych w kontinuum.

### 2.1.2. Rozkład Hodge’a‑Helmholtza pola przemieszczeń w $\mathbb{R}^4$

Aby zachować rygor matematyczny w przestrzeni czterowymiarowej, pole przemieszczeń strukturalnych osnowy $\mathbf{u}(\mathbf{x})$ reprezentujemy jako 1‑formę różniczkową $\Phi \in \Omega^1(\mathbb{R}^4)$. Zgodnie z twierdzeniem Hodge’a, pole to rozbija się jednoznacznie na sumę formy ścisłej (podłużnej) i ko‑ścisłej (poprzecznej):

$$\Phi = \Phi_L + \Phi_T = d\alpha + \delta\beta \tag{2.1.1}$$

Gdzie:
- $d$ – pochodna zewnętrzna (operator gradientu),
- $\delta$ – operator ko‑dyferencjału ($\delta = \pm \star d \star$),
- $\alpha \in \Omega^0(\mathbb{R}^4)$ – potencjał skalarny generujący fale podłużne (L),
- $\beta \in \Omega^2(\mathbb{R}^4)$ – 2‑forma potencjału tensorowego generująca fale poprzeczne (T).

### 2.1.3. Równania ruchu i separacja modów

Dynamika 0‑Matrycy rządzona jest równaniem Naviera‑Cauchy’ego w przestrzeni 4D:

$$\rho_0 \frac{\partial^2 \Phi}{\partial t^2} = (\lambda + 2\mu) d\delta \Phi - \mu \delta d \Phi \tag{2.1.2}$$

Gdzie:
- $\rho_0$ – gęstość masy bezwładnej osnowy $[\text{kg} \cdot \text{m}^{-4}]$,
- $\lambda, \mu$ – współczynniki sprężystości Lamégo $[\text{Pa} \cdot \text{m}]$.

Podstawiając rozkład (2.1.1) do (2.1.2) i wykorzystując tożsamości nilpotentne ($d^2 = 0, \delta^2 = 0$), uzyskujemy dwa niezależne równania falowe dla modów o różnych prędkościach propagacji:

$$c_L = \sqrt{\frac{\lambda + 2\mu}{\rho_0}}, \quad c_{\perp} = \sqrt{\frac{\mu}{\rho_0}} \tag{2.1.4}$$

**Warunek cechowania:** Aby zapewnić jednoznaczność pola przemieszczeń poprzecznych przy zdefiniowanym ko‑potencjale $\beta$, narzuca się warunek zamkniętości:

$$d\beta = 0 \tag{2.1.5}$$

W tym cechowaniu operator Laplace’a‑de Rhama działający na $\beta$ redukuje się do $\Delta\beta = d\delta\beta$. Pole fizyczne $\Phi_T$ (identyfikowane ze światłem i grawitacją) spełnia równanie:

$$\frac{\partial^2 \beta}{\partial t^2} = -c_{\perp}^2 d \delta \beta \tag{2.1.6}$$

### 2.1.4. Rzutowanie 3D + $x^4$: Rozszerzona mapa pól fizycznych

Rozdzielenie współrzędnych 3‑brany ($x^1, x^2, x^3$) od osi ortogonalnej Bulk ($x^4$) pozwala na fizyczną interpretację składowych 2‑formy $\beta$:

$$\beta = \bar{\beta} + \bar{\psi} \wedge dx^4 \tag{2.1.7}$$

1. **Sektor Elektromagnetyczny ($\bar{\beta}$):** Reprezentuje płaszczyzny polaryzacji zamknięte wewnątrz brany. Generuje potencjał cechowania $A_\mu$, a jego wirowość tworzy tensor pola EM ($F = d\bar{\beta}$).
2. **Sektor Grawitacyjny ($\bar{\psi}$):** Reprezentuje sprzężenie z wymiarem ortogonalnym. Generuje poprzeczny naciąg membrany w osi $x^4$, postrzegany makroskopowo jako grawitacja.

Warunek $d\beta = 0$ wymusza relację kompatybilności $d_{3D} \bar{\psi} = \partial_4 \bar{\beta}$, co oznacza, że dynamika grawitacyjna jest nierozerwalnie sprzężona ze zmianą potencjału elektromagnetycznego wzdłuż czwartego wymiaru.

---

## 2.2. Sformalizowany model Faddeeva‑Skyrme’a (TSM‑FS) w przestrzeni $\mathbb{R}^4$

W reżimie wysokich energii ($\phi \ge \phi_{\text{lock}}$) liniowa elastodynamika ustępuje miejsca nieliniowemu modelowi solitonowemu. Cząstki materii definiujemy jako stabilne węzły pola orientacji komórek sieci $\mathbf{n}(\mathbf{x}, x^4) \in S^2$.

### 2.2.1. Rozszerzony Lagrangian 4D i rozwiązanie Derricka

Zgodnie z modelem Faddeeva-Skyrme’a, aby splot o ładunku topologicznym (indeksie Hopfa $Q_H$) był stabilny w 3D, Lagrangian musi zawierać człony wyższego rzędu. W TSM pełna gęstość energii układu (Hamiltonian) w $\mathbb{R}^4$ wynosi:

$$\mathcal{H}_{\text{4D}} = \underbrace{c_2 \sum_{\mu=1}^4 (\partial_\mu \mathbf{n})^2}_{\text{Sprężystość liniowa}} + \underbrace{c_4 \sum_{i,j=1}^3 (\partial_i \mathbf{n} \times \partial_j \mathbf{n})^2}_{\text{Blokada Skyrme'a}} + \underbrace{\frac{1}{2} \sigma (\partial_i \psi)^2 + \lambda (\partial_4 \mathbf{n} \cdot \nabla_3 \psi)}_{\text{Kotwica ortogonalna}} \tag{2.2.1}$$

Gdzie:
- $c_2 \propto \mu$ – liniowy moduł ścinania osnowy $[\text{Pa} \cdot \text{m}]$,
- $c_4 \propto \phi_{\text{lock}}$ – moduł nieliniowy wynikający z progu zakleszczenia,
- $\psi(\mathbf{x})$ – głębokość ugięcia brany w czwarty wymiar $[\text{m}]$,
- $\sigma$ – napięcie powierzchniowe 3‑brany.

Klasyczne twierdzenie Derricka postuluje niestabilność solitonów w polach skalarowych. TSM rozwiązuje ten problem poprzez **blokadę geometryczną**: gdy węzeł próbuje się skurczyć, gradienty orientacji rosną, generując nieliniowy opór strukturalny 0‑cząstek (człon $c_4$). Węzeł osiąga stabilny promień $L \approx \sqrt{c_4/c_2}$, w którym napięcie dążące do wygładzenia sieci równoważy się z oporem zgniecionych komórek sieci.

### 2.2.2. Emergencja masy leptonów i Reguła Koidego

Masa spoczynkowa leptonów ($e, \mu, \tau$) wynika z rezonansowej interferencji trzech modów drgań własnych splotu wzdłuż osi $x^4$. Ponieważ energia odkształcenia (masa) jest proporcjonalna do kwadratu amplitudy ($m \propto A^2$), pierwiastek z masy reprezentuje czystą amplitudę geometryczną ($\sqrt{m} \propto A$). 

Reguła Koidego zostaje wyprowadzona jako wynik symetrii $Z_3$ krystalicznej osnowy w wymiarze Bulk:

$$\frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3} \tag{2.2.2}$$

Trzy generacje leptonów to trzy stany orientacyjne tego samego podstawowego splotu $\mathcal{W}=3$, których fazy drgań w 4D są rozłożone symetrycznie co $120^\circ$. Faza Koidego $\theta_K \approx 2/9$ radiana jest bezwzględnym kątem nachylenia płaszczyzny splotu względem osi $x^4$.

---

## 2.3. Ontologia Baryonu: Warkocze i chiralna frustracja

Bariony (proton, neutron) są złożonymi strukturami wielopasmowymi, zwanymi w TSM **warkoczami 4D**. Kwarki nie są osobnymi cząstkami, lecz składowymi pasmami (strands) splotu.

### 2.3.1. Różnica mas $m_n > m_p$ jako efekt energii frustracji

Masa baryonu jest determinowana przez wielomian energii naprężeń, w którym kluczową rolę odgrywa człon **chiralnej frustracji** $\xi$:

$$\mathcal{E}_{\text{baryon}} = \mathcal{E}_{\text{linear}} + \xi \cdot [\mathbf{n}_1 \cdot (\mathbf{n}_2 \times \mathbf{n}_3)]^2 \tag{2.3.1}$$

Gdzie $\mathbf{n}_i$ to wektory orientacji poszczególnych pasm.
- W **protonie** ($uud$) dwa pasma są współliniowe, co zeruje człon frustracji ($\mathcal{K}^2 \approx 0$). Energia splotu ucieka w dalekosiężny rzut EM (ładunek dodatni).
- W **neutronie** ($udd$) warunek neutralności topologicznej ($\mathcal{W}_{\text{net}}=0$) wymusza ortogonalne splątanie pasm. Maksymalizuje to człon frustracji $\xi$. To dodatkowe napięcie wewnętrzne „wypycha” splot głębiej w wymiar Bulk, generując nadwyżkę energii sprężystej, co tłumaczy, dlaczego neutron jest cięższy od protonu o $\Delta m \approx 1.29$ MeV.

### 2.3.2. Geometryczna blokada rozpadu $\beta$

W jądrach atomowych warkocze nukleonów ulegają splątaniu kontaktowemu. Ta blokada mechaniczna uniemożliwia swobodną rotację pasm neutronu (zmianę kąta $\theta_4$), co trwale zamraża proces rozpadu $\beta$. Stabilność jądra wynika zatem z hydrodynamicznego zakleszczenia struktur w 4D.

---

## 2.4. Hydrodynamiczny mechanizm bezwładności i bariera Peierlsa‑Nabarro

Masa spoczynkowa $m_0$ to zintegrowana energia potencjalna odkształcenia sprężystego zmagazynowana w 0‑Matrycy:

$$m_0 = \frac{1}{c_{\perp}^2} \int_{\mathbb{R}^3} \mathcal{H}_{\text{3D}} \, d^3x \tag{2.4.1}$$

Ruch węzła polega na sekwencyjnym transferze stanu odkształcenia między komórkami sieci. Dzięki asymetrii skal między rozmiarem węzła $L$ (femtometry) a stałą sieci $a$ (skala sub-planckowska), dyskretna bariera oporu sieci, znana jako energia Peierlsa‑Nabarro, znika wykładniczo:

$$E_{PN} \propto \exp\left(-\pi \frac{L}{a}\right) \approx 0 \tag{2.4.2}$$

Pozwala to cząstkom na bezstratny „ślizg” przez osnowę przy stałej prędkości, co stanowi mechaniczną ontologię Pierwszej Zasady Dynamiki Newtona.

---

## 2.5. Antymateria jako inwersja chiralności

Antycząstka w TSM to defekt o dokładnie lustrzanym wektorze skrętu (przeciwna helisowość splotu) przy zachowaniu identycznej geometrii ugięcia w $x^4$ (identyczna masa dodatnia). Anihilacja jest procesem czysto mechanicznym: spotkanie przeciwnych skręceń powoduje koalescencję splotów do stanu płaskiej sieci ($Q_{net}=0$). Cała zmagazynowana energia ugięcia brany zostaje gwałtownie uwolniona jako poprzeczne fale ścinające – fotony.

---

## 2.6. Geometryczne pochodzenie spinu 1/2

Spin 1/2 nie jest abstrakcyjnym parametrem, lecz konsekwencją uwięzienia 4D‑solitonu w kontinuum. Obrót rdzenia o $360^\circ$ w płaszczyźnie Bulk ($x^4$) pozostawia linie naprężeń tła w stanie skręcenia topologicznego. Dopiero wykonanie drugiego pełnego obrotu (łącznie $720^\circ = 4\pi$) pozwala liniom naprężeń na powrót do stanu zerowego. Jest to fizyczna realizacja podwójnego nakrycia grupy rotacji $SO(3)$ przez grupę spinorową $SU(2)$.

---

## 2.7. Podsumowanie Rozdziału 2

- **Cząstka jako defekt:** Fermiony to skwantowane, nieliniowe sploty (Skyrmiony/Hopfiony) 0‑Matrycy o ładunku $\mathcal{W} \in \mathbb{Z}$.
- **Masa z ugięcia:** Masa wynika z energii ugięcia brany w wymiar $x^4$, a jej wielkość zależy od złożoności splotu.
- **Stabilizacja:** Niestabilność Derricka zostaje pokonana przez geometryczny próg zakleszczenia $\phi_{\text{lock}}$.
- **Reguła Koidego:** Jest prawem interferencji amplitud drgań własnych splotu w osi ortogonalnej osnowy.
- **Bariony:** To wielopasmowe warkocze 4D, w których masa zależy od stopnia chiralnej frustracji splotu.
