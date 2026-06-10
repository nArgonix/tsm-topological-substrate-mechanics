<!-- ver:2.1.0 -->
# Rozdział 1: Formalizm Mechaniki Substratu Topologicznego – czas emergentny, dynamika i kinematyka relatywistyczna

Zgodnie z aksjomatami sformułowanymi w Rozdziale 0, fundamentalna przestrzeń to 4‑wymiarowa, skończona bańka wypełniona zakleszczonymi 0‑cząstkami. Zanim przejdziemy do opisu oddziaływań i struktur materialnych, konieczne jest rygorystyczne zdefiniowanie czasu oraz dynamiki samej osnowy. Model TSM całkowicie odrzuca koncepcję absolutnego czasu newtonowskiego oraz relatywistycznej czasoprzestrzeni jako bytu pierwotnego. Czas, podobnie jak przestrzeń, jest zjawiskiem w pełni emergentnym.

---

## 1.1. Czas w ujęciu TSM – od lokalnej gęstości osnowy do mierzonego upływu zjawisk

### 1.1.1. Granica poznania – dlaczego szum nie definiuje czasu

0‑Matryca w Stanie Zero nie jest statyczna. Mikroskopijne drgania 0‑cząstek wokół ich położeń równowagi tworzą permanentny, niekoherentny szum termiczny – temperaturę Substratu $T_{\text{sub}}$. Ten chaotyczny szum tła nie dostarcza jednak żadnej regularnej okresowości, niezbędnej do odmierzania upływu zjawisk. Żadna teoria fizyczna nie może zdefiniować czasu, opierając się wyłącznie na niespójnych fluktuacjach – byłoby to błędne koło, w którym „upływu czasu” używa się do określenia, czym jest „upływ”. TSM uznaje tę granicę i nie próbuje konstruować globalnego parametru czasowego z chaotycznych zderzeń 0‑cząstek.

### 1.1.2. Konieczność okresowości – zegar elementarny

Aby w ogóle mówić o czasie, potrzebny jest proces **okresowy** – coś musi cyklicznie wracać do tego samego stanu. W TSM najbardziej fundamentalnym procesem okresowym jest **pełny cykl oscylacji pojedynczej 0‑cząstki wewnątrz jej sfery oddziaływania**. 0‑cząstka, uwięziona w swojej komórce Wignera‑Seitza, nieustannie uderza w jej granice, odbija się i powraca – to ruch ściśle okresowy, wynikający z geometrycznego uwięzienia i zachowania pędu. Czas trwania jednego takiego cyklu w niezakłóconej, płaskiej osnowie nazywamy **elementarnym okresem referencyjnym** $T_0$.

Wartość $T_0$ jest stałą materiałową 0‑Matrycy, związaną z częstotliwością referencyjną $f_0 = 1/T_0$, zdefiniowaną przez średnią statystyczną w Stanie Zero (Rozdział 0.3).

### 1.1.3. Lokalny czas własny – definicja fundamentalna

Cykl oscylacji 0‑cząstki nie jest jednak sztywno ustalony – zależy od lokalnych warunków fizycznych. W obszarach skompresowanych (np. w pobliżu węzła topologicznego) sfera oddziaływania ulega odkształceniu, droga swobodna skraca się, a częstotliwość uderzeń rośnie. Jednak – co kluczowe – **nie ta częstotliwość definiuje upływ czasu**, lecz gęstość upakowania osnowy, która bezpośrednio wpływa na tempo procesów cyklicznych.

Wprowadzamy **lokalny ułamek upakowania** $\phi(\mathbf{x})$, będący stosunkiem objętości zajmowanej przez nieściśliwe jądra 0‑cząstek do całkowitej objętości komórki. W Stanie Zero, w płaskiej, niezakłóconej osnowie, $\phi = \phi_0$ (wartość referencyjna).

Niech w infinitezymalnym obszarze wokół punktu $\mathbf{x}$ elementarny zegar – proces okresowy (np. rotacja wewnętrzna węzła, oscylacja fali stojącej) – wykona $dN$ pełnych cykli. Lokalny przyrost **czasu własnego** definiujemy jako:

