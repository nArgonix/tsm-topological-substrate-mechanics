<!-- ver:2.1.0 -->
# Rozdział 3: Dynamika naprężeń 0-Matrycy – od elektrodynamiki i topologicznych sił jądrowych do mechaniki obwodów

W klasycznej elektrodynamice pole elektromagnetyczne jest traktowane jako abstrakcyjny byt rozchodzący się w próżni. Ponieważ w Mechanice Substratu Topologicznego (TSM) niefizyczna próżnia nie istnieje, zjawiska elektromagnetyczne stanowią wyłącznie obserwowalną makroskopowo mechanikę odkształceń ciągłego, 4‑wymiarowego ośrodka sprężystego – w szczególności jego naprężeń ścinających i skrętnych zachodzących wewnątrz izotropowej 3‑brany. Zgodnie z Rozdziałami 0 i 1, cała dynamika rozgrywa się w lokalnym czasie $t$, emergentnym z gęstości upakowania 0‑Matrycy.

---

## 3.0. Czas lokalny w dynamice elektromagnetycznej – przypomnienie i osadzenie

Zgodnie z Rozdziałem 1.1, TSM odrzuca absolutny czas newtonowski i relatywistyczną czasoprzestrzeń. Podstawą opisu ewolucji pól jest **lokalny czas własny** $t$, płynący z gęstości upakowania 0‑cząstek:

$$dt = dN \cdot T_0 \cdot \frac{\phi(\mathbf{x})}{\phi_0} \tag{3.0.1}$$

gdzie:
- $dt$ – przyrost czasu lokalnego w punkcie $\mathbf{x}$ $[\text{s}]$,
- $dN$ – liczba cykli procesu okresowego (bezwymiarowa),
- $T_0$ – elementarny okres referencyjny $[\text{s}]$,
- $\phi(\mathbf{x})$ – lokalny ułamek upakowania (bezwymiarowy),
- $\phi_0$ – referencyjny ułamek upakowania w płaskiej osnowie.

W płaskiej, niezakłóconej 3‑branie ($\phi = \phi_0$) czas własny pokrywa się z **czasem współrzędnościowym** $t_{\text{flat}}$, który jest naturalną zmienną w równaniach pola. W pobliżu węzłów topologicznych ($\phi > \phi_0$) lokalny czas zwalnia, co modyfikuje obserwowaną dynamikę fal elektromagnetycznych (efekt Shapiro, dylatacja grawitacyjna). Wszystkie równania tego rozdziału sformułowane są w czasie współrzędnościowym $t = t_{\text{flat}}$, o ile nie zaznaczono inaczej.

---

## 3.1. Od skrętu topologicznego do potencjału cechowania

W Rozdziale 2 wprowadzono wektor orientacji $\mathbf{n}(\mathbf{x})$, opisujący lokalny kierunek osi skręcenia komórek sieci wokół węzła topologicznego (fermionu). W granicy kontinuum, dla układu wielu węzłów, pole to definiuje ciągłe pole torsji. Matematyczne przejście do elektrodynamiki odbywa się przez utożsamienie wektora orientacji $\mathbf{n}$ z kierunkiem polaryzacji poprzecznego przemieszczenia ośrodka.

### 3.1.1. Czteropotencjał torsyjny

Formalnie wprowadzamy 4‑potencjał $A_{\mu} = (\varphi_{\mathrm{t}}/c_{\perp}, \mathbf{A})$, gdzie:
- $\varphi_{\mathrm{t}}$ – skalarowy potencjał ciśnienia torsyjnego (statycznego naciągu) $[\text{V}]$,
- $\mathbf{A}$ – wektor przemieszczenia ścinającego $[\text{T} \cdot \text{m}]$, którego składowe są proporcjonalne do składowych $\mathbf{n}$ pomnożonych przez amplitudę skręcenia,
- $c_{\perp}$ – prędkość poprzecznych fal ścinających $[\text{m} \cdot \text{s}^{-1}]$.

W pobliżu rdzenia węzła faza torsji $\phi$ zmienia się o wielokrotność $2\pi$ przy pełnym obrocie. Związek z potencjałem cechowania ma postać:

$$\oint_{\partial S} \mathbf{A} \cdot d\mathbf{l} = \Phi_0 \cdot n \tag{3.1.1}$$

gdzie:
- $\partial S$ – zamknięty kontur otaczający rdzeń węzła,
- $\Phi_0$ – elementarny strumień torsji $[\text{T} \cdot \text{m}^2]$,
- $n \in \mathbb{Z}$ – liczba obrotów fazy.

