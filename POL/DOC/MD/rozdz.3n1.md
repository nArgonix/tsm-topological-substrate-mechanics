<!-- ver:3.2.0 -->
# Rozdział 3: Dynamika naprężeń 0-Matrycy – od elektrodynamiki i topologicznych sił jądrowych do mechaniki obwodów

W klasycznej elektrodynamice pole elektromagnetyczne jest traktowane jako abstrakcyjny byt rozchodzący się w próżni. Ponieważ w Mechanice Substratu Topologicznego (TSM) niefizyczna próżnia nie istnieje, zjawiska elektromagnetyczne stanowią wyłącznie obserwowalną makroskopowo mechanikę odkształceń ciągłego, 4‑wymiarowego ośrodka sprężystego – w szczególności jego naprężeń ścinających i skrętnych zachodzących wewnątrz izotropowej 3‑brany. Zgodnie z Rozdziałami 0 i 1, cała dynamika rozgrywa się w lokalnym czasie $t$, emergentnym z gęstości upakowania 0‑Matrycy.

---

## 3.0. Czas lokalny w dynamice elektromagnetycznej – przypomnienie i osadzenie

Zgodnie z Rozdziałem 1.1, TSM odrzuca absolutny czas newtonowski i relatywistyczną czasoprzestrzeń. Podstawą opisu ewolucji pól jest **lokalny czas własny** $t$, płynący z gęstości upakowania 0‑cząstek:

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi\rangle_{\text{macro}}} \tag{3.0.1}$$

gdzie:
- $dt$ – przyrost czasu lokalnego w punkcie $\mathbf{x}$ $[\text{s}]$,
- $dN$ – liczba cykli procesu okresowego (bezwymiarowa),
- $T_0$ – elementarny okres referencyjny $[\text{s}]$,
- $\phi_0$ – podstawowa gęstość upakowania 0-Matrycy w Stanie Zero,
- $\langle\phi\rangle_{\text{macro}}$ – uśredniona hydrodynamicznie gęstość osnowy w obszarze zajmowanym przez układ pomiarowy.

W płaskiej, niezakłóconej 3‑branie ($\phi = \phi_0$) czas własny pokrywa się z **czasem współrzędnościowym** $t_{\text{flat}}$, który jest naturalną zmienną w równaniach pola. W pobliżu węzłów topologicznych ($\langle\phi\rangle_{\text{macro}} > \phi_0$) lokalny czas zwalnia, co modyfikuje obserwowaną dynamikę fal elektromagnetycznych (efekt Shapiro, dylatacja grawitacyjna). Wszystkie równania tego rozdziału sformułowane są w czasie współrzędnościowym $t = t_{\text{flat}}$, o ile nie zaznaczono inaczej.

---

## 3.1. Od skrętu topologicznego do potencjału cechowania

W Rozdziale 2 wprowadzono wektor orientacji $\mathbf{n}(\mathbf{x})$, opisujący lokalny kierunek osi skręcenia komórek sieci wokół węzła topologicznego (fermionu). W granicy kontinuum, dla układu wielu węzłów, pole to definiuje ciągłe pole torsji. Matematyczne przejście do elektrodynamiki odbywa się przez utożsamienie wektora orientacji $\mathbf{n}$ z kierunkiem polaryzacji poprzecznego przemieszczenia ośrodka.

### 3.1.1. Czteropotencjał torsyjny

Formalnie wprowadzamy 4‑potencjał $A_{\mu} = (\varphi_{\mathrm{t}}/c_{\perp}, \mathbf{A})$, gdzie:
- $\varphi_{\mathrm{t}}$ – skalarowy potencjał ciśnienia torsyjnego (statycznego naciągu) $[\text{V}]$,
- $\mathbf{A}$ – wektor przemieszczenia ścinającego $[\text{T} \cdot \text{m}]$, którego składowe są proporcjonalne do składowych $\mathbf{n}$ pomnożonych przez amplitudę skręcenia,
- $c_{\perp}$ – prędkość poprzecznych fal ścinających $[\text{m} \cdot \text{s}^{-1}]$.

W pobliżu rdzenia węzła faza torsji $\theta$ zmienia się o wielokrotność $2\pi$ przy pełnym obrocie. Poza samym rdzeniem, wektorowy potencjał ścinania jest wprost proporcjonalny do gradientu tej fazy: $\mathbf{A} \approx \frac{\Phi_0}{2\pi} \nabla\theta$. Całkowy związek z potencjałem cechowania (topologiczne kwantowanie strumienia) ma postać:

$$\oint_{\partial S} \mathbf{A} \cdot d\mathbf{l} = \Phi_0 \cdot n \tag{3.1.1}$$

gdzie:
- $\partial S$ – zamknięty kontur otaczający rdzeń węzła,
- $\Phi_0$ – elementarny strumień torsji $[\text{T} \cdot \text{m}^2]$,
- $n \in \mathbb{Z}$ – liczba obrotów fazy.

### 3.1.2. Ładunek elektryczny jako strumień skrętu

**Ładunek elektryczny** $q$ definiujemy jako całkowity **obieg (cyrkulację)** wektora gradientu fazy torsji $\nabla\theta$ wzdłuż zamkniętego konturu otaczającego rdzeń węzła, przeskalowany przez ładunek elementarny:

$$q \equiv e \cdot \frac{1}{2\pi} \oint_{\mathrm{pętla}} \nabla\theta \cdot d\mathbf{l} \tag{3.1.2}$$

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
- $\varepsilon_{ijk}$ – symbol Levi‑Civitàego.

### 3.2.1. Równania Maxwella z dynamiki Naviera‑Cauchy'ego

Z definicji (3.2.1) wynika natychmiast, że antysymetryczna kombinacja pochodnych cząstkowych tensora $F_{\mu\nu}$ znika tożsamościowo (tożsamość Bianchi):

$$\nabla \cdot \mathbf{B} = 0 \tag{3.2.3a}$$
$$\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0 \tag{3.2.3b}$$

