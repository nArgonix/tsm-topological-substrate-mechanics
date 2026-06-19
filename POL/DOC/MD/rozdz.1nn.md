\setcounter{chapter}{1}

---
<!-- ver:4.0.0 -->
# 1. Elasto-mechanika 0-Matrycy: Emergencja Czasu, Metryki i Kinematyki Relatywistycznej {#sec:rom-tsm}

## Wprowadzenie i ramy konceptualne

Niniejszy rozdział stanowi formalny rdzeń teorii Mechaniki Substratu Topologicznego (TSM), implementując ścisły aparat matematyczno-fizyczny dla jej pojęciowych fundamentów. O ile poprzednie rozważania ugruntowały ontologiczną konieczność istnienia sub-planckowskiego podłoża, o tyle w tym miejscu uwaga zostaje skoncentrowana na matematycznej rekonstrukcji makroskopowych praw fizyki z dynamicznej sieci geometrycznej — 0-Matrycy. Paradygmat TSM kategorycznie odrzuca pojęcie pustej czasoprzestrzeni jako fundamentalnego tła fizycznego. W zamian, za pomocą rygorystycznego aparatu elasto-mechaniki dyskretnej, wykazuje, że czas makroskopowy, efektywna metryka grawitacyjna $g_{ab}$ oraz transformacje relatywistyczne nie są pierwotnymi atrybutami rzeczywistości, lecz zjawiskami wtórnymi (emergentnymi), wyłaniającymi się z uśrednionych stanów naprężeń, odkształceń i konfiguracji topologicznych zablokowanej osnowy 4D.

Sformalizowany wywód zmierzający do rekonstrukcji kontinuum makroskopowego odzwierciedla ścisły ciąg redukcjonistyczny, podzielony na cztery kluczowe etapy:

1. **Architektura podłoża i geneza czasu:** Rozdział otwiera analiza mikrostruktury 0-Matrycy, opartej na sferach oscylacji 0-Cząstek. Przedstawiony zostaje mechanizm ich geometrycznego, globalnego zakleszczenia, który formuje izotropową 3‑branę. Dopiero na tym fizycznym podłożu, poprzez matematyczny formalizm uśredniania fluktuacji stochastycznych, zdefiniowana zostaje Efektywna Gęstość Substratu. Czas makroskopowy zostaje tu wyprowadzony nie jako kontinuum, lecz jako kanoniczna miara sukcesji kolejnych stanów sieci.
2. **Elastodynamika fali i prędkość światła:** Zamiast postulować stałość prędkości światła jako nadrzędny aksjomat, formalizm wyprowadza ją bezpośrednio z właściwości materiałowych osnowy. Prędkość $c$ zostaje zdefiniowana jako prędkość propagacji poprzecznych zaburzeń ścinania w zablokowanej mechanicznie strukturze 4D, a jej lokalna zmienność ($c_{\perp}$) zostaje powiązana ze stałymi materiałowymi sieci.
3. **Emergencja geometrii i kinematyki relatywistycznej:** W sferze kinematyki nieliniowej rozdział dowodzi, że efektywna metryka makroskopowa $g_{ab}$ jest matematycznym opisem lokalnych odkształceń Substratu. W konsekwencji relatywistyczna dylatacja czasu zyskuje czysto mechaniczną interpretację jako izotropowe spiętrzenie (zagęszczenie) osnowy. Pozwala to na pełne wyprowadzenie transformacji relatywistycznych bezpośrednio z praw rządzących elasto-mechaniką zdegenerowanej sieci krystalicznej, bez odwoływania się do postulatów Szczególnej Teorii Względności.
4. **Równania pola i aksjomat materii:** W obszarze dynamiki falowej rozdział asymiluje rozwiązania matematyczne Ogólnej Teorii Względności, jednak bez jej założeń ontologicznych — równania pola stają się tu opisem stanów naprężeń sieci w podwójnym reżimie elastodynamicznym (fale sprężyste kontra nieliniowa blokada). Kulminacją tego opisu jest definicja aksjomatu materii: cząstki zostają sformalizowane jako stabilne konfiguracje solitonowe (lokalne strefy blokady topologicznej). Pozwala to na rygorystyczne, geometryczne rozdzielenie masy (jako lokalnego defektu gęstości osnowy) od ładunku elektrycznego (jako jej skręcenia topologicznego).

</br>

## 1.1. Mikrostruktura 0-Matrycy i stan globalnego zakleszczenia

Punktem wyjścia dla Mechaniki Substratu Topologicznego (TSM) jest całkowite odrzucenie pojęcia pierwotnej, ciągłej czasoprzestrzeni jako fundamentalnego tła fizycznego. Jedyną obiektywną rzeczywistością ontologiczną jest 0-Matryca – zdegenerowana, wibrująca sieć krystaliczna. Wszelkie przejawiane w skali makroskopowej zjawiska relatywistyczne oraz oddziaływania nie stanowią cech samej przestrzeni, lecz są emergentnym rezultatem stanów naprężeń, deformacji oraz dynamiki falowej tej pierwotnej, ukrytej struktury.

### 1.1.1. Geometria sieci: 0-Cząstki w sferach oscylacji jako fundament osnowy

W przeciwieństwie do klasycznych modeli eteru, mikrostruktura 0-Matrycy wykazuje rygorystyczny, quasi-krystaliczny porządek sieciowy, funkcjonując w stanie podstawowym jako sztywne, sprężyste szkło topologiczne w czterowymiarowej przestrzeni euklidesowej Substratu. Na poziomie fundamentalnym pojedyncza 0-Cząstka jest obiektem niepodzielnym o stałej objętości $V_{00}$, uwięzionym topologicznie w przypisanym węźle sieci. Jej objętość spełnia warunek sub-planckowskiej skali:

$$0 < V_{00} \ll V_{\text{Planck}}$$

W reżimie niskich i średnich energii pojedyncze elementy osnowy są pozbawione swobody translacyjnej, co wyklucza zjawiska takie jak makroskopowy przepływ przez ośrodek. 0-Cząstka może wykonywać ruchy wyłącznie wewnątrz ściśle ograniczonej przestrzeni, zdefiniowanej jako komórka konfiguracyjna (sfera oscylacji). Formalnie, jeśli $\mathbf{X}_i$ oznacza statyczne położenie równowagi $i$-tego węzła w 4D, to chwilowe przesunięcie 0-Cząstki $\mathbf{u}_i$ podlega rygorystycznemu ograniczeniu geometrycznemu:

$$|\mathbf{u}_i| = |\mathbf{x}_i - \mathbf{X}_i| \le R_0$$

gdzie $R_0$ stanowi promień sfery w stanie pełnej relaksacji 0-Matrycy. Granica tej sfery nie jest barierą potencjału w sensie kwantowym, lecz twardym ograniczeniem topologicznym, wynikającym z maksymalnego geometrycznego upakowania i fizycznego sąsiedztwa innych stref w zdegenerowanej sieci.

#### 1.1.1.1. Mikrodynamika komórki: Mechanizm bilardu Sinaja

Geometria komórki konfiguracyjnej determinuje unikalny charakter wewnętrznego ruchu 0-Cząstki. Jej ścianek nie tworzy gładka, pusta wnęka, lecz wypukłe sfery oddziaływań sąsiednich 0-Cząstek. Ruch w obszarze ograniczonym takimi wypukłymi przeszkodami rozpraszającymi klasyfikowany jest jako bilard Sinaja (model matematyczny gazu Lorentza).

W odróżnieniu od bilardu o gładkich ściankach (np. całkowalnego ruchu w pustej sferze omijającego środek), bilard rozpraszający tego typu wykazuje silną własność mieszania oraz pełną ergodyczność. Niezależnie od warunku początkowego, rozkład przestrzenny obecności cząstki zbiega wykładniczo szybko do jednorodnego rozkładu równowagowego na całej dostępnej objętości komórki. Ruch ten jest ściśle deterministyczny, lecz stochastycznie nieprzewidywalny dla obserwatora makroskopowego ze względu na sub-planckowską skalę przestrzenną.

#### 1.1.1.2. Emergencja makroskopowej tarczy sferycznej

