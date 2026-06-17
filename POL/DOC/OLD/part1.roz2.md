<!-- ver:2.2.0 -->
# Rozdział 2: Węzły topologiczne i emergencja solitoniczna w TSM – czas lokalny, hydrodynamika bezwładności, antymateria, geometryczne pochodzenie spinu 1/2 oraz formalizm sztywności Substratu

Zdefiniowanie lokalnego czasu $t$ (Rozdział 1.1) oraz makroskopowych właściwości kontinuum pozwala na przejście do kluczowego zagadnienia Mechaniki Substratu Topologicznego (TSM): pytania o to, w jaki sposób z globalnie zakleszczonego tła 0‑cząstek wyłaniają się skwantowane, stabilne formy materii. Model TSM całkowicie odrzuca dualizm korpuskularno‑falowy w jego tradycyjnym, abstrakcyjnym ujęciu. Cząstki elementarne nie są punktami poruszającymi się w próżni; są lokalnymi, nieliniowymi defektami topologicznymi (solitonami) samej struktury osnowy.

---

## 2.0. Czas lokalny w formalizmie dynamiki Substratu – przypomnienie i osadzenie

Zgodnie z Rozdziałem 1.1, TSM odrzuca zarówno absolutny czas newtonowski, jak i relatywistyczną czasoprzestrzeń jako byt pierwotny. Fundamentem dynamiki jest **lokalny czas własny** $t$, wyłaniający się z gęstości upakowania 0‑Matrycy.

Z @sec-roz1-czas przypomnijmy definicję kanoniczną – przyrost czasu własnego w punkcie $\mathbf{x}$: 

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi\rangle_{\text{macro}}}$$ (@eq-r1-czasEmergentny)

gdzie:
- $dt$ – przyrost lokalnego czasu mierzonego w punkcie $\mathbf{x}$,
- $dN$ – liczba pełnych cykli procesu okresowego (bezwymiarowa),
- $T_0$ – elementarny okres referencyjny w płaskiej osnowie $[\text{s}]$,
- $\phi(\mathbf{x})$ – lokalny ułamek upakowania 0‑cząstek (bezwymiarowy),
- $\phi_0$ – referencyjny ułamek upakowania w płaskiej, niezakłóconej osnowie.

W asymptotycznie płaskim obszarze 3‑brany ($\phi = \phi_0$) lokalny czas własny pokrywa się z **czasem współrzędnościowym** $t_{\text{flat}}$, który stanowi naturalną zmienną niezależną w równaniach dynamiki osnowy. W dalszej części tego rozdziału symbol $t$ oznacza właśnie ten płaski czas współrzędnościowy – wspólną miarę ewolucji dla niezakłóconego Substratu. W obszarach o podwyższonej gęstości (w pobliżu węzłów) czas lokalny zwalnia zgodnie z (1.1.4), co zostanie uwzględnione w dynamice solitonów.

---

## 2.1. Mikroskopowy mechanizm skończonej ściśliwości i rygorystyczny formalizm elasto‑dynamiczny w $\mathbb{R}^4$

### 2.1.1. Stan globalnego zakleszczenia i skończona sztywność objętościowa

Zgodnie z Rozdziałem 0.3, cała 4‑wymiarowa 0‑Matryca od początku znajduje się w stanie **globalnego zakleszczenia (jamming)** – ułamek upakowania przekracza wartość krytyczną $\phi_c$ w całej objętości bańki. Nie istniała pierwotna faza chaotyczna – osnowa od początku jest sztywnym, sprężystym szkłem topologicznym, zdolnym do przenoszenia naprężeń we wszystkich czterech wymiarach.

W odróżnieniu od modeli zakładających nieskończoną sztywność, TSM definiuje stan osnowy jako ośrodek o wysokiej, lecz skończonej ściśliwości. Ułamek upakowania $\phi$ oscyluje wokół wartości referencyjnej $\phi_0$ (w obszarach niezakłóconych) i może lokalnie wzrastać aż do granicy $\phi_{\text{max}}$ (kontaktu jąder 0‑cząstek). To implikuje, że sfery oddziaływań posiadają mierzalną, elastomechaniczną podatność.

W konsekwencji, dynamiczny opis 0‑Matrycy musi uwzględniać dwa niezależne parametry materiałowe: moduł sprężystości objętościowej $K$ (odpowiedzialny za reakcję na zmianę gęstości) oraz moduł sprężystości poprzecznej $\mu$ (odpowiedzialny za reakcję na ścinanie). Te stałe materiałowe determinują istnienie dwóch odrębnych klas wzbudzeń falowych w kontinuum, charakteryzujących się różnymi prędkościami propagacji.