$$\boxed{dt(\mathbf{x}) = dN \cdot T_0 \cdot \frac{\phi(\mathbf{x})}{\phi_0}} \tag{1.1.1}$$

gdzie:
- $dt$ – przyrost lokalnego czasu mierzonego w punkcie $\mathbf{x}$,
- $dN$ – liczba pełnych cykli procesu okresowego (bezwymiarowa),
- $T_0$ – elementarny okres referencyjny w płaskiej osnowie $[\text{s}]$,
- $\phi(\mathbf{x})$ – lokalny ułamek upakowania 0‑cząstek (bezwymiarowy, $\phi \in [\phi_0, \phi_{\text{max}}]$),
- $\phi_0$ – referencyjny ułamek upakowania w płaskiej, niezakłóconej osnowie.

**Fizyczna interpretacja:** W gęstszej osnowie ($\phi > \phi_0$) drogi propagacji naprężeń są bardziej poskręcane, efektywna „lepkość” strukturalna rośnie, a każdy proces cykliczny napotyka większy opór. Czas trwania jednego cyklu wydłuża się proporcjonalnie do $\phi/\phi_0$, więc lokalny zegar tyka wolniej. Czas mierzony przez obserwatora w danym punkcie to po prostu całka:

$$t(\mathbf{x}) = T_0 \int \frac{\phi(\mathbf{x})}{\phi_0} \, dN \tag{1.1.2}$$

### 1.1.4. Czas współrzędnościowy brany

W asymptotycznie płaskim obszarze 3‑brany, daleko od wszelkich węzłów topologicznych, $\phi = \phi_0$ jest stałe. Tam wszystkie lokalne zegary tykają w tym samym tempie, definiując **czas współrzędnościowy $t_{\text{flat}}$** – wspólną miarę upływu zjawisk dla całej niezakłóconej brany:

$$dt_{\text{flat}} = dN \cdot T_0 \tag{1.1.3}$$

W obszarach zakrzywionych (w pobliżu mas), gdzie $\phi \neq \phi_0$, lokalny czas własny $dt$ różni się od $t_{\text{flat}}$. Stosunek ten definiuje **czynnik dylatacji czasu**:

$$\frac{dt}{dt_{\text{flat}}} = \frac{\phi(\mathbf{x})}{\phi_0} \tag{1.1.4}$$

Ponieważ w obszarach skompresowanych grawitacyjnie $\phi > \phi_0$, mamy $dt/dt_{\text{flat}} > 1$ – oznacza to, że gdy w płaskiej osnowie upływa 1 sekunda, lokalny zegar wskazuje więcej niż 1 sekundę swojego czasu, czyli **lokalny czas płynie wolniej**. Jest to zgodne z klasyczną dylatacją grawitacyjną.

### 1.1.5. Dylatacja grawitacyjna – związek z potencjałem $\Phi$

W Rozdziale 0.5 określono, że grawitacja to odkształcenie 3‑brany w czwarty wymiar, wywołane obecnością węzłów topologicznych. Odkształcenie to powoduje radialny gradient gęstości upakowania – im bliżej źródła, tym większa kompresja i większe $\phi$.

W słabym polu grawitacyjnym przyjmujemy liniową zależność:

$$\phi(\mathbf{x}) \approx \phi_0 \left(1 + \frac{2 |\Phi(\mathbf{x})|}{c_{\perp}^2}\right) \tag{1.1.5}$$

gdzie $\Phi(\mathbf{x})$ to newtonowski potencjał grawitacyjny ($\Phi \le 0$), a $c_{\perp}$ to prędkość poprzecznych fal ścinających (światła). Podstawiając do (1.1.4):

$$\frac{dt}{dt_{\text{flat}}} \approx 1 + \frac{2 |\Phi|}{c_{\perp}^2} \tag{1.1.6}$$

Daje to poprawne przybliżenie dylatacji grawitacyjnej, zgodne co do znaku i rzędu wielkości z klasyczną formułą OTW.

### 1.1.6. Dylatacja kinematyczna – ruch węzła w osnowie

Rozważmy węzeł topologiczny poruszający się z prędkością $v$ względem osnowy. Zgodnie z mechaniką ośrodków ciągłych, przed poruszającym się obiektem tworzy się front zagęszczenia. Efektywna gęstość wewnątrz węzła rośnie zgodnie z czynnikiem Lorentza:

$$\phi(v) = \frac{\phi_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} = \gamma \phi_0 \tag{1.1.7}$$

gdzie $\gamma = 1/\sqrt{1 - v^2/c_{\perp}^2}$ to czynnik Lorentza.

Podstawiając do (1.1.4):

$$\frac{dt}{dt_{\text{flat}}} = \frac{\phi(v)}{\phi_0} = \gamma \tag{1.1.8}$$

Gdy $v \to c_{\perp}$, $\gamma \to \infty$, a lokalny czas zwalnia – zegar w poruszającym się węźle tyka coraz wolniej. To wyprowadza **dylatację czasu szczególnej teorii względności** bez odwoływania się do czasoprzestrzeni – jest ona bezpośrednią konsekwencją oporu hydrodynamicznego osnowy.

---

## 1.2. Ośrodek i przestrzeń: Globalne zakleszczenie i izotropowa 3‑brana

Mając zdefiniowany czas lokalny, możemy formalnie opisać strukturę przestrzenną. Zgodnie z Rozdziałem 0.3 i 0.5, fundamentalna przestrzeń $\mathcal{M}^4$ jest 4‑wymiarową, skończoną bańką wypełnioną 0‑cząstkami w stanie **globalnego zakleszczenia (jamming)**.

### 1.2.1. Stan globalnego zakleszczenia

W całej objętości $\mathcal{M}^4$ ułamek upakowania przekracza wartość krytyczną:

$$\phi \ge \phi_c \quad \text{(globalnie w 4D)} \tag{1.2.1}$$

0‑cząstki są trwale uwięzione w komórkach Wignera‑Seitza i nie mają swobody translacyjnej. Ośrodek posiada pełny tensor sztywności i może przenosić fale poprzeczne we wszystkich czterech wymiarach. W absolutnym Stanie Zero, przed Wielkim Wydarzeniem, makroskopowe naprężenie ścinające wynosi $\sigma_{ab} = 0$, a jedyną dynamikę stanowi niekoherentny szum termiczny $T_{\text{sub}}$.

### 1.2.2. Izotropowa 3‑brana jako defekt topologiczny

Wielkie Wydarzenie – pierwotne zaburzenie spoza zakresu TSM – spowodowało lokalne plastyczne skręcenie osnowy („przekręcenie bańki”). Powstały trwały defekt topologiczny to właśnie nasza 3‑brana – trójwymiarowa hiperpowierzchnia o wymiarze $D-1 = 3$. Z powodu statystycznego uśredniania kierunków na poziomie makroskopowym, 3‑brana zachowuje się jak idealnie ciągły, izotropowy, nieliniowy ośrodek sprężysty, zdolny do propagacji fal poprzecznych z prędkością $c_{\perp}$ (światło).

Obszar 4D poza 3‑braną pozostaje sztywnym, niezakłóconym szkłem topologicznym. Ponieważ jest idealnie sprężysty i w równowadze, nie generuje żadnych dodatkowych sił działających na branę.

---

## 1.3. Kinematyka nieliniowa: Emergencja metryki $g_{ab}$ z odkształcenia

W TSM metryka przestrzenna $g_{ab}$ nie jest bytem pierwotnym abstrakcyjnej geometrii; jest ona fizycznym rzutem stanu odkształcenia Substratu. W płaskiej, niezakłóconej 3‑branie (daleko od węzłów) ośrodek opisuje płaska metryka euklidesowa $\delta_{ab}$.

Wprowadzamy fizyczne wektorowe pole przemieszczenia osnowy $\phi^a(\mathbf{x})$, opisujące odkształcenie elementu objętości od położenia równowagi. Metryka obserwowalna (Riemanna) wyłania się rygorystycznie z nieliniowych gradientów przemieszczenia:

$$g_{ab} = \delta_{ab} + \nabla_a \phi_b + \nabla_b \phi_a + \delta_{cd} \nabla_a \phi^c \nabla_b \phi^d \tag{1.3.1}$$

