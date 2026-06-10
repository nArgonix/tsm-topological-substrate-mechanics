# Rozdział 2: Węzły topologiczne i emergencja solitoniczna w TSM: Hydrodynamika bezwładności, antymateria, geometryczne pochodzenie spinu 1/2 oraz formalizm sztywności Substratu

Zdefiniowanie globalnego parametru ewolucyjnego $\tau$ oraz makroskopowych właściwości kontinuum pozwala na przejście do kluczowego zagadnienia Mechaniki Substratu Topologicznego (TSM): pytania o to, w jaki sposób z czysto kinetycznego tła zderzających się 0-cząstek wyłania się sztywny ośrodek sprężysty, a w nim – skwantowane, stabilne formy materii. Model TSM całkowicie odrzuca dualizm korpuskularno-falowy w jego tradycyjnym, abstrakcyjnym ujęciu. Cząstki elementarne nie są punktami poruszającymi się w próżni; są lokalnymi, nieliniowymi defektami topologicznymi (solitonami) samej struktury osnowy.

## 2.1. Mikroskopowy mechanizm skończonej ściśliwości i rygorystyczny formalizm elasto-dynamiczny w $\mathbb{R}^4$

### 2.1.1. Stan przed-zakleszczeniowy (Pre-jamming) i skończona sztywność objętościowa

Przejście od chaotycznej, mikro-skalowej kinetyki 0-cząstek do makroskopowego kontinuum zdolnego do przenoszenia odkształceń zachodzi w reżimie gęstego upakowania geometrycznego. W odróżnieniu od modeli zakładających nieskończoną sztywność lub nieściśliwość, TSM definiuje stan osnowy jako ośrodek o wysokiej, lecz skończonej ściśliwości.

Definiujemy lokalny ułamek upakowania 0-cząstek jako $\phi = V_0 / V_{\text{cell}}$, gdzie $V_0$ jest niezmienną, minimalną objętością samej 0-cząstki, a $V_{\text{cell}}$ jest objętością jej komórki interakcji Wignera-Seitza. Gdy układ dąży do wartości krytycznej $\phi \to \phi_c$, swoboda translacyjna centrów 0-cząstek zostaje całkowicie zablokowana. Układ osiąga stan przed-zakleszczeniowy (*pre-jamming*), w którym sfery oddziaływań stykają się ze sobą stacjonarnie, a jedynym możliwym stopniem swobody stają się oscylacje wokół węzłów oraz sprężyste deformacje geometrii samych sfer, co nadaje ośrodkowi mierzalną, elastomechaniczną podatność.

W konsekwencji, dynamiczny opis 0-Matrycy w skali makroskopowej musi uwzględniać dwa niezależne parametry materiałowe: moduł sprężystości objętościowej $K$ (odpowiedzialny za reakcję na zmianę gęstości) oraz moduł sprężystości poprzecznej $\mu$ (odpowiedzialny za reakcję na ścinanie), powiązane bezpośrednio ze stałymi Lamégo $\lambda$ i $\mu$. Te stałe materiałowe determinują istnienie dwóch odrębnych klas wzbudzeń falowych w kontinuum, charakteryzujących się różnymi prędkościami propagacji. Dowolne zaburzenie geometryczne nie rozchodzi się już poprzez losową dyfuzję cząstek, lecz jako spójna fala elasto-dynamiczna wewnątrz kontinuum $\mathbb{R}^4$.

### 2.1.2. Pełny rozkład Hodge’a-Helmholtza pola przemieszczeń w $\mathbb{R}^4$ i konstrukcja algebraiczna potencjałów

Aby zachować pełną niezmienniczość wymiarową i rygor matematyczny w przestrzeni czterowymiarowej, pole przemieszczeń strukturalnych osnowy reprezentujemy jako 1-forma różniczkowa $\Phi \in \Omega^1(\mathbb{R}^4)$, zdefiniowana w bazie współrzędnych przestrzennych $(x^1, x^2, x^3, x^4)$:

$$\Phi = \Phi_1 dx^1 + \Phi_2 dx^2 + \Phi_3 dx^3 + \Phi_4 dx^4$$