### 2.1.2. Pełny rozkład Hodge’a‑Helmholtza pola przemieszczeń w $\mathbb{R}^4$

Aby zachować pełną niezmienniczość wymiarową i rygor matematyczny w przestrzeni czterowymiarowej, pole przemieszczeń strukturalnych osnowy reprezentujemy jako 1‑formę różniczkową $\Phi \in \Omega^1(\mathbb{R}^4)$, zdefiniowaną w bazie współrzędnych przestrzennych $(x^1, x^2, x^3, x^4)$:

$$\Phi = \Phi_1 dx^1 + \Phi_2 dx^2 + \Phi_3 dx^3 + \Phi_4 dx^4 \tag{2.1.1}$$

gdzie:
- $\Phi_i$ – składowe pola przemieszczeń $[\text{m}]$,
- $dx^i$ – baza 1‑form w $\mathbb{R}^4$.

Zgodnie z twierdzeniem Hodge’a o rozkładzie ortogonalnym na płaskiej rozmaitości $\mathbb{R}^4$, pole to rozbija się jednoznacznie na sumę formy ścisłej, ko‑ścisłej oraz składnika harmonicznego (który w rozważaniach lokalnych przyjmujemy jako zerowy):

$$\Phi = \Phi_L + \Phi_T = d\alpha + \delta\beta \tag{2.1.2}$$

gdzie:
- $d: \Omega^k \to \Omega^{k+1}$ – pochodna zewnętrzna (uogólniony gradient, generujący rotację i ekspansję),
- $\delta: \Omega^k \to \Omega^{k-1}$ – operator ko‑dyferencjału (uogólniona dywergencja), zdefiniowany poprzez gwiazdkę Hodge’a $\star$ jako $\delta = -\star d \star$,
- $\alpha \in \Omega^0(\mathbb{R}^4)$ – 0‑forma (potencjał skalarny pola podłużnego),
- $\beta \in \Omega^2(\mathbb{R}^4)$ – 2‑forma (potencjał tensorowy pól poprzecznych).

W odróżnieniu od ograniczeń fazy izostatycznej, potencjał $\alpha \neq 0$, co oznacza, że lokalne zagęszczenia i rozrzedzenia substratu stanowią aktywny fizycznie stopień swobody.

### 2.1.3. Równania ruchu i separacja modów

Ogólne 4‑wymiarowe równanie elasto‑dynamiczne Naviera‑Cauchy’ego dla ośrodka o gęstości masowej $\rho_0$ i stałych Lamégo $\lambda$ oraz $\mu$ przyjmuje w notacji zewnętrznej postać:

$$\rho_0 \frac{\partial^2 \Phi}{\partial t^2} = (\lambda + 2\mu) d\delta \Phi - \mu \delta d \Phi \tag{2.1.3}$$

gdzie:
- $\rho_0$ – gęstość masy bezwładnej 0‑cząstek w Stanie Zero $[\text{kg} \cdot \text{m}^{-4}]$,
- $\lambda, \mu$ – stałe Lamégo osnowy $[\text{Pa}]$,
- $t$ – czas współrzędnościowy płaskiej osnowy $[\text{s}]$.

Podstawiając pełny rozkład Hodge’a $\Phi = d\alpha + \delta\beta$ oraz wykorzystując tożsamości nilpotentne operatorów ($d^2 = 0$ oraz $\delta^2 = 0$), równanie ruchu ulega automatycznej separacji na dwa niezależne układy dynamiczne:

$$\rho_0 d \left( \frac{\partial^2 \alpha}{\partial t^2} \right) + \rho_0 \delta \left( \frac{\partial^2 \beta}{\partial t^2} \right) = (\lambda + 2\mu) d(\delta d \alpha) - \mu \delta(d \delta \beta) \tag{2.1.4}$$

Z racji ortogonalności przestrzeni form ścisłych i ko‑ścisłych, powyższa tożsamość rozpada się na dwa niezależne równania falowe:

**1. Równanie modu podłużnego (dla 0‑formy $\alpha$):**

$$\frac{\partial^2 \alpha}{\partial t^2} = c_L^2 \delta d \alpha \quad \implies \quad \frac{\partial^2 \alpha}{\partial t^2} = c_L^2 \nabla^2_{4D} \alpha \tag{2.1.5}$$

gdzie prędkość fali podłużnej wynosi:

$$c_L = \sqrt{\frac{\lambda + 2\mu}{\rho_0}} \tag{2.1.6}$$

**2. Równanie modu poprzecznego (dla 2‑formy $\beta$):**