gdzie:
- $g_{ab}$ – tensor metryczny (obserwowalna geometria przestrzeni),
- $\delta_{ab}$ – płaska metryka euklidesowa (niezakłócona osnowa),
- $\phi^a$ – wektor przemieszczenia osnowy $[\text{m}]$,
- $\nabla_a$ – pochodna kowariantna w metryce tła $\delta_{ab}$.

Zakrzywienie przestrzeni i wynikająca z niego grawitacja to mechaniczne naciągnięcie lokalnych komórek 0‑cząstek, tworzące makroskopowy gradient gęstości upakowania $\phi$ w stronę czwartego wymiaru przestrzennego.

---

## 1.4. Dynamika falowa Substratu i równania pola

Mechanika Substratu podlega uogólnionemu formalizmowi Lagrange’a. Gęstość lagrangianu $\mathcal{L}$ izotropowej 3‑brany zdefiniowana jest przez jej całkowitą energię sprężystą, wykorzystując tensor modułów sprężystości $K^{abcd}$:

$$\mathcal{L} = \frac{1}{2} K^{abcd} \epsilon_{ab} \epsilon_{cd} + \mathcal{O}(\epsilon^3) \tag{1.4.1}$$

gdzie:
- $\mathcal{L}$ – gęstość lagrangianu $[\text{J} \cdot \text{m}^{-3}]$,
- $K^{abcd}$ – tensor modułów sprężystości $[\text{Pa}]$,
- $\epsilon_{ab}$ – tensor odkształcenia (bezwymiarowy), $\epsilon_{ab} = \frac{1}{2}(\nabla_a \phi_b + \nabla_b \phi_a)$.

Pochodna lagrangianu względem tensora odkształcenia jednoznacznie określa tensor naprężenia:

$$\sigma^{ab} = \frac{\partial \mathcal{L}}{\partial \epsilon_{ab}} = K^{abcd} \epsilon_{cd} \tag{1.4.2}$$

Drobne odkształcenia pola w 3‑branie spełniają równanie falowe w lokalnym czasie współrzędnościowym $t$:

$$\nabla^2 \phi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \phi}{\partial t^2} = \mathcal{S}(\mathbf{x}, t) \tag{1.4.3}$$

gdzie:
- $\nabla^2$ – laplasjan w metryce tła $\delta_{ab}$,
- $c_{\perp}$ – prędkość propagacji poprzecznych fal ścinających (bazowa prędkość światła) $[\text{m} \cdot \text{s}^{-1}]$,
- $\mathcal{S}(\mathbf{x}, t)$ – funkcja źródła, reprezentująca obecność trwałych odkształceń topologicznych (węzłów).

Krzywizna geometryczna $g_{ab}$ jest bezpośrednim odzwierciedleniem tensora naprężenia tła, sprzężonym przez elastyczne stałe materiałowe Substratu.

---

## 1.5. Podwójny reżim elasto‑dynamiki: Fale sprężyste a nieliniowa blokada topologiczna

Wprowadzenie mechanizmu natychmiastowej relaksacji naprężeń poprzez geometryczne sfery odpychania kinetycznego generuje fundamentalny problem dynamiczny: w jaki sposób w idealnie sprężystym ośrodku, który z definicji błyskawicznie rozprasza wszelkie nadmiary ciśnienia, może uformować się i utrzymać stabilna, trwała struktura materialna (cząstka)? Rozwiązanie tego pozornego paradoksu wymaga rygorystycznego rozdzielenia dynamiki Substratu na dwa komplementarne reżimy, rozgraniczone krytycznym progiem ułamka upakowania $\phi_{\text{lock}}$ (progiem zamrożenia topologicznego).

### 1.5.1. Reżim I: Liniowa relaksacja akustyczna ($\phi < \phi_{\text{lock}}$)

Dopóki lokalna kompresja sieci nie przekracza krytycznego progu stabilności geometrycznej klatek Wignera‑Seitza, Substrat zachowuje się jak idealne, liniowe kontinuum sprężyste. W tym stanie:

- Odkształcenia są zachowawcze. Sfery odpychania kinetycznego ulegają deformacji (np. spłaszczeniu), ale 0‑cząstki rygorystycznie zachowują macierz swoich dotychczasowych sąsiadów. Nie dochodzi do zmiany lokalnej topologii sieci.
- Nadmiar efektywnego ciśnienia $P_{\text{eff}}$ jest transferowany symetrycznie na zewnątrz na zasadzie kaskady brzegowej. Ośrodek relaksuje energię poprzez propagację fal poprzecznych z prędkością $c_{\perp}$ oraz fal podłużnych. Rozpraszanie zjawisk zaburzających jest natychmiastowe i całkowite.

### 1.5.2. Reżim II: Nieliniowa blokada topologiczna ($\phi \ge \phi_{\text{lock}}$)

Sytuacja zmienia się drastycznie, gdy na skutek ekstremalnej koncentracji energii (np. megafluktuacji podczas Wielkiego Wydarzenia lub późniejszych katastroficznych zdarzeń) układ zostaje skompresowany poza granicę plastyczności $\phi_{\text{lock}}$.

- Klatki kinetyczne zostają zniekształcone geometrycznie. Zgodnie z aksjomatem absolutnego uwięzienia, 0‑cząstki nie przemieszczają się do innych komórek – zmianie ulega kształt ich sfer oddziaływania.
- Drastycznej deformacji ulega geometryczny kształt klatek. Wektory orientacji naprężeń ulegają lokalnemu skręceniu, co wymusza permanentną rotację kierunku pędu kolizyjnego uwięzionych 0‑cząstek. Zamiast przekazywać pęd na zewnątrz, wektory odkształceń krzyżują się pod niestandardowymi kątami wewnątrz silnie zgniecionego obszaru.
- Następuje kinetyczne ograniczenie swobody sfer oddziaływań w formie splotu: 0‑cząstki uderzają w zdeformowane granice swoich komórek tak intensywnie i z tak zmodyfikowanym kątem padania, że wygenerowane w ten sposób pola naprężeń zapętlają się w samopodtrzymujący się wir. Każda próba powrotu sfery do liniowego stanu geometrycznego jest natychmiast blokowana przez napływający pod kątem pęd sąsiedniej 0‑cząstki, uwięzionej w tej samej lokalnej rotacji wektorów.

W tym reżimie Substrat traci zdolność do uwalniania naprężeń przestrzennych poprzez zwykłą emisję akustyczną. Powstaje nieliniowy splot (soliton), który zyskuje stabilność, ponieważ rozplecenie tego węzła wymagałoby ponownego przejścia układu przez stan ekstremalnej kompresji, co stwarza potężną barierę energetyczną. Paradoks zostaje zażegnany: ośrodek doskonale propaguje fale sprężyste w swojej liniowej granicy, ale trwale więzi energię poprzez deformację kształtu sfer i rotacyjne skręcenie wektorów pędu w granicy topologicznej, dając początek skwantowanej materii.

---

## 1.6. Aksjomat materii: Skwantowane węzły topologiczne i rygorystyczne rozdzielenie masy od ładunku

Pod wpływem ekstremalnej kompresji nieliniowej, w której lokalny ułamek upakowania Substratu przekracza krytyczny próg zamrożenia topologicznego ($\phi(\mathbf{x}) \ge \phi_{\text{lock}}$), liniowe fluktuacje tracą zdolność relaksacji falowej. Wektory pędu szybkich oscylatorów zmuszone są do geometrycznej zmiany macierzy sąsiedztwa i zapętlenia. W 4‑wymiarowym kontinuum formują one stabilne fale stojące (solitony), będące w istocie trwałymi węzłami topologicznymi, które fizyka makroskopowa identyfikuje jako fermiony. Węzły te są **tworami w pełni 4‑wymiarowymi** – ich struktura rozciąga się również w czwarty wymiar, co ma fundamentalne znaczenie dla grawitacji i oddziaływań jądrowych.

### 1.6.1. Matematyczna geneza kwantowania materii

Skwantowany charakter cząstek elementarnych nie jest w TSM założeniem dodanym ad hoc, lecz ścisłym wymogiem aparatury topologii algebraicznej. Stan odkształcenia (skręcenia) klatek kinetycznych opisujemy wektorowym polem orientacji osnowy $\mathbf{n}(\mathbf{x})$ (gdzie $|\mathbf{n}| = 1$). Aby węzeł utrzymywał stabilność, pole $\mathbf{n}$ z dala od rdzenia splotu musi płynnie asymptotycznie dążyć do niezaburzonego, jednorodnego stanu tła. To ograniczenie brzegowe wymusza zamknięcie przestrzeni parametrów na sferze.