Kluczowym czynnikiem transformującym tę mikrodynamikę w stabilne struktury makroskopowe jest asymetria skal czasowych. Częstotliwość oscylacji 0-Cząstki, wyrażona w wirtualnych sekundach, przewyższa o dziesiątki rzędów wielkości makroskopowo rozróżnialne jednostki czasu. Czas potrzebny na osiągnięcie pełnego wymieszania przestrzennego z perspektywy czasu emergentnego jest praktycznie zerowy.

0-Cząstka nie "przemierza" więc swojej sfery w obserwowalnym czasie; wypełnia ją swoją fizyczną obecnością niemal natychmiastowo. Z zewnątrz ta ultraszybka oscylacja manifestuje się jako dynamiczna, nieprzenikalna tarcza o idealnej symetrii sferycznej. Ustanawia to ścisły podział na chaotyczną dynamikę wewnętrzną a uśrednione zjawiska makroskopowe, gdzie lokalna gęstość osnowy jest pochodną zagęszczenia tych sfer.

#### 1.1.1.3. Reżim krytyczny i Klauzula Krytycznego Przemieszczenia

Stan fundamentalnego uwięzienia ulega zmianie wyłącznie w warunkach krytycznych – pod wpływem ekstremalnego ciśnienia zewnętrznego lub silnego skręcenia topologicznego. Gdy lokalne naprężenia ścinające przekroczą krytyczny próg plastyczności, aktywacji ulega Klauzula Krytycznego Przemieszczenia.

Ponieważ asymptotyczna bariera siłowa zabrania fizycznego kontaktu rdzeni, proces ten jest ściśle kolektywny. Przemieszczenie realizowane jest jako sprzężony, synchroniczny przesuw klastra 0-Cząstek w formie fali solitonowej, wykorzystujący obszary rozrzedzenia do kompensacji naporu. Elementy sieci fizycznie zmieniają pozycję (zyskują nową topologię sąsiedztwa) bez naruszania minimalnej odległości międzycząstkowej. W momencie spadku naprężeń poniżej progu, 0-Cząstki natychmiast odzyskują sfery oddziaływań i powracają do stanu uwięzionych mikro-oscylacji, zamykając proces rearanżacji.

### 1.1.2. Mechanizm globalnego zakleszczenia i wyłonienie izotropowej 3‑brany

Stanem bazowym 0-Matrycy, umożliwiającym zaistnienie obserwowalnego świata, jest stan **globalnego zakleszczenia** (*structural jamming*). Przy osiągnięciu krytycznej gęstości upakowania $\phi \ge \phi_c$, niezależne stopnie swobody 0-Cząstek zostają wzajemnie zablokowane przez siły kontaktu topologicznego w czterech wymiarach przestrzennych.

W wyniku tego izotropowego zakleszczenia, nieliniowe oddziaływania prowadzą do wyłonienia stabilnej, trójwymiarowej hiperpowierzchni – izotropowej 3-brany (obszaru lokalnego ugięcia wywołanego zaburzeniem w Stanie Zero). Dla obserwatora wewnętrznego 3-brana jawi się jako trójwymiarowa metryka. Makroskopowy tensor naprężeń sieci w stanie czystego zakleszczenia ma postać:

$$T_{IJ}^{(0)} = -P_0 \delta_{IJ}$$

gdzie $I,J \in \{1,2,3,4\}$, a $P_0$ oznacza izotropowe ciśnienie zakleszczenia w przestrzeni 4D. Idealna symetria tensora maskuje dyskretną naturę matrycy przed przyrządami pomiarowymi.


</br>


### 1.2. Emergencja czasu makroskopowego z dynamiki sub-planckowskiej

#### 1.2.1. Granica poznania i eliminacja fluktuacji stochastycznych

W stanie podstawowym 0-Matryca charakteryzuje się permanentnymi, mikroskopijnymi drganiami cząstek osnowy wokół położeń równowagi. Zjawisko to, opisywane w mikroskali jako bilard Sinaja (patrz rozdz. 1.1.1.1), generuje niekoherentny szum tła definiowany jako fundamentalna temperatura Substratu ($T_{\text{sub}}$). Zgodnie z zasadą rygoru empirycznego, model TSM kategorycznie odrzuca próbę definiowania czasu makroskopowego poprzez te pierwotne, chaotyczne oscylacje.

Wszelkie efekty falowe oraz lokalne zmiany częstotliwości zachodzące bezpośrednio na pojedynczych elementach sieci mają charakter sub-planckowski — zachodzą poniżej granicy skali Plancka ($\sim 10^{-35}$ m) — i są stochastycznie nieprzewidywalne. Próba ich operacyjnego definiowania z makroskopowego punktu widzenia jest pozbawiona sensu mierzalnego. Z tego względu model TSM rezygnuje z postulowania mikroskopijnych zależności kinematycznych pojedynczych 0-Cząstek, przenosząc cały ciężar formalizmu na makroskopowe uśrednianie elasto-mechaniczne zdegenerowanej sieci krystalicznej.

#### 1.2.2. Matematyczny formalizm uśredniania – Efektywna Gęstość Substratu

Kluczowym parametrem wiążącym dyskretną dynamikę sieci z obserwowalną rzeczywistością makroskopową jest fundamentalna gęstość upakowania 0-Cząstek, zdefiniowana jako ciągłe pole w pełnej, 4-wymiarowej przestrzeni Substratu: $\phi(\mathbf{X}) = \phi(x^1, x^2, x^3, x^4)$. Operator uśredniania makroskopowego wygładza lokalne, nieciągłe anomalie gęstości wokół pojedynczych komórek sieci z wykorzystaniem splotu z funkcją okna $W$ o skali odcięcia równej skali Plancka ($\Lambda_{\text{Planck}}$):