Są to **geometryczne tożsamości** wynikające z ciągłości ośrodka i zerowania się rotacji gradientu — linie sił $\mathbf{B}$ nie mają początku ani końca w nierozerwalnym kontinuum. Nie wymagają żadnych dodatkowych postulatów.

Równania ze źródłami posiadają silniejszy status niż postulat — są algebraiczną konsekwencją falowej dynamiki torsyjnego pola przemieszczeń w obecności węzłów topologicznych.

**Falowe równanie pola w obecności węzłów topologicznych.**

Składowe elektromagnetyczne 4-potencjału $A_\mu = (\varphi_{\mathrm{t}}/c_\perp,\, \mathbf{A})$ opisują torsyjne przemieszczenia ścinające 3-brany (Sekcja 3.1.1). Ich dynamika w obszarze wolnym od węzłów wynika z równania Naviera-Cauchy'ego dla poprzecznych modów substratu (Rozdział 2, Sekcja 2.1.3). W warunku cechowania Lorentza:

$$\partial^\mu A_\mu = 0 \tag{3.2.4a}$$

który wynika bezpośrednio z warunku domknięcia 2-formy torsyjnej $d\beta = 0$ (Rozdział 2, Równanie 2.1.5), jednorodne równanie falowe przyjmuje postać:

$$\Box A^\mu = 0, \qquad \Box \equiv \nabla^2 - \frac{1}{c_\perp^2}\frac{\partial^2}{\partial t^2} \tag{3.2.4b}$$

zgodną z ogólnym równaniem falowym substratu (Rozdział 1, Równanie 1.4.3).

Węzeł topologiczny o ładunku $q = \mathcal{W} \cdot e$ (Sekcja 3.1.2) jest trwałą, zlokalizowaną anomalią torsyjną: polem fazy $\theta$ o niezerowym nawinięciu. Jego obecność wprowadza do równania falowego jawny człon źródłowy. Motywacja fizyczna: warunek nawinięcia fazy $\oint \nabla\theta \cdot d\mathbf{l} = 2\pi\mathcal{W}$ wymusza, by statyczny potencjał torsyjny węzła spełniał równanie Poissona:

$$\nabla^2 \varphi_{\mathrm{t}} = -\frac{q}{\epsilon_0}\,\delta^3(\mathbf{x} - \mathbf{x}_0) \tag{3.2.4c}$$

Jest to statyczny limit ($\partial_t = 0$, $\mathbf{J} = \mathbf{0}$) ogólnego kowariancyjnego równania falowego dla ruchomego węzła. Uogólnienie na przypadek dynamiczny przeprowadzamy w dwóch krokach. Po pierwsze, operator $\Box$ jest skalarem Lorentza — wynika to z niezmienniczości jednorodnego równania falowego substratu względem transformacji Lorentza (Sekcja 1.8.1, Równanie 1.7.1d). Po drugie, 4-prąd torsyjny $J^\mu = (c_\perp\rho_e, \mathbf{J})$ transformuje się jak 4-wektor, co jest konsekwencją topologicznej niezmienniczości ładunku $q = \mathcal{W}\cdot e$ (Sekcja 3.1.2) oraz równania ciągłości $\partial_\mu J^\mu = 0$ (Sekcja 3.3.1). Dowód: ponieważ $q$ jest skalarem Lorentza i zachodzi $q = \int J^0 d^3x$, a przy transformacji Lorentza wzdłuż x objętość ulega kontrakcji $x$ daje $d^3x' = d^3x/\gamma$, to $J^0 = \rho_e$ musi transformować się jak $\gamma\rho_e$ — co jest transformacją składowej czasowej 4-wektora. Składowa przestrzenna $\mathbf{J} = \rho_e \mathbf{v}$ transformuje się zgodnie.
 Ponieważ $\Box$ i $J^\mu$ posiadają właściwe właściwości transformacyjne, kowariantna postać równania falowego z obecnością źródeł jest jednoznacznie wyznaczona:

$$\Box A^\mu = -\mu_0 J^\mu$$
 
Przy zachowaniu izotropii 0-Matrycy i kowariancji Lorentza (emergentnej własności granicy liniowej, Sekcja 3.4.1), daje:

$$\Box A^\mu = -\mu_0 J^\mu \tag{3.2.4d}$$

gdzie:
- $\Box$ – operator d'Alemberta (3.2.4b),
- $J^\mu = (c_\perp \rho_e,\, \mathbf{J})$ – 4-prąd torsyjny węzłów,
- $\mu_0 = 1/(\epsilon_0 c_\perp^2)$ – przenikalność magnetyczna osnowy $[\mathrm{N \cdot A^{-2}}]$.

Weryfikacja spójności znaku: dla statycznego węzła $\nabla^2 A_0 = -\mu_0 J_0$. Przy $A_0 = \varphi_{\mathrm{t}}/c_\perp$ i $J_0 = c_\perp\rho_e$ daje $\nabla^2\varphi_{\mathrm{t}} = -\mu_0 c_\perp^2 \rho_e = -\rho_e/\epsilon_0$, co odtwarza Równanie (3.2.4c) dokładnie. $\checkmark$

**Algebraiczne wyprowadzenie.**

Obliczamy 4-dywergencję tensora $F^{\mu\nu}$ zdefiniowanego w (3.2.1):

$$\partial_\nu F^{\mu\nu} = \partial_\nu\!\left(\partial^\mu A^\nu - \partial^\nu A^\mu\right) = \partial^\mu\!\left(\partial_\nu A^\nu\right) - \Box A^\mu \tag{3.2.4e}$$

Stosując warunek Lorentza (3.2.4a) oraz równanie falowe z źródłem (3.2.4d):

$$\partial_\nu F^{\mu\nu} = \partial^\mu(0) - \left(-\mu_0 J^\mu\right) \tag{3.2.4f}$$

