# Rozdział 3: Elektromagnetyzm jako dynamika naprężeń 0-Matrycy: Od topologii splotu do mechaniki obwodów

W klasycznej elektrodynamice pole elektromagnetyczne jest traktowane jako abstrakcyjny byt rozchodzący się w próżni. Ponieważ w Topologicznej Geometrodynamice Matrycy (TGM) niefizyczna próżnia nie istnieje, zjawiska elektromagnetyczne stanowią wyłącznie obserwowalną makroskopowo mechanikę odkształceń ciągłego, 4-wymiarowego ośrodka sprężystego – w szczególności jego naprężeń ścinających i skrętnych zachodzących wewnątrz izotropowej 3-brany.

## 3.1. Od skrętu topologicznego do potencjału cechowania

W Rozdziale 2 wprowadzono wektor orientacji $\mathbf{n}(\mathbf{x})$, opisujący lokalny kierunek osi skręcenia komórek sieci wokół węzła topologicznego (fermionu). W granicy kontinuum, dla układu wielu węzłów, pole to definiuje ciągłe pole torsji. Matematyczne przejście do elektrodynamiki odbywa się przez utożsamienie wektora orientacji $\mathbf{n}$ z kierunkiem polaryzacji poprzecznego przemieszczenia ośrodka.

Formalnie wprowadzamy 4-potencjał $A_{\mu} = (\varphi_{\mathrm{t}}/c, \mathbf{A})$, gdzie:

* $\varphi_{\mathrm{t}}$ jest skalarowym potencjałem ciśnienia torsyjnego (statycznego naciągu),
* $\mathbf{A}$ jest wektorem przemieszczenia ścinającego, którego składowe są proporcjonalne do składowych $\mathbf{n}$ pomnożonych przez amplitudę skręcenia.

W pobliżu rdzenia węzła faza torsji $\phi$ zmienia się o wielokrotność $2\pi$ przy pełnym obrocie. Związek z potencjałem cechowania ma postać:

$$\oint_{\partial S} \mathbf{A} \cdot d\mathbf{l} = \Phi_0 \cdot n$$

gdzie $\Phi_0$ jest elementarnym strumieniem torsji. W ten sposób topologiczny skręt splotu zostaje precyzyjnie zmapowany na cechowanie pola elektromagnetycznego.

**Ładunek elektryczny** $q$ definiujemy jako całkowity strumień wektora gradientu fazy torsji $\nabla\phi$ wzdłuż zamkniętego konturu otaczającego rdzeń węzła:

$$q \equiv e \cdot \frac{1}{2\pi} \oint_{\mathrm{pętla}} \nabla\phi \cdot d\mathbf{l}$$

gdzie $e$ jest ładunkiem elementarnym. Ponieważ ciągłość fazy wokół zamkniętej pętli wymusza całkowitą wielokrotność obrotów, natychmiast otrzymujemy **skwantowanie ładunku elektrycznego** ($q = ne$, gdzie $n \in \mathbb{Z}$).

## 3.2. Tensor naprężeń ścinających a tensor pola elektromagnetycznego

W TGM potencjał $A_\mu$ jest fizycznym polem przemieszczeń ścinających $\mathbf{u}(\mathbf{x},t)$ w 0-Matrycy, gdzie $\mathbf{A} \propto \mathbf{u}$. Antysymetryczna część gradientu przemieszczeń stanowi miarę lokalnej wirowości ośrodka. W czasoprzestrzeni 4-wymiarowej odpowiada to tensorowi pola elektromagnetycznego:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

przy czym składowe czasoprzestrzenne identyfikujemy jako:

$$E_i = c F_{0i}, \qquad B_i = \tfrac{1}{2}\varepsilon_{ijk} F_{jk}$$

Zatem **pole elektryczne $\mathbf{E}$** jest przestrzennym gradientem ciśnienia torsyjnego (skręcenia statycznego), a **pole magnetyczne $\mathbf{B}$** – wektorem wirowości naprężeń ścinających.