Zgodnie z twierdzeniem Hodge’a o rozkładzie ortogonalnym na płaskiej rozmaitości $\mathbb{R}^4$, pole to rozbija się jednoznacznie na sumę formy ścisłej, ko-ścisłej oraz składnika harmonicznego (który w rozważaniach lokalnych przyjmujemy jako zerowy):

$$\Phi = \Phi_L + \Phi_T = d\alpha + \delta\beta$$

Gdzie:

* $d: \Omega^k \to \Omega^{k+1}$ to pochodna zewnętrzna (uogólniony gradient, generujący rotację i ekspansję).
* $\delta: \Omega^k \to \Omega^{k-1}$ to operator ko-dyferencjału (uogólniona dywergencja), zdefiniowany w $\mathbb{R}^4$ poprzez gwiazdkę Hodge’a $\star$ jako $\delta = -\star d \star$.
* $\alpha \in \Omega^0(\mathbb{R}^4)$ jest 0-formą (potencjał skalarny pola podłużnego).
* $\beta \in \Omega^2(\mathbb{R}^4)$ jest antysymetryczną 2-formą (potencjał tensorowy pól poprzecznych).

W odróżnieniu od ograniczeń fazy izostatycznej, potencjał $\alpha \neq 0$, co oznacza, że lokalne zagęszczenia i rozrzedzenia substratu stanowią aktywny fizycznie stopień swobody. W standardowej bazie różniczkowej $\{dx^\mu \wedge dx^\nu\}$ ($\mu, \nu \in \{1, 2, 3, 4\}$), gdzie indeksy $1, 2, 3$ odpowiadają współrzędnym zamkniętym wewnątrz naszej trójwymiarowej membrany (3-brany), a indeks $4$ reprezentuje kierunek ortogonalny (Bulk), 2-forma $\beta$ przyjmuje jawną postać:

$$\beta = \sum_{\mu < \nu} \beta_{\mu\nu} dx^\mu \wedge dx^\nu = \beta_{12} dx^1 \wedge dx^2 + \beta_{13} dx^1 \wedge dx^3 + \beta_{23} dx^2 \wedge dx^3 + \beta_{14} dx^1 \wedge dx^4 + \beta_{24} dx^2 \wedge dx^4 + \beta_{34} dx^3 \wedge dx^4$$

Zapis macierzowy tensora odkształceń potencjału $\beta$ w bazie $\mathbb{R}^4$ ma jawną strukturę antysymetryczną:

$$[\beta_{\mu\nu}] = \begin{pmatrix}
0 & \beta_{12} & -\beta_{31} & \beta_{14} \\
-\beta_{12} & 0 & \beta_{23} & \beta_{24} \\
\beta_{31} & -\beta_{23} & 0 & \beta_{34} \\
-\beta_{14} & -\beta_{24} & -\beta_{34} & 0
\end{pmatrix}$$

Dokonujemy rygorystycznego rozkładu składowych tensora $[\beta_{\mu\nu}]$ na dwa niezależne wektory trójwymiarowe w celu fizycznej mapowalności zjawisk. Składowe wewnątrzbranowe reprezentujemy jako trójwymiarowy wektor pseudorotacji osnowy $\mathbf{B}_{\beta}$:

$$\mathbf{B}_{\beta} = (\beta_{23}, \beta_{31}, \beta_{12})$$

Natomiast składowe wiążące branę z wymiarem ortogonalnym Bulk reprezentujemy jako trójwymiarowy wektor ugięcia poprzecznego $\mathbf{E}_{\beta}$:

$$\mathbf{E}_{\beta} = (\beta_{14}, \beta_{24}, \beta_{34})$$

### 2.1.3. Równania ruchu, separacja modów i warunek cechowania

Ogólne 4-wymiarowe równanie elasto-dynamiczne Naviera-Cauchy’ego dla ośrodka o gęstości masowej $\rho_0$ i stałych Lamégo $\lambda$ oraz $\mu$ przyjmuje w notacji zewnętrznej postać:

$$\rho_0 \frac{\partial^2 \Phi}{\partial \tau^2} = (\lambda + 2\mu) d\delta \Phi - \mu \delta d \Phi$$