$$\boxed{\partial_\nu F^{\mu\nu} = \mu_0 J^\mu} \tag{3.2.4}$$

Równanie (3.2.4) jest zatem **algebraiczną konsekwencją** falowej dynamiki torsyjnego pola przemieszczeń z obecnością źródeł topologicznych w warunku cechowania Lorentza — nie postulatem. Rozwinięcie składowe odtwarza:

dla $\mu = 0$:

$$\nabla \cdot \mathbf{E} = \frac{\rho_e}{\epsilon_0} \tag{3.2.4g}$$

dla $\mu = i$:

$$\nabla \times \mathbf{B} - \frac{1}{c_\perp^2}\frac{\partial \mathbf{E}}{\partial t} = \mu_0 \mathbf{J} \tag{3.2.4h}$$

**Granica identyfikacyjna.** Jedynym elementem wymagającym identyfikacji jest zapis 4-prądu torsyjnego w terminach gęstości ładunku i prądu:

$$J^\mu = \left(c_\perp \rho_e,\, \mathbf{J}\right), \qquad \rho_e = \sum_k q_k\,\delta^3(\mathbf{x} - \mathbf{x}_k(t)), \qquad \mathbf{J} = \sum_k q_k\,\mathbf{v}_k\,\delta^3(\mathbf{x} - \mathbf{x}_k(t)) \tag{3.2.4i}$$

gdzie $q_k = \mathcal{W}_k \cdot e$ to ładunek $k$-tego węzła wyznaczony przez jego liczbę splotu. Identyfikacja ta nie jest aksjomatem niezależnym — wynika wprost z Sekcji 3.1.2, w której ładunek elektryczny zdefiniowano jako cyrkulację gradientu fazy torsyjnej, a jego skwantowanie do wielokrotności $e$ wywiedziono z geometrycznej konieczności domknięcia fazy o wielokrotność $2\pi$.

**Brak monopoli magnetycznych.** Równania (3.2.3a,b) są tożsamościami geometrycznymi wynikającymi z ciągłości 3-brany. Monopol magnetyczny wymagałby wolnego końca struny naprężeń w sposób niemożliwy w nieprzerwalnym kontinuum — stąd $\nabla \cdot \mathbf{B} = 0$ jest trywialną konsekwencją topologicznej spójności substratu, niezależną od struktury 4-prądu.

---

## 3.3. Prawa zachowania i dynamika falowa

### 3.3.1. Zachowanie ładunku elektrycznego

Zasada opisywana równaniem ciągłości:

$$\partial_\mu J^\mu = 0 \quad \implies \quad \frac{\partial \rho_e}{\partial t} + \nabla \cdot \mathbf{J} = 0 \tag{3.3.1}$$

ma charakter ściśle topologiczny. Liczba splotu węzła $\mathcal{W}$ (Rozdział 2.2.2) nie może ulec zmianie bez fizycznego rozerwania węzła (anihilacji z antywęzłem). Zmiany gęstości skręcenia mogą się jedynie przemieszczać.

### 3.3.2. Foton i propagacja

Jak ustalono w Rozdziale 2, foton jest skwantowaną poprzeczną falą ścinającą, której prędkość propagacji jest ściśle zdefiniowana przez lokalny moduł ścinania 0-Matrycy ($c_{\perp}$). W obszarach bez swobodnych ładunków równania Maxwella redukują się do równania falowego d'Alemberta.

Zgodnie ze zjawiskiem akustoelastyczności (Rozdział 1.8), silne lokalne naprężenie wirowe (pole magnetyczne) nieliniowo modyfikuje zastępczą przenikalność sprężystą osnowy. Wyrażony przez stałą Murnaghana $\mathcal{A}$ i moduł ścinania osnowy $\mu_s$ parametr sprzężenia wynosi $\kappa \approx \mathcal{A}/\mu_s$ (por. Równanie 1.8.1). W układzie spoczynku 0-Matrycy prowadzi to do:

$$\epsilon_{\mathrm{eff}} = \epsilon_0 \left(1 + \kappa B^2\right) \tag{3.3.2}$$

co obniża lokalną prędkość propagacji fali ścinającej:

$$c_{\mathrm{lok}}(B) = \frac{c_{\perp}}{\sqrt{1 + \kappa B^2}} \approx c_{\perp}\left(1 - \tfrac{1}{2} \kappa B^2\right) \tag{3.3.3}$$

gdzie:
- $\epsilon_0$ – przenikalność elektryczna płaskiej osnowy $[\text{F} \cdot \text{m}^{-1}]$,
- $\kappa$ – stała sprzężenia magneto‑elastycznego, powiązana z acustoelastyczną stałą Murnaghana $[\text{T}^{-2}]$.

Formuły (3.3.2) i (3.3.3) są sformułowane w uprzywilejowanym układzie spoczynku 0-Matrycy. Kowariantność Lorentza jest emergentną własnością liniowego przybliżenia ($\kappa \to 0$), w którym odtwarza się standardowa elektrodynamika Maxwella. Pomiary prędkości światła w polach rzędu 10 T nie wykazały odchyleń większych niż $10^{-8}$, co nakłada rygorystyczny limit: $\kappa \lesssim 10^{-6}\ \text{T}^{-2}$, spójny z brakiem obserwowalnych efektów acustoelastycznych w dotychczasowych eksperymentach optycznych. Niezależne ograniczenie pochodzi z eksperymentu ATLAS (2017), który zmierzył rozpraszanie foton-foton w ultraperyferykalnych zderzeniach jonów ołowiu — wynik jest zgodny ze standardową elektrodynamiką kwantową i nie pozostawia miejsca na korekcje większe niż $\kappa \lesssim 10^{-6}\ \text{T}^{-2}$.

---

## 3.4. Mechanika oddziaływania: Nieliniowe równania pola, sprzężenia zwrotne i siły Maxwella