Równania Maxwella są bezpośrednią konsekwencją dynamiki sprężystej Matrycy. Bezźródłowe równania są tożsamością wynikającą z definicji $F_{\mu\nu}$ przez potencjał, wyrażającą geometryczną niesprzeczność pola przemieszczeń ($\nabla\cdot\mathbf{B}=0$). Równania ze źródłami otrzymujemy z równań Naviera-Cauchy’ego (wprowadzonych w sekcji 2.1), wyodrębniając antysymetryczną część wirową i utożsamiając jej dywergencję z 4-prądem torsji $J^\mu = (c\rho_e, \mathbf{J})$:

$$\partial_\nu F^{\mu\nu} = \mu_0 J^\mu$$

**Brak monopoli magnetycznych:** Monopol magnetyczny wymagałby istnienia wolnego końca struny naprężeń zawieszonego w przestrzeni. W ciągłym, zablokowanym ośrodku Matrycy zerwanie takiej ciągłości wymusiłoby nieskończoną lokalną energię ścinania i natychmiastowy kolaps. Prawo $\nabla\cdot\mathbf{B}=0$ jest więc trywialną konsekwencją sprężystej nierozerwalności 3-brany.

## 3.3. Prawa zachowania i dynamika falowa

**Zachowanie ładunku elektrycznego:** Zasada opisywana równaniem ciągłości $\partial_\mu J^\mu = 0$ ma charakter ściśle topologiczny. Liczba splotu węzła ($\mathcal{W}$) nie może ulec zmianie bez fizycznego rozerwania węzła (anihilacji z antywęzłem). Zmiany gęstości skręcenia mogą się jedynie przemieszczać. Eksperyment Millikana (1911) dowiódł dyskretności ładunku; w TGM jest to mechaniczny wymóg zamknięcia obwodu fazy o wielokrotność $2\pi$.

**Foton i propagacja:** Jak ustalono wcześniej, foton jest skwantowaną poprzeczną falą ścinającą (mod $c_T$). W obszarach bez swobodnych ładunków równania Maxwella redukują się do równania falowego d’Alemberta. Zgodnie ze zjawiskiem akustoelastyczności (sekcja 1.7), silne pole magnetyczne nieliniowo modyfikuje zastępczą przenikalność osnowy $\epsilon_{\mathrm{eff}} = \epsilon_0(1 + \kappa B^2)$, co obniża lokalną prędkość propagacji fali ścinającej:

$$c_{\mathrm{lok}}(B) = \frac{c_0}{\sqrt{1 + \kappa B^2}} \approx c_0\left(1 - \tfrac12 \kappa B^2\right)$$

Pomiary prędkości światła w polach rzędu **10 T** nie wykazały odchyleń większych niż **10⁻⁸**, co nakłada rygorystyczny limit na stałą sprzężenia magnetycznego $\kappa \lesssim 10^{-6} \text{ T}^{-2}$.

## 3.4. Mechanika oddziaływania: Nieliniowe równania pola, sprzężenia zwrotne i siły Maxwella

Oddziaływania elektromagnetyczne w TSM nie są tajemniczym „działaniem na odległość”, lecz bezpośrednim przejawem sprężystej odpowiedzi 0-Matrycy na lokalne odkształcenia torsyjne. Kluczowym narzędziem do opisu tej dynamiki jest pełen, nieliniowy formalizm elasto-dynamiczny.

### 3.4.1. Nieliniowy Lagrangian TSM i pełne równania Eulera-Lagrange'a

Wychodzimy z założenia, że pole elektromagnetyczne opisywane jest przez potencjał cechowania $A_\mu = (\varphi_{\mathrm{t}}/c_T, \mathbf{A})$, reprezentujący przemieszczenia ścinające w 0-Matrycy. Zgodnie z nieliniową akustoelastycznością osnowy, przenikalność ośrodka zależy od lokalnego skręcenia wirowego, co wyraża pełna gęstość lagrangianu:

$$\mathcal{L}_{\mathrm{TSM}} = \frac{1}{2}\epsilon_0(1 + \kappa \mathbf{B}^2) \mathbf{E}^2 - \frac{1}{2\mu_0}\mathbf{B}^2$$

Aby rygorystycznie opisać dynamikę, wyznaczamy pełne równania ruchu Eulera-Lagrange'a. Wymaga to obliczenia pochodnych funkcjonalnych lagrangianu względem pól $\mathbf{E}$ (gradient ciśnienia torsyjnego) oraz $\mathbf{B}$ (wirowość odkształcenia ścinającego), co pozwala zdefiniować uogólnione wektory reakcji osnowy (odpowiedniki indukcji):