### 3.1.2. Ładunek elektryczny jako strumień skrętu

**Ładunek elektryczny** $q$ definiujemy jako całkowity strumień wektora gradientu fazy torsji $\nabla\phi$ wzdłuż zamkniętego konturu otaczającego rdzeń węzła:

$$q \equiv e \cdot \frac{1}{2\pi} \oint_{\mathrm{pętla}} \nabla\phi \cdot d\mathbf{l} \tag{3.1.2}$$

gdzie $e$ jest ładunkiem elementarnym $[\text{C}]$. Ponieważ ciągłość fazy wokół zamkniętej pętli wymusza całkowitą wielokrotność obrotów, natychmiast otrzymujemy **skwantowanie ładunku elektrycznego**: $q = ne$, $n \in \mathbb{Z}$.

---

## 3.2. Tensor naprężeń ścinających a tensor pola elektromagnetycznego

W TSM potencjał $A_\mu$ jest fizycznym polem przemieszczeń ścinających $\mathbf{u}(\mathbf{x},t)$ w 0‑Matrycy, gdzie $\mathbf{A} \propto \mathbf{u}$. Antysymetryczna część gradientu przemieszczeń stanowi miarę lokalnej wirowości ośrodka:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu \tag{3.2.1}$$

Składowe fizyczne identyfikujemy jako:

$$E_i = c_{\perp} F_{0i}, \qquad B_i = \tfrac{1}{2}\varepsilon_{ijk} F_{jk} \tag{3.2.2}$$

gdzie:
- $\mathbf{E}$ – pole elektryczne $[\text{V} \cdot \text{m}^{-1}]$ – przestrzenny gradient ciśnienia torsyjnego,
- $\mathbf{B}$ – pole magnetyczne $[\text{T}]$ – wektor wirowości naprężeń ścinających,
- $\varepsilon_{ijk}$ – symbol Levi‑Civity.

### 3.2.1. Równania Maxwella z dynamiki Naviera‑Cauchy’ego

Równania Maxwella są bezpośrednią konsekwencją dynamiki sprężystej 0‑Matrycy (Rozdział 2.1.3). Bezźródłowe równania są tożsamością:

$$\nabla \cdot \mathbf{B} = 0 \tag{3.2.3}$$

wyrażającą geometryczną niesprzeczność pola przemieszczeń – linie sił $\mathbf{B}$ nie mają początku ani końca w nierozerwalnym kontinuum.

Równania ze źródłami otrzymujemy z równań Naviera‑Cauchy’ego, wyodrębniając antysymetryczną część wirową i utożsamiając jej dywergencję z 4‑prądem torsji $J^\mu = (c_{\perp}\rho_e, \mathbf{J})$:

$$\partial_\nu F^{\mu\nu} = \mu_0 J^\mu \tag{3.2.4}$$

gdzie:
- $\mu_0$ – przenikalność magnetyczna osnowy $[\text{N} \cdot \text{A}^{-2}]$,
- $\rho_e$ – gęstość ładunku elektrycznego $[\text{C} \cdot \text{m}^{-3}]$,
- $\mathbf{J}$ – gęstość prądu elektrycznego $[\text{A} \cdot \text{m}^{-2}]$.

**Brak monopoli magnetycznych:** Monopol wymagałby wolnego końca struny naprężeń zawieszonego w przestrzeni. W ciągłym, zablokowanym ośrodku zerwanie takiej ciągłości wymusiłoby nieskończoną lokalną energię ścinania i natychmiastowy kolaps. Równanie $\nabla \cdot \mathbf{B} = 0$ jest więc trywialną konsekwencją sprężystej nierozerwalności 3‑brany.

---

## 3.3. Prawa zachowania i dynamika falowa

### 3.3.1. Zachowanie ładunku elektrycznego

Zasada opisywana równaniem ciągłości:

$$\partial_\mu J^\mu = 0 \quad \implies \quad \frac{\partial \rho_e}{\partial t} + \nabla \cdot \mathbf{J} = 0 \tag{3.3.1}$$

ma charakter ściśle topologiczny. Liczba splotu węzła $\mathcal{W}$ (Rozdział 2.2.2) nie może ulec zmianie bez fizycznego rozerwania węzła (anihilacji z antywęzłem). Zmiany gęstości skręcenia mogą się jedynie przemieszczać.

