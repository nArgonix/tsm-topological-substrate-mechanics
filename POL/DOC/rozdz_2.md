<!-- ver:2.3.0 -->
- [Rozdział 2: Węzły topologiczne i emergencja solitoniczna w TSM – czas lokalny, hydrodynamika bezwładności, antymateria, geometryczne pochodzenie spinu 1/2 oraz formalizm sztywności Substratu]
  - [2.0. Czas lokalny w formalizmie dynamiki Substratu – przypomnienie i osadzenie]
  - [2.1. Mikroskopowy mechanizm skończonej ściśliwości i rygorystyczny formalizm elasto‑dynamiczny w $\\mathbb{R}^4$]
    - [2.1.1. Stan globalnego zakleszczenia i skończona sztywność objętościowa]
    - [2.1.2. Pełny rozkład Hodge’a‑Helmholtza pola przemieszczeń w $\\mathbb{R}^4$]
    - [2.1.3. Równania ruchu, separacja modów i warunek cechowania]
    - [2.1.4. Rzutowanie 3D + $x^4$: Rozszerzona mapa pól fizycznych]
  - [2.2. Załamanie superpozycji, nieliniowa konwersja modów i hybrydowe węzły topologiczne (Skyrmiony-Hopfiony)]
    - [2.2.1. Nieliniowa konwersja modów i próg plastyczności]
    - [2.2.2. Model Faddeeva-Skyrme’a i rozwiązanie niestabilności Derricka (Błąd nr 3)]
    - [2.2.3. Dualizm Skyrmion-Hopfion i struktura warkoczowa barionów]
  - [2.3. Hydrodynamiczny mechanizm bezwładności i bariera Peierlsa‑Nabarro]
    - [2.3.1. Masa jako zintegrowana energia odkształcenia]
    - [2.3.2. Ruch bezstratny – transfer stanu odkształcenia]
    - [2.3.3. Zniesienie barier dyskretnych (efekt Peierlsa‑Nabarro)]
  - [2.4. Istota ładunku i rozdzielenie od masy spoczynkowej]
  - [2.5. Antymateria jako inwersja topologiczna]
    - [2.5.1. Chiralność węzła]
    - [2.5.2. Mechanizm anihilacji]
  - [2.6. Geometryczne pochodzenie spinu 1/2 i podwójne nakrycie]
    - [2.6.1. Przestrzeń konfiguracji 4D i struktura rotacji]
  - [2.7. Podsumowanie Rozdziału 2]


# Rozdział 2: Węzły topologiczne i emergencja solitoniczna w TSM – czas lokalny, hydrodynamika bezwładności, antymateria, geometryczne pochodzenie spinu 1/2 oraz formalizm sztywności Substratu

Zdefiniowanie lokalnego czasu $t$ (Rozdział 1.1) oraz makroskopowych właściwości kontinuum pozwala na przejście do kluczowego zagadnienia Mechaniki Substratu Topologicznego (TSM): pytania o to, w jaki sposób z globalnie zakleszczonego tła 0‑cząstek wyłaniają się skwantowane, stabilne formy materii. Model TSM całkowicie odrzuca dualizm korpuskularno‑falowy w jego tradycyjnym, abstrakcyjnym ujęciu. Cząstki elementarne nie są punktami poruszającymi się w próżni; są lokalnymi, nieliniowymi defektami topologicznymi (solitonami) samej struktury osnowy.

---

## 2.0. Czas lokalny w formalizmie dynamiki Substratu – przypomnienie i osadzenie



Zgodnie z Rozdziałem 1.1, TSM odrzuca zarówno absolutny czas newtonowski, jak i relatywistyczną czasoprzestrzeń jako byt pierwotny. Fundamentem dynamiki jest **lokalny czas własny** $t$, wyłaniający się z gęstości upakowania 0‑Matrycy.

Przypomnijmy definicję kanoniczną – przyrost czasu własnego w punkcie $\mathbf{x}$:

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi\rangle_{\text{macro}}}$$ 

gdzie:
* $dt$ – przyrost lokalnego czasu własnego [s],
* $dN$ – liczba cykli makroskopowego procesu okresowego (np. oscylacji atomowych w zegarze),
* $T_0$ – okres referencyjny w niezaburzonej, stacjonarnej osnowie,
* $\phi_0$ – podstawowa gęstość upakowania 0-Matrycy w Stanie Zero,
* $\langle\phi\rangle_{\text{macro}}$ – uśredniona hydrodynamicznie gęstość osnowy w obszarze zajmowanym przez układ pomiarowy.