$$\mathbf{D} = \frac{\partial \mathcal{L}}{\partial \mathbf{E}} = \epsilon_0(1 + \kappa \mathbf{B}^2)\mathbf{E}$$

$$\mathbf{H} = -\frac{\partial \mathcal{L}}{\partial \mathbf{B}} = \frac{\mathbf{B}}{\mu_0} - \epsilon_0 \kappa \mathbf{E}^2 \mathbf{B}$$

Podstawiając te wielkości do kanonicznych równań wariacyjnych dla potencjałów ($\nabla \cdot \mathbf{D} = \rho_e$ oraz $\nabla \times \mathbf{H} - \partial_t \mathbf{D} = \mathbf{J}$), uzyskujemy ścisłe, nieliniowe równania elektrodynamiki 0-Matrycy.

**Zmodyfikowane Prawo Gaussa:**
Różniczkując wektor $\mathbf{D}$, otrzymujemy bezpośredni wpływ gradientów pola magnetycznego na rozkład gęstości skręcenia:

$$\epsilon_0(1 + \kappa \mathbf{B}^2)\nabla \cdot \mathbf{E} + \epsilon_0 \kappa \nabla(\mathbf{B}^2) \cdot \mathbf{E} = \rho_e$$

**Zmodyfikowane Prawo Ampère'a-Maxwella:**
Rozwijając równanie dla rotacji pola $\mathbf{H}$, uzyskujemy potężny człon sprzężenia krzyżowego:

$$\frac{1}{\mu_0}\nabla \times \mathbf{B} - \epsilon_0 \kappa \left[ \mathbf{E}^2 (\nabla \times \mathbf{B}) + \nabla(\mathbf{E}^2) \times \mathbf{B} \right] = \mathbf{J} + \partial_t \left[ \epsilon_0(1 + \kappa \mathbf{B}^2)\mathbf{E} \right]$$

### 3.4.2. Efekt dwójłomności i topologiczna stabilizacja splotu

Pełne równania nieliniowe demaskują ukrytą mechanikę 0-Matrycy, która w reżimach skrajnie wysokich energii odpowiada za stabilność samej materii.

1. **Efektywne prądy zaporowe (Stabilizacja pancerza):** W bezpośrednim sąsiedztwie rdzenia węzła topologicznego (fermionu), gradient ciśnienia torsyjnego $\nabla(\mathbf{E}^2)$ rośnie niemal asymptotycznie. Człon $\nabla(\mathbf{E}^2) \times \mathbf{B}$ w zmodyfikowanym prawie Ampère'a zachowuje się jak potężny, wtórny prąd wirowy osnowy. Ten "wirtualny prąd naprężeń" stanowi elastyczny pancerz – stawia gigantyczny opór strukturalny, zapobiegając rozluźnieniu i płynnemu rozplątaniu się węzła. Wyjaśnia to fizyczną stabilność materii bez konieczności wprowadzania dodatkowych oddziaływań silnych do opisu samej cząstki.
2. **Dwójłomność 0-Matrycy:** Człon $\nabla(\mathbf{B}^2) \cdot \mathbf{E}$ w prawie Gaussa dowodzi, że silny gradient skręcenia poprzecznego indukuje efektywny ładunek (zmianę gęstości ciśnienia statycznego). Osnowa staje się w tym miejscu dwójłomna i moduluje prędkość rozchodzenia się fal ścinających (światła), dopuszczając samo-ogniskowanie pakietów falowych w skrajnie zakrzywionych przestrzeniach.

### 3.4.3. Przybliżenie liniowe i klasyczny tensor naprężeń Maxwella

Aby przejść do klasycznej dynamiki zjawisk makroskopowych (z dala od rdzeni splotów), stosujemy przybliżenie liniowe dla obszarów o słabych polach, gdzie $\kappa \mathbf{B}^2 \ll 1$ oraz $\epsilon_0 \kappa \mathbf{E}^2 \ll \mu_0^{-1}$. Nieliniowe sprzężenia zwrotne wygasają, a zmienna $\epsilon_{\mathrm{eff}} \approx \epsilon_0$. Lagrangian redukuje się do klasycznej różnicy gęstości energii:

$$\mathcal{L}_{\mathrm{EM}} \approx \frac{1}{2}\epsilon_{\mathrm{eff}} \mathbf{E}^2 - \frac{1}{2\mu_0}\mathbf{B}^2$$

Z tego uproszczonego lagrangianu wyprowadzamy kanoniczny tensor energii-pędu, który po symetryzacji procedurą Belinfanta-Rosenfelda daje klasyczny tensor naprężeń Maxwella ($\sigma_{ij}^{\mathrm{M}}$). W notacji wektorowej:

$$\boldsymbol{\sigma}^{\mathrm{M}} = \epsilon_{\mathrm{eff}}\,\mathbf{E}\otimes\mathbf{E} + \frac{1}{\mu_0}\,\mathbf{B}\otimes\mathbf{B} - u\,\mathbf{I}$$

gdzie $u = \frac{1}{2}\epsilon_{\mathrm{eff}}\mathbf{E}^2 + \frac{1}{2\mu_0}\mathbf{B}^2$ jest całkowitą liniową gęstością energii sprężystej osnowy. W makroskopowym limicie TSM, tensor $\sigma_{ij}^{\mathrm{M}}$ stanowi mierzalne ciśnienie wywierane przez deformacje poprzeczne na dowolną powierzchnię.

### 3.4.4. Siła Lorentza i prawo Coulomba

W mechanice ośrodków ciągłych siła wypadkowa na element objętości równa się dywergencji tensora naprężeń. Całkując dywergencję $\boldsymbol{\sigma}^{\mathrm{M}}$ po objętości wokół ładunku próbnego $q$ (węzła) poruszającego się z prędkością $\mathbf{v}$, otrzymujemy hydro-elastyczną reakcję Matrycy:

$$\mathbf{F} = \int_V \nabla \cdot \boldsymbol{\sigma}^{\mathrm{M}} \, d^3x$$

Po przekształceniach wektorowych uzyskujemy postać:

$$\nabla \cdot \boldsymbol{\sigma}^{\mathrm{M}} = \rho_e \mathbf{E} + \mathbf{J}\times\mathbf{B} + \epsilon_{\mathrm{eff}}\,\partial_t(\mathbf{E}\times\mathbf{B})$$

Dla ładunku punktowego człon zależny od czasu (zmiana pędu fali ścinającej) staje się pomijalny, co daje klasyczną **siłę Lorentza**: $\mathbf{F} = q( \mathbf{E} + \mathbf{v}\times\mathbf{B} )$.
W przypadku statycznym, siła jest czystym gradientem statycznego naciągu torsyjnego $\varphi_{\mathrm{t}}$, co odtwarza **prawo Coulomba**: $\mathbf{F}_{12} = \frac{1}{4\pi\epsilon_{\mathrm{eff}}}\frac{q_1 q_2}{r^2}\hat{\mathbf{r}}_{12}$.

### 3.4.5. Odpychanie jednoimiennych ładunków jako interferencja naprężeń

Ujęcie nieliniowej elastodynamiki ostatecznie demaskuje mechanizm przyciągania i odpychania bez "magicznego" działania na odległość. Dwa węzły topologiczne o zgodnej chiralności (jednoimienne) wytwarzają pola torsji, których składowe w przestrzeni między ładunkami nakładają się konstruktywnie:

$$u = \tfrac{1}{2}\epsilon_{\mathrm{eff}}|\mathbf{E}_1+\mathbf{E}_2|^2 = u_1 + u_2 + \epsilon_{\mathrm{eff}}\,\mathbf{E}_1 \cdot \mathbf{E}_2$$

Człon $\epsilon_{\mathrm{eff}}\,\mathbf{E}_1 \cdot \mathbf{E}_2$ powoduje lokalny wzrost ciśnienia torsyjnego. Zgodnie z tensorem naprężeń mechanicznych, fizyczne naciągnięcie osnowy dąży do rozładowania skumulowanej energii. 0-Matryca reaguje wyrównaniem ciśnień, wypychając oba sploty w przeciwne strony – na zewnątrz strefy podwyższonej gęstości energii. W przypadku ładunków przeciwnych, interferencja jest destruktywna, co tworzy obszar o obniżonym ciśnieniu relaksacyjnym wewnątrz, powodując mechaniczne wciśnięcie węzłów ku sobie przez wyższe ciśnienie zewnętrzne osnowy tła.