### 3.3.2. Foton i propagacja

Jak ustalono w Rozdziale 2, foton jest skwantowaną poprzeczną falą ścinającą (mod $c_{\perp}$). W obszarach bez swobodnych ładunków równania Maxwella redukują się do równania falowego d’Alemberta. Zgodnie ze zjawiskiem akustoelastyczności (Rozdział 1.8), silne pole magnetyczne nieliniowo modyfikuje zastępczą przenikalność osnowy:

$$\epsilon_{\mathrm{eff}} = \epsilon_0 \left(1 + \kappa B^2\right) \tag{3.3.2}$$

co obniża lokalną prędkość propagacji fali ścinającej:

$$c_{\mathrm{lok}}(B) = \frac{c_{\perp}}{\sqrt{1 + \kappa B^2}} \approx c_{\perp}\left(1 - \tfrac{1}{2} \kappa B^2\right) \tag{3.3.3}$$

gdzie:
- $\epsilon_0$ – przenikalność elektryczna płaskiej osnowy $[\text{F} \cdot \text{m}^{-1}]$,
- $\kappa$ – stała sprzężenia magneto‑elastycznego $[\text{T}^{-2}]$.

Pomiary prędkości światła w polach rzędu 10 T nie wykazały odchyleń większych niż $10^{-8}$, co nakłada rygorystyczny limit: $\kappa \lesssim 10^{-6} \ \text{T}^{-2}$.

---

## 3.4. Mechanika oddziaływania: Nieliniowe równania pola, sprzężenia zwrotne i siły Maxwella

Oddziaływania elektromagnetyczne w TSM nie są „działaniem na odległość”, lecz bezpośrednim przejawem sprężystej odpowiedzi 0‑Matrycy na lokalne odkształcenia torsyjne.

### 3.4.1. Nieliniowy Lagrangian i równania Eulera‑Lagrange’a

Potencjał cechowania $A_\mu = (\varphi_{\mathrm{t}}/c_{\perp}, \mathbf{A})$ reprezentuje przemieszczenia ścinające. Zgodnie z nieliniową akustoelastycznością osnowy, pełna gęstość lagrangianu wynosi:

$$\mathcal{L}_{\mathrm{TSM}} = \frac{1}{2}\epsilon_0(1 + \kappa \mathbf{B}^2) \mathbf{E}^2 - \frac{1}{2\mu_0}\mathbf{B}^2 \tag{3.4.1}$$

Uogólnione wektory reakcji osnowy (odpowiedniki indukcji) definiujemy jako:

$$\mathbf{D} = \frac{\partial \mathcal{L}}{\partial \mathbf{E}} = \epsilon_0(1 + \kappa \mathbf{B}^2)\mathbf{E} \tag{3.4.2}$$

$$\mathbf{H} = -\frac{\partial \mathcal{L}}{\partial \mathbf{B}} = \frac{\mathbf{B}}{\mu_0} - \epsilon_0 \kappa \mathbf{E}^2 \mathbf{B} \tag{3.4.3}$$

Podstawiając do równań wariacyjnych ($\nabla \cdot \mathbf{D} = \rho_e$, $\nabla \times \mathbf{H} - \partial_t \mathbf{D} = \mathbf{J}$), uzyskujemy nieliniowe równania elektrodynamiki 0‑Matrycy.

**Zmodyfikowane Prawo Gaussa:**

$$\epsilon_0(1 + \kappa \mathbf{B}^2)\nabla \cdot \mathbf{E} + \epsilon_0 \kappa \nabla(\mathbf{B}^2) \cdot \mathbf{E} = \rho_e \tag{3.4.4}$$

**Zmodyfikowane Prawo Ampère’a‑Maxwella:**

$$\frac{1}{\mu_0}\nabla \times \mathbf{B} - \epsilon_0 \kappa \left[ \mathbf{E}^2 (\nabla \times \mathbf{B}) + \nabla(\mathbf{E}^2) \times \mathbf{B} \right] = \mathbf{J} + \partial_t \left[ \epsilon_0(1 + \kappa \mathbf{B}^2)\mathbf{E} \right] \tag{3.4.5}$$

### 3.4.2. Efekt dwójłomności i stabilizacja węzła

Pełne równania nieliniowe demaskują ukrytą mechanikę 0‑Matrycy:

1. **Pancerz strukturalny:** W pobliżu rdzenia węzła gradient ciśnienia torsyjnego $\nabla(\mathbf{E}^2)$ rośnie asymptotycznie. Człon $\nabla(\mathbf{E}^2) \times \mathbf{B}$ w (3.4.5) działa jak potężny wtórny prąd wirowy osnowy, stanowiąc elastyczny pancerz, który stabilizuje splot i zapobiega jego rozplątaniu – jest to **uzupełniający** mechanizm stabilności, obok topologicznej ochrony wynikającej z $\mathcal{W} \neq 0$ (Rozdział 2.2.2).
2. **Dwójłomność:** Człon $\nabla(\mathbf{B}^2) \cdot \mathbf{E}$ w (3.4.4) dowodzi, że silny gradient skręcenia poprzecznego indukuje efektywny ładunek, modulując lokalną prędkość światła i dopuszczając samo‑ogniskowanie fal.

### 3.4.3. Przybliżenie liniowe i tensor naprężeń Maxwella

Dla słabych pól ($\kappa \mathbf{B}^2 \ll 1$, $\epsilon_0 \kappa \mathbf{E}^2 \ll \mu_0^{-1}$) lagrangian redukuje się do:

$$\mathcal{L}_{\mathrm{EM}} \approx \frac{1}{2}\epsilon_{\mathrm{eff}} \mathbf{E}^2 - \frac{1}{2\mu_0}\mathbf{B}^2 \tag{3.4.6}$$

Z niego wyprowadzamy kanoniczny tensor energii‑pędu, który po symetryzacji daje tensor naprężeń Maxwella:

$$\boldsymbol{\sigma}^{\mathrm{M}} = \epsilon_{\mathrm{eff}}\,\mathbf{E}\otimes\mathbf{E} + \frac{1}{\mu_0}\,\mathbf{B}\otimes\mathbf{B} - u\,\mathbf{I} \tag{3.4.7}$$

gdzie $u = \frac{1}{2}\epsilon_{\mathrm{eff}}\mathbf{E}^2 + \frac{1}{2\mu_0}\mathbf{B}^2$ jest gęstością energii sprężystej osnowy.

### 3.4.4. Siła Lorentza i prawo Coulomba

Całkując dywergencję tensora naprężeń po objętości wokół ładunku próbnego $q$ poruszającego się z prędkością $\mathbf{v}$, otrzymujemy:

$$\mathbf{F} = \int_V \nabla \cdot \boldsymbol{\sigma}^{\mathrm{M}} \, d^3x \tag{3.4.8}$$

co prowadzi do klasycznej **siły Lorentza**:

$$\mathbf{F} = q( \mathbf{E} + \mathbf{v}\times\mathbf{B} ) \tag{3.4.9}$$

W przypadku statycznym odtwarza to **prawo Coulomba**:

$$\mathbf{F}_{12} = \frac{1}{4\pi\epsilon_{\mathrm{eff}}}\frac{q_1 q_2}{r^2}\hat{\mathbf{r}}_{12} \tag{3.4.10}$$

### 3.4.5. Odpychanie jednoimiennych ładunków jako interferencja naprężeń

Dwa węzły o zgodnej chiralności (jednoimienne) wytwarzają pola torsji, których składowe nakładają się konstruktywnie:

$$u = \tfrac{1}{2}\epsilon_{\mathrm{eff}}|\mathbf{E}_1+\mathbf{E}_2|^2 = u_1 + u_2 + \epsilon_{\mathrm{eff}}\,\mathbf{E}_1 \cdot \mathbf{E}_2 \tag{3.4.11}$$

Człon $\epsilon_{\mathrm{eff}}\,\mathbf{E}_1 \cdot \mathbf{E}_2$ powoduje lokalny wzrost ciśnienia torsyjnego. 0‑Matryca wypycha oba sploty na zewnątrz strefy podwyższonej gęstości energii. W przypadku ładunków przeciwnych interferencja jest destruktywna – powstaje obszar obniżonego ciśnienia, co powoduje mechaniczne wciśnięcie węzłów ku sobie przez wyższe ciśnienie zewnętrzne osnowy tła.

---

## 3.5. Ontologia oddziaływania silnego: Topologiczne splątanie węzłów w czwartym wymiarze

W Standardowym Modelu fizyki cząstek oddziaływanie silne postulowane jest jako niezależna, fundamentalna siła. W ramach Mechaniki Substratu Topologicznego (TSM) podejście to staje się redundantne. Zgodnie z fundamentalnymi ustaleniami Rozdziału 2, cząstki elementarne są 4‑wymiarowymi węzłami topologicznymi – ich struktura rozciąga się również w czwarty wymiar przestrzenny ($x^4$). To właśnie ta własność stanowi źródło oddziaływań jądrowych.