Po opisie swobodnej propagacji fal (fotonów), należy rozważyć pełną dynamikę oddziaływań między trwałymi węzłami. W TSM nie są one „działaniem na odległość", lecz bezpośrednim przejawem sprężystej odpowiedzi 0‑Matrycy na lokalne odkształcenia torsyjne i ich wzajemne nakładanie się.

### 3.4.1. Nieliniowy Lagrangian i równania Eulera‑Lagrange'a

Potencjał cechowania $A_\mu = (\varphi_{\mathrm{t}}/c_{\perp}, \mathbf{A})$ reprezentuje wektorowe pole przemieszczeń ścinających osnowy (gdzie $\varphi_{\mathrm{t}}$ to potencjał ciśnienia torsyjnego, a $\mathbf{A}$ to wektor przemieszczenia). Zgodnie z nieliniową akustoelastycznością 0-Matrycy, w której moduły sprężystości zależą od kwadratu odkształcenia, pełna gęstość lagrangianu (gęstość energii odkształcenia) w układzie spoczynku 0-Matrycy wynosi:

$$\mathcal{L}_{\mathrm{TSM}} = \frac{1}{2}\epsilon_0(1 + \kappa \mathbf{B}^2) \mathbf{E}^2 - \frac{1}{2\mu_0}\mathbf{B}^2 \tag{3.4.1}$$

Gdzie:
- $\mathcal{L}_{\mathrm{TSM}}$ – gęstość Lagrangianu Substratu $[\text{J} \cdot \text{m}^{-3}]$,
- $\epsilon_0, \mu_0$ – przenikalność elektryczna i magnetyczna płaskiej osnowy,
- $\kappa \approx \mathcal{A}/\mu_s$ – stała nieliniowego sprzężenia magneto‑elastycznego, wyrażona przez stałą Murnaghana $\mathcal{A}$ i moduł ścinania osnowy $\mu_s$ (por. Rozdział 1.8) $[\text{T}^{-2}]$,
- $\mathbf{E}, \mathbf{B}$ – wektory natężenia pola elektrycznego i indukcji magnetycznej.

> **Uwaga o układzie odniesienia:** Lagrangian (3.4.1) jest sformułowany w uprzywilejowanym układzie spoczynku 0-Matrycy i nie jest skalarem Lorentza. Jest to naturalna konsekwencja acustoelastycznej natury osnowy: efektywna przenikalność zależy od stanu naprężeń w ośrodku, który jest wielkością zdefiniowaną w konkretnym układzie. Kowariantna postać Lagrangianu wymaga przepisania przez niezmienniki Lorentza $\mathcal{F} = \frac{1}{2}(\epsilon_0 E^2 - B^2/\mu_0)$ i $\mathcal{G} = c\epsilon_0\mathbf{E}\cdot\mathbf{B}$ i jest przedmiotem odrębnej analizy. W granicy liniowej ($\kappa \to 0$) Lagrangian (3.4.1) redukuje się do kowariantnej elektrodynamiki Maxwella — kowariantność Lorentza jest emergentną własnością tej granicy.

Uogólnione wektory reakcji osnowy (odpowiedniki indukcji) definiujemy jako:

$$\mathbf{D} = \frac{\partial \mathcal{L}}{\partial \mathbf{E}} = \epsilon_0(1 + \kappa \mathbf{B}^2)\mathbf{E} \tag{3.4.2}$$

$$\mathbf{H} = -\frac{\partial \mathcal{L}}{\partial \mathbf{B}} = \frac{\mathbf{B}}{\mu_0} - \epsilon_0 \kappa \mathbf{E}^2 \mathbf{B} \tag{3.4.3}$$

W powyższych relacjach:
- $\mathbf{D}$ – wektor indukcji elektrycznej (elektryczna odpowiedź ośrodka),
- $\mathbf{H}$ – natężenie pola magnetycznego (magnetyczna odpowiedź ośrodka).

**Fizyczna interpretacja asymetrii D i H:** Pole $\mathbf{B}$ (wirowość naprężeń ścinających) generuje odśrodkowy nacisk na 0-cząstki komórek Wignera-Seitza, lokalnie zwiększając gęstość upakowania $\phi$. Rosnące $\phi$ zmniejsza swobodę translacyjną 0-cząstek i podnosi ich podatność na deformację elektryczną — stąd modyfikacja $\epsilon_{\text{eff}} = \epsilon_0(1+\kappa B^2)$ w $\mathbf{D}$. Odwrotnie, ciśnienie torsyjne $\mathbf{E}$ (gradient naciągu osnowy) usztywnia siatkę komórkową przeciwko dalszemu skręceniu — stąd redukcja efektywnej przenikalności magnetycznej w $\mathbf{H}$. Obie korekcje wynikają z tego samego członu sprzężenia $\frac{1}{2}\epsilon_0\kappa E^2 B^2$ w Lagrangianie i są ze sobą termodynamicznie konsekwentne.

Podstawiając do równań wariacyjnych ($\nabla \cdot \mathbf{D} = \rho_e$, $\nabla \times \mathbf{H} - \partial_t \mathbf{D} = \mathbf{J}$), uzyskujemy nieliniowe równania elektrodynamiki 0‑Matrycy.

**Zmodyfikowane Prawo Gaussa:**

$$\epsilon_0(1 + \kappa \mathbf{B}^2)\nabla \cdot \mathbf{E} + \epsilon_0 \kappa \nabla(\mathbf{B}^2) \cdot \mathbf{E} = \rho_e \tag{3.4.4}$$

**Zmodyfikowane Prawo Ampère'a‑Maxwella:**

$$\frac{1}{\mu_0}\nabla \times \mathbf{B} - \epsilon_0 \kappa \left[ \mathbf{E}^2 (\nabla \times \mathbf{B}) + \nabla(\mathbf{E}^2) \times \mathbf{B} \right] = \mathbf{J} + \partial_t \left[ \epsilon_0(1 + \kappa \mathbf{B}^2)\mathbf{E} \right] \tag{3.4.5}$$