## 3.5. Ontologia oddziaływania silnego: Nieliniowe sprzężenie skręceń topologicznych w skali femtometrowej

W Standardowym Modelu fizyki cząstek oddziaływanie silne postulowane jest jako niezależna, fundamentalna siła przenoszona przez gluony między kwarkami posiadającymi ładunek kolorowy. W świetle nieliniowej elasto-dynamiki Mechaniki Substratu Topologicznego (TSM), takie wielorakie podejście staje się redundantne. TSM dowodzi rygorystycznie, że to, co makroskopowo obserwujemy jako "oddziaływanie silne" utrzymujące jądra atomowe, nie jest nową klasą oddziaływania przestrzennego, lecz **skrajną, nieliniową manifestacją sprzężenia zwrotnego naprężeń elektromagnetycznych na dystansach femtometrowych.**

### 3.5.1. Przekroczenie granicy liniowej i fuzja pancerzy naprężeniowych

Mechanizm ten wynika bezpośrednio z pełnych równań Eulera-Lagrange'a dla elektrodynamiki 0-Matrycy, wyprowadzonych w sekcji 3.4. Przypomnijmy, że zmodyfikowane prawo Ampère'a-Maxwella zawiera krytyczny człon sprzężenia geometrycznego: $\epsilon_0 \kappa \nabla(\mathbf{E}^2) \times \mathbf{B}$. Człon ten funkcjonuje jako wtórny prąd wirowy osnowy – "pancerz" stabilizujący strukturę samego splotu topologicznego (fermionu).

Na dystansach atomowych i większych ($r \gg 10^{-15}\text{ m}$), lokalny gradient ciśnienia torsyjnego $\nabla(\mathbf{E}^2)$ szybko dąży do zera, sprzężenie nieliniowe zanika, a osnowa zachowuje się zgodnie z klasycznym prawem Coulomba. Wtedy jednoimienne sploty odpychają się.

Jednakże, gdy dwa węzły topologiczne (np. nukleony) zostaną zbliżone do siebie na odległość krytyczną (skala femtometrowa), gradienty ich ciśnień naprężeniowych rosną w sposób asymptotyczny. Dochodzi do fizycznego nałożenia się ich strukturalnych pancerzy. Wirtualne prądy $\nabla(\mathbf{E}^2) \times \mathbf{B}$ obu defektów zaczynają się przenikać i interferować.

### 3.5.2. Mechaniczny zamek topologiczny: Swoboda asymptotyczna i uwięzienie

To potężne sprzężenie zwrotne wytwarza nową strefę stabilności przestrzennej wewnątrz 3-brany, która idealnie odtwarza dwa sztandarowe fenomeny oddziaływań silnych z chromodynamiki kwantowej (QCD):

1. **Uwięzienie kinetyczne (Confinement):** Zazębienie się dwóch obszarów o ekstremalnym, nieliniowym gradiencie naprężeń tworzy topologiczny zamek. Próba rozerwania tak splecionych węzłów (oddalenia ich od siebie) drastycznie zwiększa całkowitą energię sprężystą $\mathcal{L}_{\mathrm{TSM}}$ lokalnej 0-Matrycy. Zamiast maleć z kwadratem odległości (jak w prawie Coulomba), elastyczna siła oporu rośnie wraz z próbą rozciągnięcia tego wspólnego naciągu. Przy odpowiednio dużej dostarczonej energii, zamiast uwolnienia splotów, bardziej "opłacalne" energetycznie dla osnowy staje się pęknięcie naprężenia i zrolowanie jego energii w nową parę defektów (kreacja par kwark-antykwark), co zapobiega wyizolowaniu pojedynczego składnika jądra.
2. **Swoboda asymptotyczna (Asymptotic Freedom):** Gdy węzły zostaną wtłoczone jeszcze głębiej do wnętrza wspólnego, zunifikowanego pancerza nieliniowego (gdzie $\kappa \mathbf{B}^2 \gg 1$), ich lokalne wektory wewnętrzne zaczynają dzielić tę samą studnię potencjału skręcenia. W sercu tego połączonego układu wzajemne gradienty $\nabla(\mathbf{E}^2)$ pomiędzy sąsiadującymi splotami ulegają względnemu wypłaszczeniu. W efekcie, na skrajnie krótkich dystansach wewnątrz jądra, sploty nie odczuwają już niszczących naprężeń względem siebie – zachowują się jak quasi-swobodny gaz zamknięty w elastycznym, nierozerwalnym worku osnowy.