$$\langle\phi(\mathbf{X})\rangle_{\text{macro}} = \int_{\mathbb{R}^4} \phi(\mathbf{X}') \, W(\mathbf{X} - \mathbf{X}', \Lambda_{\text{Planck}}) \, d^4\mathbf{X}'$$

 {#eq-1-2-1}

gdzie:

* $\mathbf{X} = (x^1, x^2, x^3, x^4)$ – 4-wektor pozycji w przestrzeni euklidesowej 0-Matrycy,
* $\phi(\mathbf{X}')$ – surowa, mikroskopijna gęstość lokalna osnowy w pełnej przestrzeni 4D,
* $W$ – normalizowana, 4-wymiarowa funkcja przejścia (okno filtracyjne) eliminująca szum sub-planckowski,
* $\Lambda_{\text{Planck}}$ – przestrzenna skala odcięcia.

Ponieważ wszystkie fizyczne przyrządy pomiarowe (zegary, detektory) są uformowanymi węzłami topologicznymi uwięzionymi wewnątrz zakleszczonej 3-brany, bezpośrednio dostępna eksperymentalnie jest wyłącznie wartość $\langle\phi(\mathbf{X})\rangle_{\text{macro}}$ zrestryktowana do tej hiperpowierzchni. W stanie niezakłóconym brana zajmuje hiperpowierzchnię $x^4 = 0$, natomiast w obecności lokalnych odkształceń i naprężeń jest ugięta do pozycji $x^4 = w(\mathbf{x})$. Obserwowalna makroskopowa gęstość upakowania w rzutowanym punkcie przestrzeni trójwymiarowej $\mathbf{x} = (x^1, x^2, x^3)$ wyraża się zatem rzutem:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} \equiv \left.\langle\phi(\mathbf{X})\rangle_{\text{macro}}\right|_{x^4 = w(\mathbf{x})}$$

 {#eq-1-2-2}

Dla zachowania pełnej informacji o stanie środowiska 4D wewnątrz ugiętej hiperpowierzchni, przyjmujemy, że funkcja okna $W$ jest matematycznie separowalna względem składowych brany i wymiaru ortogonalnego: $W(\mathbf{X}-\mathbf{X}', \Lambda_{\text{Planck}}) = W_3(\mathbf{x}-\mathbf{x}', \Lambda_{\text{Planck}}) \cdot W_4(x^4 - \xi, \Lambda_{\text{Planck}})$. Pozwala to zdefiniować efektywną gęstość powierzchniową 3D jako całkę ważoną funkcją $W_4$ wzdłuż osi ortogonalnej $\xi$ (odpowiadającej współrzędnej $x^4$):

$$\phi_{\text{eff}}(\mathbf{x}') \equiv \int_{-\infty}^{+\infty} \phi(\mathbf{x}', \xi) \, W_4\!\left(w(\mathbf{x}') - \xi, \, \Lambda_{\text{Planck}}\right) d\xi$$

 {#eq-1-2-3}

Ponieważ charakterystyczna grubość 3-brany w kierunku ortogonalnym jest rzędu skali Plancka, a funkcja $W_4$ rygorystycznie eliminuje wkłady spoza tego zakresu, całkowanie jest asymptotycznie zlokalizowane w otoczeniu planckowskim brany. Wyniki mierzalne pozostają niezależne od stanu głębokich struktur 0-Matrycy poza tą strefą. Ostateczna, operacyjna forma efektywnej gęstości makroskopowej na 3-branie przyjmuje postać splotu trójwymiarowego:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} = \int_{\mathbb{R}^3} \phi_{\text{eff}}(\mathbf{x}') \, W_3(\mathbf{x} - \mathbf{x}', \Lambda_{\text{Planck}}) \, d^3\mathbf{x}'$$

 {#eq-1-2-4}

W płaskiej, niezakłóconej geometrycznie 3-branie ($w \equiv 0$, gdzie gęstość $\phi$ jest jednorodna w skali planckowskiej wzdłuż czwartego wymiaru) zachodzi tożsamość $\phi_{\text{eff}}(\mathbf{x}') \equiv \phi(\mathbf{x}', 0)$, a całe sformułowanie redukuje się do standardowego splotu gęstości osnowy w przestrzeni trójwymiarowej.

**Uwaga o spójności grawitacyjno-temporalnej:** Zależność efektywnej gęstości $\phi_{\text{eff}}$ od funkcji ugięcia brany $w(\mathbf{x})$ poprzez argument jądra $W_4$ stanowi bezpośrednie, mechanistyczne uzasadnienie dla zjawiska grawitacyjnej dylatacji czasu. Węzeł topologiczny (masywny obiekt) indukujący ugięcie $w > 0$ lokalnie przesuwa punkt próbkowania funkcji $W_4$ w obszar osnowy o wyższym ciśnieniu strukturalnym. Podnosi to wartość $\langle\phi(\mathbf{x})\rangle_{\text{macro}}$ i w konsekwencji zwalnia bieg lokalnego czasu własnego zgodnie z relacją kanoniczną.

#### 1.2.3. Kanoniczna definicja czasu makroskopowego jako miary sukcesji stanów sieci

W mechanice TSM czas nie jest pierwotnym, niezależnym wymiarem ani autonomiczną areną ewolucji układów. Czas mierzony makroskopowo przez dowolne przyrządy pomiarowe — które same stanowią makroskopowe struktury złożone z sieci węzłów topologicznych — jest wyłącznie parametrem operacyjnym sukcesji zmian strukturalnych. Jego tempo upływu pozostaje ściśle i odwrotnie proporcjonalne do efektywnej gęstości elasto-mechanicznej osnowy.

Przyrost lokalnego czasu własnego $dt$ wyraża się równaniem kanonicznym:

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi(\mathbf{x})\rangle_{\text{macro}}}$$

 {#eq-1-2-5}

gdzie:

* $dt$ – przyrost lokalnego czasu własnego, wyrażony w sekundach `[s]`,
* $dN$ – liczba zarejestrowanych cykli makroskopowego procesu okresowego (np. oscylacji atomowych w zegarze),
* $T_0$ – okres referencyjny tegoż procesu zachodzącego w niezaburzonej, stacjonarnej osnowie,
* $\phi_0$ – podstawowa, izotropowa gęstość upakowania 0-Matrycy w Stanie Zero (przestrzeń płaska),
* $\langle\phi(\mathbf{x})\rangle_{\text{macro}}$ – uśredniona elasto-mechanicznie lokalna gęstość osnowy w obszarze zajmowanym przez układ pomiarowy.

Mechanizm dylatacji czasu wynika bezpośrednio z kinematyki stanu zakleszczenia strukturalnego (*structural jamming*). Lokalny wzrost gęstości komórek osnowy ($\langle\phi(\mathbf{x})\rangle_{\text{macro}} > \phi_0$) generuje proporcjonalnie wyższy opór elasto-mechaniczny sieci. Silniejsze upakowanie geometryczne drastycznie ogranicza swobodę wibracyjną uwięzionych 0-Cząstek, co spowalnia transfer energii, propagację sygnałów oraz wszelkie wewnętrzne procesy relaksacyjne układu fizycznego.

Dla stałej liczby cykli mikroskopowych $dN$ przyrost czasu własnego $dt$ ulega zmniejszeniu. Z perspektywy zewnętrznego obserwatora referencyjnego lokalna sekunda ulega fizycznemu rozciągnięciu (staje się dłuższa), ponieważ aparat matematyczny TSM w sposób rygorystyczny wiąże tempo sukcesji stanów sieci z mianownikiem operatora interwału czasowego.

</br>

## 1.3. Elastodynamika sieciowa i mikroskopowa geneza prędkości światła

Aby wyeliminować metodologiczny zarzut wprowadzenia bariery prędkości falowej $c$ jako założenia ad hoc, model TSM wyprowadza stałą prędkość światła (identyfikowaną jako prędkość poprzecznych fal ścinających $c_{\perp} \equiv c$) jako wielkość emergentną. Wyprowadzenie to realizowane jest dwuetapowo: poprzez rygorystyczny opis kontinuum elasto-dynamicznego, a następnie sprzężenie go z sub-planckowską kinetyką 0-cząstek.

### 1.3.1. Propagacja zaburzeń ścinania w zablokowanej osnowie 4D

Rozpatrzmy stan podstawowy Substratu przed sformowaniem brany. Jako 4-wymiarowy, izotropowy ośrodek sprężysty o gigantycznym zagęszczeniu kolizyjnym, 4-Matryca podlega uogólnionym równaniom Naviera-Cauchy’ego dla przemieszczeń $\mathbf{u}(x^1, x^2, x^3, x^4)$. Wprowadzamy 4-wymiarowy tensor odkształceń Cauchy’ego-Greena w postaci:

$$u_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x^j} + \frac{\partial u_j}{\partial x^i} + \frac{\partial u_k}{\partial x^i} \frac{\partial u_k}{\partial x^j} \right)$$ {#eq:tensor-odkształceń}

Gdzie indeksy $i, j, k \in \{1, 2, 3, 4\}$. Zakładając liniowy reżim sprężysty (w którym nieliniowe gradienty kwadratowe są pomijalne przed przekroczeniem progu blokady topologicznej), gęstość energii sprężystej $\mathcal{U}$ dana jest klasycznym wzorem Lamégo rozszerzonym do 4 wymiarów:

$$\mathcal{U} = \frac{1}{2} \lambda (u_{kk})^2 + \mu u_{ij} u_{ij}$$ {#eq:energia-sprężysta}

Gdzie $\lambda$ oraz $\mu$ to makroskopowe współczynniki Lamégo charakteryzujące odpowiednio sprężystość objętościową (opór przeciw ściskaniu) oraz sprężystość postaciową (opór przeciw ścinaniu) Substratu. Równanie ruchu elementu objętości osnowy w czasie płaskiego tła $t_{\text{flat}}$ przyjmuje postać:

$$\rho_{\text{eff}} \frac{\partial^2 u_i}{\partial t_{\text{flat}}^2} = (\lambda + \mu) \frac{\partial u_k}{\partial x^i \partial x^k} + \mu \frac{\partial^2 u_i}{\partial x^k \partial x^k}$$ {#eq:rownanie-ruchu}

Gdzie $\rho_{\text{eff}}$ to efektywna makroskopowa gęstość falowa 4-Matrycy. Stosując rozkład Helmholtza na składową podłużną ($\nabla \cdot \mathbf{u}$) oraz poprzeczną ($\nabla \times \mathbf{u}$), wyodrębniamy prędkość propagacji fali poprzecznej (ścinającej):

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_{\text{eff}}}}$$ {#eq:predkosc-poprzeczna}

Ponieważ 3-brana jest zdefiniowana jako makroskopowe skręcenie uwięzione wzdłuż czwartego wymiaru ($x^4$), wszelkie interakcje elektromagnetyczne w naszym świecie są falami poprzecznymi tej struktury. Prędkość $c_{\perp}$ jest zatem tożsama z prędkością światła $c$ w próżni. Wektor falowy $\mathbf{k} = (k_1, 0, 0, k_4)$ prowadzi do relacji dyspersyjnej $\omega^2 = c_{\perp}^2 (k_1^2 + k_4^2)$. Maksymalna prędkość rzutu fali poprzecznej na obserwowalną przestrzeń 3D zachodzi dla $k_4 = 0$ i wynosi dokładnie $c_{\perp}$.

#### 1.3.1.1 Dynamiczny opór relaksacyjny i sprzężenie skal prędkości

Równanie ({@eq:predkosc-poprzeczna}) opisuje zachowanie fali w makroskali, jednak moduł ścinania $\mu$ oraz efektywna bezwładność $\rho_{\text{eff}}$ nie są stałymi fundamentalnymi, lecz wyłaniają się z mikroskopowej kinetyki 0-cząstek. Kluczem do sprzężenia absolutnej prędkości sub-planckowskiej $v$ ze stałą makroskopową $c_{\perp}$ jest potężna dysproporcja skal geometrycznych.

Zdefiniujmy bezwymiarowy stosunek $\xi$ między stałą sieci osnowy $a$ (skala sub-Planckowska, $a < 1{,}6 \times 10^{-35}$ m) a długością fali mierzalnego zaburzenia makroskopowego $\lambda$:

$$\xi = \frac{a}{\lambda} \ll 1$$

| Rodzaj promieniowania | Przykładowa $\lambda$ | Górne ograniczenie $\xi \leq l_P/\lambda$ |
| --- | --- | --- |
| Radiowa | $\sim 1$ m | $\lesssim 2 \times 10^{-35}$ |
| Widzialna | $\sim 5 \times 10^{-7}$ m | $\lesssim 3 \times 10^{-29}$ |
| Rentgenowska | $\sim 10^{-10}$ m | $\lesssim 2 \times 10^{-25}$ |

Niezależnie od pasma widma, parametr $\xi$ spełnia rygorystycznie $\xi \ll 1$. Pojedyncza komórka Wignera-Seitza o objętości $V_{4D} \sim a^4$ nie doświadcza makroskopowego ugięcia fali jako zjawiska kierunkowego w sposób natychmiastowy.

Zgodnie z Aksjomatem II, w stanie izotropowym (niezaburzonym) energia kinetyczna 0-cząstek, poruszających się z prędkością $v$, jest rozłożona równomiernie na 4 stopnie swobody przestrzennej. Z ekwipartycji pędu wynika, że moduł sprężystości postaciowej (ścinania) $\mu$ jest wprost proporcjonalny do pierwotnej gęstości statycznej tła $\rho_0$ oraz wariancji prędkości ortogonalnej do kierunku rozchodzenia się fali:

$$\mu = \rho_0 \langle v_{\perp}^2 \rangle = \rho_0 \frac{v^2}{4}$$

Gdy fala makroskopowa wymusza koherentne przemieszczenie, komórki 4D stawiają opór o charakterze bezwładności żyroskopowej. Ultra-szybkie oscylacje w 4 osiach działają jak stabilizator położenia. Front fali wymusza zmianę stanu tych oscylacji, co napotyka na opór wynikający z konieczności kaskadowej redystrybucji pędu. Powoduje to, że efektywna gęstość bezwładna $\rho_{\text{eff}}$, jaką „widzi” fala, jest zwielokrotniona względem gęstości statycznej tła $\rho_0$.

Definiujemy makroskopowy parametr dynamicznego tłumienia geometrycznego $\Gamma_{4D}$:

$$\Gamma_{4D} \equiv \frac{v}{2c_{\perp}}$$

Określa on, że efektywna masa bezwładna w równaniu falowym rośnie z kwadratem tego uwięzionego, żyroskopowego oporu tła:

$$\rho_{\text{eff}} = \rho_0 \cdot \Gamma_{4D}^2$$

#### 1.3.1.2 Weryfikacja spójności kinetyki z continuum.
Aby sprawdzić, czy kinetyczne postulaty stanu podstawowego są zgodne z makroskopowym równaniem falowym, podstawiamy relacje powyżej do wzoru na $c_{\perp}$:

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_{\text{eff}}}} = \sqrt{\frac{\rho_0 \frac{v^2}{4}}{\rho_0 \Gamma_{4D}^2}} = \sqrt{\frac{v^2}{4 \Gamma_{4D}^2}} = \frac{v}{2\Gamma_{4D}}$$

Podstawiając definicję $\Gamma_{4D}$, uzyskujemy:

$$c_{\perp} = \frac{v}{2 \left( \frac{v}{2c_{\perp}} \right)} = c_{\perp}$$

Tożsamość zostaje spełniona w sposób absolutnie ścisły i matematycznie zamknięty. Prędkość fali na 3-branie staje się bezwzględnie zablokowana przez stosunek $v/\Gamma_{4D}$. Zgodnie z aksjomatem dynamiki sub-planckowskiej, pierwotne oscylacje zachodzą z prędkością $v \gg c_{\perp}$. Wniosek jest rygorystyczny: w czasie, gdy front fali makroskopowej przemieszcza się o jeden sub-planckowski skok $a$, pierwotne 0-cząstki wykonują $\Gamma_{4D}$ cykli zderzeniowych. Ośrodek stawia tak gigantyczny żyroskopowy opór bezwładny, że prędkość propagacji zaburzeń (światła) zwalnia do wielkości minimalnej w stosunku do pierwotnej dynamiki substratu.

#### 1.3.1.3 Zachowawczy charakter propagacji falowej i brak dyssypacji energii
Zdefiniowanie potężnego oporu żyroskopowego rodzi zasadnicze pytanie: w jaki sposób w medium zdominowanym przez procesy kaskadowych kolizji stabilność energetyczna fali nie ulega natychmiastowej dyssypacji na ciepło? Model TSM eliminuje dyssypację poprzez dwa warunki ontologiczne:

1. **Brak sub-poziomu strukturalnego:** Zderzenia 0-cząstek są twarde, niepodzielne i bezwzględnie sprężyste. Ponieważ nie istnieje "wnętrze" 0-cząstki, energia nie ma jak ulec termalizacji do niższych wymiarów czy wewnętrznego tarcia.
   
2. **Czysto reaktywny charakter impedancji sieci:** Komórki sieciowe działają jak geometryczny akumulator energii. Na przednim zboczu fali pochłaniają pęd makroskopowy, na tylnym w pełni i bezstratnie go oddając.

Całkowity bilans energetyczny transferu pędu w jednym pełnym cyklu falowym wynosi dokładnie zero. Dlatego też redshift obserwowany w kosmologii nie jest efektem tarcia fotonu o osnowę, lecz wynika ze zmiennej, uśrednionej gęstości substratu.

#### 1.3.1.4 Status fali podłużnej: Superluminalne fale gęstości 4D i fluktuacje czasu

Rozkład Helmholtza ujawnia istnienie drugiego modu – fali podłużnej (dylatacyjnej), której prędkość wynosi:

$$c_{\parallel} = \sqrt{\frac{\lambda + 2\mu}{\rho_{\text{eff}}}}$$

Komórki kinetyczne stawiają potężny opór przeciwko ściskaniu objętościowemu ($\lambda \gg \mu$), w efekcie $c_{\parallel} \gg c_{\perp}$. Fizyczna manifestacja tej fali uwięzionej na 3-branie polega na chwilowych, przestrzennych oscylacjach ułamka upakowania osnowy ($\phi$). Zgodnie z równaniem kanonicznym czasu, lokalna zmiana gęstości wprost determinuje tempo procesów fizycznych. Fale podłużne rozchodzące się w 0-Matrycy to sub-planckowskie **fale dylatacji czasu**, niewidoczne dla detektorów EM, lecz generujące tło szumu kwantowego.

### 1.3.2. Stałe materiałowe osnowy a lokalna zmienność propagacji fal ($c_{\perp}$)

Prędkość światła nie jest stałą uniwersalną; wynika bezpośrednio z nieliniowego zjawiska akustoelastyczności gęstego kontinuum. W obszarze poddanym napięciu mechanicznemu ($\Sigma$), lokalna prędkość fal poprzecznych $c_{\perp,\text{lok}}$ modulowana jest przez sztywność nieliniową (stałe Murnaghana $\mathcal{A}$):

$$c_{\perp,\text{lok}}^2 = \frac{\mu}{\rho_0} \left( 1 + \mathcal{A} \Sigma \right)$$ {#eq:zmienność-c}

W zapisie elektrodynamicznym przekłada się to na efektywną przepustowość Substratu:

$$c_{\perp,\text{lok}} = \frac{1}{\sqrt{\epsilon_{\text{eff}} \mu_0}}$$

Parametr $\epsilon_{\text{eff}}$ zależy od lokalnych gradientów naprężeń wywołanych polami magnetycznymi lub grawitacyjnym ugięciem w kierunku czwartego wymiaru:

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \kappa B^2 + \lambda \frac{\Phi}{c_{\perp}^2} + \dots\right)$$

W modelu TSM dotychczasowe bezwymiarowe stałe fizyczne tracą swój abstrakcyjny status, stając się parametrami mechanotermodynamicznymi i stałymi materiałowymi 4‑wymiarowego kontinuum (np. $\kappa, \lambda$ jako stałe nieliniowego sprzężenia elasto-dynamicznego).

<br>

## 1.4. Kinematyka nieliniowa i emergencja efektywnej geometrii makroskopowej

W mechanice TSM metryka przestrzenna $g_{ab}$ nie jest bytem pierwotnym abstrakcyjnej geometrii; stanowi ona wyłącznie fizyczny i matematyczny rzut stanu odkształcenia elasto-mechanicznego Substratu. Całkowicie eliminujemy pojęcie unifikującej czasoprzestrzeni – w opisie makroskopowym mamy do czynienia wyłącznie z uśrednioną geometrią przestrzenną 3-brany, na którą rzutują dynamiczne naprężenia zdegenerowanej sieci krystalicznej 4D.

### 1.4.1. Wyłonienie efektywnej metryki $g_{ab}$ z lokalnych odkształceń Substratu

W płaskiej, niezakłóconej 3-brane (w dużej odległości od węzłów topologicznych) ośrodek charakteryzuje się płaską metryką euklidesową $\delta_{ab}$. Wprowadzamy fizyczne wektorowe pole przemieszczenia osnowy $u(\mathbf{x})$, które opisuje lokalne odkształcenie elementu objętości sieci od jego położenia równowagi. Obserwowalna makroskopowo metryka Riemanna wyłania się rygorystycznie z nieliniowych gradientów tego przemieszczenia:

$$g_{ab} = \delta_{ab} + \nabla_a u_b + \nabla_b u_a + \delta_{cd} \nabla_a u_c \nabla_b u_d$$

 {#eq-1-4-1}

gdzie:

* $g_{ab}$ – tensor metryczny stanowiący obserwowalną geometrię przestrzeni,
* $\delta_{ab}$ – płaska metryka euklidesowa niezakłóconej sieci tła,
* $u$ – wektor fizycznego przemieszczenia osnowy Substratu,
* $\times$ – pochodna kowariantna zdefiniowana w metryce tła $\delta_{ab}$.

Wszelkie zakrzywienia przestrzeni oraz wynikające z nich zjawiska grawitacyjne są w ten sposób bezpośrednim skutkiem mechanicznego naciągnięcia układu komórek 0-Cząstek. Generuje to makroskopowy gradient efektywnej gęstości upakowania $\phi$ skierowany w stronę czwartego, ortogonalnego wymiaru przestrzennego $x^4$.

#### 1.4.2. Kinematyczna dylatacja czasu jako izotropowe spiętrzenie osnowy

Ruch struktury makroskopowej (węzła) nie polega na przepychaniu materii przez ośrodek, lecz na propagacji samej deformacji topologicznej poprzez zdegenerowaną, wibrującą sieć krystaliczną osnowy. 0-cząstki nie ulegają fizycznej translacji; to kształt ich sfer oddziaływań ulega kaskadowej deformacji wraz z ruchem impulsu falowego. 
Jest to bezstratna propagacja kolektywnego wzoru węzłów-solitonów przez zakleszczony Substrat. Na poziomie fundamentalnym 0-Cząstki nie ulegają fizycznej translacji w ślad za poruszającym się ciałem; to kształt ich sfer oddziaływań ulega kaskadowej, falowej deformacji wraz z ruchem impulsu solitonowego. Materia zachowuje się jak porowata siatka topologiczna, przez którą bezoporowo propaguje się stan odkształcenia sieci.

Podczas ruchu tego układu z prędkością współrzędnościową $v$, na każdej pojedynczej, wyginanej geometrycznie sferze dochodzi do mikroskopijnych, lokalnych spiętrzeń. Ponieważ efekty te zachodzą w skali sub-planckowskiej, ich jednostkowe występowanie nie wprowadza lokalnej anizotropii kierunkowej. Jednak w skali makroskopowej, wewnątrz obwiedni poruszającego się układu, następuje konstruktywna, izotropowa akumulacja tych mikro-odkształceń. Generuje to jednorodne spiętrzenie uśrednionej osnowy w całym ciele:

$$\langle\phi(v)\rangle_{\text{macro}} = \phi_0 \cdot \gamma = \frac{\phi_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$

 {#eq-1-4-2}

Dzięki temu, że spiętrzenie przyjmuje formę jednorodnego pola skalarnego wewnątrz obwiedni poruszającego się obiektu:

1. Wszystkie mikroskopijne oscylatory i zegary wewnątrz tego ciała doświadczają identycznego spowolnienia procesów relaksacyjnych (zgodnie z kanonicznym wzorem dylatacji z sekcji 1.2.3), co całkowicie eliminuje gradient kierunkowy i wyjaśnia negatywne wyniki eksperymentów Michelsona-Morleya oraz Kennedy’ego-Thorndike’a.
   
2. Czynnik Lorentza $\gamma$ zostaje rygorystycznie wyprowadzony z nieliniowej sprężystości oraz oporu falowego 0-Matrycy, bez konieczności wprowadzania postulatów o stałości prędkości światła jako abstrakcyjnego pewnika.

#### 1.4.2.1 Dylatacja grawitacyjna – związek z potencjałem $\Phi$

Odkształcenie 3-brany w czwarty wymiar przestrzenny, wywołane obecnością pasywnych węzłów topologicznych (masy), powoduje radialny gradient gęstości upakowania osnowy wokół źródła. W reżimie słabego pola grawitacyjnego przyjmujemy liniową zależność gęstości efektywnej od modułu lokalnego potencjału grawitacyjnego $\Phi(\mathbf{x})$:

$$\phi(\mathbf{x}) \approx \phi_0 \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right)$$

 {#eq-1-4-3}

Podstawiając tę zależność do kanonicznej definicji czasu, stosunek przyrostu lokalnego czasu własnego $dt$ do niezaburzonego czasu płaskiego tła $dt_{\text{flat}}$ przyjmuje postać:

$$\frac{dt}{dt_{\text{flat}}} = \frac{\phi_0}{\phi(\mathbf{x})} \approx \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right)^{-1} \approx 1 - \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}$$

 {#eq-1-4-4}

Równanie to dostarcza poprawnego empirycznie przybliżenia dylatacji grawitacyjnej, tożsamego z wynikami eksperymentu Pounda-Rebki oraz poprawkami relatywistycznymi stosowanymi w systemach nawigacji satelitarnej.

### 1.4.3. Wyprowadzenie transformacji relatywistycznych z elasto-mechaniki sieci 0-Matrycy

Transformacje współrzędnych oraz relacja równoważności energii i masy ($E = mc_{\perp}^2$) stanowią bezpośrednią konsekwencję oporu falowego podczas ruchu fal stojących (węzłów solitonowych) w gęstym, zniekształcalnym kontinuum krystalicznym.

##### 1.4.3.1 Konstrukcja prędkości i kontrakcja długości

Dla zachowania rygoru pojęciowego definiujemy dwie komplementarne reprezentacje prędkości makroskopowej:

1. Prędkość współrzędnościowa tła ($v$): wyraża zmianę pozycji względem statycznej sieci referencyjnej:

$$v = \frac{dx}{dt_{\text{flat}}}$$


2. Prędkość własna węzła ($\eta$): mierzona czasem lokalnym ulegającym dylatacji:

$$\eta = \frac{dx}{dt}$$



Związek transformacyjny między nimi wynika bezpośrednio z mechanizmu spiętrzenia osnowy ($dt = dt_{\text{flat}} / \gamma$):

$$\eta = \frac{dx}{\frac{dt_{\text{flat}}}{\gamma}} = \gamma \cdot v = \frac{v}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$

 {#eq-1-4-5}

Gdy prędkość współrzędnościowa zbliża się do poprzecznej granicy ścinania osnowy ($v \to c_{\perp}$), narastająca inercja topologiczna sprawia, że czynnik $\gamma \to \infty$, podczas gdy prędkość własna $\eta \to \infty$. To rozróżnienie naturalnie eliminuje paradoks nieskończonej prędkości kinematycznej w ujęciu bezwzględnym.

Ruch węzła generuje przed obiektem front kompresji elastycznej. Wprowadzając współrzędną uciekającą $u = x - vt_{\text{flat}}$, przekształcenie jednorodnego równania falowego dla zachowania niezmienniczości kształtu solitonu wymusza przeskalowanie osi przestrzennej wzdłuż wektora pędu:

$$x' = \frac{u}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} = \gamma (x - vt_{\text{flat}})$$

 {#eq-1-4-6}

Pod wpływem tego jednostronnego oporu elasto-mechanicznego, kształt każdego węzła solitonowego ulega rzeczywistej kompresji mechanicznej, co makroskopowo manifestuje się jako skrócenie długości w kierunku ruchu: $L' = L / \gamma$.


### 1.4.4. Energia, pęd i masa relatywistyczna

Energia deformacji elastycznej węzła (której bazowym ekwiwalentem jest masa spoczynkowa $m_0$) proporcjonalnie wibruje z nałożonym obciążeniem gęstości osnowy. Ponieważ dla poruszającego się układu zachodzi spiętrzenie pola gęstości $\langle\phi(v)\rangle_{\text{macro}} = \phi_0\gamma$, masa relatywistyczna — rozumiana jako chwilowa, efektywna inercja topologiczna solitonowego węzła — skaluje się jako:

$$m = \gamma m_0 = \frac{m_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$

 {#eq-1-4-7}

Pęd niesiony przez przemieszczającą się deformację przyjmuje postać sprzężoną z prędkością własną $\eta$:

$$p = m_0 \frac{dx}{dt} = m_0 \eta = \gamma m_0 v$$

 {#eq-1-4-8}

Różniczkując pęd po czasie płaskiego tła ($t_{\text{flat}}$), otrzymujemy dynamiczne równanie siły, które odsłania mechanizm asymptotycznego oporu sieci:

$$F = \frac{dp}{dt_{\text{flat}}} = \frac{d}{dt_{\text{flat}}}(\gamma m_0 v) = m_0 \gamma^3 \frac{d2 x}{dt_{\text{flat}}^2} = m_0 \gamma^3 a$$

 {#eq-1-4-9}

Aby wykazać równoważność masy i energii bezpośrednio z mechaniki środowiska ciągłego, zdefiniujmy przyrost makroskopowej energii kinetycznej ($E_k$) jako pracę wykonaną przez siłę $F$ podczas przyspieszania węzła od stanu spoczynku ($v=0$) do prędkości $v$ na drodze $x$:

$$E_k = \int_0^x F \, dx' = \int_0^t F v \, dt_{\text{flat}}'$$

 {#eq-1-4-10}

Podstawiając do całki elasto-mechaniczne równanie siły (@eq-1-4-9), transformujemy zmienną całkowania z czasu na prędkość współrzędnościową:

$$E_k = \int_0^v \left( m_0 \gamma^3 \frac{dv'}{dt_{\text{flat}}'} \right) v \, dt_{\text{flat}}' = m_0 \int_0^v \gamma^3 v' \, dv'$$

 {#eq-1-4-11}

Rozpisując jawnie czynnik Lorentza $\gamma$, otrzymujemy całkę, którą rozwiązujemy przez rygorystyczne podstawienie:

$$E_k = m_0 \int_0^v \frac{v'}{\left(1 - \frac{v'^2}{c_{\perp}^2}\right)^{3/2}} \, dv'$$

 {#eq-1-4-12}

Wynikiem tego całkowania jest bezpośrednia zależność energii kinetycznej od konfiguracji kompresyjnej sieci:

$$E_k = \left[ \frac{m_0 c_{\perp}^2}{\sqrt{1 - \frac{v'^2}{c_{\perp}^2}}} \right]_0^v = \frac{m_0 c_{\perp}^2}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} - m_0 c_{\perp}^2 = \gamma m_0 c_{\perp}^2 - m_0 c_{\perp}^2$$

 {#eq-1-4-13}

Zgodnie z aksjomatyką TSM, stan zbiegający do spoczynku ($v=0$, czyli $\gamma=1$) nie oznacza zerowej energii kontinuum. Każdy węzeł solitonowy, aby w ogóle istnieć w gęstej sieci krystalicznej, wymaga permanentnego, lokalnego naciągnięcia sfer oddziaływań 0-Cząstek. Energia tego spoczynkowego naciągnięcia stanowi wrodzoną energię strukturalną Substratu: $E_0 = m_0 c_{\perp}^2$.

Definiując całkowitą energię relatywistyczną układu ($E$) jako sumę energii kinetycznej (pracy wprowadzonej do sieci) oraz energii spoczynkowej (wrodzonej geometrii węzła), otrzymujemy pełne wyprowadzenie relacji Einsteina:

$$E = E_k + E_0 = (\gamma m_0 c_{\perp}^2 - m_0 c_{\perp}^2) + m_0 c_{\perp}^2 = \gamma m_0 c_{\perp}^2$$

 {#eq-1-4-14}

Biorąc pod uwagę relatywistyczne skalowanie masy inercyjnej zdefiniowane w @eq-1-4-7, powyższe równanie sprowadza się do ostatecznej, poszukiwanej formy równoważności masowo-energetycznej kontinuum:

$$E = m c_{\perp}^2$$

 {#eq-1-4-15}

Gdy prędkość współrzędnościowa zbliża się do poprzecznej granicy ścinania ($v \to c_{\perp}$), praca wymagana do dalszej kompresji frontu falowego dąży do nieskończoności. Z matematycznego sprzężenia równań całkowitej energii (@eq-1-4-14) oraz pędu fali stojącej (@eq-1-4-8) wynika niezmiennicza relacja dyspersyjna inercji sieci, potwierdzająca bezstratny charakter propagacji:

$$E^2 = (pc_{\perp})^2 + (m_0 c_{\perp}^2)^2$$

 {#eq-1-4-16}

### 1.4.5. Wnioski końcowe i synteza kinematyki TSM

Wyprowadzenie nieliniowej kinematyki makroskopowej w ramach Mechaniki Substratu Topologicznego pozwala na sformułowanie czterech kluczowych wniosków, które redefiniują paradygmat relatywistyczny:

1. **Ontologiczna redukcja czasoprzestrzeni:** TSM udowadnia, że czasoprzestrzeń Minkowskiego nie jest samodzielną, pierwotną areną fizyczną. Czterowymiarowy formalizm relatywistyczny jest wyłącznie efektem matematycznym, wyłaniającym się z faktu, że czas makroskopowy jest parametrem operacyjnym sukcesji zmian (zależnym od lokalnej gęstości osnowy $\phi$), a mierzona przestrzeń to fizycznie ugięta i naciągnięta 3-brana.
2. **Mechanistyczny sens stałości prędkości światła:** Stałość prędkości światła ($c_{\perp}$) w próżni przestaje być bezwarunkowym, aksjomatycznym postulatem kinematycznym. Staje się ona fizyczną, stałą materiałową zdegenerowanej sieci 0-Matrycy — graniczną prędkością propagacji poprzecznych fal akustycznych (ścinania) w sprężystym szkle topologicznym.
3. **Fizykalność kontrakcji i dylatacji:** Kontrakcja długości Lorentza ($L'=L/\gamma$) oraz kinematyczna dylatacja czasu nie są iluzjami perspektywicznymi wynikającymi z abstrakcyjnej geometrii układów odniesienia. Są to realne, elasto-mechaniczne deformacje. Ruch struktury solitonowej generuje fizyczne spiętrzenie osnowy wokół węzłów, co zwiększa opór relaksacyjny sieci i obiektywnie spowalnia wszelkie wewnętrzne procesy okresowe (zegary) poruszającego się ciała.
4. **Jedność grawitacji i inercji:** Poprzez tożsamość mianowników w relacjach dylatacji kinematycznej (@eq-1-4-2) i grawitacyjnej (@eq-1-4-4), TSM unifikuje oba zjawiska na poziomie mikroskopowym. Niezależnie od tego, czy lokalny wzrost gęstości osnowy $\langle\phi\rangle_{\text{macro}}$ jest wywołany ugięciem brany w czwartym wymiarze przez masę centralną (grawitacja), czy też konstruktywnym spiętrzeniem frontu falowego przez ruch własny solitonu (kinematyka), efekt temporalny jest identyczny, ponieważ aparat pomiarowy reaguje wyłącznie na wypadkowe, bezwzględne upakowanie komórek 0-Matrycy.

</br>

## 1.5. Dynamika falowa Substratu i podwójny reżim elasto‑dynamiki

Mechanika Substratu podlega uogólnionemu formalizmowi Lagrange’a, asymilując rozwiązania matematyczne Ogólnej Teorii Względności, lecz bez jej relatywistycznych założeń ontologicznych. Przestrzeń i jej dynamika nie są geometryczną abstrakcją, lecz konsekwencją stanów fizycznych sieci krystalicznej 0-Matrycy.

### 1.5.1. Równania pola osnowy jako opis stanów naprężeń sieci

Gęstość lagrangianu $\mathcal{L}$ izotropowej 3-brany zdefiniowana jest przez jej całkowitą energię sprężystą. Wykorzystując tensor modułów sprężystości $K^{abcd}$, kontinuum modelujemy w reżimie niskich odkształceń za pomocą rozwinięcia:

$$\mathcal{L} = \frac{1}{2} K^{abcd} \epsilon_{ab} \epsilon_{cd} + \mathcal{O}(\epsilon^3)$$

 {#eq-1-5-1}

gdzie tensor małych odkształceń $\epsilon_{ab}$ wyznacza się z pola przemieszczeń osnowy $u$:

$$\epsilon_{ab} = \frac{1}{2}(\nabla_a u_b + \nabla_b u_a)$$

 {#eq-1-5-2}

Właściwości makroskopowe zawarte w tensorze $K^{abcd}$ oraz wynikający z nich tensor naprężeń $\sigma^{ab}$ wynikają bezpośrednio ze stanu elasto-mechanicznego uwięzionych, sub-planckowskich 0-Cząstek i ich sfer odpychania. Dla idealnie izotropowej sieci krystalicznej, tensor modułów sprężystości redukuje się do dwóch niezależnych stałych Lamego ($\lambda$ oraz $\mu$):

$$K^{abcd} = \lambda \eta^{ab}\eta^{cd} + \mu (\eta^{ac}\eta^{bd} + \eta^{ad}\eta^{bc})$$

 {#eq-1-5-3}

gdzie $\eta^{ab}$ oznacza płaską, euklidesową metrykę tła Substratu. Pochodna lagrangianu względem tensora odkształcenia określa tensor naprężenia układu:

$$\sigma^{ab} = \frac{\partial \mathcal{L}}{\partial \epsilon_{ab}} = K^{abcd} \epsilon_{cd} = \lambda \eta^{ab} \epsilon^c_c + 2\mu \epsilon^{ab}$$

 {#eq-1-5-4}

Lokalną makroskopową gęstość osnowy $\phi$ definiujemy jako funkcję stopnia lokalnego zagęszczenia lub rozrzedzenia komórek sieci, co matematycznie odpowiada śladowi tensora odkształceń (dylatacji objętościowej $\epsilon^c_c = \nabla \cdot \mathbf{u}$):

$$\phi = \phi_0 (1 - \epsilon^c_c) = \phi_0 (1 - \nabla \cdot \mathbf{u})$$

 {#eq-1-5-5}

gdzie $\phi_0$ to niezniekształcona, bazowa gęstość upakowania 0-Matrycy w stanie równowagi.

Stosując zasadę najmniejszego działania Hamiltona ($\delta \int \mathcal{L} \, d^4x = 0$) względem pola przemieszczeń $u_a$, otrzymujemy dynamiczne równanie ruchu Substratu (odpowiednik równania Naviera-Cauchy’ego w środowisku ciągłym):

$$\phi_0 \frac{\partial^2 u^a}{\partial t_{\text{flat}}^2} = \nabla_b \sigma^{ab} = (\lambda + \mu) \nabla^a (\nabla \cdot \mathbf{u}) + \mu \nabla^2 u^a$$

 {#eq-1-5-6}

Zgodnie z mechaniką ośrodków krystalicznych, pole przemieszczeń $u^a$ można jednoznacznie rozłożyć (dekompozycja Helmholtza) na składową bezrotacyjną (fale podłużne) oraz bezdywergencyjną (fale poprzeczne ścinania): $\mathbf{u} = \nabla \Phi + \nabla \times \mathbf{\Psi}$. Podstawiając ten rozkład do równania ruchu (@eq-1-5-6) dla składowej poprzecznej $\mathbf{\Psi}$ (gdzie $\nabla \cdot \mathbf{\Psi} = 0$), otrzymujemy czyste, jednorodne równanie falowe:

$$\nabla^2 \mathbf{\Psi} - \frac{\phi_0}{\mu} \frac{\partial^2 \mathbf{\Psi}}{\partial t_{\text{flat}}^2} = 0$$

 {#eq-1-5-7}

Powyższe podstawienie rygorystycznie definiuje poprzeczną prędkość fali ścinania jako fundamentalną stałą materiałową sieci: $c_{\perp} = \sqrt{\mu / \phi_0}$. W ogólnym przypadku, w obecności trwałych zniekształceń sieci (węzłów), dowolna funkcja składowych pola odkształceń poprzecznych $\psi \in \mathbf{\Psi}$ spełnia niejednorodne równanie falowe:

$$\nabla^2 \psi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \psi}{\partial t_{\text{flat}}^2} = \mathcal{S}(\mathbf{x}, t_{\text{flat}})$$

 {#eq-1-5-8}

gdzie $\mathcal{S}(\mathbf{x}, t_{\text{flat}})$ to funkcja źródła, reprezentująca gęstość nieliniowych odkształceń topologicznych.

Ewoluująca w skali makroskopowej krzywizna geometryczna efektywnego tensora metrycznego $g_{ab}$ staje się bezpośrednim matematycznym odwzorowaniem stanu naprężeń mechanicznych tła $\sigma_{ab}$. Relację tę zadaje liniowe sprzężenie konstytutywne TSM:

$$g_{ab} = \eta_{ab} - \chi \sigma_{ab}$$

 {#eq-1-5-9}

gdzie $\chi$ jest makroskopową podatnością elastyczną Substratu. W ten sposób grawitacja wyłania się jako tensorowe pole naprężeń sieci, eliminując potrzebę zakrzywiania samej pierwotnej ontologii przestrzeni.

### 1.5.2. Fale sprężyste a nieliniowa blokada topologiczna

W idealnie sprężystym ośrodku, który bezstratnie i symetrycznie rozprasza nadmiary lokalnego ciśnienia, formowanie jakichkolwiek trwałych, zlokalizowanych struktur materialnych (cząstek) byłoby niemożliwe. Aby zapobiec natychmiastowej relaksacji i dyspersji energii, mechanika TSM rozdziela dynamikę Substratu na dwa komplementarne reżimy fizyczne, ostro rozgraniczone krytycznym progiem zamrożenia geometrycznego, nazywanym **gęstością blokady topologicznej $\phi_{\text{lock}}$**.

**Reżim I: Liniowa relaksacja akustyczna ($\phi < \phi_{\text{lock}}$)**

Dopóki lokalna kompresja sieci nie przekracza progu stabilności geometrycznej klatek Wignera-Seitza ($\epsilon^c_c > \epsilon_{\text{crit}}$), Substrat zachowuje się jak idealne, liniowe kontinuum sprężyste. Odkształcenia komórek mają charakter zachowawczy – sfery odpychania ulegają przejściowej deformacji, lecz 0-Cząstki bezwzględnie zachowują nienaruszoną macierz swoich pierwotnych sąsiadów. Nadmiar lokalnego ciśnienia jest transferowany izotropowo na zewnątrz, a ośrodek skutecznie relaksuje energię poprzez propagację klasycznych fal poprzecznych z niezmienniczą prędkością materiałową $c_{\perp}$. W tym reżimie tło pozostaje bezmasową próżnią fizyczną.

**Reżim II: Nieliniowa blokada topologiczna ($\phi \ge \phi_{\text{lock}}$)**

Sytuacja zmienia się diametralnie, gdy lokalny układ komórek zostaje skompresowany poza granicę plastyczności geometrycznej ($\epsilon^c_c \le \epsilon_{\text{crit}}$). Klatki kinetyczne Wignera-Seitza doznają wówczas krytycznego zniekształcenia. Zgodnie z fundamentalnym aksjomatem absolutnego uwięzienia, 0-Cząstki nie mogą przeskoczyć ani fizycznie przemieścić się do sąsiednich komórek – drastycznej i nieodwracalnej deformacji ulega kształt oraz orientacja samych klatek sieci.

Nieliniowe skrócenie osi komórek w strefie ekstremalnego ściskania aktywuje człony wyższego rzędu $\mathcal{O}(\epsilon^3)$ w lagrangianu (@eq-1-5-1), co wymusza trwałą rotację głównych kierunków naprężeń sprężystych. Zamiast sekwencyjnego przekazywania pędu na zewnątrz (relaksacja falowa), linie naprężeń zamykają się same w sobie, tworząc przestrzennie zablokowaną strukturę:

1. **Następuje kinetyczne i geometryczne ograniczenie swobody sfer oddziaływań 0-Cząstek.**
2. **Pola naprężeń zapętlają się w samopodtrzymujący się, rotacyjny splot, czyli mikroskopijny wir solitonowy.** Stan ten opisuje matematycznie niezerowy tensor wirowości mechanicznej $\Omega_{ab} = \frac{1}{2}(\nabla_a u_b - \nabla_b u_a)$, którego zamknięta cyrkulacja staje się niezmiennikiem topologicznym całego układu.
3. **Substrat w tym konkretnym obszarze całkowicie traci zdolność do uwalniania zgromadzonej energii poprzez zwykłą emisję fal akustycznych $c_{\perp}$.**

Powstaje nieliniowy węzeł topologiczny, który uzyskuje niezależną stabilność strukturalną. Jego rozplecenie lub zniszczenie wymagałoby ponownego dostarczenia energii wystarczającej do pokonania stanu granicznej kompresji, co stwarza potężną, skwantowaną barierę energetyczną. W ten sposób nieliniowa mechanika zniekształceń krystalicznych daje bezpośredni początek stabilnej, skwantowanej materii makroskopowej.

### 1.5.3 Podsumowanie dynamicznego dualizmu Substratu

Wprowadzenie uogólnionego formalizmu elasto-dynamiki pozwala na jednoznaczne sformułowanie mechanicznej definicji przestrzeni i materii w TSM. Całość dynamicznych stanów 0-Matrycy można ująć w rygorystyczną strukturę komplementarną:

| Parametr / Cecha | Reżim I: Liniowa relaksacja akustyczna | Reżim II: Nieliniowa blokada topologiczna |
| --- | --- | --- |
| **Kryterium przejścia** | $\phi < \phi_{\text{lock}}$ \ (lub $\epsilon^c_c > \epsilon_{\text{crit}}$) | $\phi \ge \phi_{\text{lock}}$ \ (lub $\epsilon^c_c \le \epsilon_{\text{crit}}$) |
| **Stan klatek sieci** | Niskie, zachowawcze odkształcenia elastyczne. | Krytyczne, plastyczne zniekształcenie klatek Wignera-Seitza. |
| **Zachowanie 0-Cząstek** | Wibracje wewnątrz klatek; zachowanie pełnej macierzy pierwotnych sąsiadów. | Absolutne uwięzienie; trwała rotacja głównych kierunków naprężeń sprężystych. |
| **Transfer energii** | Swobodna, izotropowa emisja fal poprzecznych z prędkością materiałową $c_{\perp}$. | Brak możliwości liniowej emisji; zapętlenie linii naprężeń w rotacyjny splot. |
| **Matematyczny niezmiennik** | Jednorodne równanie hiperboliczne: \ $\nabla^2 \mathbf{\Psi} - \frac{1}{c_{\perp}^2}\frac{\partial^2\mathbf{\Psi}}{\partial t^2} = 0$ | Niezerowy, skwantowany tensor wirowości mechanicznej: $\Omega_{ab} \neq 0$. |
| **Wyłoniony status fizyczny** | **Bezmasowa próżnia fizyczna** (tło propagacji fal elektromagnetycznych). | **Stabilna, skwantowana materia makroskopowa** (cząstki elementarne jako wezły). |

</br>

## 1.6. Aksjomat materii: Skwantowane węzły topologiczne

### 1.6.1. Lokalne strefy blokady jako stabilne konfiguracje solitonowe

W obszarach gęstości równej lub przewyższającej $\phi_{\text{lock}}$, naprężenia formują węzły topologiczne (solitony). Ponieważ rdzeń splotu musi asymptotycznie dążyć do izotropowego tła sieciowego, topologia zmuszona jest zamknąć wektory w pełne obroty fazowe. Twierdzenia matematyczne wymuszają, by zjawisko takie było bezwzględnie całkowitoliczbowe — ładunek topologiczny (liczba splotu) $\mathcal{W} \in \mathbb{Z}$. W ten sposób makroskopowa porcja materii uzyskuje twardą, niepodzielną kwantyzację, zachowując absolutną stabilność i odporność na rozpady termiczne 0-Matrycy. 

### 1.6.2. Rygorystyczne rozdzielenie masy od ładunku

Sieciowa architektura rozdziela dwie fundamentalne cechy defektu materii:
- **Ładunek:** Jest płaskim rzutem 3D wielokrotności obrotu wektora naprężenia fazowego ($2\pi$). Ponieważ cykl ten musi się domknąć z nienaruszoną krystaliczną osnową zewnętrzną, rzut daje spójny skwantowany ładunek $\pm 1e$, ukrywając wyższe zawiłości topologiczne wektora wewnątrz węzła.
- **Masa:** Wynika rygorystycznie z mechanicznego wzdęcia ortogonalnego układu w kierunku wyższego wymiaru $x^4$. Bardziej zagęszczony i ciasny splot warkocza (proton) ugnie strukturę 3-brany i osnowy wokół niej głębiej i wymusi zmagazynowanie większej makroskopowej energii sprężystej $m_0$ niż prostszy skręt (elektron), mimo bycia źródłem identycznej asymetrii ładunkowej na powierzchni.

</br>

## 1.7. Podsumowanie Rozdziału

Elasto-mechanika Mechaniki Substratu Topologicznego przedstawia absolutnie redukcjonistyczny aparat zastępujący czysto geometryczne założenia fizyki współczesnej spójną ontologią 0-Matrycy. Całkowicie usunięto pojęcie abstraktu przestrzeni. Odrzucono kinematyczne postulaty relatywistyczne zastępując je emergentnymi skutkami mechanicznego spiętrzenia zdegenerowanej sieci krystalicznej ($dt \propto 1/\gamma \langle\phi\rangle$). Oddzielono makroskopową zjawiskowość od zablokowanego tła, dając solidne podstawy inercji topologicznej dla barier $c_{\perp}$. Kategorycznie rozróżniono dynamikę liniowego rozproszenia od nieliniowej blokady materiotwórczej. Pozwala to operować zjawiskami makroskopowymi – metryką $g_{ab}$, siłami ciążenia i dylatacją czasu – używając uogólnionych równań z dziedziny mechaniki ośrodków ciągłych z uwzględnieniem obciążeń tensorowych sieci bez utraty rygoru kwantowego.