W asymptotycznie płaskim obszarze 3‑brany ($\phi = \phi_0$) lokalny czas własny pokrywa się z **czasem współrzędnościowym** $t_{\text{flat}}$, który stanowi naturalną zmienną niezależną w równaniach dynamiki osnowy. W dalszej części tego rozdziału symbol $t$ oznacza właśnie ten płaski czas współrzędnościowy – wspólną miarę ewolucji dla niezakłóconego Substratu. 

W obszarach o podwyższonej gęstości, takich jak rdzenie stabilnych solitonów, gdzie ułamek upakowania gwałtownie wzrasta, lokalny czas własny ulega ekstremalnemu spowolnieniu. Ta silna dylatacja temporalna w skali mikro stanowi bezpośrednią konsekwencję geometrycznego zakleszczenia struktury, co zostanie powiązane z wewnętrzną dynamiką węzłów.

---

## 2.1. Mikroskopowy mechanizm skończonej ściśliwości i rygorystyczny formalizm elasto‑dynamiczny w $\mathbb{R}^4$

### 2.1.1. Stan globalnego zakleszczenia i skończona sztywność objętościowa

Zgodnie z Rozdziałem 0.3, cała 4‑wymiarowa 0‑Matryca od początku znajduje się w stanie **globalnego zakleszczenia (jamming)** – ułamek upakowania przekracza wartość krytyczną $\phi_c$ w całej objętości bańki. Nie istniała pierwotna faza chaotyczna – osnowa od początku jest sztywnym, sprężystym szkłem topologicznym, zdolnym do przenoszenia naprężeń we wszystkich czterech wymiarach. Pierwotne 0-cząstki nie poruszają się swobodnie jak gaz, lecz wykonują szybkie oscylacje wewnątrz ustalonych, ściśle ograniczonych sfer swojego kinetycznego wpływu.

W odróżnieniu od modeli zakładających nieskończoną sztywność, TSM definiuje stan osnowy jako ośrodek o wysokiej, lecz skończonej ściśliwości. Ułamek upakowania $\phi$ oscyluje wokół wartości referencyjnej $\phi_0$ (w obszarach niezakłóconych) i może lokalnie wzrastać aż do granicy $\phi_{\text{max}}$ (kontaktu jąder 0‑cząstek). To implikuje, że sfery oddziaływań posiadają mierzalną, elastomechaniczną podatność.

W konsekwencji, dynamiczny opis 0‑Matrycy musi uwzględniać dwa parametry materiałowe: moduł sprężystości objętościowej $K$ (odpowiedzialny za reakcję na zmianę gęstości) oraz moduł sprężystości poprzecznej $\mu$ (odpowiedzialny za reakcję na ścinanie). Te stałe materiałowe determinują istnienie dwóch odrębnych klas wzbudzeń falowych w kontinuum.

### 2.1.2. Pełny rozkład Hodge’a‑Helmholtza pola przemieszczeń w $\mathbb{R}^4$

Aby zachować pełną niezmienniczość wymiarową i rygor matematyczny w przestrzeni czterowymiarowej, pole przemieszczeń strukturalnych osnowy reprezentujemy jako 1‑formę różniczkową $\Phi \in \Omega^1(\mathbb{R}^4)$, zdefiniowaną w bazie współrzędnych przestrzennych $(x^1, x^2, x^3, x^4)$:

$$\Phi = \Phi_1 dx^1 + \Phi_2 dx^2 + \Phi_3 dx^3 + \Phi_4 dx^4 \tag{2.1.1}$$

gdzie:
- $\Phi_i$ – składowe pola przemieszczeń $[\text{m}]$,
- $dx^i$ – baza 1‑form w $\mathbb{R}^4$.

Zgodnie z twierdzeniem Hodge’a o rozkładzie ortogonalnym na płaskiej rozmaitości $\mathbb{R}^4$, pole to rozbija się jednoznacznie na sumę formy ścisłej, ko‑ścisłej oraz składnika harmonicznego:

$$\Phi = \Phi_L + \Phi_T = d\alpha + \delta\beta \tag{2.1.2}$$

gdzie:
- $d: \Omega^k \to \Omega^{k+1}$ – pochodna zewnętrzna (uogólniony gradient),
- $\delta: \Omega^k \to \Omega^{k-1}$ – operator ko‑dyferencjału, zdefiniowany poprzez gwiazdkę Hodge’a $\star$ jako $\delta = -\star d \star$,
- $\alpha \in \Omega^0(\mathbb{R}^4)$ – 0‑forma (potencjał skalarny pola podłużnego),
- $\beta \in \Omega^2(\mathbb{R}^4)$ – 2‑forma (potencjał tensorowy pól poprzecznych).