Rygorystyczne twierdzenia topologiczne dowodzą, że całka z gęstości takiego przestrzennego skręcenia może przyjmować wyłącznie wartości całkowite. Zjawisko to definiuje niezmienną liczbę splotu (ładunek topologiczny) $\mathcal{W} \in \mathbb{Z}$. Węzeł, który posiada ładunek $\mathcal{W} = 1$, nie może płynnie wypromieniować ułamka swojego splotu, ponieważ wymagałoby to globalnego, makroskopowego rozdarcia ciągłości krystalicznej sieci osnowy. Próg $\phi_{\text{lock}}$ działa jako mechanizm zapłonowy uwięzienia, ale to twarde reguły geometrii sfery wymuszają niepodzielną kwantyzację uformowanego solitonowego defektu.

Dzięki temu fundamentowi, TSM rygorystycznie oddziela pojęcie masy od ładunku:

- **Ładunek elektryczny (Rzut 3D):** Jest bezpośrednio mierzonym strumieniem wektora skrętu fazowego węzła zrzutowanym na płaszczyznę naszej 3‑brany. Ponieważ zamknięty skręt zawsze musi domknąć się do pełnego obrotu fazowego (stanowiąc wielokrotność geometryczną $2\pi$), ładunek ulega absolutnemu skwantowaniu do wartości $\pm 1e$, niezależnie od wewnętrznego skomplikowania węzła w wyższym wymiarze.
- **Masa spoczynkowa (Zanurzenie 4D):** Zdefiniowana jest jako makroskopowy ekwiwalent energii sprężystej zmagazynowanej w napiętej strukturze węzła. Odpowiada ona bezpośrednio głębokości, z jaką uformowany splot wybrzusza ortogonalnie 3‑branę w czwarty wymiar przestrzenny. Wyjaśnia to ostatecznie asymetrię mas: złożony, wielokrotny warkocz topologiczny (proton) wymusza znacznie głębszą deformację 4D i generuje nieporównywalnie silniejszy gradient naprężeń tła niż prosty splot (elektron), mimo posiadania identycznego rzutu ładunku $\pm 1e$.

### 1.6.2. Ruch płynny i asymptotyczne wygaszenie barier dyskretnych

Propagacja materii w przestrzeni nie polega na przepychaniu 0‑cząstek przez ośrodek, lecz na bezstratnym, falowym transferze samego stanu topologicznego splątania przez kolejne sfery oddziaływania.

Rozmiar przestrzenny rdzenia węzła ($L$) drastycznie przewyższa mikroskopowy rozmiar pojedynczej komórki Wignera‑Seitza ($a$). Ta fundamentalna asymetria skal powoduje, że okresowy potencjał oporu sieci krystalicznej ulega uśrednieniu przestrzennemu. Prowadzi to do wykładniczego wygaszenia dyskretnej bariery energetycznej Peierlsa‑Nabarro, określającej minimalną siłę potrzebną do przesunięcia defektu w ciele stałym:

$$E_{PN} \propto \exp\left(-\pi \frac{L}{a}\right) \approx 0 \tag{1.6.1}$$

W rezultacie, tak sformowany węzeł topologiczny ślizga się wewnątrz Substratu w sposób idealnie płynny, bez rozpraszania energii, co rygorystycznie i bezsiłowo realizuje Pierwszą Zasadę Dynamiki Newtona. Wypromieniowanie energii w postaci fal poprzecznych (fotonów) następuje wyłącznie przy odkształceniach węzła wynikających ze zderzeń lub gwałtownego przyspieszenia.

---

## 1.7. Wyprowadzenie kinematyki relatywistycznej z hydro‑elastyczności Substratu

Transformacje Lorentza i zasada $E = mc^2$ są rygorystyczną konsekwencją oporu hydrodynamicznego podczas ruchu fal stojących (węzłów) w gęstym kontinuum. W TSM cała kinematyka relatywistyczna wynika z mechaniki ośrodka i lokalnej natury czasu.