### 3.5.1. Splątanie 4D jako źródło sił jądrowych

Gdy dwa węzły topologiczne (nukleony) znajdą się dostatecznie blisko siebie na 3‑branie (odległość rzędu femtometrów), ich **części zanurzone w czwartym wymiarze mogą ulec bezpośredniemu splątaniu topologicznemu**. Dochodzi do fizycznego zazębienia się struktur 4D – linie naprężeń jednego węzła przeplatają się z liniami drugiego w wyższym wymiarze.

To splątanie generuje dodatkowe, potężne naprężenie w osnowie, które w rzucie na 3‑branę obserwujemy jako **krótkozasięgowe, silne przyciąganie**. Mechanizm ten jest w pełni zgodny z Aksjomatem 4 – nie wprowadza żadnej nowej siły, a jedynie wykorzystuje fakt, że węzły są tworami 4D, a sprężystość 0‑Matrycy działa we wszystkich czterech wymiarach.

### 3.5.2. Wyjaśnienie kluczowych własności oddziaływania silnego

| Własność | Wyjaśnienie w TSM (splątanie topologiczne 4D) |
|---|---|
| **Krótki zasięg ($\sim 1$ fm)** | Splątanie wymaga nałożenia się części węzłów zanurzonych w $x^4$. Poza tą odległością struktury 4D nie zazębiają się – oddziaływanie zanika wykładniczo. |
| **Wysycenie** | Jeden węzeł może splątać się w 4D tylko z ograniczoną liczbą sąsiadów – wynika to z geometrii zanurzenia (analogia do liczby koordynacyjnej w sieci krystalicznej). |
| **Niezależność ładunkowa** | Splątanie zależy od pełnej geometrii 4D węzła, a nie od jego rzutu 3D (ładunku elektrycznego). Neutron i proton mają podobną strukturę w $x^4$, stąd oddziałują podobnie, mimo różnicy ładunku. |
| **Uwięzienie (confinement)** | Rozplątanie wymagałoby pokonania bariery topologicznej w 4D – energia potrzebna do „przecięcia” splotu jest ogromna. Zamiast uwolnienia, następuje kreacja nowych par węzłów (hadronizacja). |
| **Swoboda asymptotyczna** | Przy ekstremalnym zbliżeniu, części 4D nakładają się tak silnie, że gradienty naprężeń między węzłami ulegają wypłaszczeniu – węzły zachowują się jak gaz swobodny wewnątrz wspólnego worka topologicznego. |

### 3.5.3. Rola nieliniowego EM jako efektu uzupełniającego

Nieliniowe człony elektromagnetyczne wyprowadzone w sekcji 3.4 (w szczególności „pancerz” $\nabla(\mathbf{E}^2) \times \mathbf{B}$) nie są głównym źródłem sił jądrowych, lecz pełnią rolę **uzupełniającego mechanizmu stabilizującego** pojedyncze węzły. Dodatkowo, w warunkach ekstremalnych gęstości wewnątrz plazmoidów (Rozdział 0.6), nieliniowe efekty EM mogą modulować dynamikę już splątanych układów hadronów.

---

## 3.6. Napięcie i prąd jako mechanika falowa w przewodnikach

Model TSM zastępuje abstrakcyjne przepływy punktów rygorystyczną mechaniką ośrodków ciągłych:

- **Napięcie elektryczne $U$:** Fizyczna różnica ciśnień skręcenia (gradientu potencjału torsyjnego) między dwoma obszarami 0‑Matrycy $[\text{V}]$.
- **Natężenie prądu $I$:** Falowy, konwekcyjny strumień torsji $[\text{A}]$. Sieć jonowa metalu działa jak falowód dla fal torsyjnych. Elektrony (węzły) pełnią rolę kotwic, które przesuwają się powoli (prędkość dryfu $\sim \text{mm/s}$), ale generują sygnał falowy pędzący wzdłuż sieci z prędkością bliską $c_{\perp}$.
- **Opór Ohma i ciepło Joule’a:** Dyssypacja sprężystej energii fali torsyjnej wskutek rozpraszania na niedoskonałościach sieci jonowej, wypromieniowywana jako drgania termiczne (podczerwień i fonony).

---