### 3.4.2. Acustoelastyczny pancerz strukturalny i modulacja prędkości lokalnej

Pełne równania nieliniowe ujawniają ukrytą mechanikę 0‑Matrycy:

1. **Acustoelastyczny pancerz strukturalny:** W pobliżu rdzenia węzła gradient ciśnienia torsyjnego $\nabla(\mathbf{E}^2)$ rośnie asymptotycznie. Człon $\nabla(\mathbf{E}^2) \times \mathbf{B}$ w równaniu (3.4.5) działa jak potężny wtórny **acustoelastyczny prąd wirowy osnowy**: jest to reaktywny (niezdyssypatywny) prąd indukowany przez gradient ciśnienia torsyjnego, który cyrkuluje w sposób stabilizujący rdzeń węzła i zapobiegający jego rozplątaniu. Stanowi on **uzupełniający** mechanizm stabilności, obok topologicznej ochrony wynikającej z liczby splotu $\mathcal{W} \neq 0$ (Rozdział 2.2.2).

2. **Modulacja lokalnej prędkości propagacji:** Człon $\nabla(\mathbf{B}^2) \cdot \mathbf{E}$ w równaniu (3.4.4) modyfikuje lokalną efektywną gęstość ładunku (a więc i lokalną przenikalność), co prowadzi do przestrzennej modulacji prędkości fali w obszarach silnych gradientów naprężeń wirowych. Efekt ten umożliwia samo-ogniskowanie fal elektromagnetycznych w rejonach podwyższonego $B^2$ oraz jest fizycznym źródłem polaryzacyjnej zależności prędkości propagacji (dwójłomność acustoelastyczna): fala spolaryzowana prostopadle do $\mathbf{B}_0$ i fala spolaryzowana równolegle do $\mathbf{B}_0$ napotykają różne wartości $\nabla(B^2)\cdot\mathbf{E}$, co prowadzi do różnicy prędkości rzędu $\kappa^2 B_0^4$ — całkowicie nieobserwowalnej przy $\kappa \lesssim 10^{-6}\ \text{T}^{-2}$.

### 3.4.3. Przybliżenie liniowe i tensor naprężeń Maxwella

Dla słabych pól ($\kappa \mathbf{B}^2 \ll 1$, $\epsilon_0 \kappa \mathbf{E}^2 \ll \mu_0^{-1}$) Lagrangian redukuje się do:

$$\mathcal{L}_{\mathrm{EM}} \approx \frac{1}{2}\epsilon_{\mathrm{eff}} \mathbf{E}^2 - \frac{1}{2\mu_0}\mathbf{B}^2 \tag{3.4.6}$$

Z niego wyprowadzamy kanoniczny tensor energii‑pędu, który po symetryzacji daje **tensor naprężeń Maxwella** $\boldsymbol{\sigma}^{\mathrm{M}}$. W TSM tensor ten reprezentuje fizyczny rozkład gęstości sił sprężystych i parcia kinetycznego wewnątrz 0‑Matrycy:

$$\boldsymbol{\sigma}^{\mathrm{M}} = \epsilon_{\mathrm{eff}}\,\mathbf{E}\otimes\mathbf{E} + \frac{1}{\mu_0}\,\mathbf{B}\otimes\mathbf{B} - u\,\mathbf{I} \tag{3.4.7}$$

Gdzie:
- $\boldsymbol{\sigma}^{\mathrm{M}}$ – tensor naprężeń Maxwella $[\text{N} \cdot \text{m}^{-2}]$,
- $\otimes$ – iloczyn zewnętrzny (tensorowy),
- $\mathbf{I}$ – tensor jednostkowy (macierz Kroneckera),
- $u = \frac{1}{2}\epsilon_{\mathrm{eff}}\mathbf{E}^2 + \frac{1}{2\mu_0}\mathbf{B}^2$ – całkowita gęstość energii sprężystej $[\text{J} \cdot \text{m}^{-3}]$,
- $\epsilon_{\mathrm{eff}}$ – efektywna przenikalność zdefiniowana w (3.3.2).

Równoważna postać składowa tensora potwierdza symetrię:
$$\sigma^{\mathrm{M}}_{ij} = \epsilon_{\mathrm{eff}}\!\left(E_i E_j - \tfrac{1}{2}\delta_{ij}E^2\right) + \frac{1}{\mu_0}\!\left(B_i B_j - \tfrac{1}{2}\delta_{ij}B^2\right)$$

### 3.4.4. Siła Lorentza i prawo Coulomba jako efekty mechaniczne

W klasycznej elektrodynamice siły te są opisane fenomenologicznymi wzorami:
- **Siła Lorentza:** $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$ – opisuje siłę działającą na ładunek $q$ w polu elektrycznym $\mathbf{E}$ i magnetycznym $\mathbf{B}$,
- **Prawo Coulomba:** $F = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2}$ – opisuje oddziaływanie elektrostatyczne między dwoma punktowymi ładunkami.

W TSM oddziaływania te nie są własnością pierwotną „ładunku", lecz wynikiem oddziaływania węzła z polem naprężeń tła. Siłę całkowitą $\mathbf{F}$ $[\text{N}]$ działającą na objętość $V$ wyznaczamy całkując dywergencję tensora naprężeń:

$$\mathbf{F} = \int_V \nabla \cdot \boldsymbol{\sigma}^{\mathrm{M}} \, d^3x \tag{3.4.8}$$

Proces wyprowadzenia gęstości siły $\mathbf{f} = \nabla \cdot \boldsymbol{\sigma}^{\mathrm{M}}$ opiera się na tożsamościach różniczkowych. Dla członu elektrycznego ($\mathbf{E}$):