$$\delta \left( \frac{\partial^2 \beta}{\partial t^2} + c_{\perp}^2 d\delta\beta \right) = 0 \tag{2.1.7}$$

gdzie prędkość fali poprzecznej (ścinania) wynosi:

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_0}} \tag{2.1.8}$$

### 2.1.4. Kalibracja pola potencjału ścinania (Warunek cechowania)

Wprowadzenie fizycznego pola przemieszczeń poprzecznych jako formy ko‑ścisłej $\Phi_T = \delta\beta$ (gdzie $\beta$ jest 2‑formą potencjału) niesie za sobą strukturalną redundancję opisu geometrycznego. Z właściwości operatora ko‑dyferencjału wynika, że dla dowolnej gładkiej 3‑formy $\chi$ transformacja cechowania postaci:

$$\beta \to \beta + \delta\chi$$

nie modyfikuje mierzalnego pola fizycznego, ponieważ $\delta^2 \chi \equiv 0$. Aby usunąć te niefizyczne stopnie swobody i zapewnić jednoznaczność rozwiązań równań dynamicznych, konieczne jest narzucenie rygorystycznego więzu kalibracyjnego.

W odróżnieniu od klasycznej elektrodynamiki (gdzie dla wektorowego potencjału $A$ stosuje się cechowanie Lorenza $\delta A = 0$), w mechanice odkształceń Substratu narzucenie warunku $\delta\beta = 0$ prowadziłoby do natychmiastowego, niefizycznego wyzerowania samego pola przemieszczeń ($\Phi_T = 0$). Właściwym formalnie warunkiem cechowania, ortogonalnym do obrazu operatora $\delta$, jest warunek zewnętrznej zamkniętości 2‑formy potencjału:

$$d\beta = 0 \tag{2.1.9}$$

Warunek (2.1.9) skutecznie zamraża gradienty zewnętrzne potencjału ścinania, eliminując niefizyczne rotacje wyższych rzędów, jednocześnie w żaden sposób nie ograniczając swobody formowania poprzecznych falowych deformacji sieci przez operator ko‑dyferencjału.

### 2.1.5. Równanie ewolucji fal poprzecznych w reżimie kalibracyjnym

Sformułowanie więzu cechowania $d\beta = 0$ pozwala na bezpośrednią redukcję ogólnego operatora Laplace'a–de Rhama ($\Delta = d\delta + \delta d$), który rządzi dyspersją i dynamiką naprężeń sprężystych w wielowymiarowych ośrodkach ciągłych. Działając operatorem $\Delta$ na 2‑formę potencjału $\beta$, przy uwzględnieniu warunku (2.1.9), człon zawierający dyferencjał zewnętrzny znika ($\delta d\beta = 0$). W konsekwencji operator Laplace'a–de Rhama redukuje się do postaci ściśle sprzężonej z ko‑dyferencjałem: $\Delta\beta = d\delta\beta$.

Dynamiczne równanie falowe, opisujące bezstratną propagację lokalnych deformacji ścinających (utożsamianych w skali makroskopowej z wolnymi falami elektromagnetycznymi oraz perturbacjami grawitacyjnymi wewnątrz 3‑brany), przyjmuje w lokalnym układzie odniesienia czasowego $t$ następującą formę kanoniczną:

$$\frac{\partial^2 \beta}{\partial t^2} = -c_{\perp}^2 d\delta \beta \tag{2.1.10}$$

gdzie stała $c_{\perp} = \sqrt{\mu/\rho_0}$ reprezentuje prędkość poprzeczną Substratu (prędkość światła $c$), zdeterminowaną przez mikroskopowy moduł sztywności na ścinanie $\mu$ oraz podstawową gęstość upakowania tła $\rho_0$.

Spójność i poprawność fizyczną równania (2.1.10) potwierdza operacja obustronnego nałożenia operatora $\delta$. Generuje ona bezpośrednie przejście od poziomu abstrakcyjnego potencjału do poziomu obserwowalnego pola przemieszczeń:

$$\frac{\partial^2 (\delta\beta)}{\partial t^2} = -c_{\perp}^2 \delta(d\delta \beta)$$

Z definicji pola $\Phi_T = \delta\beta$ oraz tożsamości dla form ko‑zamkniętych ($\delta\Phi_T = \delta^2\beta = 0$), operator po prawej stronie redukuje się do pełnego d'Alembertianu pola fizycznego: $\delta d\Phi_T = (d\delta + \delta d)\Phi_T = \Delta\Phi_T$. Otrzymujemy ostatecznie klasyczne, rygorystyczne równanie falowe:

$$\frac{\partial^2 \Phi_T}{\partial t^2} = -c_{\perp}^2 \Delta \Phi_T$$

Dowodzi to, że wprowadzone cechowanie (2.1.9) oraz zmodyfikowane równanie ewolucji (2.1.10) w sposób matematycznie zamknięty i wolny od sprzeczności opisują stabilną propagację światła jako fali deformacji poprzecznych 0‑Matrycy.

### 2.1.6. Rzutowanie 3D + $x^4$: Rozszerzona mapa pól fizycznych

Rozdzielenie współrzędnych wewnątrzpowierzchniowych 3‑brany ($x^1, x^2, x^3$) od osi ortogonalnej Bulk ($x^4$) pozwala na zmapowanie składowych form różniczkowych na obserwowalne makroskopowo oddziaływania.

**Dekompozycja modu poprzecznego ($\beta \in \Omega^2(\mathbb{R}^4)$):**

2‑formę $\beta$ rozbijamy na składowe wewnętrzne i zewnętrzne względem brany:

$$\beta = \bar{\beta} + \bar{\psi} \wedge dx^4 \tag{2.1.11}$$

- $\bar{\beta} = \frac{1}{2}\beta_{ij} dx^i \wedge dx^j$ (3 składowe): reprezentuje płaszczyzny polaryzacji zamknięte wewnątrz 3‑brany. Generuje poprzeczne fale elektromagnetyczne, poruszające się z prędkością graniczną $c = c_{\perp}$. Składowe formy $\bar{\beta}$ mapują się bezpośrednio na potencjał cechowania $A_\mu$, a jej pochodna zewnętrzna wyznacza antysymetryczny tensor pola elektromagnetycznego $F = d\bar{\beta}$ (pomost do Rozdziału 3).
- $\bar{\psi} = \beta_{i4} dx^i$ (3 składowe): reprezentuje płaszczyzny polaryzacji sprzężone z kierunkiem ortogonalnym. Generuje naciąg mechaniczny membrany w osi $x^4$, interpretowany jako pole grawitacyjne.

Warunek cechowania $d\beta = 0$ w tym rozbiciu przyjmuje formę układu strukturalnych więzów geometrycznych dla poszczególnych rzutów:

$$d_{3D}\bar{\beta} = 0 \tag{2.1.12}$$

$$d_{3D}\bar{\psi} = \partial_4 \bar{\beta} \tag{2.1.13}$$

Równanie (2.1.12) orzeka o lokalnej zamkniętości 3‑wymiarowej składowej potencjału, co odpowiada bezźródłowości pól powiązanych z wewnętrznymi rotacjami brany. Z kolei równanie (2.1.13) określa bezpośrednie sprzężenie przestrzennej rotacji pola naciągu grawitacyjnego $\bar{\psi}$ ze zmianami profilu pola elektromagnetycznego $\bar{\beta}$ wzdłuż wymiaru Bulk ($x^4$). Zapewnia to dynamiczną spójność i lokalne równoważenie naprężeń elektromagnetycznych przez gradienty sił ortogonalnych.

**Dekompozycja modu podłużnego ($\alpha \in \Omega^0(\mathbb{R}^4)$):**

Pochodna zewnętrzna 0‑formy potencjału podłużnego tworzy pole gradientów:

$$d\alpha = \bar{d}\alpha + \partial_4 \alpha dx^4 = \left(\sum_{i=1}^3 \partial_i \alpha dx^i\right) + \partial_4 \alpha dx^4 \tag{2.1.14}$$

- Składnik $\bar{d}\alpha$ (wewnątrzbrany): generuje podłużne fale ciśnienia mechanicznego bezpośrednio w trójwymiarowej płaszczyźnie osnowy. Objawia się jako skalarowe pole gęstości tła, związane z relaksacją Substratu.
- Składnik $\partial_4 \alpha$ (ortogonalny): definiuje symetryczne ściskanie i rozszerzanie profilu grubości 3‑brany w przestrzeni Bulk.

Ponieważ prędkość fali podłużnej $c_L = \sqrt{(\lambda + 2\mu)/\rho_0}$ jest jawnie większa od prędkości fal poprzecznych $c_{\perp} = \sqrt{\mu/\rho_0}$, skalarowe zaburzenia kompresyjne osnowy propagują się w sposób superluminalny ($c_L > c$). Zjawisko to nie narusza wewnętrznej spójności TSM, gdyż prędkość światła $c$ jest zdefiniowana wyłącznie przez próg propagacji modów poprzecznych ($\bar{\beta}$), a fale podłużne nie przenoszą informacji w sektorze elektromagnetycznym.

---