### 3.5.3. Redukcja ilości fundamentalnych oddziaływań

Definicja oddziaływania silnego jako geometrodynamicznego sprzężenia zwrotnego ma doniosłe znaczenie dla elegancji teorii. TSM radykalnie upraszcza ontologię fizyki mikroświata. Wykazuje matematycznie, że natura nie musi wymyślać nowej "siły jądrowej", by zbudować materię. Wystarczy, że przy ekstremalnie gęstych ugięciach elastycznego ośrodka zaczynają dominować człony nieliniowe tensora odkształceń, te same, które w reżimie liniowym odpowiadają za propagację klasycznego światła i pola magnetycznego. Elektromagnetyzm i oddziaływania silne okazują się dwiema skrajnymi manifestacjami tego samego matematycznego aparatu elasto-dynamiki 4D.


## 3.6. Napięcie i prąd jako mechanika falowa w przewodnikach

Model TGM zastępuje abstrakcyjne przepływy punktów rygorystyczną mechaniką płynów i ciał stałych:

* **Napięcie elektryczne $U$:** Jest fizyczną różnicą ciśnień skręcenia (gradientu potencjału torsyjnego) między dwoma obszarami 0-Matrycy.
* **Natężenie prądu $I$:** Jest falowym, konwekcyjnym strumieniem torsji. Sieć jonowa metalu działa jak falowód dla fal torsyjnych. Elektrony pełnią jedynie rolę węzłów-kotwic, które przesuwają się niezwykle powoli (prędkość dryfu rzędu mm/s), ale generują sygnał falowy pędzący wzdłuż sieci z prędkością bliską $c_{\mathrm{lok}}$.
* **Opór Ohma i ciepło Joule’a:** To dyssypacja sprężystej energii fali torsyjnej wskutek rozpraszania na niedoskonałościach sieci jonowej, wypromieniowywana ostatecznie jako drgania termiczne (podczerwień i fonony).

## 3.7. Inercja elektromechaniczna: Reaktancja i przesunięcia fazowe

Przesunięcia fazowe w obwodach prądu zmiennego wynikają wprost z bezwładności hydrodynamicznej Matrycy i jej własności elastycznych:

* **Indukcyjność $L$:** To masa efektywna (bezwładność) wirującego pola naprężeń $\mathbf{B}$. Zmiana kierunku rotacji ośrodka wymaga czasu na przezwyciężenie oporu kinetycznego 0-cząstek.
* **Pojemność $C$:** Odzwierciedla statyczną podatność sprężystą izolatora. Prąd przesunięcia to miara czasowej zmiany gęstości skręcenia (naciągania „sprężyny” dielektryka).

Równanie przesunięcia fazowego $\tan\varphi = (\omega L - (\omega C)^{-1})/R$ jest ścisłym makroskopowym bilansem między inercją rotacyjną, sprężystością a tarciem falowym ośrodka.

## 3.8. Aplikacje kwantowe: Nadprzewodnictwo i Efekt Halla

* **Nadprzewodnictwo:** W ultraniskich temperaturach szum wibracyjny sieci ulega minimalizacji. Zgodnie z dynamiką topologiczną, fermiony o przeciwnych chiralnościach splatają osnowy, formując opływowy węzeł sparowany (soliton par Coopera). Jego symetryczna topologia ślizga się wewnątrz krystalicznej sieci jonowej bez wzbudzania poprzecznych fal ścinających (dyssypacji), co objawia się zerową rezystancją.
* **Efekt Halla:** Kinetyczne znoszenie toru poruszającego się węzła wymuszone przez zewnętrzny gradient odkształceń wirowych ($\mathbf{B}$). Kwantowy efekt Halla, ujawniający się w układach 2D, odzwierciedla dyskretność stabilnych prążków przestrzennych (stanów solitonowych) w głęboko skwantowanej siatce napięć Matrycy.