## 3.7. Inercja elektromechaniczna: Reaktancja i przesunięcia fazowe

Przesunięcia fazowe w obwodach prądu zmiennego wynikają z bezwładności hydrodynamicznej 0‑Matrycy i jej własności elastycznych:

- **Indukcyjność $L$:** Masa efektywna (bezwładność) wirującego pola naprężeń $\mathbf{B}$ $[\text{H}]$. Zmiana kierunku rotacji ośrodka wymaga czasu na przezwyciężenie oporu kinetycznego 0‑cząstek.
- **Pojemność $C$:** Statyczna podatność sprężysta izolatora $[\text{F}]$. Prąd przesunięcia to miara czasowej zmiany gęstości skręcenia (naciągania „sprężyny” dielektryka).

Równanie przesunięcia fazowego:

$$\tan\varphi = \frac{\omega L - (\omega C)^{-1}}{R} \tag{3.7.1}$$

jest ścisłym makroskopowym bilansem między inercją rotacyjną, sprężystością a tarciem falowym ośrodka.

---

## 3.8. Aplikacje kwantowe: Nadprzewodnictwo i Efekt Halla

- **Nadprzewodnictwo:** W ultraniskich temperaturach szum wibracyjny sieci $T_{\text{sub}}$ ulega minimalizacji. Fermiony o przeciwnych chiralnościach splatają osnowy, formując opływowy węzeł sparowany (soliton pary Coopera). Jego symetryczna topologia ślizga się wewnątrz krystalicznej sieci jonowej bez wzbudzania poprzecznych fal ścinających (dyssypacji), co objawia się zerową rezystancją.
- **Efekt Halla:** Kinetyczne znoszenie toru poruszającego się węzła wymuszone przez zewnętrzny gradient odkształceń wirowych ($\mathbf{B}$). Kwantowy efekt Halla, ujawniający się w układach 2D, odzwierciedla dyskretność stabilnych prążków przestrzennych (stanów solitonowych) w głęboko skwantowanej siatce napięć 0‑Matrycy.

---

## 3.9. Podsumowanie Rozdziału 3

Sformułowanie pełnych, nieliniowych równań elasto‑dynamicznych 0‑Matrycy pozwoliło na ostateczne domknięcie logiczne klasycznej teorii pól oddziaływań oraz fizyki obwodów. Najważniejsze wnioski:

- **Topologiczna geneza ładunku:** Czteropotencjał $A_\mu$ jest fizycznym polem przemieszczeń ścinających. Skwantowanie ładunku ($q = ne$) to mechaniczny wymóg zamknięcia fazy skrętu o wielokrotność $2\pi$.
- **Mechanizacja równań Maxwella:** $F_{\mu\nu}$ odzwierciedla antysymetryczną część gradientu przemieszczeń sieci. $\mathbf{E}$ to gradient ciśnienia torsyjnego, $\mathbf{B}$ – wirowość naprężeń ścinających. Brak monopoli magnetycznych wynika z nierozerwalności 3‑brany.
- **Nieliniowa elektrodynamika:** Równania Eulera‑Lagrange’a z nieliniowym $\kappa$ opisują akustoelastyczną odpowiedź osnowy. Wirtualny prąd $\epsilon_0 \kappa \nabla(\mathbf{E}^2) \times \mathbf{B}$ tworzy pancerz stabilizujący węzły.
- **Demistyfikacja sił EM:** Siła Lorentza i prawo Coulomba wyprowadzone z dywergencji tensora naprężeń Maxwella. Odpychanie i przyciąganie to wynik interferencji konstruktywnej/destruktywnej pól naprężeń.
- **Oddziaływanie silne jako splątanie 4D:** Siły jądrowe nie są nową siłą, lecz bezpośrednim efektem topologicznego splątania węzłów w czwartym wymiarze. Wyjaśnia to krótki zasięg, wysycenie, niezależność ładunkową i uwięzienie, w pełnej zgodzie z aksjomatami TSM.
- **Hydrodynamiczna teoria obwodów:** Napięcie i prąd zdefiniowane mechanicznie. Indukcyjność to bezwładność pola $\mathbf{B}$, pojemność – podatność dielektryka. Przesunięcie fazowe to bilans inercji, sprężystości i tarcia.
- **Stany kwantowe jako przejścia fazowe:** Nadprzewodnictwo i kwantowy efekt Halla to dynamiczne uporządkowania w siatce napięć 0‑Matrycy przy minimalnym szumie $T_{\text{sub}}$.