W odróżnieniu od ograniczeń fazy izostatycznej, potencjał $\alpha \neq 0$, co oznacza, że lokalne zagęszczenia i rozrzedzenia substratu stanowią aktywny fizycznie stopień swobody.

### 2.1.3. Równania ruchu, separacja modów i warunek cechowania

Ogólne 4‑wymiarowe równanie elasto‑dynamiczne Naviera‑Cauchy’ego dla ośrodka o gęstości masowej $\rho_0$ i modułach Lamégo $\lambda$ oraz $\mu$ przyjmuje w notacji zewnętrznej postać:

$$\rho_0 \frac{\partial^2 \Phi}{\partial t^2} = (\lambda + 2\mu) d\delta \Phi - \mu \delta d \Phi \tag{2.1.3}$$

gdzie:
- $\rho_0$ – gęstość masy bezwładnej 0‑cząstek w Stanie Zero $[\text{kg} \cdot \text{m}^{-4}]$,
- $\lambda, \mu$ – współczynniki elastyczności Lamégo osnowy $[\text{Pa}]$,
- $t$ – czas współrzędnościowy płaskiej osnowy $[\text{s}]$.

*Zastrzeżenie metodologiczne:* Równanie (2.1.3) oraz wynikająca z niego separacja modów zachowują ścisłą liniowość wyłącznie w reżimie niskich energii, czyli w przybliżeniu asymptotycznie płaskiej osnowy, gdzie odkształcenia są znikome ($\phi \approx \phi_0$), a parametry $\lambda, \mu = \text{const}$. W miarę zbliżania się do krytycznych obszarów solitonicznych, stałe te stają się silnie nieliniowymi funkcjami lokalnego ułamka upakowania $\phi$, co prowadzi do sprzężenia i nieliniowej konwersji modów, opisanej w sekcji 2.2.

Podstawiając w reżimie liniowym pełny rozkład Hodge’a $\Phi = d\alpha + \delta\beta$ oraz wykorzystując tożsamości nilpotentne operatorów ($d^2 = 0$ oraz $\delta^2 = 0$), równanie ruchu ulega automatycznej separacji na dwa niezależne układy dynamiczne:

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