### 1.7.1. Kontrakcja długości

Rozważmy węzeł topologiczny poruszający się wzdłuż osi $x$ z prędkością $v = dx/dt$ względem płaskiej osnowy. Ruch węzła generuje przed sobą front kompresji – efektywna gęstość wewnątrz węzła rośnie zgodnie z (1.1.7). Wprowadzamy współrzędną uciekającą $u = x - vt$. Przekształcenie jednorodnego równania falowego (1.4.3) wymaga przeskalowania osi $x$ w celu zachowania izotropowej formy solitonu:

$$x' = \frac{u}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} = \gamma (x - vt) \tag{1.7.1}$$

Kształt węzła ulega mechanicznej kompresji o czynnik geometryczny $\gamma = 1/\sqrt{1 - v^2/c_{\perp}^2}$ pod wpływem oporu elastycznego kontinuum. Długość mierzona w kierunku ruchu ulega skróceniu: $L' = L / \gamma$.

### 1.7.2. Energia, pęd i masa relatywistyczna

Energia całkowita węzła poruszającego się z prędkością $v$ składa się z energii spoczynkowej (sprężystej deformacji 4D) oraz energii kinetycznej (odpowiedzi osnowy na ruch). Całkowita energia odkształcenia osnowy w obecności poruszającego się węzła wynosi:

$$E = \gamma E_0 = \frac{E_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} \tag{1.7.2}$$

gdzie $E_0 = m_0 c_{\perp}^2$ to energia spoczynkowa węzła w układzie własnym, a $m_0$ to masa spoczynkowa (energia sprężysta splotu w 4D).

Masa relatywistyczna – jako miara całkowitej energii – wynosi:

$$m = \gamma m_0 = \frac{m_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} \tag{1.7.3}$$

Pęd węzła definiujemy jako strumień energii sprężystej w kierunku ruchu:

$$p = \gamma m_0 v \tag{1.7.4}$$

Równanie siły działającej na węzeł wewnątrz osnowy – po uwzględnieniu lokalnego czynnika dylatacji czasu (1.1.8) – ujawnia zjawisko asymptotycznego oporu falowego przy próbie zmiany stanu pędu:

$$F = \frac{dp}{dt} = m_0 \gamma^3 \frac{d^2 x}{dt^2} \tag{1.7.5}$$

Gdy prędkość węzła zbliża się do prędkości fal ścinających ($v \to c_{\perp}$), czynnik $\gamma \to \infty$. Opór falowy osnowy staje się nieskończony, co uniemożliwia solitonowi przekroczenie progu $c_{\perp}$ na płaszczyźnie 3‑brany.

### 1.7.3. Związek energii i pędu – relacja dyspersyjna

Z równań (1.7.2) i (1.7.4) natychmiast wynika relatywistyczna relacja dyspersyjna:

$$E^2 = (pc_{\perp})^2 + (m_0 c_{\perp}^2)^2 \tag{1.7.6}$$

Dla fotonu – fali poprzecznej bez masy spoczynkowej ($m_0 = 0$) – energia i pęd są związane przez $E = pc_{\perp}$, co jest zgodne z klasyczną elektrodynamiką i mechaniką kwantową.

---

## 1.8. Zmienna propagacja fal (lokalne $c_{\perp}$) i stałe materiałowe

Prędkość światła nie jest stałą uniwersalną; wynika bezpośrednio z nieliniowego zjawiska akustoelastyczności gęstego kontinuum. W obszarze poddanym napięciu mechanicznemu ($\Sigma$), lokalna prędkość fal poprzecznych $c_{\perp,\text{lok}}$ modulowana jest przez sztywność nieliniową (stałe Murnaghana $\mathcal{A}$):

$$c_{\perp,\text{lok}}^2 = \frac{\mu}{\rho_0} \left( 1 + \mathcal{A} \Sigma \right) \tag{1.8.1}$$

gdzie:
- $\mu$ – moduł sztywności postaciowej osnowy $[\text{Pa}]$,
- $\rho_0$ – gęstość masy (bezwładnej) 0‑cząstek $[\text{kg} \cdot \text{m}^{-3}]$,
- $\mathcal{A}$ – stała nieliniowości Murnaghana $[\text{Pa}^{-1}]$,
- $\Sigma$ – ślad tensora naprężenia $[\text{Pa}]$.