Podstawiając pełny rozkład Hodge’a $\Phi = d\alpha + \delta\beta$ oraz wykorzystując tożsamości nilpotentne operatorów ($d^2 = 0$ oraz $\delta^2 = 0$), równanie ruchu ulega automatycznej separacji na dwa niezależne układy dynamiczne:

$$\rho_0 d \left( \frac{\partial^2 \alpha}{\partial \tau^2} \right) + \rho_0 \delta \left( \frac{\partial^2 \beta}{\partial \tau^2} \right) = (\lambda + 2\mu) d(\delta d \alpha) - \mu \delta(d \delta \beta)$$

Z racji ortogonalności przestrzeni form ścisłych ($d\alpha$) i ko-ścisłych ($\delta\beta$), powyższa tożsamość rozpada się na dwa niezależne równania falowe:

1. **Równanie modu podłużnego (dla 0-formy $\alpha$):**

$$\frac{\partial^2 \alpha}{\partial \tau^2} = c_L^2 \delta d \alpha \quad \implies \quad \frac{\partial^2 \alpha}{\partial \tau^2} = c_L^2 \nabla^2_{4D} \alpha$$



Gdzie prędkość fali podłużnej (kompresyjnej) wynosi $c_L = \sqrt{\frac{\lambda + 2\mu}{\rho_0}}$.

2. **Równanie modu poprzecznego (dla 2-formy $\beta$):**

$$\delta \left( \frac{\partial^2 \beta}{\partial \tau^2} + c_{\perp}^2 d\delta\beta \right) = 0$$



Gdzie prędkość fali poprzecznej (ścinania) wynosi $c_{\perp} = \sqrt{\frac{\mu}{\rho_0}}$.

