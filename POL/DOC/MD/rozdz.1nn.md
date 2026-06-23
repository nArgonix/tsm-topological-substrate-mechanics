---
---
<!-- ver:4.5.8 -->
# 1. Elasto-mechanika 0-Matrycy: Emergencja Czasu, Metryki i Kinematyki Relatywistycznej {#sec:rom-tsm}

## 1.1. Wprowadzenie i ramy konceptualne {#sub-wprowadznie}

Niniejszy rozdział stanowi formalny rdzeń teorii Mechaniki Substratu Topologicznego (TSM), implementując ścisły aparat matematyczno-fizyczny dla jej pojęciowych fundamentów. O ile poprzednie rozważania ugruntowały ontologiczną konieczność istnienia sub-planckowskiego podłoża, o tyle w tym miejscu uwaga zostaje skoncentrowana na matematycznej rekonstrukcji makroskopowych praw fizyki z dynamicznej sieci geometrycznej — 0-Matrycy. Paradygmat TSM kategorycznie odrzuca pojęcie pustej czasoprzestrzeni jako fundamentalnego tła fizycznego. W zamian, za pomocą rygorystycznego aparatu elasto-mechaniki dyskretnej, wykazuje, że czas makroskopowy, efektywna metryka grawitacyjna $g_{ab}$ oraz transformacje relatywistyczne nie są pierwotnymi atrybutami rzeczywistości, lecz zjawiskami wtórnymi (emergentnymi), wyłaniającymi się z uśrednionych stanów naprężeń, odkształceń i konfiguracji topologicznych zablokowanej osnowy 4D.

Sformalizowany wywód zmierzający do rekonstrukcji kontinuum makroskopowego odzwierciedla ścisły ciąg redukcjonistyczny, podzielony na cztery kluczowe etapy:

1. **Architektura podłoża i geneza czasu:** Rozdział otwiera analiza mikrostruktury 0-Matrycy, opartej na sferach oscylacji 0-Cząstek. Przedstawiony zostaje mechanizm ich geometrycznego, globalnego zakleszczenia, który formuje izotropową 3‑branę. Dopiero na tym fizycznym podłożu, poprzez matematyczny formalizm uśredniania fluktuacji stochastycznych, zdefiniowana zostaje Efektywna Gęstość Substratu. Czas makroskopowy zostaje tu wyprowadzony nie jako kontinuum, lecz jako kanoniczna miara sukcesji kolejnych stanów sieci.
2. **Elastodynamika fali i prędkość światła:** Zamiast postulować stałość prędkości światła jako nadrzędny aksjomat, formalizm wyprowadza ją bezpośrednio z właściwości materiałowych osnowy. Prędkość $c$ zostaje zdefiniowana jako prędkość propagacji poprzecznych zaburzeń ścinania w zablokowanej mechanicznie strukturze 4D, a jej lokalna zmienność ($c_{\perp}$) zostaje powiązana ze stałymi materiałowymi sieci.
3. **Emergencja geometrii i kinematyki relatywistycznej:** W sferze kinematyki nieliniowej rozdział dowodzi, że efektywna metryka makroskopowa $g_{ab}$ jest matematycznym opisem lokalnych odkształceń Substratu. W konsekwencji relatywistyczna dylatacja czasu zyskuje czysto mechaniczną interpretację jako izotropowe spiętrzenie (zagęszczenie) osnowy. Pozwala to na pełne wyprowadzenie transformacji relatywistycznych bezpośrednio z praw rządzących elasto-mechaniką zdegenerowanej sieci krystalicznej, bez odwoływania się do postulatów Szczególnej Teorii Względności.
4. **Równania pola i aksjomat materii:** W obszarze dynamiki falowej rozdział asymiluje rozwiązania matematyczne Ogólnej Teorii Względności, jednak bez jej założeń ontologicznych — równania pola stają się tu opisem stanów naprężeń sieci w podwójnym reżimie elastodynamicznym (fale sprężyste kontra nieliniowa blokada). Kulminacją tego opisu jest definicja aksjomatu materii: cząstki zostają sformalizowane jako stabilne konfiguracje solitonowe (lokalne strefy blokady topologicznej). Pozwala to na rygorystyczne, geometryczne rozdzielenie masy (jako lokalnego defektu gęstości osnowy) od ładunku elektrycznego (jako jej skręcenia topologicznego).

</br>

## 1.2. Mikrostruktura 0-Matrycy i stan globalnego zakleszczenia {#sec-1-1}

Punktem wyjścia dla Mechaniki Substratu Topologicznego (TSM) jest całkowite odrzucenie pojęcia pierwotnej, ciągłej czasoprzestrzeni jako fundamentalnego tła fizycznego. Jedyną obiektywną rzeczywistością ontologiczną jest 0-Matryca – zdegenerowana, wibrująca sieć krystaliczna. Wszelkie przejawiane w skali makroskopowej zjawiska relatywistyczne oraz oddziaływania nie stanowią cech samej przestrzeni, lecz są emergentnym rezultatem stanów naprężeń, deformacji oraz dynamiki falowej tej pierwotnej, ukrytej struktury.

### 1.2.1. Geometria sieci: 0-Cząstki w sferach oscylacji jako fundament osnowy {#sec-1-1-1}

W przeciwieństwie do klasycznych modeli eteru, mikrostruktura 0-Matrycy wykazuje rygorystyczny, quasi-krystaliczny porządek sieciowy, funkcjonując w stanie podstawowym jako sztywne, sprężyste szkło topologiczne w czterowymiarowej przestrzeni euklidesowej Substratu. Na poziomie fundamentalnym pojedyncza 0-Cząstka jest obiektem niepodzielnym o stałej objętości $V_{00}$, uwięzionym topologicznie w przypisanym węźle sieci. Jej objętość spełnia warunek sub-planckowskiej skali:

$$0 < V_{00} \ll V_{\text{Planck}}$$ {#eq-wz1-1}

* *W konwencji notacyjnej całego rozdziału podwójny subskrypt `00` oznacza wielkość mikroskopową, wewnętrzną dla pojedynczej 0-Cząstki i niezależną od jej otoczenia (np. $V_{00}$, $m_{00}$) — w odróżnieniu od pojedynczego subskryptu `0`, rezerwowanego dla wielkości wyznaczonych przez kolektywny kontekst sieci, czy to na poziomie geometrii komórki ($R_0$), czy pól makroskopowych Stanu Zero ($\phi_0$, $\rho_0$, $T_0$, $P_0$).*

W reżimie niskich i średnich energii pojedyncze elementy osnowy są pozbawione swobody translacyjnej, co wyklucza zjawiska takie jak makroskopowy przepływ przez ośrodek. 0-Cząstka może wykonywać ruchy wyłącznie wewnątrz ściśle ograniczonej przestrzeni, zdefiniowanej jako komórka konfiguracyjna (sfera oscylacji). Formalnie, jeśli $\mathbf{X}_i$ oznacza statyczne położenie równowagi $i$-tego węzła w 4D, to chwilowe przesunięcie 0-Cząstki $\mathbf{u}_i$ podlega rygorystycznemu ograniczeniu geometrycznemu:

$$|\mathbf{u}_i| = |\mathbf{x}_i - \mathbf{X}_i| \le R_0$$ {#eq-wz1-2}

gdzie $R_0$ stanowi promień sfery w stanie pełnej relaksacji 0-Matrycy. Granica tej sfery nie jest barierą potencjału w sensie kwantowym, lecz twardym ograniczeniem topologicznym, wynikającym z maksymalnego geometrycznego upakowania i fizycznego sąsiedztwa innych stref w zdegenerowanej sieci.

Dla pełnej jasności modelu, mechanika TSM wprowadza w tym miejscu rygorystyczne rozróżnienie między **absolutnie twardym rdzeniem 0-Cząstki** a jej **sferą oscylacji (oddziaływań)**:

* **Rdzeń** stanowi fizyczną, nieprzenikalną i fundamentalnie niepodzielną bryłę o objętości $V_{00}$. Nie posiada on żadnej struktury wewnętrznej, a jego objętość nie ulega jakiejkolwiek kompresji nawet w warunkach ekstremalnego naporu. Posiada także niezmienniczą masę $m_{00}$ — fundamentalną własność mikroskopową, identyczną dla wszystkich 0-Cząstek i niezależną od stanu makroskopowego osnowy. Masa $m_{00}$ jest **aksjomatem pierwotnym** modelu TSM: nie wyłania się z geometrii sieci ani z dynamiki kolizji, lecz stanowi ontologicznie pierwotną wielkość definiującą skalę energetyczną 0-Matrycy, analogicznie jak ładunek elementarny w elektrodynamice.
* **Sfera oscylacji** definiuje z kolei objętość komórki konfiguracyjnej w pełnej przestrzeni 4D, $V_0 = \frac{\pi^2}{2}R_0^4$ (objętość 4-kuli), stanowiącą efektywną jednostkę objętości przypadającą na pojedynczy węzeł sieci w stanie relaksacji w obrębie której rdzeń wykonuje swoją chaotyczną kinetykę.

Rdzenie sąsiadujących 0-Cząstek w liniowym reżimie osnowy nigdy nie ulegają bezpośredniemu, statycznemu kontaktowi. Zbliżenie rdzeni napotyka na asymptotycznie rosnącą barierę siłową, która jest emergentnym skutkiem ich własnego uwięzienia i ultra-szybkich, sprężystych kolizji wewnątrz gęsto upakowanej, krystalicznej sieci. Sfera oddziaływań jest więc w istocie barierą kinetyczną, a nie polem siłowym w klasycznym sensie.

#### 1.2.1.1. Mikrodynamika komórki: Mechanizm bilardu Sinaja {#sec-1-1-1-1}

Geometria komórki konfiguracyjnej determinuje unikalny charakter wewnętrznego ruchu 0-Cząstki. Jej ścianek nie tworzy gładka, pusta wnęka, lecz wypukłe sfery oddziaływań sąsiednich 0-Cząstek. Ruch w obszarze ograniczonym takimi wypukłymi przeszkodami rozpraszającymi klasyfikowany jest jako bilard Sinaja (model matematyczny gazu Lorentza). Fizyczna spójność modelu bilardu wymaga spełnienia warunku geometrycznego $r_{00}<R_0$, gdzie $r_{00}$ oznacza promień rdzenia 0-Cząstki powiązany z jego objętością przez $V_{00}=\frac{\pi^2}{2}r_{00}^4$ (objętość 4-kuli). Iloraz $r_{00}/R_0$ determinuje mikroskopicznie zarówno średnią drogę swobodną $\ell$, jak i 4-wymiarowy przekrój czynny rozpraszania $S_{4D}$ — parametry, które w dalszym wywodzie (@sec1-3-3) pozostają fenomenologicznie otwarte, lecz których fizyczna skala jest tym samym ograniczona od dołu przez $r_{00}>0$ i od góry przez $r_{00}<R_0<l_P$.

W odróżnieniu od bilardu o gładkich ściankach (np. całkowalnego ruchu w pustej sferze omijającego środek), bilard rozpraszający tego typu wykazuje silną własność mieszania oraz pełną ergodyczność. Niezależnie od warunku początkowego, rozkład przestrzenny obecności cząstki zbiega wykładniczo szybko do jednorodnego rozkładu równowagowego na całej dostępnej objętości komórki. Ruch ten jest ściśle deterministyczny, lecz stochastycznie nieprzewidywalny dla obserwatora makroskopowego ze względu na sub-planckowską skalę przestrzenną.

#### 1.2.1.2. Emergencja makroskopowej tarczy sferycznej {#sec-1-1-1-2}

Kluczowym czynnikiem transformującym tę mikrodynamikę w stabilne struktury makroskopowe jest asymetria skal czasowych. Częstotliwość oscylacji 0-Cząstki, wyrażona w wirtualnych sekundach, przewyższa o dziesiątki rzędów wielkości makroskopowo rozróżnialne jednostki czasu. Czas potrzebny na osiągnięcie pełnego wymieszania przestrzennego z perspektywy czasu emergentnego jest praktycznie zerowy.

0-Cząstka nie "przemierza" więc swojej sfery w obserwowalnym czasie; wypełnia ją swoją fizyczną obecnością niemal natychmiastowo. Z zewnątrz ta ultraszybka oscylacja manifestuje się jako dynamiczna, nieprzenikalna tarcza o idealnej symetrii sferycznej. Ustanawia to ścisły podział na chaotyczną dynamikę wewnętrzną a uśrednione zjawiska makroskopowe, gdzie lokalna gęstość osnowy jest pochodną zagęszczenia tych sfer.

#### 1.2.1.3. Reżim krytyczny i Klauzula Krytycznego Przemieszczenia {#sec-1-1-1-3}

Stan fundamentalnego uwięzienia ulega zmianie wyłącznie w warunkach krytycznych – pod wpływem ekstremalnego ciśnienia zewnętrznego lub silnego skręcenia topologicznego. Gdy lokalne naprężenia ścinające przekroczą krytyczny próg plastyczności, aktywacji ulega Klauzula Krytycznego Przemieszczenia.

Ponieważ asymptotyczna bariera siłowa zabrania fizycznego kontaktu rdzeni, proces ten jest ściśle kolektywny. Przemieszczenie realizowane jest jako sprzężony, synchroniczny przesuw klastra 0-Cząstek w formie fali solitonowej, wykorzystujący obszary rozrzedzenia do kompensacji naporu. Elementy sieci fizycznie zmieniają pozycję (zyskują nową topologię sąsiedztwa) bez naruszania minimalnej odległości międzycząstkowej. W momencie spadku naprężeń poniżej progu, 0-Cząstki natychmiast odzyskują sfery oddziaływań i powracają do stanu uwięzionych mikro-oscylacji, zamykając proces rearanżacji.

### 1.2.2. Mechanizm globalnego zakleszczenia i wyłonienie izotropowej 3‑brany {#sec-1-1-2}

Stanem bazowym 0-Matrycy, umożliwiającym zaistnienie obserwowalnego świata, jest stan **globalnego zakleszczenia** (*structural jamming*). Przy osiągnięciu krytycznej gęstości upakowania $\phi \ge \phi_c$, niezależne stopnie swobody 0-Cząstek zostają wzajemnie zablokowane przez siły kontaktu topologicznego w czterech wymiarach przestrzennych.

W wyniku tego izotropowego zakleszczenia, nieliniowe oddziaływania prowadzą do wyłonienia stabilnej, trójwymiarowej hiperpowierzchni – izotropowej 3-brany (obszaru lokalnego ugięcia wywołanego zaburzeniem w Stanie Zero). Dla obserwatora wewnętrznego 3-brana jawi się jako trójwymiarowa metryka. Makroskopowy tensor naprężeń sieci w stanie czystego zakleszczenia ma postać:

$$T_{IJ}^{(0)} = -P_0 \delta_{IJ}$$  {#eq-sek1-1-tens-zaklesz}

gdzie:

* $I,J \in \{1,2,3,4\}$ — indeksy przestrzenne w pełnej, 4-wymiarowej przestrzeni euklidesowej Substratu,
* $\delta_{IJ}$ — delta Kroneckera, odzwierciedlająca idealną izotropię stanu zakleszczenia (brak wyróżnionego kierunku naprężeń),
* $P_0$ — izotropowe ciśnienie zakleszczenia w przestrzeni 4D, traktowane w tym rozdziale jako **parametr referencyjny Stanu Zero**, na równi z $\phi_0$ (§1.2.3), $\rho_0$ (§1.3.2) i $T_0$ (§1.2.3). Podobnie jak te wielkości, $P_0$ nie jest tu wyprowadzane z głębszej teorii mikroskopowej, lecz przyjmowane jako fenomenologiczna własność stanu podstawowego 0-Matrycy w progu zakleszczenia $\phi\ge\phi_c$ — zgodnie z praktyką fizyki ośrodków zakleszczonych (*jamming physics*), gdzie ciśnienie progowe jest wielkością empiryczną układu, a nie analitycznie wyprowadzaną.

Idealna symetria tensora maskuje dyskretną naturę matrycy przed przyrządami pomiarowymi.

</br>

### 1.2.3. Emergencja czasu makroskopowego z dynamiki sub-planckowskiej {#sec-1-2}

#### 1.2.3.1. Granica poznania i eliminacja fluktuacji stochastycznych {#sec-1-2-1}

W stanie podstawowym 0-Matryca charakteryzuje się permanentnymi, mikroskopijnymi drganiami cząstek osnowy wokół położeń równowagi. Zjawisko to, opisywane w mikroskali jako bilard Sinaja ( @sec-1-1-1-1), generuje niekoherentny szum tła definiowany jako fundamentalna temperatura Substratu ($T_{\text{sub}}$). Zgodnie z zasadą rygoru empirycznego, model TSM kategorycznie odrzuca próbę definiowania czasu makroskopowego poprzez te pierwotne, chaotyczne oscylacje.

Wszelkie efekty falowe oraz lokalne zmiany częstotliwości zachodzące bezpośrednio na pojedynczych elementach sieci mają charakter sub-planckowski — zachodzą poniżej granicy skali Plancka ($\sim 10^{-35}$ m) — i są stochastycznie nieprzewidywalne. Próba ich operacyjnego definiowania z makroskopowego punktu widzenia jest pozbawiona sensu mierzalnego. Z tego względu model TSM rezygnuje z postulowania mikroskopijnych zależności kinematycznych pojedynczych 0-Cząstek, przenosząc cały ciężar formalizmu na makroskopowe uśrednianie elasto-mechaniczne zdegenerowanej sieci krystalicznej.

#### 1.2.3.2. Matematyczny formalizm uśredniania – Efektywna Gęstość Substratu {#sec-1-2-2}

Kluczowym parametrem wiążącym dyskretną dynamikę sieci z obserwowalną rzeczywistością makroskopową jest fundamentalna gęstość upakowania 0-Cząstek, zdefiniowana jako ciągłe pole w pełnej, 4-wymiarowej przestrzeni Substratu: $\phi(\mathbf{X}) = \phi(x^1, x^2, x^3, x^4)$. Operator uśredniania makroskopowego wygładza lokalne, nieciągłe anomalie gęstości wokół pojedynczych komórek sieci z wykorzystaniem splotu z funkcją okna $W$ o skali odcięcia równej skali Plancka ($\Lambda_{\text{Planck}}$):

$$\langle\phi(\mathbf{X})\rangle_{\text{macro}} = \int_{\mathbb{R}^4} \phi(\mathbf{X}') \, W(\mathbf{X} - \mathbf{X}', \Lambda_{\text{Planck}}) \, d^4\mathbf{X}'$$ {#eq-1-2-1}

gdzie:

* $\mathbf{X} = (x^1, x^2, x^3, x^4)$ – 4-wektor pozycji w przestrzeni euklidesowej 0-Matrycy,
* $\phi(\mathbf{X}')$ – surowa, mikroskopijna gęstość lokalna osnowy w pełnej przestrzeni 4D,
* $W$ – normalizowana, 4-wymiarowa funkcja przejścia (okno filtracyjne) eliminująca szum sub-planckowski,
* $\Lambda_{\text{Planck}}$ – przestrzenna skala odcięcia.

Ponieważ wszystkie fizyczne przyrządy pomiarowe (zegary, detektory) są uformowanymi węzłami topologicznymi uwięzionymi wewnątrz zakleszczonej 3-brany, bezpośrednio dostępna eksperymentalnie jest wyłącznie wartość $\langle\phi(\mathbf{X})\rangle_{\text{macro}}$ zrestryktowana do tej hiperpowierzchni. W stanie niezakłóconym brana zajmuje hiperpowierzchnię $x^4 = 0$, natomiast w obecności lokalnych odkształceń i naprężeń jest ugięta do pozycji $x^4 = w(\mathbf{x})$. Obserwowalna makroskopowa gęstość upakowania w rzutowanym punkcie przestrzeni trójwymiarowej $\mathbf{x} = (x^1, x^2, x^3)$ wyraża się zatem rzutem:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} \equiv \left.\langle\phi(\mathbf{X})\rangle_{\text{macro}}\right|_{x^4 = w(\mathbf{x})}$$ {#eq-1-2-2}

Dla zachowania pełnej informacji o stanie środowiska 4D wewnątrz ugiętej hiperpowierzchni, przyjmujemy, że funkcja okna $W$ jest matematycznie separowalna względem składowych brany i wymiaru ortogonalnego: $W(\mathbf{X}-\mathbf{X}', \Lambda_{\text{Planck}}) = W_3(\mathbf{x}-\mathbf{x}', \Lambda_{\text{Planck}}) \cdot W_4(x^4 - \xi, \Lambda_{\text{Planck}})$. Pozwala to zdefiniować efektywną gęstość powierzchniową 3D jako całkę ważoną funkcją $W_4$ wzdłuż osi ortogonalnej $\xi$ (odpowiadającej współrzędnej $x^4$):

$$\phi_{\text{eff}}(\mathbf{x}') \equiv \int_{-\infty}^{+\infty} \phi(\mathbf{x}', \xi) \, W_4\!\left(w(\mathbf{x}') - \xi, \, \Lambda_{\text{Planck}}\right) d\xi$$ {#eq-1-2-3}

Ponieważ charakterystyczna grubość 3-brany w kierunku ortogonalnym jest rzędu skali Plancka, a funkcja $W_4$ rygorystycznie eliminuje wkłady spoza tego zakresu, całkowanie jest asymptotycznie zlokalizowane w otoczeniu planckowskim brany. Wyniki mierzalne pozostają niezależne od stanu głębokich struktur 0-Matrycy poza tą strefą. Ostateczna, operacyjna forma efektywnej gęstości makroskopowej na 3-branie przyjmuje postać splotu trójwymiarowego:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} = \int_{\mathbb{R}^3} \phi_{\text{eff}}(\mathbf{x}') \, W_3(\mathbf{x} - \mathbf{x}', \Lambda_{\text{Planck}}) \, d^3\mathbf{x}'$$ {#eq-1-2-4}

W płaskiej, niezakłóconej geometrycznie 3-branie ($w \equiv 0$, gdzie gęstość $\phi$ jest jednorodna w skali planckowskiej wzdłuż czwartego wymiaru) zachodzi tożsamość $\phi_{\text{eff}}(\mathbf{x}') \equiv \phi(\mathbf{x}', 0)$, a całe sformułowanie redukuje się do standardowego splotu gęstości osnowy w przestrzeni trójwymiarowej.

**Uwaga o spójności grawitacyjno-temporalnej:** Zależność efektywnej gęstości $\phi_{\text{eff}}$ od funkcji ugięcia brany $w(\mathbf{x})$ poprzez argument jądra $W_4$ stanowi bezpośrednie, mechanistyczne uzasadnienie dla zjawiska grawitacyjnej dylatacji czasu. Węzeł topologiczny (masywny obiekt) indukujący ugięcie $w > 0$ lokalnie przesuwa punkt próbkowania funkcji $W_4$ w obszar osnowy o wyższym ciśnieniu strukturalnym. Podnosi to wartość $\langle\phi(\mathbf{x})\rangle_{\text{macro}}$ i w konsekwencji zwalnia bieg lokalnego czasu własnego zgodnie z relacją kanoniczną.

#### 1.2.3.3. Kanoniczna definicja czasu makroskopowego jako miary sukcesji stanów sieci {#sec-1-2-3}

W mechanice TSM czas nie jest pierwotnym, niezależnym wymiarem ani autonomiczną areną ewolucji układów. Czas mierzony makroskopowo przez dowolne przyrządy pomiarowe — które same stanowią makroskopowe struktury złożone z sieci węzłów topologicznych — jest wyłącznie parametrem operacyjnym sukcesji zmian strukturalnych. Jego tempo upływu pozostaje ściśle i odwrotnie proporcjonalne do efektywnej gęstości elasto-mechanicznej osnowy.

Przyrost lokalnego czasu własnego $dt$ wyraża się równaniem kanonicznym:

$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi(\mathbf{x})\rangle_{\text{macro}}}$$ {#eq-1-2-5}

gdzie:

* $dt$ – przyrost lokalnego czasu własnego, wyrażony w sekundach `[s]`,
* $dN$ – liczba zarejestrowanych cykli makroskopowego procesu okresowego (np. oscylacji atomowych w zegarze),
* $T_0$ – okres referencyjny tegoż procesu zachodzącego w niezaburzonej, stacjonarnej osnowie,
* $\phi_0$ – podstawowa, izotropowa gęstość upakowania 0-Matrycy w Stanie Zero (przestrzeń płaska),
* $\langle\phi(\mathbf{x})\rangle_{\text{macro}}$ – uśredniona elasto-mechanicznie lokalna gęstość osnowy w obszarze zajmowanym przez układ pomiarowy.

Mechanizm dylatacji czasu wynika bezpośrednio z kinematyki stanu zakleszczenia strukturalnego (*structural jamming*). Lokalny wzrost gęstości komórek osnowy ($\langle\phi(\mathbf{x})\rangle_{\text{macro}} > \phi_0$) generuje proporcjonalnie wyższy opór elasto-mechaniczny sieci. Silniejsze upakowanie geometryczne drastycznie ogranicza swobodę wibracyjną uwięzionych 0-Cząstek, co spowalnia transfer energii, propagację sygnałów oraz wszelkie wewnętrzne procesy relaksacyjne układu fizycznego.

Dla stałej liczby cykli mikroskopowych $dN$ przyrost czasu własnego $dt$ ulega zmniejszeniu. Z perspektywy zewnętrznego obserwatora referencyjnego lokalna sekunda ulega fizycznemu rozciągnięciu (staje się dłuższa), ponieważ aparat matematyczny TSM w sposób rygorystyczny wiąże tempo sukcesji stanów sieci z mianownikiem operatora interwału czasowego.

</br>

## 1.3. Elastodynamika sieciowa i mikroskopowa geneza prędkości światła {#sec-1-3}

Aby wyeliminować metodologiczny zarzut wprowadzenia bariery prędkości falowej $c$ jako założenia ad hoc, model Topological Substrate Mechanics (TSM) wyprowadza stałą prędkość światła (identyfikowaną jako prędkość poprzecznych fal ścinających $c_{\perp} \equiv c$) jako wielkość emergentną. Wyprowadzenie to realizowane jest dwuetapowo: poprzez rygorystyczny opis kontinuum elasto-dynamicznego z uwzględnieniem stanu zablokowania topologicznego, a następnie przez sprzężenie go z sub-planckowską kinetyką 0-cząstek.

### 1.3.1. Propagacja zaburzeń ścinania i blokada fal podłużnych w osnowie 4D {#sec-1-3-1}

Rozpatrzmy stan podstawowy Substratu przed sformowaniem brany. W klasycznej teorii sprężystości w ośrodku ciągłym mogą rozchodzić się dwa główne typy fal: fale podłużne (zagęszczenia/rozrzedzenia, zależne od modułu ściśliwości) oraz fale poprzeczne (ścinania, skrętne, zależne od modułu sztywności postaciowej).

Jako 4-wymiarowy, izotropowy ośrodek sprężysty o gigantycznym zagęszczeniu kolizyjnym, 0-Matryca podlega uogólnionym równaniom Naviera-Cauchy'ego dla przemieszczeń $\mathbf{u}(x^1, x^2, x^3, x^4)$. Przyjmujemy tu i w dalszej części rozdziału następującą konwencję notacyjną: indeksy łacińskie ze środka alfabetu ($i,j,k,\dots$) oraz wielkie ($I,J$, wprowadzone w §1.1.2) oznaczają zamiennie współrzędne pełnej, 4-wymiarowej przestrzeni euklidesowej Substratu i przebiegają zakres $\{1,2,3,4\}$; natomiast indeksy $a,b,c,d$, używane od §1.4 wzwyż, są zarezerwowane wyłącznie dla 3-wymiarowej hiperpowierzchni 3-brany ($\{1,2,3\}$). Wprowadzamy 4-wymiarowy tensor odkształceń Cauchy'ego-Greena w postaci:

$$u_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x^j} + \frac{\partial u_j}{\partial x^i} + \frac{\partial u_k}{\partial x^i} \frac{\partial u_k}{\partial x^j} \right)$$ {#eq-sek131-4wym-tensor-odkszt}

Zakładając liniowy reżim sprężysty (w którym nieliniowe gradienty kwadratowe są pomijalne przed przekroczeniem progu blokady topologicznej), gęstość energii sprężystej $\mathcal{U}$ dana jest klasycznym wzorem Lamégo rozszerzonym do 4 wymiarów:

$$\mathcal{U} = \frac{1}{2} \lambda (u_{kk})^2 + \mu u_{ij} u_{ij}$$ {#eq-sek131-gest-energ-sprezU}

Gdzie $\lambda$ oraz $\mu$ to makroskopowe współczynniki Lamégo charakteryzujące odpowiednio sprężystość objętościową (opór przeciw ściskaniu) oraz sprężystość postaciową (opór przeciw ścinaniu) Substratu.

Równanie ruchu elementu objętości osnowy w czasie płaskiego tła $t_{\text{flat}}$ można zapisać w postaci wektorowej (gdzie $\rho_{\text{eff}}$ to efektywna makroskopowa gęstość falowa):

$$(\lambda + \mu) \nabla (\nabla \cdot \mathbf{u}) + \mu \nabla^2 \mathbf{u} = \rho_{\text{eff}} \frac{\partial^2 \mathbf{u}}{\partial t_{\text{flat}}^2}$$ {#eq-sek131-rown-ruchu-elemVosn}

W tym miejscu ujawnia się kluczowa mechanika modelu TSM. W stanie geometrycznego zablokowania (jamming state), sfery oddziaływań 0-cząstek ulegają gęstemu upakowaniu (podczas gdy same rdzenie cząstek zachowują swobodną dynamikę sub-planckowską). Powoduje to, że ośrodek staje się **lokalnie nieściśliwy** dla makroskopowych oddziaływań. Próba wymuszenia fali podłużnej napotyka na asymptotycznie nieskończony opór, co matematycznie wyraża się dążeniem pierwszego parametru Lamégo do nieskończoności ($\lambda \to \infty$) przy jednoczesnym zerowaniu się dywergencji przemieszczenia ($\nabla \cdot \mathbf{u} \to 0$).

Zgodnie z twierdzeniem Helmholtza, rozkładając pole wektorowe na część bezrotacyjną (podłużną) $\mathbf{u}_\parallel$ oraz bezźródłową (poprzeczną) $\mathbf{u}_\perp$:

$$\mathbf{u} = \mathbf{u}_\parallel + \mathbf{u}_\perp, \quad \text{gdzie} \quad \nabla \times \mathbf{u}_\parallel = 0 \quad \text{oraz} \quad \nabla \cdot \mathbf{u}_\perp = 0$$ {#eq-sek131-pole-wekt}

Warunek nieściśliwości eliminuje fale podłużne z fizycznego spektrum makroskopowego. Równanie Naviera-Cauchy'ego redukuje się wyłącznie do poprzecznej składowej $\mathbf{u}_\perp$, reprezentującej lokalne ścinanie (rotację sfer oddziaływań):

$$\mu \nabla^2 \mathbf{u}_\perp = \rho_{\text{eff}} \frac{\partial^2 \mathbf{u}_\perp}{\partial t_{\text{flat}}^2} \implies \nabla^2 \mathbf{u}_\perp - \frac{\rho_{\text{eff}}}{\mu} \frac{\partial^2 \mathbf{u}_\perp}{\partial t_{\text{flat}}^2} = 0$$ {#eq-sek131-redukc-rownNC}

Wyodrębniamy stąd prędkość propagacji fali poprzecznej (ścinającej):

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_{\text{eff}}}}$$ {#eq-sek131-propag-fali-poprzecznej}

Ponieważ 3-brana jest zdefiniowana jako makroskopowe skręcenie uwięzione wzdłuż czwartego wymiaru ($x^4$), wszelkie interakcje w naszym świecie są falami poprzecznymi tej struktury. Wektor falowy $\mathbf{k} = (k_1, 0, 0, k_4)$ prowadzi do relacji dyspersyjnej $\omega^2 = c_{\perp}^2 (k_1^2 + k_4^2)$. Maksymalna prędkość rzutu fali poprzecznej na obserwowalną przestrzeń 3D zachodzi dla $k_4 = 0$ i wyznacza absolutną granicę prędkości zjawisk fizycznych. Prędkość $c_{\perp}$ jest zatem tożsama z makroskopową prędkością światła $c$ w próżni.

### 1.3.2. Dynamiczny opór relaksacyjny i mikroskopowe ugruntowanie parametrów {#sec-1-3-2}

Równanie falowe dla $c_{\perp}$ opisuje zachowanie kontinuum w makroskali, jednak moduł ścinania $\mu$ oraz efektywna gęstość falowa $\rho_{\text{eff}}$ nie są stałymi fundamentalnymi. Wyłaniają się one z mikroskopowej kinetyki bilardu Sinaja. Kluczem do sprzężenia absolutnej prędkości sub-planckowskiej $v_\text{00}$ ze stałą makroskopową $c_{\perp}$ jest potężna dysproporcja skal geometrycznych.

Wprowadźmy w tym miejscu stałą sieci osnowy $a$ — odległość między równowagowymi położeniami sąsiednich węzłów $\mathbf{X}_i$. Wielkość ta nie jest niezależnym parametrem modelu, lecz wynika wprost z geometrii sfer oscylacji wprowadzonych w [@sec-1-1-1] w stanie pełnej relaksacji zakleszczonej sieci sąsiadujące sfery oddziaływań o promieniu $R_0$ stykają się stycznie, definiując graniczny kontakt komórek konfiguracyjnych [@sec-1-1-1-1]. Dla izotropowej sieci o identycznych sferach oscylacji odległość międzywęzłowa równa jest zatem sumie promieni dwóch sąsiednich komórek:

$$a = 2R_0$$ {#eq-sek1-3-stala-sieci}

co potwierdza spójność skali: skoro $a < 1{,}6 \times 10^{-35}$ m (skala sub-planckowska), to również $R_0 < 0{,}8 \times 10^{-35}$ m.

Zdefiniujmy bezwymiarowy stosunek $\xi$ między stałą sieci osnowy $a$ a długością fali mierzalnego zaburzenia makroskopowego $\lambda$:

$$\xi = \frac{a}{\lambda_\text{fala}} \ll 1$$ {#eq-sek1-3-bezw-stos-sieci-al}

| Rodzaj promieniowania | Przykładowa $\lambda_\text{fala}$ | Górne ograniczenie $\xi \leq l_P/\lambda_\text{fala}$ |
| --- | --- | --- |
| Radiowa | $\sim 1$ m | $\lesssim 2 \times 10^{-35}$ |
| Widzialna | $\sim 5 \times 10^{-7}$ m | $\lesssim 3 \times 10^{-29}$ |
| Rentgenowska | $\sim 10^{-10}$ m | $\lesssim 2 \times 10^{-25}$ |

{#tab-1-3-2}

Niezależnie od pasma widma, parametr $\xi$ spełnia rygorystycznie $\xi \ll 1$. Pojedyncza komórka nie doświadcza makroskopowego ugięcia fali jako zjawiska jednokierunkowego w sposób natychmiastowy.

Podstawowa statyczna gęstość tła $\rho_0$ wynika wprost z masy pojedynczego rdzenia $m_{00}$ oraz objętości sfery oddziaływań w stanie relaksacji $V_0$: $\rho_0 = m_{00} / V_0$. Zgodnie z Aksjomatem II, w stanie izotropowym energia kinetyczna 0-cząstek, poruszających się z prędkością $v_\text{00}$, jest rozłożona równomiernie na 4 stopnie swobody. Z ekwipartycji pędu wynika, że moduł sprężystości postaciowej $\mu$ zależy wprost od wariancji prędkości ortogonalnej:

$$\mu = \rho_0 \langle v_{\text{00}\perp}^2 \rangle = \rho_0 \frac{v_{\text{00}}^2}{4}$$  {#eq-sek1-3-mod-sprez}

Gdy fala makroskopowa przemieszcza się przez sieć, sąsiednie 0-cząstki nie zderzają się czołowo, lecz kaskadowo deformują geometrię swoich sfer oddziaływań, przekazując impuls skrętny. Te ultra-szybkie oscylacje w 4 osiach stawiają opór o charakterze bezwładności żyroskopowej. Front fali napotyka opór wynikający z konieczności kaskadowej redystrybucji pędu.

Definiujemy makroskopowy parametr geometrycznego wzmocnienia bezwładności $\Gamma_{4D}$, reprezentujący liczbę sub-planckowskich mikro-cykli kolizyjnych niezbędnych do wykonania makroskopowego, w pełni zachowawczego przekazu impulsu (por. [@sec-1-3-5]).

### 1.3.3. Derywacja $\Gamma_{4D}$ z błądzenia przypadkowego rdzenia {#sec-1-3-3}

Aby uniknąć definiowania parametru wzomcnienia bezwładności $\Gamma_{4D}$ operacyjnie poprzez samą stałą $c_\perp$ (co prowadziłoby do błędnego koła), wyprowadzamy go wyłącznie z geometrii sieci i statystyki zderzeń mikroskopowych.

Definiujemy fundamentalne parametry układu w $d=4$: gęstość liczbową 0-Cząstek $n$ (węzłów na jednostkę 4-objętości), efektywną stałą sieci $a$ (z relacją geometryczną $a\equiv n^{-1/4}$, zgodną z $a=2R_0$ wyprowadzonym w §1.3.2 z geometrii stycznych sfer oscylacji; relacja ta jest ścisłą definicją stałej sieci dla regularnej, izotropowej sieci zakleszczonej, w której każdemu węzłowi przypada 4-objętość dokładnie równa $a^4$), 4-wymiarowy przekrój czynny rozpraszania $S_{4D}$, oraz średnią drogę swobodną $\ell$ swobodnego rdzenia poruszającego się wewnątrz zablokowanych sfer. Należy w tym miejscu rygorystycznie zdefiniować naturę przekroju czynnego $S_{4D}$. W przestrzeni 4-wymiarowej przekrój czynny nie jest dwuwymiarowym polem powierzchni, lecz trójwymiarową hiper-powierzchnią uderzeniową (efektywną objętością 3-kuli kolizyjnej), posiadającą wymiar geometryczny $[L^3]$. Biorąc pod uwagę gęstość liczbową osnowy $n \equiv a^{-4}$ o wymiarze $[L^{-4}]$, średnia droga swobodna $\ell$ z klasycznej teorii kinetycznej uogólnionej na 4 wymiary przyjmuje postać:

$$\ell = \frac{1}{\sqrt{2}\, n\, S_{4D}}$$

 {#eq-1-3-3-wz1}

Wymiarowość mianownika redukuje się do $[L^{-1}]$, co poprawnie nadaje drodze swobodnej $\ell$ fizyczny wymiar długości $[L^1]$. Gwarantuje to absolutną spójność analizy wymiarowej w dalszych krokach.

Podstawiając $n=a^{-4}$:

$$a^4 = \sqrt{2}\,\ell\,S_{4D} \implies a^2 = \sqrt[4]{2}\sqrt{\ell\,S_{4D}}$$

 {#eq-1-3-3-wz2}

Ze względu na warunek lokalnej nieściśliwości Substratu, makroskopowy transfer pędu fali poprzecznej wymaga kaskadowej redystrybucji energii wewnątrz komórki sieci. Ruch rdzenia wewnątrz sfery ma charakter błądzenia przypadkowego: po $N$ zderzeniach o długości $\ell$, średni kwadrat przemieszczenia wynosi $\langle r^2\rangle=N\ell^2$. Zgodnie z tą samą zasadą ekwipartycji na 4 stopnie swobody, która w §1.3.2 dała $\mu=\rho_0v^2/4$, postęp w pojedynczej osi poprzecznej wynosi:

$$\langle x_{\perp}^2\rangle = \frac14 N\ell^2$$ {#eq01-3-3-wz3}
Definiujemy $\Gamma_{4D}\equiv N$ jako liczbę mikro-zderzeń niezbędnych do przetransferowania impulsu na odległość pojedynczej sfery oddziaływań $a$. Kładąc warunek graniczny $\langle x_\perp^2\rangle=a^2$:

$$\Gamma_{4D} = 4\left(\frac{a}{\ell}\right)^2 = 4\sqrt[4]{2}\,\frac{\sqrt{S_{4D}}}{\ell^{3/2}}$$ {#eq-1-3-gamma4d}

Dzięki ustalonemu wcześniej wymiarowi $[L^3]$ dla wielkości $S_{4D}$, pierwiastek w liczniku przyjmuje postać $[L^{1.5}]$, co idealnie skraca się z mianownikiem $\ell^{3/2}$. Czyni to parametr geometrycznego wzmocnienia bezwładności $\Gamma_{4D}$ wielkością rygorystycznie bezwymiarową.

Wielkość ta jest teraz funkcją wyłącznie geometrii sieci ($a$) i statystyki zderzeń ($\ell$, $S_{4D}$) — bez odwołania do $c_\perp$ czy $v_\text{00}$. Oznacza to, że efektywna gęstość bezwładna, jaką „widzi” przemieszczająca się fala, rośnie z kwadratem uwięzionego, żyroskopowego oporu tła względem pierwotnej gęstości masowej $\rho_0$. Aby formalnie dowieść tej zależności i uniknąć arbitralnego postulowania wartości gęstości makroskopowej, należy wyprowadzić ją bezpośrednio z bilansu energii kinetycznej oraz mechanizmu wzmocnienia kinematycznego.

Gdy przez 0-Matrycę propaguje się makroskopowa fala ścinania, wymusza ona na elemencie objętościowym Substratu makroskopową prędkość przemieszczenia poprzecznego $\dot{u}_{\text{macro}}$. Ponieważ jednak impuls musi fizycznie przebyć krętą ścieżkę składającą się z $N = \Gamma_{4D}$ mikro-zderzeń (błądzenie przypadkowe rdzenia), rzeczywista, wymuszona prędkość mikroskopowa przesyłu impulsu między 0-Cząstkami ($\dot{u}_{\text{mikro}}$) jest proporcjonalnie wyższa. Współczynnik $\Gamma_{4D}$ pełni tu rolę efektywnego opóźnienia propagacji:

$$\dot{u}_{\text{mikro}} = \Gamma_{4D} \cdot \dot{u}_{\text{macro}}$$

 {#eq-1-3-3-wz5-a}

W makroskopowym kontinuum gęstość energii kinetycznej fali opisywana jest za pomocą poszukiwanej, jednorodnej gęstości efektywnej $\rho_{\text{eff}}^{(0)}$ w stanie równowagowym:

$$E_k = \frac{1}{2} \rho_{\text{eff}}^{(0)} (\dot{u}_{\text{macro}})^2$$

 {#eq-1-3-3-wz5-b}

Z drugiej strony, na fundamentalnym poziomie mikroskopowym, ta sama energia kinetyczna jest zmagazynowana w rzeczywistym ruchu rdzeni o bazowej gęstości masowej tła $\rho_0$:

$$E_k = \frac{1}{2} \rho_0 (\dot{u}_{\text{mikro}})^2$$

 {#eq-1-3-3-wz5-c}

Podstawiając relację wzmocnienia kinematycznego do mikroskopowego bilansu energii, otrzymujemy:

$$E_k = \frac{1}{2} \rho_0 (\Gamma_{4D} \cdot \dot{u}_{\text{macro}})^2 = \frac{1}{2} (\rho_0 \Gamma_{4D}^2) (\dot{u}_{\text{macro}})^2$$

 {#eq-1-3-3-wz5-d}

Porównując ten wynik bezpośrednio z ujęciem makroskopowym, otrzymujemy rygorystyczną, analityczną postać równowagowej gęstości bezwładnej, obowiązującej w niezakłóconym stanie zakleszczenia 0-Matrycy:

$$\rho_{\text{eff}}^{(0)} = \rho_0 \cdot \Gamma_{4D}^2$$

 {#eq-1-3-3-wz5}

To właśnie $\rho_{\text{eff}}^{(0)}$, a nie surowa gęstość mikroskopowa $\rho_0=m_{00}/V_0$, jest wielkością bezpośrednio wstawianą do relacji Helmholtza $c_\perp=\sqrt{\mu/\rho_{\text{eff}}^{(0)}}$ w §1.3.4 oraz do równania ruchu Substratu (@eq-1-5-6) w @sec-1-5-1 jako wartość odniesienia, wokół której fluktuuje pole $\rho_{\text{eff}}(\mathbf{x})$ wprowadzone tam dla opisu lokalnych zaburzeń grawitacyjnych.

### 1.3.4. Derywacja $c_{\perp}$ i jej interpretacja fizyczna {#sec-1-3-4}

Podstawiając niezależnie wyprowadzone $\mu=\rho_0v_\text{00}^2/4$ (§1.3.2) oraz $\rho_{\text{eff}}^{(0)}=\rho_0\Gamma_{4D}^2$ (@eq-1-3-3-wz5, §1.3.3) do redukcji Helmholtza $c_\perp=\sqrt{\mu/\rho_{\text{eff}}^{(0)}}$:

$$c_{\perp} = \sqrt{\frac{\rho_0\frac{v_\text{00}^2}{4}}{\rho_0\Gamma_{4D}^2}} = \frac{v_\text{00}}{2\Gamma_{4D}} = \frac{v_\text{00}}{8}\left(\frac{\ell}{a}\right)^2 = \frac{v_{00}}{8\sqrt[4]{2}}\,\frac{\ell^{3/2}}{\sqrt{S_{4D}}}$$ {#eq-1-3-c-perp-final}

gdzie ostatnia forma wynika z jawnej, geometrycznej postaci $\Gamma_{4D}=4\sqrt[4]{2}\,\sqrt{S_{4D}}/\ell^{3/2}$ (eq-1-3-gamma4d).

W odróżnieniu od czysto definicyjnej zależności $\Gamma_{4D}\equiv v_\text{00}/(2c_\perp)$, powyższe wyprowadzenie ufundowuje $c_\perp$ wyłącznie na geometrii sieci ($a$) i statystyce zderzeń mikroskopowych ($\ell$, $S_{4D}$) — eliminując cykliczność rozumowania. Równanie to nie jest tautologią, lecz fundamentalnym mostem fizycznym teorii TSM: dowodzi, że obserwowalna makroskopowo prędkość światła (utożsamiana w tym reżimie z $c_\perp$) nie jest niezależną, abstrakcyjną stałą uniwersalną, lecz jawną funkcją wewnętrznej prędkości kinetycznej 0-Cząstek ($v_{00}$) oraz parametrów geometrii i przekroju czynnego zablokowanej sieci.

Wynik niesie jasny sens fizyczny: w stanie zakleszczenia ($\ell\ll a$, rdzeń przebywa wiele mikro-zderzeń, zanim impuls dotrze do sąsiedniej komórki) ułamek $(\ell/a)^2$ jest ekstremalnie mały, silnie tłumiąc pierwotną prędkość sub-planckowską $v_\text{00}\gg c_\perp$ do mierzalnej wartości $c_\perp$.

W ten sposób przejście z opisu dyskretnego (dynamiki 0-Cząstek) do opisu ciągłego (continuum elastodynamicznego 3-brany) zostaje domknięte matematycznie bez wprowadzania fenomenologicznych parametrów dopasowawczych. Relacja ta jednoznacznie wykazuje, że niezmienność $c$ dla obserwatora makroskopowego jest bezpośrednią konsekwencją stabilności termodynamicznej i stałości gęstości upakowania 0-Matrycy w jej Stanie Zero. Lokalne fluktuacje gęstości osnowy będą zatem modyfikować efektywny lokalny tensor sztywności, co w skali makroskopowej manifestuje się jako ugięcie metryki, czyli pole grawitacyjne.

### 1.3.5. Zachowawczy charakter propagacji falowej i brak dyssypacji energii {#sec-1-3-5}

Zdefiniowanie parametru geometrycznego wzmocnienia bezwładności $\Gamma_{4D}$ rodzi zasadnicze pytanie: w jaki sposób w medium zdominowanym przez procesy kaskadowych kolizji stabilność energetyczna fali nie ulega natychmiastowej dyssypacji na ciepło? Model TSM eliminuje dyssypację poprzez dwa warunki ontologiczne:

1. **Brak sub-poziomu strukturalnego:** Zderzenia 0-cząstek są twarde, niepodzielne i bezwzględnie sprężyste. Ponieważ nie istnieje "wnętrze" 0-cząstki, energia nie ma jak ulec termalizacji do niższych wymiarów czy wewnętrznego tarcia.
2. **Czysto reaktywny charakter impedancji sieci:** Komórki sieciowe działają jak geometryczny akumulator energii. Na przednim zboczu fali pochłaniają pęd makroskopowy, na tylnym w pełni i bezstratnie go oddając.

Całkowity bilans energetyczny transferu pędu w jednym pełnym cyklu falowym wynosi dokładnie zero. Dlatego też redshift obserwowany w kosmologii nie jest efektem tarcia fotonu o osnowę (co odróżnia TSM od modeli „zmęczonego światła"), lecz wynika z kosmologicznej ewolucji uśrednionej gęstości substratu $\langle\phi\rangle_{\rm macro}$ — poprzez mechanizm wstępni opisany w Rozdziale 0.4 oraz dokładniej w Rozdziale 6. A lokalna zmiana $\langle\phi\rangle_\text{macro}$ modyfikuje tempo kanonicznego czasu (@eq-1-2-5), co obserwator rejestruje jako zmianę częstotliwości fali.

### 1.3.6. Status fali podłużnej: Superluminalne fale gęstości 4D i fluktuacje czasu {#sec-1-3-6}

Rozkład Helmholtza ujawnia istnienie drugiego modu – fali podłużnej (dylatacyjnej), której prędkość wynosi:

$$c_{\parallel} = \sqrt{\frac{\lambda + 2\mu}{\rho_{\text{eff}}}}$$ {#eq-1-3-predk-fali-podluz}

Należy doprecyzować status parametru $\lambda$ względem ścisłego warunku nieściśliwości przyjętego w §1.3.1. Tam idealizacja $\lambda\to\infty$ (przy jednoczesnym $\nabla\cdot\mathbf{u}\to0$) formalnie eliminuje falę podłużną z widma makroskopowego — tj. obserwowanego na poziomie 3-brany przez detektory elektromagnetyczne. W niniejszym podrozdziale rozpatrujemy nie ten ścisły limit, lecz rezydualny, formalnie bardzo duży, lecz skończony opór objętościowy ($\lambda\gg\mu$, $\lambda<\infty$) — odpowiadający niezerowej, choć ekstremalnie małej ściśliwości resztkowej osnowy w skali sub-planckowskiej. Dzięki temu $c_\parallel$ pozostaje skończona, choć $c_\parallel\gg c_\perp$, co uzasadnia określenie „superluminalna” bez wprowadzania formalnej rozbieżności. Fizyczna manifestacja tej fali uwięzionej na 3-branie polega na chwilowych, przestrzennych oscylacjach ułamka upakowania osnowy ($\phi$). Zgodnie z równaniem kanonicznym czasu, lokalna zmiana gęstości wprost determinuje tempo procesów fizycznych. Fale podłużne rozchodzące się w 0-Matrycy to sub-planckowskie **fale dylatacji czasu**, niewidoczne dla detektorów EM, lecz generujące tło szumu kwantowego. Relację między tym rezydualnym $\lambda$ a ścisłym limitem $\lambda\to\infty$ z §1.3.1 — w szczególności mikroskopowe pochodzenie skali, przy której opór objętościowy przestaje być traktowany jako nieskończony — pozostawiamy jako otwarty problem ilościowy tego rozdziału.

## 1.4. Kinematyka nieliniowa i emergencja efektywnej geometrii makroskopowej {#sec-1-4}

W mechanice TSM metryka przestrzenna $g_{ab}$ nie jest bytem pierwotnym abstrakcyjnej geometrii; stanowi ona wyłącznie fizyczny i matematyczny rzut stanu odkształcenia elasto-mechanicznego Substratu. Całkowicie eliminujemy pojęcie unifikującej czasoprzestrzeni – w opisie makroskopowym mamy do czynienia wyłącznie z uśrednioną geometrią przestrzenną 3-brany, na którą rzutują dynamiczne naprężenia zdegenerowanej sieci krystalicznej 4D.

### 1.4.1. Wyłonienie efektywnej metryki $g_{ab}$ z lokalnych odkształceń Substratu {#sec-1-4-1}

W płaskiej, niezakłóconej 3-brane (w dużej odległości od węzłów topologicznych) ośrodek charakteryzuje się płaską metryką euklidesową $\delta_{ab}$. Wprowadzamy fizyczne wektorowe pole przemieszczenia osnowy $u(\mathbf{x})$, które opisuje lokalne odkształcenie elementu objętości sieci od jego położenia równowagi. Obserwowalna makroskopowo metryka Riemanna wyłania się rygorystycznie z nieliniowych gradientów tego przemieszczenia (indeksy $a,b,c,d\in\{1,2,3\}$ zgodnie z konwencją §1.3.1, ograniczone do hiperpowierzchni 3-brany):

$$g_{ab} = \delta_{ab} + \nabla_a u_b + \nabla_b u_a + \delta_{cd} \nabla_a u_c \nabla_b u_d$$ {#eq-1-4-1}

gdzie:

* $g_{ab}$ – tensor metryczny stanowiący obserwowalną geometrię przestrzeni,
* $\delta_{ab}$ – płaska metryka euklidesowa niezakłóconej sieci tła,
* $u$ – wektor fizycznego przemieszczenia osnowy Substratu,
* $\nabla$ – operator pochodnej kowariantnej zdefiniowanej w metryce tła $\delta_{ab}$.

Wszelkie zakrzywienia przestrzeni oraz wynikające z nich zjawiska grawitacyjne są w ten sposób bezpośrednim skutkiem mechanicznego naciągnięcia układu komórek 0-Cząstek. Generuje to makroskopowy gradient efektywnej gęstości upakowania $\phi$ skierowany w stronę czwartego, ortogonalnego wymiaru przestrzennego $x^4$.

### 1.4.2. Kinematyczna dylatacja czasu jako izotropowe spiętrzenie osnowy {#sec-1-4-2}

Ruch struktury makroskopowej (węzła) nie polega na przepychaniu materii przez ośrodek, lecz na propagacji samej deformacji topologicznej poprzez zdegenerowaną, wibrującą sieć krystaliczną osnowy. Na poziomie fundamentalnym 0-Cząstki nie ulegają fizycznej translacji w ślad za poruszającym się ciałem; to kształt ich sfer oddziaływań ulega kaskadowej, falowej deformacji wraz z ruchem impulsu solitonowego. Jest to bezstratna propagacja kolektywnego wzoru węzłów-solitonów przez zakleszczony Substrat. Materia zachowuje się jak porowata siatka topologiczna, przez którą bezoporowo propaguje się stan odkształcenia sieci.

Podczas ruchu tego układu z prędkością współrzędnościową $v$, na każdej pojedynczej, wyginanej geometrycznie sferze dochodzi do mikroskopijnych, lokalnych spiętrzeń. Ponieważ efekty te zachodzą w skali sub-planckowskiej, ich jednostkowe występowanie nie wprowadza lokalnej anizotropii kierunkowej. Jednak w skali makroskopowej, wewnątrz obwiedni poruszającego się układu, następuje konstruktywna, izotropowa akumulacja tych mikro-odkształceń.

Mechanizm tego spiętrzenia wynika bezpośrednio z zasady zachowania objętości rdzenia 0-Cząstki ($V_{00}=\text{const}$, §1.1.1) w połączeniu z kontrakcją przestrzenną struktury solitonowej w kierunku ruchu. Jak wykazano niezależnie w §1.4.3.1 (eq-1-4-6) z wymogu niezmienniczości kształtu solitonu względem jednorodnego równania falowego osnowy, poruszający się węzeł ulega skróceniu rozciągłości przestrzennej wzdłuż kierunku ruchu o czynnik $1/\gamma$: $L'=L/\gamma$. Ponieważ liczba 0-Cząstek $N$ tworzących strukturę solitonu oraz objętość ich pojedynczych, niepodzielnych rdzeni $V_{00}$ pozostają niezmienione (absolutna sztywność rdzenia, §1.1.1.1), redukcja objętości przestrzennej zajmowanej przez tę samą liczbę cząstek wymusza proporcjonalny wzrost lokalnej gęstości upakowania:

$$\langle\phi(v)\rangle_{\text{macro}} = \phi_0\cdot\frac{V}{V'} = \frac{\phi_0}{\sqrt{1 - \dfrac{v^2}{c_{\perp}^2}}} = \phi_0\cdot\gamma$$ {#eq-1-4-2}

Parametr $\phi_0$ w powyższej relacji oznacza sub-Planckowe upakowanie 0-Cząstek w 0-Matrycy na poziomie mikroskopowym (Poziom I). Soliton jako obiekt fizyczny jest jednak defektem topologicznym wyższego rzędu organizacji (Poziom II): zbudowany jest z $N_\text{str}$ stref topologicznych, z których każda angażuje $M$ 0-Cząstek, tworząc razem strukturę mezoskopową o własnym efektywnym module kompresji $K_\text{eff}$. Dla prostych cząstek elementarnych $N_\text{str}$ jest małe (np. dla hopfionów bazowych $N_\text{str}=1$), dla cząstek złożonych — jąder atomowych, hadronów wielokwarkowych — $N_\text{str}$ może wynosić dziesiątki lub tysiące, proporcjonalnie do masy spoczynkowej (§1.6).

Ta hierarchia poziomów jest kluczowa dla interpretacji zachowania granicznego wzoru (eq-1-4-2). Statyczna granica upakowania 0-Cząstek $\phi_\text{max}^\text{stat}$ — wyznaczona geometrią twardych rdzeni hiperkulistych w 4D i rządząca progami $\phi_c$ oraz $\phi_\text{lock}$ w §1.5.2 — dotyczy wyłącznie Poziomu I i opisuje równowagowe przetasowanie sieci. Kinematyczna kompresja osnowy przez poruszający się soliton operuje natomiast na strefach Poziomu II, które nie są twardymi kulami, lecz strukturami topologicznymi — hopfionami i ich lokalnymi wariantami. Co więcej, czas przejścia solitonu przez pojedynczy węzeł sieci jest krótszy od czasu relaksacji strukturalnej $T_0$, zatem sieć reaguje wyłącznie sprężyście, bez topologicznego przetasowania Poziomu I. W tym dynamicznym reżimie efektywna granica kompresji nie jest wyznaczona przez geometryczny sufit $\phi_\text{max}^\text{stat}$, lecz przez energię sprężystą:

$$U_\text{comp}(v) \approx \frac{1}{2}K_\text{eff}\left(\frac{\phi_0\gamma - \phi_0}{\phi_0}\right)^2 \cdot V_\text{sol} \xrightarrow{v \to c_\perp} \infty$$ {#eq-1-4-2b}

Dywergencja $U_\text{comp}$ przy $v\to c_\perp$ oznacza, że bariera prędkości $v_\text{lock} = c_\perp$ jest asymptotyczną barierą energetyczną — nie geometrycznym sufitem upakowania rdzeni. Niezależnie od stopnia złożoności solitonu ($N_\text{str}$, masa spoczynkowa $m_0$), żaden skończony nakład energii nie pozwala osiągnąć $v=c_\perp$. Wynik ten jest wewnętrznie spójny z dywergencją energii kinetycznej $E=\gamma m_0 c_\perp^2$ z §1.4.4 — oba opisy wyrażają tę samą niemożliwość fizyczną z dwóch komplementarnych perspektyw: energetycznej i geometryczno-topologicznej.

Dzięki temu, że spiętrzenie ( @eq-1-4-2) przyjmuje formę jednorodnego pola skalarnego wewnątrz obwiedni poruszającego się obiektu:

1. Wszystkie mikroskopijne oscylatory i zegary wewnątrz tego ciała doświadczają identycznego spowolnienia procesów relaksacyjnych (zgodnie z kanonicznym wzorem dylatacji z §1.2.3), co całkowicie eliminuje gradient kierunkowy i wyjaśnia negatywne wyniki eksperymentów Michelsona-Morleya oraz Kennedy'ego-Thorndike'a.

2. Czynnik Lorentza $\gamma$ zostaje rygorystycznie wyprowadzony z nieliniowej sprężystości oraz oporu falowego 0-Matrycy, bez konieczności wprowadzania postulatów o stałości prędkości światła jako abstrakcyjnego pewnika.

#### 1.4.2.1. Dylatacja grawitacyjna — związek z potencjałem $\Phi$ {#sec-1-4-2-1}

Odkształcenie 3-brany w czwarty wymiar przestrzenny, wywołane obecnością pasywnych węzłów topologicznych (masy), powoduje radialny gradient gęstości upakowania osnowy wokół źródła. W reżimie słabego pola grawitacyjnego przyjmujemy liniową zależność gęstości efektywnej od modułu lokalnego potencjału grawitacyjnego $\Phi(\mathbf{x})$:

$$\phi(\mathbf{x}) \approx \phi_0 \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right)$$ {#eq-1-4-3}

Podstawiając tę zależność do kanonicznej definicji czasu, stosunek przyrostu lokalnego czasu własnego $dt$ do niezaburzonego czasu płaskiego tła $dt_\text{flat}$ przyjmuje postać:

$$\frac{dt}{dt_{\text{flat}}} = \frac{\phi_0}{\phi(\mathbf{x})} \approx \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right)^{-1} \approx 1 - \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}$$ {#eq-1-4-4}

Równanie to dostarcza poprawnego empirycznie przybliżenia dylatacji grawitacyjnej, tożsamego z wynikami eksperymentu Pounda-Rebki oraz poprawkami relatywistycznymi stosowanymi w systemach nawigacji satelitarnej. Należy podkreślić, że rozwinięcie liniowe (eq-1-4-3) obowiązuje wyłącznie w reżimie słabego pola, gdzie $|\Phi|/c_\perp^2\ll 1$; w reżimie silnego pola (otoczenie ultra-gęstych plazmoidów zastępujących osobliwości) wymagane jest nieliniowe ujęcie zależności $\phi(\mathbf{x})$, co pozostaje otwartym problemem dalszych rozdziałów.

### 1.4.3. Wyprowadzenie transformacji relatywistycznych z elasto-mechaniki sieci 0-Matrycy {#sec-1-4-3}

Transformacje współrzędnych oraz relacja równoważności energii i masy ($E = mc_{\perp}^2$) stanowią bezpośrednią konsekwencję oporu falowego podczas ruchu fal stojących (węzłów solitonowych) w gęstym, zniekształcalnym kontinuum krystalicznym.

#### 1.4.3.1. Konstrukcja prędkości i kontrakcja długości {#sec-1-4-3-1}

Dla zachowania rygoru pojęciowego definiujemy dwie komplementarne reprezentacje prędkości makroskopowej:

1. Prędkość współrzędnościowa tła ($v$): wyraża zmianę pozycji względem statycznej sieci referencyjnej:
$$v = \frac{dx}{dt_{\text{flat}}}$$ {#eq-1-4-3-vtla}
2. Prędkość własna węzła ($q$): mierzona czasem lokalnym ulegającym dylatacji:
$$q = \frac{dx}{dt}$$ {#eq-1-4-3-vwezla}

Związek transformacyjny między nimi wynika bezpośrednio z mechanizmu spiętrzenia osnowy ($dt = dt_{\text{flat}} / \gamma$):

$$q = \frac{dx}{\frac{dt_{\text{flat}}}{\gamma}} = \gamma \cdot v = \frac{v}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$ {#eq-1-4-3-wz1}

Gdy prędkość współrzędnościowa zbliża się do poprzecznej granicy ścinania osnowy ($v_\text{00} \to c_{\perp}$), narastająca inercja topologiczna sprawia, że czynnik $\gamma \to \infty$, podczas gdy prędkość własna $q \to \infty$. To rozróżnienie naturalnie eliminuje paradoks nieskończonej prędkości kinematycznej w ujęciu bezwzględnym.

Ruch węzła generuje przed obiektem front kompresji elastycznej. Wprowadzając współrzędną uciekającą $u = x - vt_{\text{flat}}$, przekształcenie jednorodnego równania falowego dla zachowania niezmienniczości kształtu solitonu wymusza przeskalowanie osi przestrzennej wzdłuż wektora pędu:

$$x' = \frac{u}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} = \gamma (x - vt_{\text{flat}})$$ {#eq-1-4-6}

Pod wpływem tego jednostronnego oporu elasto-mechanicznego, kształt każdego węzła solitonowego ulega rzeczywistej kompresji mechanicznej, co makroskopowo manifestuje się jako skrócenie długości w kierunku ruchu: $L' = L / \gamma$.

### 1.4.4. Energia, pęd i masa relatywistyczna {#sec-1-4-4}

Energia deformacji elastycznej węzła (której bazowym ekwiwalentem jest masa spoczynkowa $m_0$) proporcjonalnie wibruje z nałożonym obciążeniem gęstości osnowy. Ponieważ dla poruszającego się układu zachodzi spiętrzenie pola gęstości $\langle\phi(v)\rangle_{\text{macro}} = \phi_0\gamma$, masa relatywistyczna — rozumiana jako chwilowa, efektywna inercja topologiczna solitonowego węzła — skaluje się jako:

$$m = \gamma m_0 = \frac{m_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}}$$ {#eq-1-4-7}

Pęd niesiony przez przemieszczającą się deformację przyjmuje postać sprzężoną z prędkością własną $q$:

$$p = m_0 \frac{dx}{dt} = m_0 q = \gamma m_0 v$$ {#eq-1-4-8}

Różniczkując pęd po czasie płaskiego tła ($t_{\text{flat}}$), otrzymujemy dynamiczne równanie siły, które odsłania mechanizm asymptotycznego oporu sieci:

$$F = \frac{dp}{dt_{\text{flat}}} = \frac{d}{dt_{\text{flat}}}(\gamma m_0 v) = m_0 \gamma^3 \frac{d^2 x}{dt_{\text{flat}}^2} = m_0 \gamma^3 a$$  {#eq-1-4-9}

 *(Powyższe przejście zakłada ruch jednowymiarowy wzdłuż kierunku propagacji solitonu, zgodnie z konwencją całego §1.4.3–1.4.4; dla składowej siły prostopadłej do $v$ czynnik skalujący wynosiłby $\gamma^1$, nie $\gamma^3$.)*

Aby wykazać równoważność masy i energii bezpośrednio z mechaniki środowiska ciągłego, zdefiniujmy przyrost makroskopowej energii kinetycznej ($E_k$) jako pracę wykonaną przez siłę $F$ podczas przyspieszania węzła od stanu spoczynku ($v=0$) do prędkości $v$ na drodze $x$:

$$E_k = \int_0^x F \, dx' = \int_0^t F v \, dt_{\text{flat}}'$$ {#eq-1-4-10}

Podstawiając do całki elasto-mechaniczne równanie siły (@eq-1-4-9), transformujemy zmienną całkowania z czasu na prędkość współrzędnościową:

$$E_k = \int_0^v \left( m_0 \gamma^3 \frac{dv'}{dt_{\text{flat}}'} \right) v \, dt_{\text{flat}}' = m_0 \int_0^v \gamma^3 v' \, dv'$$ {#eq-1-4-11}

Rozpisując jawnie czynnik Lorentza $\gamma$, otrzymujemy całkę, którą rozwiązujemy przez rygorystyczne podstawienie:

$$E_k = m_0 \int_0^v \frac{v'}{\left(1 - \frac{v'^2}{c_{\perp}^2}\right)^{3/2}} \, dv'$$ {#eq-1-4-12}

Wynikiem tego całkowania jest bezpośrednia zależność energii kinetycznej od konfiguracji kompresyjnej sieci:

$$E_k = \left[ \frac{m_0 c_{\perp}^2}{\sqrt{1 - \frac{v'^2}{c_{\perp}^2}}} \right]_0^v = \frac{m_0 c_{\perp}^2}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} - m_0 c_{\perp}^2 = \gamma m_0 c_{\perp}^2 - m_0 c_{\perp}^2$$ {#eq-1-4-13}

Zgodnie z aksjomatyką TSM, stan zbiegający do spoczynku ($v=0$, czyli $\gamma=1$) nie oznacza zerowej energii kontinuum. Każdy węzeł solitonowy, aby w ogóle istnieć w gęstej sieci krystalicznej, wymaga permanentnego, lokalnego naciągnięcia sfer oddziaływań 0-Cząstek. Energia tego spoczynkowego naciągnięcia stanowi wrodzoną energię strukturalną Substratu: $E_0 = m_0 c_{\perp}^2$.

Definiując całkowitą energię relatywistyczną układu ($E$) jako sumę energii kinetycznej (pracy wprowadzonej do sieci) oraz energii spoczynkowej (wrodzonej geometrii węzła), otrzymujemy pełne wyprowadzenie relacji Einsteina:

$$E = E_k + E_0 = (\gamma m_0 c_{\perp}^2 - m_0 c_{\perp}^2) + m_0 c_{\perp}^2 = \gamma m_0 c_{\perp}^2$$ {#eq-1-4-14}

Biorąc pod uwagę relatywistyczne skalowanie masy inercyjnej zdefiniowane w @eq-1-4-7, powyższe równanie sprowadza się do ostatecznej, poszukiwanej formy równoważności masowo-energetycznej kontinuum:

$$E = m c_{\perp}^2$$ {#eq-1-4-15}

Gdy prędkość współrzędnościowa zbliża się do poprzecznej granicy ścinania ($v \to c_{\perp}$), praca wymagana do dalszej kompresji frontu falowego dąży do nieskończoności. Z matematycznego sprzężenia równań całkowitej energii (@eq-1-4-14) oraz pędu fali stojącej (@eq-1-4-8) wynika niezmiennicza relacja dyspersyjna inercji sieci, potwierdzająca bezstratny charakter propagacji.

Bezpośrednie podstawienie $E=\gamma m_0 c_\perp^2$ oraz $p=\gamma m_0 v$ daje:
$$E^2-(pc_\perp)^2=\gamma^2 m_0^2 c_\perp^2(c_\perp^2-v^2)=\gamma^2 m_0^2 c_\perp^4\left(1-\frac{v^2}{c_\perp^2}\right)=m_0^2c_\perp^4$$ {#eq-1-4-16przed}

skąd natychmiast:

$$E^2 = (pc_{\perp})^2 + (m_0 c_{\perp}^2)^2$$ {#eq-1-4-16}

### 1.4.5. Stałe materiałowe osnowy a lokalna zmienność propagacji fal ($c_{\perp}$) {#sec-1-4-5}

Prędkość światła nie jest stałą uniwersalną; wynika bezpośrednio z nieliniowego zjawiska akustoelastyczności gęstego kontinuum. W obszarze poddanym napięciu mechanicznemu ($\Sigma$), lokalna prędkość fal poprzecznych $c_{\perp,\text{lok}}$ modulowana jest przez sztywność nieliniową (stałe Murnaghana $\mathcal{A}$):

$$c_{\perp,\text{lok}}^2 = \frac{\mu}{\rho_{\text{eff}}^{(0)}} \left( 1 + \mathcal{A} \Sigma \right) = c_{\perp}^2 \left( 1 + \mathcal{A} \Sigma \right)$$ {#eq-zmiennosc-c}

Stała akustoelastyczna $\mathcal{A}$ ma wymiar odwrotności naprężenia $[\text{Pa}^{-1}]$, zapewniając bezwymiarowość członu $\mathcal{A}\Sigma$; jej związek z bezwymiarowymi stałymi trzeciego rzędu Murnaghana realizuje się poprzez normalizację do modułu ścinania: $\mathcal{A} = \tilde{\mathcal{A}}/\mu$, gdzie $\tilde{\mathcal{A}}$ jest bezwymiarową stałą materiałową. Jawna postać tego związku pozostaje fenomenologicznie otwarta.

Aby przejść od ogólnego naprężenia mechanicznego $\Sigma$ do konkretnych źródeł fizycznych (pole magnetyczne, potencjał grawitacyjny), identyfikujemy $\Sigma$ z odpowiednim tensorem naprężeń pochodzącym od danego oddziaływania:

**Wkład pola magnetycznego.** Naprężenie Maxwella generowane przez pole $B$ w ośrodku wynosi $\Sigma_B = B^2/(2\mu_{\rm em})$, gdzie $\mu_{\rm em}$ oznacza przenikalność magnetyczną próżni (symbol wyróżniony od modułu ścinania Lamégo $\mu$ stosowanego w całym rozdziale). Podstawiając do ( @eq-zmiennosc-c):

$$c_{\perp,\text{lok}}^2 \approx c_{\perp}^2\left(1 + \mathcal{A}\frac{B^2}{2\mu_{\rm em}}\right)$$ {#eq-1-4-5-wz1}

**Wkład potencjału grawitacyjnego.** Z relacji gęstości @sec-1-4-2-1 (@eq-14-3), $\phi(\mathbf{x})\approx\phi_0(1+|\Phi|/c_\perp^2)$, oraz mostu gęstości $\rho_{\text{eff}}=\rho_0\cdot\phi/\phi_0$ wprowadzonego w @sec-1-5-1, otrzymujemy $\rho_{\text{eff}}(\mathbf{x})\approx\rho_0(1+|\Phi|/c_\perp^2)$. Ponieważ $c_{\perp,\text{lok}}^2=\mu/\rho_{\text{eff}}$, rozwinięcie do pierwszego rzędu daje:

$$c_{\perp,\text{lok}}^2 \approx \frac{\mu}{\rho_0}\left(1 - \frac{|\Phi|}{c_\perp^2}\right)$$ {#eq-1-4-5-wz2}

Przyjmujemy tu standardową konwencję znaku potencjału grawitacyjnego: $\Phi\le0$ dla pola przyciągającego, skąd $|\Phi|=-\Phi$. Łącząc oba wkłady i przechodząc do zapisu elektrodynamicznego ($c_{\perp,\text{lok}}=1/\sqrt{\epsilon_{\text{eff}}\mu_0}$, gdzie $\epsilon_{\text{eff}}\propto 1/c_{\perp,\text{lok}}^2$), otrzymujemy efektywną przenikalność wyrażoną już w zmiennej $\Phi$ ze znakiem (a nie $|\Phi|$):

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 - \kappa B^2 + \beta_\Phi \frac{\Phi}{c_{\perp}^2} + \dots\right)$$ {#eq-1-4-5-wz3}

ze stałą sprzężenia magnetycznego jawnie wyrażoną przez stałą Murnaghana:

$$\kappa = \frac{\mathcal{A}}{2\mu_{\rm em}}$$ {#eq-1-4-5-wz4}

Współczynnik grawitacyjny wynosi $\beta_\Phi=-1$: ponieważ $|\Phi|/c_\perp^2=-\Phi/c_\perp^2$ przy przyjętej konwencji $\Phi\le0$, podstawienie $|\Phi|\to-\Phi$ we wzorze na $\epsilon_{\text{eff}}$ daje wprost współczynnik $-1$ przy zmiennej $\Phi$. Wartość ta wynika zatem z liniowej relacji gęstości $\rho_{\text{eff}}(\Phi)$ (a nie z mechanizmu akustoelastycznego $\mathcal{A}\Sigma$) i w obecnym ujęciu modelu jest stałą niezależną od $\mathcal{A}$. Pełna redukcja obu stałych do wspólnego źródła $\mathcal{A}$ wymagałaby wykazania, że gradient gęstości wywołany przez $\Phi$ jest fizycznie równoważny naprężeniu Murnaghana — co pozostaje otwartym problemem badawczym tego rozdziału.

Jak widać w modelu TSM dotychczasowe bezwymiarowe stałe fizyczne tracą swój abstrakcyjny status, stając się parametrami mechanotermodynamicznymi i stałymi materiałowymi 4‑wymiarowego kontinuum, jawnie sprowadzalnymi do jednej, wspólnej stałej nieliniowości sprężystej $\mathcal{A}$.

### 1.4.6. Wnioski końcowe i synteza kinematyki TSM {#sec-1-4-6}

Wyprowadzenie nieliniowej kinematyki makroskopowej w ramach Mechaniki Substratu Topologicznego pozwala na sformułowanie czterech kluczowych wniosków, które redefiniują paradygmat relatywistyczny:

1. **Ontologiczna redukcja czasoprzestrzeni:** TSM udowadnia, że czasoprzestrzeń Minkowskiego nie jest samodzielną, pierwotną areną fizyczną. Czterowymiarowy formalizm relatywistyczny jest wyłącznie efektem matematycznym, wyłaniającym się z faktu, że czas makroskopowy jest parametrem operacyjnym sukcesji zmian (zależnym od lokalnej gęstości osnowy $\phi$), a mierzona przestrzeń to fizycznie ugięta i naciągnięta 3-brana.
2. **Mechanistyczny sens stałości prędkości światła:** Stałość prędkości światła ($c_{\perp}$) w próżni przestaje być bezwarunkowym, aksjomatycznym postulatem kinematycznym. Staje się ona fizyczną, stałą materiałową zdegenerowanej sieci 0-Matrycy — graniczną prędkością propagacji poprzecznych fal akustycznych (ścinania) w sprężystym szkle topologicznym.
3. **Fizykalność kontrakcji i dylatacji:** Kontrakcja długości Lorentza ($L'=L/\gamma$) oraz kinematyczna dylatacja czasu nie są iluzjami perspektywicznymi wynikającymi z abstrakcyjnej geometrii układów odniesienia. Są to realne, elasto-mechaniczne deformacje. Ruch struktury solitonowej generuje fizyczne spiętrzenie osnowy wokół węzłów, co zwiększa opór relaksacyjny sieci i obiektywnie spowalnia wszelkie wewnętrzne procesy okresowe (zegary) poruszającego się ciała.
4. **Jedność grawitacji i inercji:** Poprzez tożsamość mianowników w relacjach dylatacji kinematycznej (@eq-1-4-2) i grawitacyjnej (@eq-1-4-4), TSM unifikuje oba zjawiska na poziomie mikroskopowym. Niezależnie od tego, czy lokalny wzrost gęstości osnowy $\langle\phi\rangle_{\text{macro}}$ jest wywołany ugięciem brany w czwartym wymiarze przez masę centralną (grawitacja), czy też konstruktywnym spiętrzeniem frontu falowego przez ruch własny solitonu (kinematyka), efekt temporalny jest identyczny, ponieważ aparat pomiarowy reaguje wyłącznie na wypadkowe, bezwzględne upakowanie komórek 0-Matrycy.

</br>

## 1.5. Dynamika falowa Substratu i podwójny reżim elasto‑dynamiki {#sec-1-5}

Mechanika Substratu podlega uogólnionemu formalizmowi Lagrange’a, asymilując rozwiązania matematyczne Ogólnej Teorii Względności, lecz bez jej relatywistycznych założeń ontologicznych. Przestrzeń i jej dynamika nie są geometryczną abstrakcją, lecz konsekwencją stanów fizycznych sieci krystalicznej 0-Matrycy.

### 1.5.1. Równania pola osnowy jako opis stanów naprężeń sieci {#sec-1-5-1}

Gęstość lagrangianu $\mathcal{L}$ izotropowej 3-brany stanowi różnicę gęstości energii kinetycznej i potencjalnej sprężystej. Wykorzystując tensor modułów sprężystości $K^{abcd}$, kontinuum modelujemy w reżimie niskich odkształceń za pomocą rozwinięcia:

$$\mathcal{L} = \frac{1}{2}\rho_{\text{eff}} \, \delta_{ab} \frac{\partial u^a}{\partial t_{\text{flat}}} \frac{\partial u^b}{\partial t_{\text{flat}}} - \frac{1}{2}K^{abcd}\epsilon_{ab}\epsilon_{cd} + \mathcal{O}(\epsilon^3)$$ {#eq-1-5-1}

gdzie pierwszy człon opisuje gęstość energii kinetycznej pola przemieszczeń, a drugi — gęstość energii potencjalnej sprężystej $\mathcal{U}$.

Gdzie tensor małych odkształceń $\epsilon_{ab}$ wyznacza się z pola przemieszczeń osnowy $u$:

$$\epsilon_{ab} = \frac{1}{2}(\nabla_a u_b + \nabla_b u_a)$$ {#eq-1-5-2}

Właściwości makroskopowe zawarte w tensorze $K^{abcd}$ oraz wynikający z nich tensor naprężeń $\sigma^{ab}$ wynikają bezpośrednio ze stanu elasto-mechanicznego uwięzionych, sub-planckowskich 0-Cząstek i ich sfer odpychania. Dla idealnie izotropowej sieci krystalicznej, tensor modułów sprężystości redukuje się do dwóch niezależnych stałych Lamego ($\lambda$ oraz $\mu$):

$$K^{abcd} = \lambda \delta^{ab}\delta^{cd} + \mu (\delta^{ac}\delta^{bd} + \delta^{ad}\delta^{bc})$$ {#eq-1-5-3}

gdzie $\delta^{ab}$ oznacza płaską, euklidesową metrykę tła Substratu. Pochodna lagrangianu względem tensora odkształcenia określa tensor naprężenia układu:

$$\sigma^{ab} = \frac{\partial \mathcal{L}}{\partial \epsilon_{ab}} = K^{abcd} \epsilon_{cd} = \lambda \delta^{ab} \epsilon^c_c + 2\mu \epsilon^{ab}$$ {#eq-1-5-4}

Pole $\phi(\mathbf{x})$ wprowadzone fenomenologicznie w @sec-1-2-2 jako splot mikroskopowego stopnia upakowania sieci z oknem filtracyjnym $W$ ( @eq-1-2-1-4) utożsamiamy w granicy continuum elastycznego z polem zdefiniowanym wprost przez lokalną dylatację objętościową ośrodka. To utożsamienie — analogiczne do standardowego związku między mikroskopową gęstością liczbową a makroskopową dywergencją przemieszczenia w klasycznej teorii sprężystości ośrodków ziarnistych — stanowi założenie konstytutywne modelu TSM, a nie twierdzenie wyprowadzone wprost z mikrodynamiki bilardu Sinaja ( @sec-1-1-1-1); jego ścisły dowód pozostaje otwartym problemem badawczym tego rozdziału, na równi z derywacją $c_\perp$ (@sec-1-4-5) i strukturą radialną solitonu (@sec-1-6-1).

*Uwaga o hierarchii progów:* W TSM obowiązuje ścisłe uporządkowanie $\phi_0 \le \phi_c < \phi_{\rm lock}$. Próg $\phi_c$ wyznacza globalny stan zakleszczenia sieci będący tłem fizycznym; próg $\phi_{\rm lock}$ jest lokalnym kryterium tworzenia trwałych węzłów topologicznych (materii) i zawsze przekracza $\phi_c$. Ilościowa relacja między tymi progami — oraz ich zależność od wymiaru przestrzeni i geometrii rdzeni — jest otwartym problemem ilościowym modelu.

Lokalną makroskopową gęstość osnowy $\phi$ definiujemy zatem jako funkcję stopnia lokalnego zagęszczenia lub rozrzedzenia komórek sieci, co matematycznie odpowiada śladowi tensora odkształceń (dylatacji objętościowej $\epsilon^c_c = \nabla \cdot \mathbf{u}$):

$$\phi = \phi_0 (1 - \epsilon^c_c) = \phi_0 (1 - \nabla \cdot \mathbf{u})$$  {#eq-1-5-5}

*Uwaga:* Wyrażenie (@eq-1-5-5) zakłada, że $\epsilon^c_c$ jest małe, lecz skończone — zgodnie z wyjaśnieniem w @sec-1-3-6, gdzie idealizacja $\lambda\to\infty$ z @sec-1-3-1 stanowi przybliżenie widma makroskopowego, nie limit ścisły. Rezydualna, skończona ściśliwość ($\lambda\gg\mu$, $\lambda<\infty$) w skali sub-planckowskiej pozwala $\epsilon^c_c$ przyjmować małe, niezerowe wartości, które generują obserwowalne gradienty $\phi$ odpowiedzialne za pole grawitacyjne.

gdzie $\phi_0$ to niezniekształcona, bazowa, **bezwymiarowa** gęstość upakowania 0-Matrycy w stanie równowagi. Ponieważ równanie ruchu Substratu wymaga współczynnika bezwładności o wymiarze gęstości masowej (a nie bezwymiarowego ułamka upakowania), wiążemy $\phi$ z jednorodną gęstością bezwładną $\rho_{\text{eff}}^{(0)}$ wyprowadzoną mikroskopowo w §1.3.3 (@eq-1-3-3-wz5) prostą proporcją:

$$\rho_{\text{eff}}(\mathbf{x}) = \rho_{\text{eff}}^{(0)} \cdot \frac{\phi(\mathbf{x})}{\phi_0}$$ {#eq-1-5-5b}

co w stanie równowagi ($\phi=\phi_0$) redukuje się do $\rho_{\text{eff}}=\rho_{\text{eff}}^{(0)}$, zgodnie z definicją mikrokinetyczną z §1.3.3. Należy podkreślić, że $\rho_{\text{eff}}^{(0)}\neq\rho_0$: surowa gęstość masowa rdzeni $\rho_0=m_{00}/V_0$ (§1.3.2) jest wielkością czysto materiałową, podczas gdy $\rho_{\text{eff}}^{(0)}=\rho_0\Gamma_{4D}^2$ uwzględnia dodatkowo żyroskopowy opór kaskadowej redystrybucji pędu w zakleszczonej sieci — i to właśnie ta druga wielkość poprawnie odtwarza zmierzoną wartość $c_\perp$.

Stosując zasadę najmniejszego działania Hamiltona ($\delta \int \mathcal{L} \, d^4x = 0$) względem pola przemieszczeń $u_a$, otrzymujemy dynamiczne równanie ruchu Substratu (odpowiednik równania Naviera-Cauchy’ego w środowisku ciągłym):

$$\rho_{\text{eff}} \frac{\partial^2 u^a}{\partial t_{\text{flat}}^2} = \nabla_b \sigma^{ab} = (\lambda + \mu) \nabla^a (\nabla \cdot \mathbf{u}) + \mu \nabla^2 u^a$$ {#eq-1-5-6}

Zgodnie z mechaniką ośrodków krystalicznych, pole przemieszczeń $u^a$ można jednoznacznie rozłożyć (dekompozycja Helmholtza) na składową bezrotacyjną (fale podłużne) oraz bezdywergencyjną (fale poprzeczne ścinania): $\mathbf{u} = \nabla \varphi_{\rm H} + \nabla \times \mathbf{\Psi}$, gdzie $\varphi_{\rm H}$ jest skalarnym potencjałem dekompozycji (symbol wyróżniony od grawitacyjnego $\Phi$ z @sec-1-4-2-1). Podstawiając ten rozkład do równania ruchu (@eq-1-5-6) dla składowej poprzecznej $\mathbf{\Psi}$ (gdzie $\nabla \cdot \mathbf{\Psi} = 0$), otrzymujemy czyste, jednorodne równanie falowe:

$$\nabla^2 \mathbf{\Psi} - \frac{\rho_{\text{eff}}}{\mu} \frac{\partial^2 \mathbf{\Psi}}{\partial t_{\text{flat}}^2} = 0$$ {#eq-1-5-7}

Powyższe podstawienie rygorystycznie definiuje poprzeczną prędkość fali ścinania jako fundamentalną stałą materiałową sieci: $c_{\perp} = \sqrt{\mu / \rho_{\text{eff}}}$ — zgodnie z definicją wyprowadzoną już mikroskopowo w §1.3.1–1.3.4.
W ogólnym przypadku, w obecności trwałych zniekształceń sieci (węzłów), dowolna funkcja składowych pola odkształceń poprzecznych $\psi \in \mathbf{\Psi}$ spełnia niejednorodne równanie falowe:

$$\nabla^2 \psi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \psi}{\partial t_{\text{flat}}^2} = \mathcal{S}(\mathbf{x}, t_{\text{flat}})$$ {#eq-1-5-8}

gdzie $\mathcal{S}(\mathbf{x}, t_{\text{flat}})$ to funkcja źródła, reprezentująca gęstość nieliniowych odkształceń topologicznych.

Relacja ta nie jest niezależnym postulatem, lecz liniową granicą pełnej, nieliniowej metryki deformacyjnej wprowadzonej w §1.4.1 (@eq-1-4-1). Pomijając człon kwadratowy $\delta_{cd}\nabla_a u_c\nabla_b u_d$ (uzasadnione w reżimie małych odkształceń, $|\nabla u|\ll1$, identycznym z założeniem liniowości przyjętym w (@eq-1-5-1)), metryka redukuje się do:

$$g_{ab} \approx \delta_{ab} + 2\epsilon_{ab}$$ {#eq-1-5-9}

gdzie $\epsilon_{ab}$ to tensor małych odkształceń zdefiniowany w eq-1-5-2. W reżimie lokalnej nieściśliwości ustalonym już w §1.3.1 ($\lambda\to\infty$, $\nabla\cdot\mathbf{u}=\epsilon^c_c\to0$), prawo konstytutywne (eq-1-5-4) upraszcza się do $\sigma_{ab}=2\mu\epsilon_{ab}$, skąd $\epsilon_{ab}=\sigma_{ab}/(2\mu)$. Podstawiając:

$$g_{ab} = \delta_{ab} + \frac{1}{\mu}\sigma_{ab}$$ {#eq-1-5-9a}

Powyższe odtwarza postać liniowego sprzężenia konstytutywnego TSM

$$g_{ab} = \delta_{ab} - \chi\sigma_{ab}$$ {#eq-1-5-9b}

z makroskopową podatnością elastyczną Substratu jednoznacznie wyrażoną przez moduł ścinania: $\chi \equiv -1/\mu$. *(Znak współczynnika $\chi$ zależy od przyjętej konwencji znaku naprężenia $\sigma_{ab}$ — w tym tekście konwencja $T^{(0)}_{IJ}=-P_0\delta_{IJ}$ z §1.1.2 implikuje, że naprężenie kompresyjne jest ujemne; w tej konwencji $\chi=-1/\mu$ daje fizycznie poprawny kierunek: kompresja zwiększa $g_{ab}$. Jeśli przyjmujesz odwrotną konwencję znaku $\sigma_{ab}$ w Rozdz. 3, zweryfikuj spójność znaku tutaj.)* W ten sposób grawitacja wyłania się jako liniowa aproksymacja tego samego pola naprężeń, które w pełnej, nieliniowej postaci opisuje eq-1-4-1 — eliminując potrzebę zakrzywiania samej pierwotnej ontologii przestrzeni.

### 1.5.2. Fale sprężyste a nieliniowa blokada topologiczna {#sec-1-5-2}

W idealnie sprężystym ośrodku, który bezstratnie i symetrycznie rozprasza nadmiary lokalnego ciśnienia, formowanie jakichkolwiek trwałych, zlokalizowanych struktur materialnych (cząstek) byłoby niemożliwe. Aby zapobiec natychmiastowej relaksacji i dyspersji energii, mechanika TSM rozdziela dynamikę Substratu na dwa komplementarne reżimy fizyczne, ostro rozgraniczone krytycznym progiem zamrożenia geometrycznego, nazywanym **gęstością blokady topologicznej $\phi_{\text{lock}}$**.

#### 1.5.2.1. **Reżim I: Liniowa relaksacja akustyczna ($\phi < \phi_{\text{lock}}$)** {#sec-1-5-2-1}

Dopóki lokalna kompresja sieci nie przekracza progu stabilności geometrycznej klatek Wignera-Seitza ($\epsilon^c_c > \epsilon_{\text{crit}}$), Substrat zachowuje się jak idealne, liniowe kontinuum sprężyste. Odkształcenia komórek mają charakter zachowawczy – sfery odpychania ulegają przejściowej deformacji, lecz 0-Cząstki bezwzględnie zachowują nienaruszoną macierz swoich pierwotnych sąsiadów. Nadmiar lokalnego ciśnienia jest transferowany izotropowo na zewnątrz, a ośrodek skutecznie relaksuje energię poprzez propagację klasycznych fal poprzecznych z niezmienniczą prędkością materiałową $c_{\perp}$. W tym reżimie tło pozostaje bezmasową próżnią fizyczną.

#### 1.5.2.2. **Reżim II: Nieliniowa blokada topologiczna ($\phi \ge \phi_{\text{lock}}$)** {#sec-1-5-2-2}

Sytuacja zmienia się diametralnie, gdy lokalny układ komórek zostaje skompresowany poza granicę plastyczności geometrycznej ($\epsilon^c_c \le \epsilon_{\text{crit}}$). Klatki kinetyczne Wignera-Seitza doznają wówczas krytycznego zniekształcenia. W reżimie II indywidualne, nieskorelowane przeskoki 0-Cząstek są wzbronione; jedyną formą zmiany sąsiedztwa jest kolektywny przesuw opisany w [ @sec-1-1-1-3], który prowadzi do rearanżacji topologii 0-Matrycy.

Nieliniowe skrócenie osi komórek w strefie ekstremalnego ściskania aktywuje człony wyższego rzędu $\mathcal{O}(\epsilon^3)$ w lagrangianu (@eq-1-5-1), co wymusza trwałą rotację głównych kierunków naprężeń sprężystych. Zamiast sekwencyjnego przekazywania pędu na zewnątrz (relaksacja falowa), linie naprężeń zamykają się same w sobie, tworząc przestrzennie zablokowaną strukturę:

1. **Następuje kinetyczne i geometryczne ograniczenie swobody sfer oddziaływań 0-Cząstek.**
2. **Pola naprężeń zapętlają się w samopodtrzymujący się, rotacyjny splot, czyli mikroskopijny wir solitonowy.** Stan ten opisuje matematycznie niezerowy tensor wirowości mechanicznej $\Omega_{ab} = \frac{1}{2}(\nabla_a u_b - \nabla_b u_a)$, którego zamknięta cyrkulacja staje się niezmiennikiem topologicznym całego układu.
3. **Substrat w tym konkretnym obszarze całkowicie traci zdolność do uwalniania zgromadzonej energii poprzez zwykłą emisję fal akustycznych $c_{\perp}$.**

Powstaje nieliniowy węzeł topologiczny, który uzyskuje niezależną stabilność strukturalną. Jego rozplecenie lub zniszczenie wymagałoby ponownego dostarczenia energii wystarczającej do pokonania stanu granicznej kompresji, co stwarza potężną, skwantowaną barierę energetyczną. W ten sposób nieliniowa mechanika zniekształceń krystalicznych daje bezpośredni początek stabilnej, skwantowanej materii makroskopowej.

### 1.5.3. Podsumowanie dynamicznego dualizmu Substratu {#sec-1-5-3}

Wprowadzenie uogólnionego formalizmu elasto-dynamiki pozwala na jednoznaczne sformułowanie mechanicznej definicji przestrzeni i materii w TSM. Całość dynamicznych stanów 0-Matrycy można ująć w rygorystyczną strukturę komplementarną:

| Parametr / Cecha | Reżim I: Liniowa relaksacja akustyczna | Reżim II: Nieliniowa blokada topologiczna |
| --- | --- | --- |
| **Kryterium przejścia** | $\phi < \phi_{\text{lock}}$ \\ (równoważnie: $\epsilon^c_c > \epsilon_{\text{crit}}$, gdzie $\epsilon_{\text{crit}} \equiv 1 - \phi_\text{lock}/\phi_0 < 0$) | $\phi \ge \phi_{\text{lock}}$ \\ (równoważnie: $\epsilon^c_c \le \epsilon_{\text{crit}}$, gdzie $\epsilon_{\text{crit}} \equiv 1 - \phi_\text{lock}/\phi_0 < 0$) |
| **Stan klatek sieci** | Niskie, zachowawcze odkształcenia elastyczne. | Krytyczne, plastyczne zniekształcenie klatek Wignera-Seitza. |
| **Zachowanie 0-Cząstek** | Wibracje wewnątrz klatek; zachowanie pełnej macierzy pierwotnych sąsiadów. | Absolutne uwięzienie; trwała rotacja głównych kierunków naprężeń sprężystych. |
| **Transfer energii** | Swobodna, izotropowa emisja fal poprzecznych z prędkością materiałową $c_{\perp}$. | Brak możliwości liniowej emisji; zapętlenie linii naprężeń w rotacyjny splot. |
| **Matematyczny niezmiennik** | Jednorodne równanie hiperboliczne: \ $\nabla^2 \mathbf{\Psi} - \frac{1}{c_{\perp}^2}\frac{\partial^2\mathbf{\Psi}}{\partial t^2} = 0$ | Niezerowy tensor wirowości mechanicznej $\Omega_{ab} \neq 0$, którego zamknięta cyrkulacja przestrzenna jest skwantowanym niezmiennikiem topologicznym. |
| **Wyłoniony status fizyczny** | **Bezmasowa próżnia fizyczna** (tło propagacji fal elektromagnetycznych). | **Stabilna, skwantowana materia makroskopowa** (cząstki elementarne jako wezły). |

</br>

## 1.6. Aksjomat materii: Matematyczna struktura defektów, inercja i spin {#sec-1-6}

Pod wpływem ekstremalnej kompresji nieliniowej ($\phi(\mathbf{x}) \ge \phi_{\text{lock}}$), liniowe fluktuacje akustyczne tracą zdolność relaksacji falowej, a komórki sieci zmuszone są do geometrycznego zapętlenia. W 4-wymiarowym kontinuum Substratu formują się stabilne fale stojące (solitony), będące w istocie trwałymi węzłami topologicznymi, które fizyka makroskopowa identyfikuje jako fermiony. Węzły te są tworami w pełni 4-wymiarowymi – ich struktura rozciąga się również w czwarty wymiar przestrzenny ($x^4$), co ma merytoryczne znaczenie dla emergencji grawitacji oraz oddziaływań jądrowych.

### 1.6.1. Matematyczna struktura ładunku topologicznego i profilu solitonu {#sec-1-6-1}

Aby nadać pojęciu „skręcenia topologicznego” ścisły sens matematyczny, pole deformacji fazowej osnowy w otoczeniu defektu należy reprezentować jako ciągłe odwzorowanie gładkie z przestrzeni fizycznej $\mathbb{R}^3$ (uzupełnionej o punkt w nieskończoności, co daje topologicznie sferę $S^3$) w przestrzeń wewnętrznych stanów fazowych $SU(2) \cong S^3$. Niech $\mathbf{U}(\mathbf{x})$ będzie macierzowym polem unitarnym zdefiniowanym jako:

$$\mathbf{U}(\mathbf{x}) = \pi_0(\mathbf{x})\mathbb{I} + i \sum_{a=1}^3 \pi_a(\mathbf{x})\sigma_a$$ {#eq-1-6-wz1}

gdzie $\sigma_a$ są macierzami Pauliego, $\mathbb{I}$ jest macierzą jednostkową, a komponenty kwaternionowe pola $\pi_\mu(\mathbf{x})$ spełniają geometryczny warunek normalizacji $\sum_{\mu=0}^3 \pi_\mu^2 = 1$.

Ładunek topologiczny $\mathcal{W}$, stanowiący kandydaturę na zachowaną liczbę kwantową cząstki (w standardowej teorii Skyrmego odpowiadający liczbie barionowej; identyfikacja z ładunkiem elektrycznym jest postulatem modelu TSM wymagającym dalszego uzasadnienia w Rozdziale 3), jest niezmiennikiem reprezentującym stopień odwzorowania (indeks homotopijny $\pi_3(S^3)$) i dany jest jawnym wzorem całkowym:

$$\mathcal{W} = \frac{1}{24\pi^2} \int_{\mathbb{R}^3} d^3x \, \epsilon^{ijk} \text{Tr}\left[ (\mathbf{U}^{-1}\partial_i \mathbf{U}) (\mathbf{U}^{-1}\partial_j \mathbf{U}) (\mathbf{U}^{-1}\partial_k \mathbf{U}) \right]$$ {#eq-1-6-wz2-w}

gdzie $\epsilon^{ijk}$ jest całkowicie antysymetrycznym tensorem Leviego-Civity w trzech wymiarach, a $\partial_i \equiv \partial/\partial x^i$. Niezmiennik $\mathcal{W}$ przyjmuje wyłącznie wartości całkowite ($\mathcal{W} \in \mathbb{Z}$), co stanowi czysto geometryczną, pierwszą zasadę absolutnego kwantowania ładunku elementarnego w modelu TSM.

Klasyczne twierdzenie Derricka postuluje, że trójwymiarowe solitony w liniowych teoriach polowych są niestabilne i samorzutnie zapadają się do punktu. W modelu TSM problem ten zostaje rozwiązany geometrycznie: próba dalszego kurczenia się solitonu wywołuje asymptotyczny wzrost energii naprężeń ścinających. Wynika to z faktu, że lokalna gęstość deformacji zbliża się do progu zakleszczenia strukturalnego $\phi_{\text{lock}}$, przy którym efektywny moduł sztywności dąży do nieskończoności. Ta geometryczna blokada zatrzymuje kolaps, stabilizując skończony rozmiar spoczynkowy rdzenia solitonu $L$.

Dynamika stabilizacji przestrzennej wynika bezpośrednio z bilansu pomiędzy dalekosiężną energią elastyczną a nieliniowym potencjałem periodycznym sieci. W pełnym ujęciu trójwymiarowym, dla zachowania sferycznej symetrii izolowanego defektu statycznego, wprowadza się tzw. ansatz jeża (*Hedgehog ansatz*), będący szczególnym, radialnie symetrycznym rozwiązaniem powyższej ogólnej postaci pola — odpowiadającym podstawieniu $\pi_0(\mathbf{x})=\cos\theta(r)$ oraz $\pi_a(\mathbf{x})=\hat{x}_a\sin\theta(r)$, co automatycznie spełnia warunek normalizacji $\sum_\mu\pi_\mu^2=1$. Macierzowe pole unitarne przyjmuje wówczas jawną postać radialną:

$$\mathbf{U}(\mathbf{x}) = \cos\theta(r)\mathbb{I} + i (\hat{\mathbf{x}} \cdot \boldsymbol{\sigma}) \sin\theta(r)$$  {#eq-1-6-wz3}

gdzie $r = |\mathbf{x}|$ reprezentuje odległość od centrum defektu, $\hat{\mathbf{x}} = \mathbf{x}/r$ jest radialnym wektorem jednostkowym, a $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ oznacza wektor macierzy Pauliego. Profil fazowy $\theta(r)$ określa przestrzenną strukturę rdzenia solitonu, a całkowita masa spoczynkowa $m_0$ wynika bezpośrednio z objętościowego całkowania trójwymiarowej gęstości energii sprężystej $\rho_{E}(\mathbf{x})$ we współrzędnych sferycznych:

$$m_0 = \int_{\mathbb{R}^3} \rho_{E}(\mathbf{x}) \, d^3x = 4\pi \int_{0}^{\infty} \rho_{E}(r) r^2 \, dr$$  {#eq-1-6-wz4-mspocz}

Ścisłe równanie różniczkowe dla profilu radialnego $\theta(r)$, wynikające z pełnego laplasjanu sferycznego w $\mathbb{R}^3$, zawiera dodatkowy człon krzywiznowy $\frac{2}{r}\theta'(r)$, nieobecny w jednowymiarowej redukcji rozpatrywanej poniżej. Z tego względu wzór na $m_0$ powyżej, choć formalnie ścisły, w ogólności wymaga numerycznego lub przybliżonego rozwiązania $\theta(r)$ tego pełnego równania radialnego, a nie bezpośredniego podstawienia profilu $\theta(x)$ uzyskanego w redukcji jednowymiarowej.

Aby uzyskać analityczne, zamknięte rozwiązania dla profili przejścia fazowego oraz przeanalizować zachowanie defektu poruszającego się wzdłuż określonej osi, dokonuje się redukcji wymiarowej do ujęcia jednowymiarowego, rozpatrując przekrój wzdłuż trajektorii propagacji falowej. Profil $\theta(x)$ i odpowiadająca mu gęstość $\rho_E(x)$, wyprowadzone poniżej w tym ujęciu zredukowanym, stosujemy następnie w całce masowej $m_0$ jako przybliżenie obowiązujące w obszarze rdzenia solitonu z dala od osobliwości krzywizny w $r=0$ — gdzie krzywizna radialna jest pomijalna względem gradientu fazowego. Ścisłe domknięcie pełnego, trójwymiarowego profilu radialnego $\theta(r)$ pozostaje otwartym problemem matematycznym tego rozdziału, analogicznym do pozostałych zidentyfikowanych powyżej (derywacja $c_\perp$ w reżimie zmiennym, §1.4.5; związek $\phi_{\text{eff}}(\mathbf{x})$ z mikrodynamiką, §1.5.1).

W tym ujęciu przestrzenną ewolucję lokalnego kąta skrętu fazowego $\theta(x)$ opisuje nieliniowe równanie różniczkowe typu Sine-Gordon:

$$\frac{\partial^2 \theta}{\partial x^2} - \frac{\rho_{\text{eff}}}{\mu}\frac{\partial^2 \theta}{\partial t_{\text{flat}}^2} = \frac{1}{L^2} \sin(\theta)$$  {#eq-1-6-wz5-kat-skret}

Dla solitonu statycznego ($\partial_t \theta = 0$) niosącego elementarny ładunek topologiczny $\mathcal{W}=1$, rozwiązaniem analitycznym wyznaczającym profil przejścia fazowego w osnowie jest struktura kinku:

$$\theta(x) = 4 \arctan\left( \exp\left( \frac{x - x_0}{L} \right) \right)$$  {#eq-1-6-wz6-kinku}

Gęstość energii sprężystej $\rho_{E}(x)$ zablokowana wewnątrz tego defektu przyjmuje rygorystyczną postać:

$$\rho_{E}(x) = \frac{\mu}{2} \left( \frac{\partial \theta}{\partial x} \right)^2 + \frac{\mu}{L^2} (1 - \cos\theta) = \frac{4\mu}{L^2} \text{sech}^2\left(\frac{x - x_0}{L}\right)$$  {#eq-1-6-wz7-esprez}

Architektura Substratu w sposób rygorystyczny rozdziela dwie fundamentalne cechy defektu:

* **Ładunek elektryczny:** Skwantowany topologicznie niezmiennik $\mathcal{W}$, zależny wyłącznie od domknięcia pełnego obrotu fazowego w przestrzeni i topologicznej niezmienniczości odwzorowania.
* **Masa spoczynkowa:** Zintegrowana energia potencjalna lokalnych naprężeń sprężystych osnowy. Bardziej złożony, gęstszy splot topologiczny generuje silniejsze gradienty pola fazowego, co wymusza zmagazynowanie większej energii $m_0$ w rdzeniu, pomimo możliwości niesienia takiego samego elementarnego ładunku topologicznego.

### 1.6.2. Elastodynamiczny opór jako źródło bezwładności {#sec-1-6-2}

Gdy soliton przemieszcza się przez dyskretną strukturę 0-Matrycy, ciągłość translacyjna tła zostaje przełamana przez potencjał błędu dopasowania krystalicznej sieci. Energię aktywacji tej bariery (potencjał Peierlsa-Nabarro) opisuje funkcja:

$$U_{\text{PN}}(b) = U_0 \cos\left( \frac{2\pi b}{a} \right)$$ {#eq-1-6-wz8-enaktyw}

gdzie $b$ określa przesunięcie środka solitonu względem najbliższego węzła sieci o stałej $a$. Amplituda bariery $U_0$ maleje wykładniczo wraz ze wzrostem stosunku $L/a$.

**Przypomnijmy:**

Ruch solitonu nie polega na fizycznej translacji elementów przez ośrodek, lecz na sekwencyjnym, bezstratnym transferze stanu odkształcenia (fali) z jednej komórki sieci do sąsiedniej. Ponieważ rozmiar rdzenia węzła $L$ (skala femtometrowa) przewyższa odległość między elementami Substratu $a$ (skala sub-planckowska) o wiele rzędów wielkości, amplituda bariery $U_0$ dąży asymptotycznie do zera. Zapewnia to makroskopowo płynny ruch zjawiskowy.

Opór pojawia się wyłącznie przy próbie zmiany stanu ruchu – konieczność lokalnej, fonicznej reorganizacji pędów wibrujących elementów krystalicznego Substratu podczas akceleracji fali deformacji generuje hydrodynamiczny opór ośrodka, obserwowany w makroskali jako **bezwładność** (inercja).

### 1.6.3. Wyjaśnienie metody geometryczno-falowej {#sec-1-6-3}

Wprowadzenie całki stopnia odwzorowania ładunku topologicznego usuwa heurystyczny charakter opisu cząstek. Z matematycznego punktu widzenia, niezmiennik ten gwarantuje, że profil pola nie może ulec ciągłej deformacji do stanu próżni ($\mathbf{U}=\mathbb{I}$) bez rozerwania ciągłości Substratu, co zapewnia absolutną trwałość materii. Równanie falowe Sine-Gordon oraz gęstość energii dają z kolei bezpośredni pomost analityczny do interpretacji masy spoczynkowej jako zmagazynowanej energii sprężystej tła, jawnie łącząc opis całkowy w $\mathbb{R}^3$ ze zredukowanymi modelami trajektorii jednowymiarowych.

### 1.6.4. Geometryczne pochodzenie spinu 1/2 i ontologia antymaterii {#sec-1-6-4}

Uwięzienie solitonu w ciągłym, elastycznym medium nakłada specyficzne warunki brzegowe na jego rotację. Defekt opisany macierzowym polem unitarnym $\mathbf{U}(\mathbf{x}) \in SU(2)$ wymaga obrotu w przestrzeni fizycznej o kąt $4\pi$ ($720^\circ$), aby trójwymiarowe linie odkształceń otaczającego tła mogły samorzutnie powrócić do stanu zerowego naprężenia (rozsupłać się). Przestrzeń konfiguracji obrotów dla tego typu topologicznych obiektów jest dwukrotnie nakrywana przez grupę spinorową, co sprawia, że spin 1/2 staje się bezpośrednią mechaniczną konsekwencją topologii ciągłego Substratu.

Model TSM redefiniuje również ontologię antymaterii, eliminując koncepcję ujemnej energii czy ruchu wstecz w czasie:

* **Symetria chiralna:** Dla każdego węzła o dodatnim ładunku topologicznym $\mathcal{W} = +1$ istnieje lustrzana konfiguracja o odwróconej chiralności pola fazowego, dla której $\mathcal{W} = -1$.
* **Masa antymaterii:** Ponieważ gęstość energii sprężystej $\rho_{E}(x)$ zależy od kwadratu pochodnych przestrzennych pola, obie konfiguracje (cząstka i antycząstka) generują identyczny, dodatni wkład do masy spoczynkowej $m_0$.
* **Anihilacja:** Zderzenie cząstki z antycząstką stanowi proces topologicznej anihilacji. Wektorowe sploty sumują się do zerowego ładunku wypadkowego ($\mathcal{W}_{\text{net}} = 0$), co prowadzi do gwałtownego rozplątania lokalnych defektów i bezresztkowego uwolnienia zmagazynowanej energii sprężystej w postaci czystych fal poprzecznych osnowy (fotonów).