W zapisie elektrodynamicznym przekłada się to bezpośrednio na efektywną przepustowość Substratu:

$$c_{\perp,\text{lok}} = \frac{1}{\sqrt{\epsilon_{\text{eff}} \mu_0}} \tag{1.8.2}$$

Parametr $\epsilon_{\text{eff}}$ zależy od lokalnych gradientów naprężeń wywołanych polami magnetycznymi lub grawitacyjnym ugięciem w kierunku czwartego wymiaru:

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \kappa B^2 + \lambda \frac{\Phi}{c_{\perp}^2} + \dots\right) \tag{1.8.3}$$

gdzie:
- $\epsilon_0$ – przenikalność elektryczna płaskiej osnowy $[\text{F} \cdot \text{m}^{-1}]$,
- $\kappa$ – stała sprzężenia magneto‑elastycznego $[\text{T}^{-2}]$,
- $\lambda$ – stała sprzężenia grawitacyjnego (bezwymiarowa),
- $\Phi$ – potencjał grawitacyjny $[\text{m}^2 \cdot \text{s}^{-2}]$.

W modelu TSM dotychczasowe bezwymiarowe stałe fizyczne tracą swój abstrakcyjny status, stając się parametrami mechanotermodynamicznymi i stałymi materiałowymi 4‑wymiarowego kontinuum:

- $c_{\perp}$ – prędkość relaksacji poprzecznej w zrelaksowanym, czystym Stanie Zero,
- $\kappa$, $\lambda$ – stałe nieliniowego sprzężenia elasto‑dynamicznego (odpowiednio: magnetyczna i grawitacyjna),
- $\chi$ – stała topologiczna determinująca bazowe napięcie i geometrię uwięzienia węzłów,
- $G_{\text{eff}}$ – efektywna stała grawitacji, zdeterminowana przez globalny stopień relaksowania i gęstość tła Substratu,
- $T_0$, $\phi_0$ – referencyjne stałe czasowe i gęstościowe, definiujące rytm lokalnych zegarów.

---

## 1.9. Podsumowanie Rozdziału 1

- **Czas jako funkcja gęstości osnowy:** Czas absolutny zostaje całkowicie odrzucony. Lokalny czas własny $t$ jest definiowany przez liczbę cykli procesów okresowych, spowalnianych przez gęstość upakowania $\phi$: $dt = dN \cdot T_0 \cdot \phi/\phi_0$. Dylatacja grawitacyjna i kinematyczna wynikają bezpośrednio ze zmian gęstości.
- **Globalne zakleszczenie:** Cała 4‑wymiarowa bańka od początku znajduje się w stanie sztywnego szkła topologicznego. 3‑brana jest trwałym defektem – skręceniem hiperpowierzchni powstałym podczas Wielkiego Wydarzenia.
- **Podwójny reżim dynamiczny:** Rozwiązano paradoks natychmiastowej relaksacji Substratu poprzez wprowadzenie progu zamrożenia topologicznego $\phi_{\text{lock}}$. Poniżej tego progu kontinuum zachowuje się liniowo. Powyżej ($\phi \ge \phi_{\text{lock}}$) dochodzi do nieliniowej blokady, formując trwałe węzły – 4‑wymiarowe solitony.
- **Rygorystyczna kwantyzacja i relatywizm falowy:** Stabilność i skwantowanie fermionów wyprowadzono z niezmienników topologicznych ($\mathcal{W} \in \mathbb{Z}$). Kinematyka relatywistyczna (kontrakcja Lorentza, $E = \gamma m_0 c_{\perp}^2$, bariera $c_{\perp}$) jest bezpośrednią konsekwencją oporu hydrodynamicznego osnowy.
- **Materializacja stałych fizycznych:** Prędkość światła to prędkość poprzecznych fal ścinających ($c_{\perp}$), zależna od lokalnych naprężeń. Fundamentalne stałe ($c, e, G, \epsilon_0$) zyskują status parametrów materiałowych 4‑wymiarowego medium sprężystego.