Ponieważ 2-forma $\beta$ w $\mathbb{R}^4$ posiada 6 niezależnych składowych, sama operacja $\Phi_T = \delta\beta$ definiuje ją z dokładnością do transformacji cechowania $\beta \to \beta + d\gamma$, gdzie $\gamma \in \Omega^1(\mathbb{R}^4)$. Aby znieść tę nadmiarowość i zapobiec propagacji niefizycznych modów pasożytniczych, narzuca się rygorystyczny warunek ko-ścisłości (cechowanie Lorentza-Hodge'a):

$$\delta\beta = 0$$

Zastosowanie cechowania $\delta\beta = 0$ redukuje operator Laplace’a-de Rhama $\Delta_2 = d\delta + \delta d$ działający na $\beta$ do czystego członu czynnego. Ostateczne, zredukowane równanie fali poprzecznej przyjmuje postać:

$$\frac{\partial^2 \beta}{\partial \tau^2} = -c_{\perp}^2 \delta d \beta \quad \implies \quad \frac{\partial^2 \beta}{\partial \tau^2} = c_{\perp}^2 \nabla^2_{4D} \beta$$

### 2.1.4. Działanie operatorów różniczkowych zewnętrznych: Gwiazdka Hodge'a i Ko-dyferencjał

Operator gwiazdki Hodge'a $\star$ w euklidesowej przestrzeni czterowymiarowej odwzorowuje każdą $k$-formę w $(4-k)$-formę. Dla naszej 2-formy $\beta$, operator $\star$ generuje nową 2-formę $\star\beta$, dokonując geometrycznego przekształcenia płaszczyzn ortogonalnych. Działanie operatora na elementy bazy różniczkowej definiujemy jako:

$$\star(dx^1 \wedge dx^2) = dx^3 \wedge dx^4, \quad \star(dx^2 \wedge dx^3) = dx^1 \wedge dx^4, \quad \star(dx^3 \wedge dx^1) = dx^2 \wedge dx^4$$

$$\star(dx^1 \wedge dx^4) = dx^2 \wedge dx^3, \quad \star(dx^2 \wedge dx^4) = dx^3 \wedge dx^1, \quad \star(dx^3 \wedge dx^4) = dx^1 \wedge dx^2$$

Aplikując to bezpośrednio do pełnego wyrażenia algebraicznego 2-formy $\beta$, otrzymujemy jawną postać dualnej 2-formy:

$$\star\beta = \beta_{12} dx^3 \wedge dx^4 + \beta_{13} dx^2 \wedge dx^4 + \beta_{23} dx^1 \wedge dx^4 + \beta_{14} dx^2 \wedge dx^3 + \beta_{24} dx^3 \wedge dx^1 + \beta_{34} dx^1 \wedge dx^2$$

W terminach zdefiniowanych trójwymiarowych wektorów składowych $\mathbf{B}_{\beta}$ oraz $\mathbf{E}_{\beta}$, gwiazdka Hodge'a dokonuje bezpośredniej inwersji funkcjonalnej:

$$\star : \mathbf{B}_{\beta} \longleftrightarrow \mathbf{E}_{\beta}$$

Ma to fundamentalne znaczenie fizyczne: operator gwiazdki Hodge'a reprezentuje mechaniczne sprzężenie zwrotne ośrodka, wiążące wewnętrzne naprężenia ścinające zachodzące w płaszczyźnie 3-brany z jej makroskopowym ugięciem w kierunku przestrzeni Bulk.

Ko-dyferencjał $\delta$ działający na 2-formę $\beta$ daje w wyniku 1-formę $\delta\beta = \sum_{\mu} (\delta\beta)_\mu dx^\mu$, która reprezentuje gęstość sił reakcji sprężystej Substratu na poszczególne składowe przemieszczeń. Wyznaczamy jawne składowe tego wektora poprzez operację różniczkowania cząstkowego:

$$(\delta\beta)_\mu = -\sum_{\nu=1}^4 \partial_\nu \beta_{\mu\nu}$$

Rozpisując komponenty dla poszczególnych osi koordynacyjnych z uwzględnieniem antysymetrii tensora:

$$(\delta\beta)_1 = -(\partial_2 \beta_{12} + \partial_3 \beta_{13} + \partial_4 \beta_{14}) = -(\nabla \times \mathbf{B}_{\beta})_1 - \partial_4 \beta_{14}$$

$$(\delta\beta)_2 = -(\partial_1 \beta_{21} + \partial_3 \beta_{23} + \partial_4 \beta_{24}) = -(\nabla \times \mathbf{B}_{\beta})_2 - \partial_4 \beta_{24}$$

$$(\delta\beta)_3 = -(\partial_1 \beta_{31} + \partial_2 \beta_{32} + \partial_4 \beta_{34}) = -(\nabla \times \mathbf{B}_{\beta})_3 - \partial_4 \beta_{34}$$

$$(\delta\beta)_4 = -(\partial_1 \beta_{41} + \partial_2 \beta_{42} + \partial_3 \beta_{43}) = \partial_1 \beta_{14} + \partial_2 \beta_{24} + \partial_3 \beta_{34} = \nabla \cdot \mathbf{E}_{\beta}$$

Równania te stanowią matematyczny dowód na to, że przestrzenne siły reakcji wewnątrzbrany ($\mu=1,2,3$) są determinowane przez rotację wewnętrznych pól ścinających ($\nabla \times \mathbf{B}_{\beta}$) oraz gradient zmiany ugięcia wzdłuż osi ortogonalnej $\partial_4 \mathbf{E}_{\beta}$. Składowa czwarta ($\mu=4$) określa czystą trójwymiarową dywergencję wektora ugięcia ($\nabla \cdot \mathbf{E}_{\beta}$), co odpowiada za lokalny rozkład ciśnienia normalnego działającego na powierzchnię 3-brany ze strony otaczającego środowiska Bulk.

### 2.1.5. Rzutowanie 3D + $x^4$: Rozszerzona mapa pól fizycznych

Rozdzielenie współrzędnych wewnątrzpowierzchniowych 3-brany ($x^1, x^2, x^3$) od osi ortogonalnej Bulk ($x^4$) pozwala na ostateczne zmapowanie składowych form różniczkowych na obserwowalne makroskopowo oddziaływania.

**Dekompozycja modu poprzecznego ($\beta \in \Omega^2(\mathbb{R}^4)$):**
2-formę $\beta$ rozbijamy na składowe wewnętrzne i zewnętrzne względem brany:

$$\beta = \bar{\beta} + \bar{\psi} \wedge dx^4$$

* $\bar{\beta} = \frac{1}{2}\beta_{ij} dx^i \wedge dx^j$ (3 składowe): reprezentuje płaszczyzny polaryzacji zamknięte wewnątrz 3-brany. Generuje poprzeczne fale elektromagnetyczne, poruszające się z prędkością graniczną $c = c_{\perp}$. W tym ujęciu składowe formy $\bar{\beta}$ mapują się bezpośrednio na potencjał cechowania $A_\mu$, a jej pochodna zewnętrzna wyznacza antysymetryczny tensor pola elektromagnetycznego $F = d\bar{\beta}$, co stanowi formalny pomost matematyczny do nieliniowej elektrodynamiki.
* $\bar{\psi} = \beta_{i4} dx^i$ (3 składowe, odpowiadające wektorowi $\mathbf{E}_{\beta}$): reprezentuje płaszczyzny polaryzacji sprzężone z kierunkiem ortogonalnym. Generuje naciąg mechaniczny membrany w osi $x^4$, interpretowany makroskopowo jako pole grawitacyjne.

Warunek cechowania $\delta\beta = 0$ w tym rozbiciu przyjmuje formę sprzężonych więzów różniczkowych:

$$\partial_i \beta_{i4} = 0 \quad \implies \quad \text{div}(\bar{\psi}) = 0$$

$$\partial_j \beta_{ji} + \partial_4 \beta_{4i} = 0 \quad \implies \quad (\nabla \times \mathbf{B}_{\beta})_i - \partial_4 \bar{\psi}_i = 0$$

Zapewnia to solenoidalność pola grawitacyjnego w branie oraz lokalne, dynamiczne równoważenie naprężeń elektromagnetycznych przez gradienty sił ortogonalnych wzdłuż czwartego wymiaru.

**Dekompozycja modu podłużnego ($\alpha \in \Omega^0(\mathbb{R}^4)$):**
Pochodna zewnętrzna 0-formy potencjału podłużnego tworzy pole gradientów:

$$d\alpha = \bar{d}\alpha + \partial_4 \alpha dx^4 = \left(\sum_{i=1}^3 \partial_i \alpha dx^i\right) + \partial_4 \alpha dx^4$$

* Składnik $\bar{d}\alpha$ (wewnątrzbrany): generuje podłużne fale ciśnienia mechanicznego bezpośrednio w trójwymiarowej płaszczyźnie osnowy. Objawia się jako uniwersalne, skalarowe pole gęstość tła powiązane z relaksacją Substratu, dynamiką ciemnej energii lub globalnymi oscylacjami ciśnienia hydro-elastycznego Substratu.
* Składnik $\partial_4 \alpha$ (ortogonalny): definiuje symetryczne ściskanie i rozszerzanie profilu grubości samego substratu 3-brany w przestrzeni Bulk.

Ponieważ prędkość fali podłużnej $c_L = \sqrt{\frac{\lambda + 2\mu}{\rho_0}}$ jest jawnie większa od prędkości fal poprzecznych $c_{\perp} = \sqrt{\frac{\mu}{\rho_0}}$, skalarowe zaburzenia kompresyjne osnowy propagują się w sposób superluminalny ($c_L > c$). Zjawisko to nie narusza wewnętrznej spójności TSM ani przyczynowości, gdyż prędkość światła $c$ jest zdefiniowana i ograniczona wyłącznie przez próg propagacji modów poprzecznych ($\bar{\beta}$), stanowiących podstawę sektora elektrodynamicznego i mierzalnej materii.

**2.2. Załamanie superpozycji, konwersja modów i węzły topologiczne w krystalicznej 3-brane**

W reżimie liniowym (przy relatywnie niskich gęstościach energii) mechanika Substratu Topologicznego (TSM) funkcjonuje jako niemal idealnie ortogonalny układ falowy. Mody podłużne (kompresyjne, reprezentowane przez 0-formę $\alpha$) oraz mody poprzeczne (ścinające, reprezentowane przez 2-formę $\beta$) propagują się w osnowie asymetrycznie jako w pełni niezależne rozwiązania liniowych równań Naviera-Cauchy'ego. Zgodnie z zasadą superpozycji, pakiety falowe obu tych modów mogą swobodnie przenikać się w przestrzeni, nie zaburzając wzajemnie swoich trajektorii ani profili fazowych.

Należy jednak podkreślić, że aparat liniowy jest jedynie asymptotycznym przybliżeniem. W warunkach skrajnej koncentracji energii i ekstremalnych naprężeń hydro-elastodynamicznych, liniowa odpowiedź 0-Matrycy ulega fundamentalnemu załamaniu. Prowadzi to wprost do zjawisk formowania skwantowanej materii z samego pola odkształceń.

**2.2.1. Nieliniowa asymetryczna sztywność i próg zamrożenia topologicznego**

Fundamentem dynamiki nieliniowej w TSM jest odrzucenie klasycznej kinematyki drobin. 0-cząstki nie posiadają swobody przemieszczania się w próżni i nie poruszają się jak cząstki klasycznego gazu. Znajdują się one w stanie uwięzienia wewnątrz własnych komórek Wignera-Seitza (sfer oddziaływań). Proces lokalnej kompresji ośrodka (np. na skutek potężnej, lokalnej fluktuacji pola dylatacyjnego) sprowadza się wyłącznie do geometrycznego odkształcenia (zgniecenia) tych sfer.

Kiedy zjawiska dylatacyjne drastycznie zwiększają zagęszczenie przestrzenne układu, zmniejsza się droga swobodna przypisana drganiom poszczególnych 0-cząstek. Z racji zasady zachowania pędu kinetycznego, zacieśnienie sfery wykładniczo zwiększa częstotliwość wewnętrznych uderzeń o granice komórki, co natychmiast potęguje siłę oddziaływań na sąsiednie węzły. W momencie, gdy lokalny ułamek upakowania sieci $\phi(\mathbf{x}, \tau)$ zbliża się do geometrycznej wartości krytycznej $\phi_c$, układ osiąga próg zamrożenia topologicznego.

W tym punkcie opór przestrzenny przeciwko dalszej kompresji dąży asymptotycznie do nieskończoności. Aby rygorystycznie zamodelować tę barierę – i tym samym kategorycznie wykluczyć powstawanie grawitacyjnych osobliwości o nieskończonej gęstości punktowej – wyprowadza się nieliniowy moduł sprężystości objętościowej $K_{\text{eff}}$:

$$K_{\text{eff}}(\phi) = K_0 \left( 1 - \frac{\phi}{\phi_c} \right)^{-\gamma}$$

Gdzie $K_0$ oznacza izotropowy moduł sztywności w niezaburzonym Stanie Zero, a $\gamma$ jest empirycznym wykładnikiem krytycznym (mierzalnym parametrem materiałowym 0-Matrycy). Zależność ta wykazuje, że sfery oddziaływań ulegają ekstremalnemu ograniczeniu przestrzennemu, uniemożliwiając zapaść grawitacyjną kontinuum do jednego bezwymiarowego punktu.

**2.2.2. Konwersja między-modowa (Mode Coupling) i próg plastyczności**

Skoro ściśliwość ma charakter skończony, napotykając na barierę zablokowania objętościowego ($K_{\text{eff}} \to \infty$), gwałtownie skompresowany system musi znaleźć inną ścieżkę geometrycznego ujścia dla narastającej, uwięzionej energii ciśnieniowej. W mechanice kontinuum, gdy opór na ściskanie rośnie znacznie szybciej niż opór postaciowy, dochodzi do wymuszonej utraty stabilności i nieliniowej konwersji modów.

Nadmiarowa energia ciśnienia zostaje kaskadowo zrzucona na mod $\beta$, wywołując ugięcia poprzeczne, co skutkuje ekstremalnym, lokalnym skręceniem i topologicznym zwichnięciem komórek sieci. W rygorystycznym zapisie matematycznym, konwersję tę wyznacza wejście równań w reżim nieliniowy, w którym równanie fali poprzecznej zostaje sprzężone krzyżowo z polem podłużnym $\alpha$ poprzez układ nieliniowych tensorów sprężystości wyższego rzędu:

$$\frac{\partial^2 \beta_{ij}}{\partial \tau^2} - c_{\perp}^2 \nabla^2 \beta_{ij} = \mathcal{C}_{ijkl} (\partial_k \alpha) (\partial_l \alpha) + \mathcal{D}_{ijklm} (\partial_k \beta_{lm}) \alpha + \mathcal{O}(\epsilon^3)$$

Gdzie człon $\mathcal{C}_{ijkl}$ to tensor akustoelastyczny determinujący zasilanie modu ścinania przez potężne gradienty przestrzenne fali kompresyjnej. Prawa strona równania działa jak permanentne źródło wymuszeń, które aktywnie pompuje energię we wirowość Substratu, wyrywając lokalne oscylatory ze strefy stabilności liniowej.

**2.2.3. Formowanie węzła topologicznego (Solitonu) i jego niezmiennik**

W wyniku trwałego wymuszenia ścinającego opisanego w poprzedniej sekcji, makroskopowa geometria osnowy ulega trwałej, plastycznej modyfikacji. Definiujemy pole wektorowe lokalnej orientacji osnowy jako znormalizowany wektor $\mathbf{n}(\mathbf{x}) = (n^1, n^2, n^3)$, podający kierunek najsilniejszej osi skręcenia komórki w punkcie przestrzeni ($|\mathbf{n}|^2 = 1$).

Po przekroczeniu progu stabilności, układ sfer oddziaływań musi się przearanżować. Wektory $\mathbf{n}(\mathbf{x})$ zmuszone są do przestrzennego zapętlenia się w konfigurację domkniętą (defekt topologiczny). W ten sposób tworzy się stabilny soliton – pole wektorowe zapętla się, tworząc makroskopowy splot, którego nie da się w sposób ciągły rozpleść ani wygładzić z powrotem do zrelaksowanej, płaskiej postaci bez rozerwania fundamentalnej ciągłości samej 4-wymiarowej osnowy.

Tego rodzaju zamrożenie układu opisuje się algebraicznie poprzez wprowadzenie niezmiennika (ładunku topologicznego), tożsamego z liczbą splotu $\mathcal{W}$, która precyzuje, ile razy pole orientacji oplata się przestrzennie:

$$\mathcal{W} = \frac{1}{12\pi^2} \int_{\mathbb{R}^3} \epsilon^{ijk} \epsilon_{abc} n^a \partial_i n^b \partial_j n^c \, d^3x$$

W powyższym całkowaniu:

* Wskaźniki $i, j, k \in \{1, 2, 3\}$ kodują pochodne przestrzenne wewnątrz izotropowej 3-brany.
* Wskaźniki $a, b, c \in \{1, 2, 3\}$ przebiegają po wymiarach znormalizowanego pola wektorowego orientacji $\mathbf{n}$.
* $\epsilon^{ijk}$ i $\epsilon_{abc}$ stanowią całkowicie antysymetryczne tensory Leviego-Civity.
* Całka po całej przestrzeni $\mathbb{R}^3$ wyznacza topologiczny stopień odwzorowania (Jacobian) sfery w sferę ($\mathbb{S}^3 \rightarrow \mathbb{S}^2$), co zgodnie z prawami geometrii różniczkowej musi skutkować wynikiem będącym liczbą całkowitą ($\mathcal{W} \in \mathbb{Z}$).

**Oceny i Wnioski Analityczne**

Rozwiązanie to dostarcza fundamentalnego mechanizmu kwantyzacji zjawisk subatomowych, uwalniając model od postulatów ad hoc. Skwantowane wartości rzutowane z ugięcia węzłów (ładunek) nie są przypisane ciałom z zewnątrz; wynikają bezpośrednio z nieciągłości w przestrzeni rozwiązań sprężystych ($\mathcal{W} \in \mathbb{Z}$).

Uwięziony soliton jest odporny na przypadkowe rozmycie falami tła. Płynne (ciągłe) przejście ze stanu np. $\mathcal{W} = 1$ do pełnej liniowej próżni $\mathcal{W} = 0$ jest zakazane mechanicznie i napotyka na opór grawitacyjno-sprężysty zmuszający makroskopowe pola do przejścia przez osobliwość rozerwania sieci. Prowadzi to do konkluzji, że stabilność fizycznych fermionów nie zależy od domniemanych sił utrzymujących ich strukturę od wewnątrz, ale z potężnego ciśnienia naprężonej, ciągłej osnowy od zewnątrz, która trzyma defekt w geometrycznym uwięzieniu (blokadzie topologicznej).