Aby znieść nadmiarowość geometryczną 2-formy $\beta$, narzuca się rygorystyczny warunek ko‑ścisłości (cechowanie Coulomba-Hodge'a):

$$\delta\beta = 0 \tag{2.1.9}$$

Zastosowanie cechowania $\delta\beta = 0$ redukuje operator Laplace’a‑de Rhama do czystego członu czynnego. Ostateczne, zredukowane równanie fali poprzecznej przyjmuje postać:

$$\frac{\partial^2 \beta}{\partial t^2} = -c_{\perp}^2 \delta d \beta \tag{2.1.10}$$

### 2.1.4. Rzutowanie 3D + $x^4$: Rozszerzona mapa pól fizycznych

Rozdzielenie współrzędnych wewnątrzpowierzchniowych 3‑brany ($x^1, x^2, x^3$) od osi ortogonalnej Bulk ($x^4$) pozwala na zmapowanie składowych form różniczkowych na obserwowalne makroskopowo oddziaływania.

**Dekompozycja modu poprzecznego ($\beta \in \Omega^2(\mathbb{R}^4)$):**

2‑formę $\beta$ rozbijamy na składowe wewnętrzne i zewnętrzne względem brany:

$$\beta = \bar{\beta} + \bar{\psi} \wedge dx^4 \tag{2.1.11}$$

- $\bar{\beta} = \frac{1}{2}\beta_{ij} dx^i \wedge dx^j$ (3 składowe): reprezentuje płaszczyzny polaryzacji zamknięte wewnątrz 3‑brany. Generuje poprzeczne fale elektromagnetyczne, poruszające się z prędkością graniczną $c = c_{\perp}$. Składowe formy $\bar{\beta}$ mapują się bezpośrednio na potencjał cechowania $A_\mu$, a jej pochodna zewnętrzna wyznacza antysymetryczny tensor pola elektromagnetycznego $F = d\bar{\beta}$.
- $\bar{\psi} = \beta_{i4} dx^i$ (3 składowe): reprezentuje płaszczyzny polaryzacji sprzężone z kierunkiem ortogonalnym. Generuje naciąg mechaniczny membrany w osi $x^4$, interpretowany makroskopowo jako pole grawitacyjne.

Warunek cechowania $d\beta = 0$ w tym rozbiciu narzuca lokalną zamkniętość pól:

$$d_{3D} \bar{\beta} = 0 \tag{2.1.12}$$

$$d_{3D} \bar{\psi} = \partial_4 \bar{\beta} \tag{2.1.13}$$

Zapewnia to solenoidalność pola grawitacyjnego w branie oraz lokalne równoważenie naprężeń elektromagnetycznych przez gradienty sił ortogonalnych wzdłuż czwartego wymiaru.

**Dekompozycja modu podłużnego ($\alpha \in \Omega^0(\mathbb{R}^4)$):**

Pochodna zewnętrzna 0‑formy potencjału podłużnego tworzy pole gradientów:

$$d\alpha = \bar{d}\alpha + \partial_4 \alpha dx^4 = \left(\sum_{i=1}^3 \partial_i \alpha dx^i\right) + \partial_4 \alpha dx^4 \tag{2.1.14}$$

- Składnik $\bar{d}\alpha$ (wewnątrzbrany): generuje podłużne fale ciśnienia mechanicznego bezpośrednio w trójwymiarowej płaszczyźnie osnowy. Objawia się jako skalarowe pole gęstości tła, związane z relaksacją Substratu.
- Składnik $\partial_4 \alpha$ (ortogonalny): definiuje symetryczne ściskanie i rozszerzanie profilu grubości 3‑brany w przestrzeni Bulk.

Ponieważ prędkość fali podłużnej $c_L$ jest jawnie większa od prędkości fal poprzecznych $c_{\perp}$, skalarowe zaburzenia kompresyjne osnowy propagują się w sposób superluminalny ($c_L > c$). Zjawisko to nie narusza wewnętrznej spójności relatywistycznej TSM, gdyż prędkość światła $c$ jest zdefiniowana wyłącznie przez próg propagacji modów poprzecznych ($\bar{\beta}$), a fale podłużne nie przenoszą informacji w sektorze elektromagnetycznym ani nie sprzęgają się liniowo z materią barionową w reżimie niskich energii.

---

## 2.2. Załamanie superpozycji, nieliniowa konwersja modów i hybrydowe węzły topologiczne (Skyrmiony-Hopfiony)

W reżimie niskich energii mody podłużne i poprzeczne propagują się w Substracie niezależnie. Sytuacja ta ulega jednak fundamentalnemu załamaniu w warunkach ekstremalnej lokalnej koncentracji energii, gdzie liniowa zasada superpozycji przestaje obowiązywać.

### 2.2.1. Nieliniowa konwersja modów i próg plastyczności

Gdy potężna, lokalna fluktuacja pola dylatacyjnego draszcznie zwiększa zagęszczenie 0‑cząstek, lokalny ułamek upakowania dąży do krytycznego progu zamrożenia topologicznego ($\phi \to \phi_{\text{lock}}$). W tym punkcie sfery oddziaływań kinetycznych 0‑cząstek stykają się bezpośrednio. Moduł ściśliwości objętościowej $K$ oraz moduł sztywności na ścinanie $\mu$ dążą wówczas asymptotycznie do nieskończoności ($\lim_{\phi \to \phi_{\text{lock}}} \mu(\phi) = \infty$).

Z powodu tej mechanicznej bariery energia fali podłużnej nie może być dłużej magazynowana w postaci zgniotu izotropowego. Nieskończony opór objętościowy przy przekroczeniu granicy plastyczności wymusza gwałtowną, nieliniową transformację energii podłużnej na deformacje ścinające. Nadmiarowa energia ciśnienia zostaje kaskadowo zrzucona na mod poprzeczny $\beta$, wywołując ekstremalne, lokalne skręcenie i zwichnięcie komórek sieci Wignera-Seitza.

### 2.2.2. Model Faddeeva-Skyrme’a i rozwiązanie niestabilności Derricka (Błąd nr 3)

To wymuszone skręcenie ścinające trwale modyfikuje lokalną geometrię osnowy. Stan mechaniczny przestrzeni fizycznej wewnątrz 3-brany jest opisywany znormalizowanym, trójskładnikowym polem wektorowym orientacji $\mathbf{n}(\mathbf{x}) \in S^2$ (gdzie $|\mathbf{n}| = 1$). Wektor ten nie jest abstrakcyjnym spinem izotopowym, lecz rzeczywistym wektorem orientacji lokalnego skręcenia komórek 0-Matrycy.

Klasyczne twierdzenie Derricka postuluje, że trójwymiarowe solitony (hopfiony lub skyrmiony) w ciągłych polach skalarowych są niestabilne i samorzutnie zapadają się do punktu pod wpływem sił napięcia powierzchniowego, o ile nie wprowadzi się sztucznych członów z wyższymi pochodnymi (np. członu Faddeeva czwartego rzędu). TSM usuwa ten błąd poprzez fizyczny, nieliniowy mechanizm blokady geometrycznej (**jamming**). 

Równanie całkowitej energii potencjalnej solitonu w przestrzeni o nieliniowej podatności przyjmuje postać:

$$E = \int_{\mathbb{R}^3} \left[ \mu(\phi) (\partial_i \mathbf{n})^2 + \mathcal{L}_{\text{int}}(\phi) \right] d^3x \tag{2.2.1}$$

gdzie $\mathcal{L}_{\text{int}}(\phi)$ opisuje lokalną energię oddziaływania sferycznych pól wpływu 0-cząstek. Ponieważ moduł sztywności na ścinanie posiada osobliwość strukturalną:

$$\lim_{\phi \to \phi_{\text{lock}}} \mu(\phi) = \infty \tag{2.2.2}$$

próba dalszego kurczenia się solitonu wywołuje asymptotyczny, gwałtowny wzrost energii naprężeń ścinających. Ta geometryczna blokada substratu działa jako naturalne, fizyczne odcięcie (cutoff), które bezwzględnie zatrzymuje kolaps solitonu, stabilizując jego skończony rozmiar spoczynkowy i trwale usuwając niestabilność Derricka.

### 2.2.3. Dualizm Skyrmion-Hopfion i struktura warkoczowa barionów

W celu zachowania pełnej spójności z globalnymi własnościami fermionów, TSM definiuje czystą cząstkę elementarną jako obiekt pierwotnie 4-wymiarowy – **Skyrmion 4D** oparty na grupie homotopii $\pi_4(S^3)$, którego rzutowanie lub przekrój przez hiperpłaszczyznęnaszej 3-brany indukuje nieliniowe pole orientacji $\mathbf{n}(\mathbf{x}) \in S^2$. 

W efekcie soliton wykazuje cechy dualne:
1. W sektorze masowym i spinowym (własności globalne wzbudzenia) zachowuje charakterystykę skyrmionową, generowaną przez rotacje w wymiarze Bulk ($x^4$).
2. W sektorze oddziaływań wewnątrzbrany (elektrodynamika i siły jądrowe) przyjmuje strukturę **Hopfiona 3D**, gdzie ładunek topologiczny jest scharakteryzowany przez niezmiennik Hopfa $Q_H \in \pi_3(S^2)$, reprezentujący liczbę skręcenia linii naprężeń w zamknięte pętle i węzły:

$$Q_H = \frac{1}{4\pi^2} \int_{\mathbb{R}^3} \epsilon^{ijk} A_i \partial_j A_k \, d^3x \tag{2.2.3}$$

gdzie $A_i$ jest wektorowym potencjałem pola unormowanego, indukowanym przez wirowość skręcenia sieci.

W tym formalizmie materia barionowa zyskuje rygorystyczną reprezentację jako **4D-warkocze topologiczne**. Kwarki ($u, d$) nie są niezależnymi cząstkami punktowymi, lecz składowymi pasmami (sub-strandami) jednego, złożonego węzła topologicznego. Stabilność konfiguracji jądrowych (np. protonu $uud$) wynika z dynamicznej równowagi: wysokiej częstotliwości zderzeń geometrycznych sfer wpływu oscylujących 0-cząstek w wymiarze 4D, co uniemożliwia relaksację (rozplecenie) warkocza, eliminując konieczność wprowadzania wirtualnych gluonów jako cząstek wymiany. Oddziaływanie silne staje się przejawem hydrodynamicznego oporu osnowy i ciągłych gradientów naprężeń sieci.

---

## 2.3. Hydrodynamiczny mechanizm bezwładności i bariera Peierlsa‑Nabarro

Wprowadzenie fizycznego ośrodka wymaga wyjaśnienia podstawowego problemu dynamicznego: dlaczego cząstka (węzeł) porusza się w gęstej sieci krystalicznej bez ciągłej straty energii na tarcie i dlaczego stawia opór przy przyspieszaniu.

### 2.3.1. Masa jako zintegrowana energia odkształcenia

Węzeł topologiczny reprezentuje zmagazynowaną, lokalną deformację sprężystą osnowy. Masa spoczynkowa cząstki $m_0$ jest równoważnikiem całkowitej energii potencjalnej tych naprężeń, obliczanej poprzez całkowanie gęstości lagrangianu sprężystego po objętości solitonu:

$$m_0 = \frac{1}{c_{\perp}^2} \int_{\mathbb{R}^3} \left( \frac{1}{2} K_{abcd}(\phi) \epsilon_{ab} \epsilon_{cd} \right) d^3x \tag{2.3.1}$$

gdzie:
- $m_0$ – masa spoczynkowa węzła $[\text{kg}]$,
- $c_{\perp}$ – prędkość poprzecznych fal ścinających (prędkość światła $c$) $[\text{m} \cdot \text{s}^{-1}]$,
- $K_{abcd}(\phi)$ – tensor modułów sprężystości, będący silnie nieliniową funkcją gęstości upakowania $[\text{Pa}]$,
- $\epsilon_{ab}$ – tensor odkształcenia (bezwymiarowy).

Ponieważ tensor $K_{abcd}(\phi)$ podlega nieliniowemu przesyceniu (jammingowi) w rdzeniu solitonu i dąży asymptotycznie do barier określonych przez próg $\phi_{\text{lock}}$, całka energetyczna (2.3.1) jest ściśle zbieżna. Przeciwdziała to ucieczce energii do nieskończoności i w sposób naturalny definiuje skończoną masę spoczynkową bez konieczności stosowania procedur renormalizacyjnych.

### 2.3.2. Ruch bezstratny – transfer stanu odkształcenia

Gdy na węzeł działa siła zewnętrzna, nie przesuwa ona fizycznych 0‑cząstek na duże odległości. Ruch solitonu polega na sekwencyjnym, bezstratnym transferze stanu odkształcenia z jednej komórki sieci do sąsiedniej – podobnie jak fala dylatacyjna lub soliton w kryształach makroskopowych. Uformowany, stabilny splot topologiczny o zdefiniowanej chiralności jest z definicji bezdylatacyjny w skali makroskopowej: nie zmienia sumarycznej objętości lokalnej osnowy wzdłuż wektora swojego ruchu, a jedynie ją skręca. Dzięki temu asymetryczny węzeł ślizga się po Substracie, nie emitując stratnego promieniowania w kanale modu podłużnego $\alpha$, dopóki nie zostanie rozerwany w procesie anihilacji.

Ponieważ jednak ruch ten wymaga lokalnego, hydrodynamicznego przeorganizowania pędów oscylujących 0‑cząstek, których sfery oddziaływań uległy restrykcyjnemu ograniczeniu geometrycznemu wewnątrz zagęszczonego kontinuum, proces ten generuje opór kinetyczny. Ten opór ośrodka przeciwko zmianie stanu ruchu fali stojącej jest tym, co makroskopowo nazywamy **bezwładnością**.

### 2.3.3. Zniesienie barier dyskretnych (efekt Peierlsa‑Nabarro)

W klasycznej fizyce ciał stałych ruch defektu w sieci dyskretnej wiąże się z pokonywaniem okresowego potencjału podłoża, co prowadzi do dyssypacji energii i hamowania. W TSM efekt ten zostaje zredukowany do zera poprzez asymetrię skal.

Rozmiar przestrzenny rdzenia węzła topologicznego (promień cząstki $L$) jest o wiele rzędów wielkości większy niż odległość między poszczególnymi 0‑cząstkami w stanie zakleszczenia ($a$). W granicy, gdzie $L \gg a$, okresowe fluktuacje potencjału sieci ulegają wykładniczemu wygaszeniu. Amplituda barier Peierlsa‑Nabarro ($E_{PN}$), określająca minimalną siłę potrzebną do poruszenia węzła, dąży asymptotycznie do zera:

$$E_{PN} \propto \exp\left(-\pi \frac{L}{a}\right) \approx 0 \tag{2.3.2}$$

gdzie:
- $E_{PN}$ – energia bariery Peierlsa‑Nabarro $[\text{J}]$,
- $L$ – rozmiar przestrzenny rdzenia węzła $[\text{m}]$,
- $a$ – odległość między 0‑cząstkami w stanie zakleszczenia $[\text{m}]$.

Dzięki temu węzeł porusza się w krystalicznym Substracie w sposób idealnie płynny, bez oporów i strat radiacyjnych przy stałej prędkości, realizując rygorystycznie Pierwszą Zasadę Dynamiki Newtona.

---

## 2.4. Istota ładunku i rozdzielenie od masy spoczynkowej

Tradycyjna fizyka traktuje masę i ładunek jako niezależne, fundamentalne parametry przypisane do punktowych cząstek. TSM oferuje czysto geometryczne rozdzielenie tych pojęć, opierając się na relacji między zanurzeniem w 4D a rzutem na naszą 3‑brane.

- **Ładunek elektryczny** jest mierzonym na płaszczyźnie naszej 3‑brany strumieniem wektora skrętu fazowego węzła. Ponieważ pole orientacji wokół stabilnego defektu musi zamknąć się w pełnym obrocie, rzut ten zawsze daje całkowitą wielokrotność geometryczną $2\pi$. Ładunek jest więc niezmiennikiem czysto topologicznym, bezpośrednio powiązanym z wartością niezmiennika Hopfa $Q_H$ dla rzutowanego pola $\mathbf{n}(\mathbf{x})$.
- **Masa spoczynkowa** zależy od geometrii zanurzenia. Defekt topologiczny, oprócz skręcenia w przestrzeni 3D, powoduje trwałe, fizyczne wybrzuszenie 3‑brany w kierunku czwartego wymiaru przestrzennego ($x^4$). Głębokość tego ugięcia oraz powiązana z nim objętość zdeformowanej sieci określają całkowitą energię sprężystą solitonu, zgodnie ze wzorem (2.3.1).

Stąd wynika fizyczne wyjaśnienie asymetrii masowej przy identycznym ładunku: proton i elektron posiadają tę samą liczbę splotu (ten sam ładunek rzutowany), lecz proton stanowi znacznie bardziej złożony, wielokrotny warkocz topologiczny w rozumieniu sekcji 2.2.3. Skomplikowana, wielopasmowa struktura jądra protonu generuje potężniejsze, głębsze wybrzuszenie 3‑brany w czwarty wymiar (Bulk), co skutkuje wielokrotnie większą masą sprężystą niż w przypadku prostego, jednopasmowego splotu elektronu.

---

## 2.5. Antymateria jako inwersja topologiczna

Koncepcja antymaterii w TSM zostaje całkowicie odarta z relatywistycznych interpretacji matematycznych, takich jak „ujemna energia” czy „ruch cząstek wstecz w czasie”. Zgodnie z Rozdziałem 1, czas $t$ nie stanowi fundamentalnego wymiaru pseudoriemannowskiego, w którym możliwa jest inwersja wektora ruchu – jest to parametr czysto lokalny, wynikający z gęstości upakowania osnowy. W tym ujęciu istnienie antycząstek nie implikuje żadnych anomalii temporalnych, lecz stanowi przejaw czysto geometrycznych transformacji konfiguracji splotu wewnątrz 3‑brany.

### 2.5.1. Chiralność węzła

Dla każdego węzła topologicznego o ładunku $Q_H = +1$ istnieje jednoznacznie zdefiniowana, lustrzana konfiguracja pola odkształceń posiadająca przeciwną chiralność (helisowość) struktury splotu, co generuje ładunek topologiczny $Q_H = -1$. Cząstka o odwróconej chiralności splotu zachowuje identyczną geometrię ugięcia w 4D (generuje identyczny rozkład naprężeń grawitacyjnych, a więc ma **dodatnią masę spoczynkową**), lecz jej rzutowany wektor skrętu fazowego ma przeciwny zwrot. Jest to antycząstka.

### 2.5.2. Mechanizm anihilacji

Gdy cząstka ($Q_H = +1$) i antycząstka ($Q_H = -1$) znajdą się w bezpośrednim kontakcie, bariera topologiczna chroniąca je przed rozpadem znika. Sumaryczny ładunek układu wynosi:

$$Q_{H,\text{total}} = +1 + (-1) = 0 \tag{2.5.1}$$

Układ staje się topologicznie równoważny płaskiej, niezaburzonej próżni. Następuje proces anihilacji, który mechanicznie jest gwałtownym, bezresztkowym rozplątaniem splotów i rozwłóknieniem lokalnych deformacji. Zmagazynowana w ugięciu brany energia potencjalna naprężeń sprężystych zostaje uwolniona w postaci rozchodzących się we wszystkich kierunkach czystych fal poprzecznych ośrodka – fotonów.

---

## 2.6. Geometryczne pochodzenie spinu 1/2 i podwójne nakrycie

Jednym z najbardziej abstrakcyjnych elementów mechaniki kwantowej jest pojęcie spinu 1/2, wymagające obrotu układu o $720^\circ$ w celu powrotu do stanu początkowego. TSM wyjaśnia ten fenomen w sposób bezpośredni i intuicyjny, odwołując się do własności geometrycznych ciągłego ośrodka sprężystego poddanego lokalnej rotacji w przestrzeni Bulk.

### 2.6.1. Przestrzeń konfiguracji 4D i struktura rotacji

Rozważmy węzeł topologiczny, który zgodnie z definicją w podrozdziale 2.2.3 stanowi pierwotnie 4-wymiarowy Skyrmion osadzony w 4-Matrycy. Ponieważ cząstka jest integralną częścią elastycznego podłoża, jej lokalny obrót pociąga za sobą deformację linii przemieszczeń otaczającego ją kontinuum. 

W przestrzeni trójwymiarowej rotacja sztywnego ciała o kąt $2\pi$ ($360^\circ$) przywraca jego punkty do pierwotnych współrzędnych fizycznych. Jednak w przypadku 4-wymiarowego solitonu, którego linie naprężeń są zakleszczone w Substracie, pełen obrót rdzenia o kąt $2\pi$ zachodzący w płaszczyźnie ortogonalnej Bulk ($x^4$) pozostawia linie otaczającej osnowy w stanie złożonego skręcenia topologicznego. Te linie polowe nie mogą ulec relaksacji w sposób ciągły bez rozrywania struktury sieci.

Dopiero wykonanie drugiego pełnego obrotu o kąt $2\pi$ (łącznie $4\pi = 720^\circ$) w pełnej przestrzeni konfiguracji 4D wprowadza układ w stan geometryczny, w którym linie odkształceń otaczającego tła mogą samorzutnie, poprzez ciągłe ślizganie się i rotacje komórek wzdłuż sfer wpływu, całkowicie się rozsupłać i powrócić do stanu zerowego naprężenia. Przestrzeń konfiguracji obrotów dla 4D-solitonów, uwięzionych w ciągłym medium i rzutowanych na 3-brane, jest w sposób naturalny dwukrotnie nakrywana przez grupę spinorową $SU(2)$, która nakrywa grupę obrotów $SO(3)$. Spin 1/2 przestaje być zatem abstrakcyjnym postulatem probabilistycznym, a staje się bezpośrednią mechaniczną konsekwencją uwięzienia i rotacji 4-wymiarowego solitonu w ciągłym, elastycznym medium Substratu.

---

## 2.7. Podsumowanie Rozdziału 2

- **Demistyfikacja dualizmu korpuskularno‑falowego:** W ramach TSM materii nie traktuje się jako zbioru punktowych obiektów poruszających się w próżni. Cząstki elementarne (fermiony) zostają zredefiniowane jako stabilne, skwantowane, nieliniowe defekty topologiczne (solitony) samej struktury ciągłego Substratu.
- **Czas lokalny w równaniach dynamiki:** Wszystkie równania ruchu sformułowane są w lokalnym czasie współrzędnościowym $t$, który w płaskiej osnowie pokrywa się z czasem własnym. Dylatacja czasu w pobliżu węzłów wynika bezpośrednio ze wzrostu lokalnej gęstości upakowania $\phi$ wywołanego zakleszczeniem.
- **Rozkład Hodge’a‑Helmholtza i superluminalność:** Rygorystyczny opis pola przemieszczeń osnowy jako 1‑formy w $\mathbb{R}^4$ pozwala na czystą separację matematyczną modów falowych. Istnieją superluminalne fale podłużne ($\alpha$, $c_L > c$) oraz poprzeczne fale ścinające ($\beta$, $c_{\perp} = \sqrt{\mu/\rho_0}$), które konstytuują prędkość światła $c$.
- **Rozwiązanie niestabilności Derricka:** Zamiast sztucznych członów wyższego rzędu, stabilizację rozmiaru solitonu osiągnięto poprzez geometryczny próg zakleszczenia Substratu ($\phi \to \phi_{\text{lock}}$), przy którym moduły sprężystości dążą do nieskończoności, tworząc naturalną barierę mechaniczną przed kolapsem.
- **Dualizm Skyrmion-Hopfion:** Własności masowe i spinowe cząstki wynikają z jej pierwotnej natury jako 4D Skyrmiona, podczas gdy sektor oddziaływań elektrodynamicznych i jądrowych wewnątrzbrany reprezentowany jest przez strukturę 3D Hopfiona o ładunku topologicznym zdefiniowanym przez niezmiennik Hopfa $Q_H \in \mathbb{Z}$.
- **Hydrodynamiczny mechanizm bezwładności:** Masa spoczynkowa cząstki to zintegrowana energia potencjalna naprężeń sprężystych wokół rdzenia solitonu, zbieżna dzięki nieliniowości $\phi_{\text{lock}}$. Ruch jednostajny jest bezstratnym transferem stanu odkształcenia, a bariera Peierlsa‑Nabarro znika dzięki asymetrii skal ($L \gg a$).
- **Ontologia antymaterii bez anomalii temporalnych:** Antycząstka to lustrzana inwersja chiralności splotu ($Q_H = -1$) o dodatniej masie. Anihilacja to mechaniczne rozplątanie do $Q_{H,\text{total}} = 0$ i emisja fal poprzecznych (fotonów).
- **Mechaniczne pochodzenie spinu 1/2:** Wymg obrotu o $720^\circ$ wynika bezpośrednio z uwięzienia 4-wymiarowego solitonu w ciągłym medium – jest to mechaniczna konsekwencja dwukrotnego nakrycia grupy $SO(3)$ przez grupę spinorową $SU(2)$ przy rotacji w płaszczyznach wymiaru Bulk.