1. **Rozwinięcie dywergencji iloczynu tensorowego:** $\nabla \cdot (\mathbf{E} \otimes \mathbf{E}) = (\nabla \cdot \mathbf{E})\mathbf{E} + (\mathbf{E} \cdot \nabla)\mathbf{E}$.
2. **Zastosowanie tożsamości wektorowej:** $(\mathbf{E} \cdot \nabla)\mathbf{E} = \frac{1}{2} \nabla E^2 - \mathbf{E} \times (\nabla \times \mathbf{E})$.
3. **Podstawienie równań pola:**
   - Za $\nabla \cdot \mathbf{E}$ podstawiamy $\rho_e / \epsilon_{\text{eff}}$ (Prawo Gaussa).
   - Za $\nabla \times \mathbf{E}$ podstawiamy $-\partial_t \mathbf{B}$ (Prawo Faradaya).

Analogiczne operacje dla członu magnetycznego ($\mathbf{B}$), przy wykorzystaniu $\nabla \cdot \mathbf{B} = 0$ oraz $\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_{\text{eff}} \partial_t \mathbf{E}$ (Prawo Ampère'a‑Maxwella), prowadzą do redukcji gradientu energii całkowitej $\nabla u$. W rezultacie gęstość siły (siła na jednostkę objętości 0‑Matrycy) przyjmuje postać:

$$\mathbf{f} = \nabla \cdot \boldsymbol{\sigma}^{\mathrm{M}} = \rho_e \mathbf{E} + \mathbf{J} \times \mathbf{B} - \frac{\partial \mathbf{g}}{\partial t} \tag{3.4.8b}$$

Gdzie:
- $\mathbf{f}$ – wektor gęstości siły $[\text{N} \cdot \text{m}^{-3}]$,
- $\rho_e$ – gęstość ładunku elektrycznego $[\text{C} \cdot \text{m}^{-3}]$ (miara skręcenia osnowy),
- $\mathbf{J}$ – gęstość prądu elektrycznego $[\text{A} \cdot \text{m}^{-2}]$ (strumień przemieszczeń skrętu),
- $\mathbf{g} = \epsilon_{\mathrm{eff}}(\mathbf{E} \times \mathbf{B})$ – gęstość pędu pola $[\text{kg} \cdot \text{m}^{-2} \cdot \text{s}^{-1}]$, powiązana z wektorem Poyntinga.

Dla trwałego węzła poruszającego się z prędkością $\mathbf{v}$, gdzie $\mathbf{J} = \rho_e \mathbf{v}$, całkujemy gęstość siły po objętości węzła $V$:

$$\mathbf{F} = \int_V \rho_e \mathbf{E} \, d^3x + \int_V (\rho_e \mathbf{v}) \times \mathbf{B} \, d^3x - \frac{d}{dt} \int_V \mathbf{g} \, d^3x \tag{3.4.8c}$$

Przy założeniu stacjonarności pędu pola w układzie własnym węzła ($\partial_t \mathbf{g} \approx 0$) oraz stałości pól $\mathbf{E}, \mathbf{B}$ w skali rozmiaru solitonowego rdzenia, otrzymujemy klasyczną **siłę Lorentza**:

$$\mathbf{F} = q( \mathbf{E} + \mathbf{v}\times\mathbf{B} ) \tag{3.4.9}$$

Gdzie:
- $\mathbf{F}$ – wypadkowa siła mechaniczna działająca na węzeł $[\text{N}]$,
- $q = \int_V \rho_e d^3x$ – całkowity ładunek topologiczny węzła $[\text{C}]$,
- $\mathbf{v}$ – prędkość współrzędnościowa węzła względem 0‑Matrycy $[\text{m} \cdot \text{s}^{-1}]$.

W przypadku elektrostatycznym ($\mathbf{v}=0, \mathbf{B}=0$), oddziaływanie między dwoma węzłami odległymi o $r$ odtwarza **prawo Coulomba**:

$$\mathbf{F}_{12} = \frac{1}{4\pi\epsilon_{\mathrm{eff}}}\frac{q_1 q_2}{r^2}\hat{\mathbf{r}}_{12} \tag{3.4.10}$$

gdzie $\hat{\mathbf{r}}_{12}$ to bezwymiarowy wektor jednostkowy wzdłuż linii łączącej środki węzłów.

### 3.4.5. Odpychanie jednoimiennych ładunków jako interferencja naprężeń

Dwa węzły o zgodnej chiralności (jednoimienne) wytwarzają wokół swoich rdzeni pola torsji (przemieszczeń), których składowe nakładają się konstruktywnie w przestrzeni między nimi. Całkowita gęstość energii sprężystej $u$ w tym obszarze wynosi:

$$u = \tfrac{1}{2}\epsilon_{\mathrm{eff}}|\mathbf{E}_1+\mathbf{E}_2|^2 = u_1 + u_2 + \epsilon_{\mathrm{eff}}\,\mathbf{E}_1 \cdot \mathbf{E}_2 \tag{3.4.11}$$

Człon interferencyjny $\epsilon_{\mathrm{eff}}\,\mathbf{E}_1 \cdot \mathbf{E}_2$ powoduje lokalny wzrost gęstości energii, a co za tym idzie – lokalny wzrost ciśnienia torsyjnego. Zgodnie z zasadą minimalizacji energii potencjalnej, 0‑Matryca generuje siłę $\mathbf{F} \propto -\nabla u$, która wypycha oba sploty na zewnątrz strefy podwyższonej gęstości energii (odpychanie). W przypadku ładunków przeciwnych (przeciwna chiralność), interferencja jest destruktywna – powstaje obszar obniżonego ciśnienia między węzłami, co powoduje ich mechaniczne wciśnięcie ku sobie przez wyższe ciśnienie zewnętrzne niezaburzonej osnowy tła (przyciąganie).

---

## 3.5. Ontologia oddziaływania silnego: Topologiczne splątanie węzłów w czwartym wymiarze

W Standardowym Modelu fizyki cząstek oddziaływanie silne postulowane jest jako niezależna, fundamentalna siła. W ramach Mechaniki Substratu Topologicznego (TSM) podejście to staje się redundantne. Zgodnie z fundamentalnymi ustaleniami Rozdziału 2, cząstki elementarne są 4‑wymiarowymi węzłami topologicznymi – ich struktura rozciąga się również w czwarty wymiar przestrzenny ($x^4$). To właśnie ta własność stanowi źródło oddziaływań jądrowych.

### 3.5.1. Splątanie 4D jako źródło sił jądrowych

Gdy dwa węzły topologiczne (nukleony) znajdą się dostatecznie blisko siebie na 3‑branie (odległość rzędu femtometrów), ich **części zanurzone w czwartym wymiarze mogą ulec bezpośredniemu splątaniu topologicznemu**. Zgodnie z modelem warkoczowym barionów (Rozdział 2.2.3), dochodzi do fizycznego zazębienia się struktur 4D – pasma warkoczy (linie naprężeń) jednego węzła przeplatają się z pasmami drugiego w wyższym wymiarze.

To splątanie (zazębienie warkoczy) generuje dodatkowe, potężne naprężenie w osnowie, które w rzucie na 3‑branę obserwujemy jako **krótkozasięgowe, silne przyciąganie**. Mechanizm ten jest w pełni zgodny z Aksjomatem IV – nie wprowadza żadnej nowej siły, a jedynie wykorzystuje fakt, że węzły są tworami 4D, a sprężystość 0‑Matrycy działa we wszystkich czterech wymiarach.

### 3.5.2. Fenomenologiczny potencjał oddziaływania

Przy geometrycznym nakładaniu się struktur 4D, efektywny potencjał oddziaływania między dwoma węzłami (nukleonami) w rzucie na 3‑branę ma postać:

$$V_{\mathrm{jądrowe}}(r) \approx -V_0\, e^{-r/r_0} \tag{3.5.1}$$

gdzie:
- $r$ – odległość między środkami węzłów na 3‑branie $[\text{m}]$,
- $r_0 \sim 1\ \text{fm}$ – zasięg oddziaływania, równy geometrycznemu zasięgowi nakładania się struktur 4D (wyznacza go głębokość zanurzenia węzła w $x^4$),
- $V_0 \sim 40\ \text{MeV}$ – amplituda potencjału przy pełnym zazębieniu warkoczów (kalibrowana do danych rozpraszania nukleon-nukleon).

Postać ta jest jakościowo zgodna z potencjałem Yukawy i twardą częścią potencjału Woods-Saxona. Dla $r \ll r_0$ (pełne zazębienie) naprężenie osnowy dąży do maksimum, co odpowiada uwięzieniu. Dla $r \gg r_0$ struktura 4D jednego węzła nie sięga drugiego, a oddziaływanie zanika wykładniczo. Parametry $V_0$ i $r_0$ muszą być wyprowadzone z geometrii rozwiązań solitonowych Rozdziału 2 — pełna kalibracja jest przedmiotem odrębnej analizy numerycznej.

### 3.5.3. Wyjaśnienie kluczowych własności oddziaływania silnego

| Własność | Wyjaśnienie w TSM (splątanie topologiczne 4D) |
|---|---|
| **Krótki zasięg ($\sim 1$ fm)** | Splątanie wymaga nałożenia się części węzłów zanurzonych w $x^4$. Poza tą odległością struktury 4D nie zazębiają się – oddziaływanie zanika wykładniczo, zgodnie z (3.5.1). |
| **Wysycenie** | Jeden węzeł może splątać się w 4D tylko z ograniczoną liczbą sąsiadów – wynika to z geometrii zanurzenia (analogia do liczby koordynacyjnej w sieci krystalicznej). |
| **Niezależność ładunkowa** | Splątanie zależy od pełnej geometrii 4D węzła, a nie od jego rzutu 3D (ładunku elektrycznego). Neutron i proton mają podobną strukturę w $x^4$, stąd oddziałują podobnie, mimo różnicy ładunku. |
| **Uwięzienie (confinement)** | Rozplątanie wymagałoby pokonania bariery topologicznej w 4D – energia potrzebna do „przecięcia" splotu jest ogromna. Zamiast uwolnienia, następuje kreacja nowych par węzłów (hadronizacja). |
| **Swoboda asymptotyczna** | Przy ekstremalnym zbliżeniu, części 4D nakładają się tak silnie, że gradienty naprężeń między węzłami ulegają wypłaszczeniu – węzły zachowują się jak gaz swobodny wewnątrz wspólnego worka topologicznego. |

### 3.5.4. Rola nieliniowego EM jako efektu uzupełniającego

Nieliniowe człony elektromagnetyczne wyprowadzone w sekcji 3.4 (w szczególności acustoelastyczny prąd wirowy osnowy $\nabla(\mathbf{E}^2) \times \mathbf{B}$) nie są głównym źródłem sił jądrowych, lecz pełnią rolę **uzupełniającego mechanizmu stabilizującego** pojedyncze węzły. Dodatkowo, w warunkach ekstremalnych gęstości wewnątrz plazmoidów (Rozdział 0.6), nieliniowe efekty EM mogą modulować dynamikę już splątanych układów hadronów.

---

## 3.6. Napięcie i prąd jako mechanika falowa w przewodnikach

Model TSM zastępuje abstrakcyjne przepływy punktów rygorystyczną mechaniką ośrodków ciągłych:

- **Napięcie elektryczne $U$:** Fizyczna różnica ciśnień skręcenia (gradientu potencjału torsyjnego) między dwoma obszarami 0‑Matrycy $[\text{V}]$.
- **Natężenie prądu $I$:** Falowy, konwekcyjny strumień torsji $[\text{A}]$. Sieć jonowa metalu działa jak falowód dla fal torsyjnych. Elektrony (węzły) pełnią rolę kotwic, które przesuwają się powoli (prędkość dryfu $\sim \text{mm/s}$), ale generują sygnał falowy pędzący wzdłuż sieci z prędkością bliską $c_{\perp}$.
- **Opór Ohma i ciepło Joule'a:** Dyssypacja sprężystej energii fali torsyjnej wskutek rozpraszania na niedoskonałościach sieci jonowej, wypromieniowywana jako drgania termiczne (podczerwień i fonony).

---

## 3.7. Inercja elektromechaniczna: Reaktancja i przesunięcia fazowe

Przesunięcia fazowe w obwodach prądu zmiennego wynikają z bezwładności hydrodynamicznej 0‑Matrycy i jej własności elastycznych:

- **Indukcyjność $L$:** Masa efektywna (bezwładność) wirującego pola naprężeń $\mathbf{B}$ $[\text{H}]$. Zmiana kierunku rotacji ośrodka wymaga czasu na przezwyciężenie oporu kinetycznego 0‑cząstek.
- **Pojemność $C$:** Statyczna podatność sprężysta izolatora $[\text{F}]$. Prąd przesunięcia to miara czasowej zmiany gęstości skręcenia (naciągania „sprężyny" dielektryka).

Równanie przesunięcia fazowego:

$$\tan\varphi = \frac{\omega L - \frac{1}{\omega C}}{R} \tag{3.7.1}$$

jest ścisłym makroskopowym bilansem między inercją rotacyjną ($\omega L$), sprężystością ($1/\omega C$) a tarciem falowym ośrodka ($R$).

---

## 3.8. Aplikacje kwantowe: Nadprzewodnictwo i Efekt Halla

- **Nadprzewodnictwo:** W ultraniskich temperaturach szum wibracyjny sieci $T_{\text{sub}}$ ulega minimalizacji. Fermiony o przeciwnych chiralnościach splatają osnowy, formując opływowy węzeł sparowany (soliton pary Coopera). Jego symetryczna topologia ślizga się wewnątrz krystalicznej sieci jonowej bez wzbudzania poprzecznych fal ścinających (dyssypacji), co objawia się zerową rezystancją. Szczegółowy mechanizm parowania (w tym zależność temperatury krytycznej od masy izotopu sieci jonowej) wymaga analizy fonon-soliton i jest przedmiotem odrębnej analizy.
- **Efekt Halla:** Kinetyczne znoszenie toru poruszającego się węzła wymuszone przez zewnętrzny gradient odkształceń wirowych ($\mathbf{B}$). Kwantowy efekt Halla, ujawniający się w układach 2D, odzwierciedla dyskretność stabilnych prążków przestrzennych (stanów solitonowych) w głęboko skwantowanej siatce napięć 0‑Matrycy — powiązanie ze skwantowaną liczbą Cherna pasm energetycznych jest przedmiotem odrębnej analizy.

---

## 3.9. Podsumowanie Rozdziału 3

Sformułowanie pełnych, nieliniowych równań elasto‑dynamicznych 0‑Matrycy pozwoliło na ostateczne domknięcie logiczne klasycznej teorii pól oddziaływań oraz fizyki obwodów. Najważniejsze wnioski:

- **Topologiczna geneza ładunku:** Czteropotencjał $A_\mu$ jest fizycznym polem przemieszczeń ścinających. Skwantowanie ładunku ($q = ne$) to mechaniczny wymóg zamknięcia fazy skrętu o wielokrotność $2\pi$.
- **Mechanizacja równań Maxwella:** $F_{\mu\nu}$ odzwierciedla antysymetryczną część gradientu przemieszczeń sieci. Równania bezźródłowe (3.2.3a,b) są geometrycznymi tożsamościami, wynikającymi z ciągłości 3-brany. Równanie ze źródłami (3.2.4) jest postulatem identyfikacyjnym łączącym dynamikę Naviera-Cauchy'ego z 4-prądem torsji. $\mathbf{E}$ to gradient ciśnienia torsyjnego, $\mathbf{B}$ – wirowość naprężeń ścinających. Brak monopoli magnetycznych wynika z nierozerwalności 3‑brany.
- **Nieliniowa elektrodynamika w układzie spoczynku 0-Matrycy:** Równania Eulera‑Lagrange'a z nieliniowym sprzężeniem magneto-elastycznym $\kappa \approx \mathcal{A}/\mu_s$ opisują acustoelastyczną odpowiedź osnowy. Acustoelastyczny prąd wirowy osnowy $\epsilon_0\kappa\,\nabla(\mathbf{E}^2) \times \mathbf{B}$ tworzy reaktywny pancerz stabilizujący węzły. Kowariantność Lorentza jest emergentną własnością granicy liniowej.
- **Demistyfikacja sił EM:** Siła Lorentza i prawo Coulomba wyprowadzone z dywergencji tensora naprężeń Maxwella. Odpychanie i przyciąganie to wynik interferencji konstruktywnej/destruktywnej pól naprężeń.
- **Oddziaływanie silne jako splątanie 4D:** Siły jądrowe nie są nową siłą, lecz bezpośrednim efektem topologicznego splątania węzłów w czwartym wymiarze. Fenomenologiczny potencjał (3.5.1) odtwarza właściwy zasięg i amplitudę, wyjaśnia wysycenie, niezależność ładunkową i uwięzienie, w pełnej zgodzie z aksjomatami TSM. Kalibracja parametrów $V_0$, $r_0$ do geometrii solitonów jest otwartym zadaniem numerycznym.
- **Hydrodynamiczna teoria obwodów:** Napięcie i prąd zdefiniowane mechanicznie. Indukcyjność to bezwładność pola $\mathbf{B}$, pojemność – podatność dielektryka. Przesunięcie fazowe to bilans inercji, sprężystości i tarcia.
- **Stany kwantowe jako przejścia fazowe:** Nadprzewodnictwo i kwantowy efekt Halla to dynamiczne uporządkowania w siatce napięć 0‑Matrycy przy minimalnym szumie $T_{\text{sub}}$. Szczegółowe mechanizmy parowania solitonowego i topologiczne powiązanie z liczbami Cherna są przedmiotami odrębnych analiz.
