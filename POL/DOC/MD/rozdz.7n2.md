<!-- ver:2.6.0 -->
# Rozdział 7: Oddziaływania subatomowe – hadrony jako pęcherzyki kawitacyjne, oddziaływanie słabe jako rozwęźlanie, hierarchia leptonów i determinizm kwantowy w TSM

W modelu Mechaniki Substratu Topologicznego (TSM) zjawiska subatomowe nie są opisane przez abstrakcyjne zbiory probabilistyczne i punktowe, bezwymiarowe cząstki zawieszone w próżni. Dynamika cząstek elementarnych to w istocie mechanika nieliniowych odkształceń, węzłów topologicznych oraz rezonansów falowych propagujących się w 4-wymiarowym, sprężystym kontinuum – 0-Matrycy. Niniejszy rozdział redefiniuje kluczowe zjawiska fizyki wysokich energii, sprowadzając je do rygorystycznych procesów z zakresu mechaniki ośrodków ciągłych, spójnych z czasem lokalnym $t$ (Rozdział 1.1) i topologiczną naturą materii (Rozdział 2).

# 7.0. Czas lokalny i formalizm elasto-dynamiczny Substratu

Wszystkie procesy opisywane w tym rozdziale – oscylacje kwarków, rozpady słabe, rezonanse i hierarchie masowe – zachodzą w lokalnym czasie własnym $t$, który wyłania się bezpośrednio z uśrednionej gęstości upakowania 0-Matrycy:

$$dt = dN \cdot T_0 \cdot \frac{\langle\phi\rangle_{\text{macro}}}{\phi_0} \tag{7.1}$$

Mikroskopowy stan przed-zakleszczeniowy (pre-jamming) i skończona sztywność objętościowa sieci Wignera-Seitza w 4D pozwalają na zdefiniowanie fundamentalnych pól opisujących stan deformacji osnowy. Stan ten reprezentowany jest przez znormalizowane pole wektorowe $\mathbf{n}(\mathbf{x})$ na trójwymiarowej branie oraz skalarną funkcję ugięcia ortogonalnego $\phi(\mathbf{x})$:

$$\mathbf{n}(\mathbf{x}) \in \mathbb{S}^2, \quad |\mathbf{n}| = 1 \tag{7.2}$$

$$\phi(\mathbf{x}) = \frac{\partial \mathbf{n}}{\partial x^4} \tag{7.3}$$

Gdzie $\phi(\mathbf{x})$ reprezentuje ugięcie (deformację) kontinuum wzdłuż dodatkowego, czwartego wymiaru przestrzennego $x^4$. Opór mechaniczny, jaki 0-Matryca stawia lokalnemu odkształceniu, określa Uniwersalna Stała Sztywności Substratu ($\mathcal{K}$), definiowana za pomocą jednostek Plancka:

$$\mathcal{K} = \frac{c^4}{G} \tag{7.4}$$

Wymiarowo stała $\mathcal{K}$ odpowiada sile Plancka (lub zintegrowanemu ciśnieniu Plancka $P_P$ na powierzchni kwadratu długości Plancka $l_P^2$). Kąt Weinberga $\theta_W$ oraz stała sprzężenia słabego $g$ stanowią makroskopowe parametry materiałowe tej osnowy, bezpośrednio wynikające ze sztywności $\mathcal{K}$.

Wewnątrz pęcherzyków kawitacyjnych oraz w pobliżu silnie skompresowanych rdzeni leptonowych efektywna gęstość $\langle\phi\rangle_{\text{macro}}$ drastycznie odbiega od wartości referencyjnej $\phi_0$. Oznacza to, że lokalne tempo upływu czasu (tempo relaksacji i cykli $dN$) jest przestrzennie niejednorodne. W zrelaksowanym wnętrzu hadronu czas płynie relatywnie szybciej niż na jego nieliniowej, silnie naprężonej ścianie granicznej lub w gęstym, wielokrotnie skręconym rdzeniu mionu.

## 7.1. Ontologia oddziaływania silnego i zmodyfikowany dowód stabilności dla stanu $\mathcal{W}=1$

Zgodnie z Rozdziałem 3.5, oddziaływanie silne (jądrowe) nie jest nową siłą fundamentalną, lecz bezpośrednim efektem topologicznego splątania węzłów w czwartym wymiarze przestrzennym ($x^4$). Gdy dwa hadrony (nukleony) zbliżają się do siebie na odległość rzędu femtometra ($\sim 1\text{ fm}$), ich części zanurzone w czwartym wymiarze ulegają mechanicznemu zazębieniu.

Linie naprężeń jednego węzła przeplatają się z liniami drugiego w wyższym wymiarze Bulk. Splątanie to generuje potężny, krótkozasięgowy poprzeczny naciąg 3-brany, który fizyka makroskopowa interpretuje jako przyciąganie jądrowe. Zjawisko to cechuje się:

Wysyceniem: Jeden węzeł w 4D może splątać się z ograniczoną geometrycznie liczbą sąsiadów (limit koordynacyjny sieci).

Niezależnością ładunkową: Splątanie zależy od pełnej struktury 4D, a nie od jej trójwymiarowego rzutu fazowego (ładunku elektrycznego).

Uwięzieniem (confinement) i swobodą asymptotyczną: Analizowanymi poniżej zperspektywy wewnętrznej struktury pojedynczego hadronu.

Tradycyjne ujęcie funkcjonalu energii solitonu oparte na uproszczonych modelach gradientowych sugerowało, że minimalny ładunek topologiczny (liczba Hopfa) zapewniający stabilność statyczną to $\mathcal{W} \ge 3$, podczas gdy stany $\mathcal{W}=1,2$ skazane były na wykładniczy zanik i rozmycie liniowe. W niniejszym sformułowaniu TSM ograniczenie to zostaje przezwyciężone poprzez uwzględnienie nieliniowego członu potencjału zakleszczenia (jamming) dla 0-cząstek o skończonej ściśliwości granicznej.

Pełny efektywny funkcjonał energii $E[\mathbf{n}]$ dla solitonowego węzła topologicznego o ładunku $\mathcal{W}$ przyjmuje postać:

$$E[\mathbf{n}] = \int_{\mathbb{R}^3} \left[ \frac{A}{2} (\nabla \mathbf{n})^2 + \frac{B}{2} (\nabla \mathbf{n})^4 + \frac{\mathcal{K}}{2} \phi(\mathbf{x})^2 + V_{\text{jam}}(\phi) \right] d^3x \tag{7.5}$$

Gdzie człon $(\nabla \mathbf{n})^2$ to klasyczna energia gradientowa, $(\nabla \mathbf{n})^4$ stanowi człon stabilizacyjny typu Skyrme'a zapobiegający kolapsowi punktowemu, natomiast kluczowy człon potencjału zakleszczenia $V_{\text{jam}}(\phi)$ definiujemy jako:

$$V_{\text{jam}}(\phi) = \frac{D \cdot \mathcal{W}^2}{\left(1 - \left(\frac{\phi}{\phi_{\max}}\right)^2\right)^n} \tag{7.6}$$

Gdzie $D$ to stała sprzężenia mikroskopowego, $\phi_{\max}$ to graniczne ugięcie ortogonalne odpowiadające maksymalnemu dopuszczalnemu zagęszczeniu (zakleszczeniu) sfer interakcji 0-cząstek, a $n \ge 2$ jest wykładnikiem nieliniowości strukturalnej. Wprowadzenie $V_{\text{jam}}(\phi)$ modyfikuje równanie ewolucji ładunku w globalnym parametrze zderzeniowym $\tau$:

$$\frac{dW}{d\tau} = -\frac{\delta E[\mathbf{n}]}{\delta \mathbf{n}} \tag{7.7}$$

Dzięki obecności bieguna asymptotycznego w $V_{\text{jam}}(\phi)$ przy $\phi \rightarrow \phi_{\max}$, dla stanu podstawowego $\mathcal{W}=1$ redukcja wariacyjna generuje głębokie, stabilne minimum lokalne (barierę potencjału). Uniemożliwia to relaksację ładunku do zera. Tym samym stan $\mathcal{W}=1$ staje się asymptotycznie trwały, stanowiąc podstawową cząstkę materii – elektron.

Geometryczne pochodzenie spinu połówkowego wyłania się bezpośrednio z definicji spinu hopfionu w TSM, skreślonego relacją:

$$s = \mathcal{W} - 2 \tag{7.8}$$

Dla elektronu o ładunku topologicznym $\mathcal{W}=1$ otrzymujemy $s = 1 - 2 = -1/2$, co precyzyjnie odtwarza połówkowy charakter spinu i statystykę Fermiego-Diraca (znak ujemny definiuje lewoskrętną chiralność stanu podstawowego).

## 7.2. Model kawitacyjny hadronu a Głębokie Rozpraszanie Nieelastyczne (DIS)

### 7.2.1. Hadron jako pęcherzyk kawitacyjny w 0-Matrycy

W TSM hadron (proton, neutron, mezon) to nie zbiór punktowych kwarków utrzymywanych w próżni, lecz lokalny obszar 4-wymiarowej 0-Matrycy, w którym gęstość naprężeń strukturalnych osiąga stan krytyczny, tworząc zamkniętą domenę – pęcherzyk kawitacyjny. Na zewnątrz pęcherzyka panuje podstawowe, wysokie ciśnienie zewnętrzne Matrycy ($\langle\phi\rangle_{\text{macro}} \approx \phi_0$), natomiast wewnątrz występuje stan częściowej relaksacji falowej ($\langle\phi\rangle_{\text{macro}} < \phi_0$).

Ściana pęcherzyka: To stromy, wysoce nieliniowy gradient naprężeń – kinetyczna bariera fazowa, która fizycznie izoluje wnętrze hadronu od reszty osnowy. Stabilność struktury hadronowej jest wyznaczana przez równowagę pomiędzy wewnętrznym napięciem powierzchniowym splotów a profilem ciśnienia hydrostatycznego pęcherzyka $p(r)$. Dla nukleonu o promieniu granicznym $r_0 \approx 0.84\, \text{fm}$ profil ciśnienia opisuje funkcja:

$$p(r) = P_{\text{sub}} \cdot \left[1 - \exp\left(-\frac{(r-r_0)^2}{\alpha^2}\right)\right] - P_{\text{max}} \cdot \operatorname{sech}^2\left(\frac{r}{\alpha}\right) \tag{7.9}$$

Gdzie $P_{\text{sub}}$ to ciśnienie tła Substratu, $P_{\text{max}}$ to maksymalne ciśnienie na sztywnej ściance granicznej pęcherzyka, a $\alpha$ stanowi stałą materiałową osnowy. Ciśnienie maleje od ścianki do geometrycznego centrum pęcherzyka, działając jako operator zaburzenia masowego dla zlokalizowanych w nim modów.

Szkielet topologiczny: Strukturę pęcherzyka stabilizuje fundamentalny defekt topologiczny – węzeł trójlistny ($3_1$), który w rzucie na 3-branę posiada trzy główne skrzyżowania (pętle naprężeń), odpowiadające trzem kwarkom walencyjnym.

Morze partoniczne: Wewnątrz zrelaksowanego pęcherzyka panuje intensywna turbulencja akustyczno-sprężysta – zbiór wyższych harmonicznych drgań samego węzła oraz uwięzionych fal stojących 0-Matrycy.

### 7.2.2. Interpretacja wyników DIS

Eksperymenty Głębokiego Rozpraszania Nieelastycznego (DIS) badają strukturę hadronów za pomocą sondy elektronowej o zmiennym przekazie pędu $Q^2$. W TSM wyniki te zyskują czysto hydrodynamiczną interpretację:

Niskie $Q^2$ (długa fala sondująca): Fala elektronu o niskiej energii nie jest w stanie rozróżnić drobnych turbulencji wewnątrz pęcherzyka. „Widzi” tylko trzy główne żyły szkieletu węzła $3_1$ i rozprasza się na kwarkach walencyjnych.

Wysokie $Q^2$ (krótka fala sondująca): Sonda o wysokiej energii wnika głęboko w mikrostrukturę pęcherzyka, rozpraszając się na gęstej pianie turbulentnych fluktuacji sprężystych – „morzu partonicznym”. Ewolucja funkcji rozkładu partonów (PDF) opisywana równaniami DGLAP nie odzwierciedla kreacji wirtualnych cząstek w próżni, lecz zmianę skali rozdzielczości widma drgań nieliniowego ośrodka sprężystego.

## 7.3. Uwięzienie topologiczne (Confinement)

W ontologii TSM uwięzienie kwarków nie wynika z wymiany hipotetycznych gluonów, lecz z mechaniki nieliniowego rozciągania ośrodka sprężystego. Kwarki są otwartymi fragmentami splotów (warkoczami), które z jednej strony tworzą rdzeń węzła $3_1$, a z drugiej – są fizycznie zakotwiczone w ścianie pęcherzyka kawitacyjnego, domykając obwód naprężeń wewnątrz hadronu.

Próba wyciągnięcia kwarka z pęcherzyka powoduje lokalne odkształcenie plastyczne ściany i wyciągnięcie jej w szyjkę – wydłużony strumień o ekstremalnym naprężeniu ścinającym. Energia potrzebna do rozciągania tej struktury rośnie liniowo z dystansem $r$:

$$E_{\text{conf}}(r) = \sigma \cdot r \tag{7.10}$$

gdzie:

$E_{\text{conf}}$ – energia uwięzienia $[\text{J}]$,

$\sigma$ – napięcie struny topologicznej $[\text{N}]$, będące bezpośrednią funkcją modułu sztywności 0-Matrycy,

$r$ – odległość między kwarkiem a resztą hadronu $[\text{m}]$.

Gdy zgromadzona energia sprężysta przekroczy próg plastyczności (równy $2 m_q c_{\perp}^2$), dochodzi do topologicznego pęknięcia continuum. Szyjka ulega gwałtownej relaksacji, a wolne końce natychmiast zwijają się, tworząc dwa nowe, zamknięte pęcherzyki – parę kwark-antykwark. Jest to mechaniczny obraz hadronizacji i powstawania dżetów w zderzeniach akceleratorowych.

## 7.4. Asymptotyczna swoboda

Zjawisko słabnięcia oddziaływań między kwarkami na małych dystansach wynika bezpośrednio z geometrii pęcherzyka kawitacyjnego. W miarę jak kwarki zbliżają się do geometrycznego środka hadronu, oddalają się od nieliniowej ściany naprężeń. Ponieważ wnętrze pęcherzyka jest obszarem zrelaksowanym, efektywne naprężenie ścinające między warkoczami dąży lokalnie do zera.

Obserwowany w QCD spadek stałej sprzężenia $\alpha_s(Q^2)$ przy wysokich energiach nie jest skutkiem matematycznego triku renormalizacji – to bezpośrednia konsekwencja wchodzenia sondy w obszar obniżonego ciśnienia i naprężeń wewnątrz pęcherzyka.

## 7.5. Masy hadronów – bilans energetyczny pęcherzyka

W Modelu Standardowym zaledwie $\sim 1\%$ masy protonu pochodzi od mas spoczynkowych kwarków walencyjnych; reszta to tzw. masa anomalna QCD. TSM w pełni potwierdza te proporcje, nadając im sens mechaniczny.

Masa hadronu to całkowita energia odkształcenia sprężystego i kinetycznego uwięziona w geometrii pęcherzyka:

$$m_{\text{hadron}} = \frac{1}{c_{\perp}^2} \left( \oint_{\text{ściana}} \sigma_{ab} \, dS^{ab} + \sum_{\text{warkocze}} E_{\text{kin}} \right) \tag{7.11}$$

gdzie:

$m_{\text{hadron}}$ – masa spoczynkowa hadronu $[\text{kg}]$,

$c_{\perp}$ – prędkość fal poprzecznych (światła) $[\text{m} \cdot \text{s}^{-1}]$,

$\sigma_{ab}$ – tensor naprężeń na ścianie pęcherzyka $[\text{Pa}]$,

$dS^{ab}$ – element powierzchni ściany $[\text{m}^2]$,

$E_{\text{kin}}$ – energia kinetyczna drgań warkoczy i uwięzionych modów falowych $[\text{J}]$.

Głównym nośnikiem masy ($\sim 99\%$) jest energia powierzchniowa ściany – nieliniowy gradient naprężeń utrzymywany przeciwko zewnętrznemu ciśnieniu Matrycy.

## 7.6. Brak wolnych gluonów

Gluony nie istnieją jako autonomiczne, swobodne cząstki. Są one wyłącznie modami plazmowymi – falami podłużnymi i poprzecznymi wzbudzonymi wewnątrz zrelaksowanego ośrodka pęcherzyka. Ich propagacja poza barierę fazową ściany jest niemożliwa: na zewnątrz pęcherzyka 0-Matryca znajduje się w stanie wysokiego zakleszczenia i naprężenia, co powoduje natychmiastowe, wykładnicze tłumienie amplitudy fali (mechanizm analogiczny do efektu Proca dla pól masywnych). Gluon „wygasa” na dystansie subatomowym, co klasyczna fizyka interpretuje jako uwięzienie gluonów.

## 7.7. Oddziaływanie słabe jako mechaniczne rozwęźlanie i rozpad stochastyczny

W TSM oddziaływanie słabe nie jest przenoszone przez punktowe bozony $W$ i $Z$. Jest to proces mechanicznego rozwęźlania nietrwałych konfiguracji topologicznych – rekonfiguracji warkoczy wewnątrz pęcherzyka, która prowadzi do zmiany ładunku i masy hadronu. Przemiany te wywoływane są bezpośrednio przez niekoherentny, termo-akustyczny szum sprężysty tła 0-Matrycy o temperaturze $T_{\text{sub}}$.

### 7.7.1. Wolny neutron jako stochastycznie zanikający oscylator

Wolny neutron to złożony, uwięziony pęcherzyk kawitacyjny stabilizowany przez szkielet węzłowy. Z racji wysokiego stopnia skomplikowania splotu, posiada on swoistą częstotliwość rezonansową relaksacji $f_n$. Częstotliwość ta pokrywa się z ciągłym widmem sub-planckowskich wibracji 0-cząstek (termicznym szumem tła 0-Matrycy o temperaturze $T_{\text{sub}}$).

Gdy fluktuacja sprężysta tła o odpowiedniej amplitudzie trafia w neutron, dostarcza mu energii do przebudowy topologicznej – pęknięcia skrzyżowania i rozwęźlenia. Struktura ulega rozplątaniu na węzeł stabilniejszy (proton), prosty węzeł o ładunku $\mathcal{W}=1$ i odwróconej chiralności (elektron) oraz poprzeczno-ortogonalny mod falowy w $x^4$ (antyneutrino).

Proces ten ma charakter czysto stochastyczny, a stała rozpadu $\lambda_n$ (odwrotność czasu życia $\tau_n$) zależy bezpośrednio od całki nakrywania gęstości widmowej szumu Matrycy $\rho(\omega)$ i funkcji rezonansowej neutronu $R_n(\omega)$:

$$\lambda_n = \frac{1}{\tau_n} = \int_0^\infty \rho(\omega) \, R_n(\omega) \, d\omega \tag{7.12}$$

Zmierzony czas życia wolnego neutronu ($\tau_n \approx 880$ s) jest bezpośrednią, fizyczną miarą odporności topologicznej jego splotu na uśrednione ciśnienie fluktuacji sprężystych 0-Matrycy.

### 7.7.2. Zatrzask fazowy: Kinematyka stabilności jąder atomowych

Klasyczna fizyka nie potrafi mechanicznie wyjaśnić, dlaczego wolny neutron rozpadający się w kilkanaście minut po wejściu w strukturę jądra atomowego staje się całkowicie stabilny. W TSM zjawisko to tłumaczy mechanizm zatrzasku fazowego (phase lock).

Wewnątrz jądra sploty nukleonów ulegają trwałemu splątaniu w czwartym wymiarze $x^4$ (Rozdział 7.1), tworząc niezwykle gęstą zbitkę odkształceń. Taka kolektywna struktura geometryczna posiada własne, makroskopowe mody wibracyjne. W stabilnych klastrach jądrowych o wysokiej symetrii przestrzennej dochodzi do destruktywnej interferencji fluktuacji tła: wewnątrz jądra powstaje geometryczny węzeł fali stojącej dla częstotliwości zagrażających przetrwaniu splotu neutronu ($f_n$).

Oznacza to drastyczne wygaszenie i wyzerowanie lokalnego szumu degradującego neutron:

$$\rho_{\text{wewn}}(f_n) \approx 0 \implies \lambda_{n,\text{jądro}} \approx 0 \tag{7.13}$$

Wskutek tego czas życia neutronu w zatrzasku fazowym dąży do nieskończoności. Odchylenia od pełnej symetrii geometrycznej klastra (w izotopach niestabilnych) wprowadzają „przecieki” fal szumu, inicjując stochastyczny rozpad beta ze zróżnicowanym czasem półtrwania.

### 7.7.3. Anomalia czasu życia neutronu jako weryfikacja zatrzasku

Fizyka eksperymentalna boryka się z rozbieżnością wyników czasu życia neutronu mierzonych metodą pułapkową ("butelkową") oraz strumieniową ("wiązkową"):

$$\tau_{\text{beam}} \approx 888{,}0 \text{ s} \quad \text{vs} \quad \tau_{\text{bottle}} \approx 879{,}5 \text{ s}$$

W TSM anomalia ta zyskuje całkowicie naturalne wyjaśnienie. Ścianki fizycznego naczynia w metodzie "butelkowej" (miedź, grafit, powłoki fluoropolimerowe) modyfikują lokalne pola echa sprężystego osnowy 0-Matrycy, zmieniając profil spektralny szumu $\rho_{\text{wewn}}(\omega)$ poprzez rezonansowe odbicia fal o częstotliwości $f_n$.

Zwiększa to uśrednioną gęstość energii fluktuacji tła w objętości pułapki, podnosząc wartość całki (7.12) i skracając mierzony czas życia. Wynik $\tau_{\text{beam}}$ zmierzony w locie (bez bliskości fizycznych barier) reprezentuje czysty czas życia w niezaburzonym, swobodnym otoczeniu.

## 7.8. Wewnętrzna dynamika kwarków – masy, hierarchia i macierz CKM

### 7.8.1. Masy biegnące jako pomiar w gradiencie naprężeń

Masa kwarka jest funkcją gęstości zmagazynowanej energii sprężystej w obszarze sondowania o promieniu $r \propto 1/\sqrt{Q^2}$:

$$m(Q^2) = \frac{1}{c_{\perp}^2} \int_{V(Q^2)} \mathcal{E}_{\text{spręż}}(\mathbf{x}) \, d^3x \tag{7.14}$$

gdzie:

$m(Q^2)$ – masa biegnąca kwarka $[\text{kg}]$,

$Q^2$ – kwadrat przekazu czteropędu $[\text{GeV}^2]$,

$V(Q^2)$ – objętość sondowania,

$\mathcal{E}_{\text{spręż}}$ – gęstość energii sprężystej $[\text{J} \cdot \text{m}^{-3}]$.

Ponieważ pęcherzyk posiada stromy gradient naprężeń (maksimum na ścianie, minimum w rdzeniu), wartość całki maleje, gdy $V(Q^2)$ kurczy się przy wysokich $Q^2$ – sonda wnika w zrelaksowane wnętrze. „Biegnące masy” w QCD to czysty efekt geometryczny.

### 7.8.2. Hierarchia mas a ciśnienie wewnątrz pęcherzyka

Ekstremalna różnica mas między kwarkiem górnym (Up, $\sim 2$ MeV) a kwarkiem szczytowym (Top, $\sim 173$ GeV) wynika ze statyki naprężeń. Tensor naprężenia warkocza rozkłada się na dewiator $s_{ab}$ (ścinanie) i człon hydrostatyczny $p$ (zgniatanie):

$$\sigma_{ab} = s_{ab} + p \, \delta_{ab} \tag{7.15}$$

Kwarki lekkie ($u, d, s$) to niskie mody wibracyjne – ich masa pochodzi głównie od ścinania $s_{ab}$.

Kwark Top to skrajny, objętościowy rezonans harmoniczny sprzężony ze ścianą pęcherzyka. Jego gigantyczna masa to całkowita praca mechaniczna wykonywana przeciwko pełnemu 4-wymiarowemu ciśnieniu hydrostatycznemu Matrycy dążącej do kolapsu pęcherzyka.

### 7.8.3. Macierz CKM jako obrót osi naprężeń

W Modelu Standardowym macierz CKM opisuje mieszanie zapachów kwarków podczas oddziaływań słabych. TSM definiuje ją jako klasyczną transformację bazy tensora odkształceń w przestrzeni 3D. Kwarki górne (ładunek $+2/3$) i dolne ($-1/3$) posiadają odmienną chiralność topologicznego skrętu warkocza, przez co ich lokalne osie główne naprężeń są przestrzennie przekrzywione.

Gdy oddziaływanie słabe przekształca jeden typ warkocza w drugi, naprężenie ulega transformacji z bazy górnej do bazy dolnej. Przeliczenie składowych tensora między dwoma przekrzywionymi układami kartezjańskimi wymaga macierzy obrotu parametryzowanej kątami Eulera:

$$V_{\text{CKM}} = R_{23}(\theta_{23}) \cdot R_{13}(\theta_{13}, \delta) \cdot R_{12}(\theta_{12}) \tag{7.16}$$

Kąt Cabibbo ($\theta_C \approx 13^\circ$) to rzeczywisty kąt geometrycznego przekrzywienia między osią odkształcenia kwarka Up a osią kwarka Down w tej samej domenie pęcherzyka.

## 7.9. Wzbudzenia topo-harmoniczne i parametry materiałowe 0-Matrycy

Podczas wysokoenergetycznych zderzeń w LHC stabilne sploty ulegają skrajnemu ściśnięciu, wywołując w sprężystym tle potężne, skwantowane fale stojące – wzbudzenia topo-harmoniczne.

### 7.9.1. Rezonanse W i Z jako mody naprężeniowe osnowy

W Modelu Standardowym oddziaływania słabe neutralne i naładowane opisywane są matematycznie przy użyciu pól cechowania $W_\mu^\pm$ i $Z_\mu$. TSM w pełni akceptuje precyzję ilościową tych równań, jednak nadaje im fizyczny sens mechaniczny:

Pole $Z_\mu$ oraz $W_\mu$ to wektory dynamicznych naprężeń ścinających tła podczas gwałtownej, przejściowej rekonfiguracji węzłów.

Stała sprzężenia $g$ oraz kąt Weinberga $\theta_W$ to w rzeczywistości emergentne makroskopowe parametry materiałowe (odpowiednio: moduł sztywności postaciowej $\mu$ i nieliniowej sprężystości objętościowej $K$ osnowy, bezpośrednio spięte z fundamentalną elastycznością Substratu $\mathcal{K}$).

Macierze Diraca $\gamma^\mu$ reprezentują geometrię ugięcia poprzecznego tej 4-wymiarowej rozmaitości.

Masa bozonów ($M_W \approx 80 \text{ GeV}$, $M_Z \approx 91 \text{ GeV}$) to zmagazynowana skrajna gęstość energii odkształcenia sprężystego (jak ekstremalnie ściśnięta i zablokowana sprężyna), a ich czasy życia ($\sim 10^{-25} \text{ s}$) to czysty czas relaksacji (dyssypacji falowej) tego nienaturalnego, przejściowego super-węzła. TSM kategorycznie odrzuca istnienie jakichkolwiek cięższych odpowiedników symetrycznych (brak supersymetrii i bozonów Z').

### 7.9.2. Reguła Koidego jako harmoniczna zależność wzbudzeń leptonowych – tajemnica 2/3

Jedną z najgłębszych zagadek fizyki cząstek jest tzw. reguła Koidego – empiryczny związek łączący masy trzech naładowanych leptonów (elektron $e$, mion $\mu$, taon $\tau$):

$$\frac{m_e + m_\mu + m_\tau}{\left( \sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau} \right)^2} = \frac{2}{3} \tag{7.17}$$

Wartość lewej strony, obliczona na podstawie zmierzonych mas, wynosi dokładnie $0{,}666 \ldots \approx 2/3$ z odchyleniem mniejszym niż $10^{-4}$, co wyklucza przypadek. Model Standardowy nie dostarcza żadnego wyjaśnienia dla tej regularności.

W TSM reguła Koidego przestaje być numerologiczną ciekawostką – staje się bezpośrednią konsekwencją geometrii odkształceń sprężystych prostego splotu leptonowego ($\mathcal{W}=1$).


#### 7.9.2.1. Leptony jako czyste mody ścinania

Zgodnie z mechaniką węzłów (Rozdział 2), leptony nie są złożonymi pęcherzykami kawitacyjnymi (jak hadrony), lecz prostymi splotami topologicznych odkształceń – pojedynczymi, zamkniętymi pętlami naprężeń ścinających. Ich energia sprężysta (masa) nie pochodzi od ciśnienia hydrostatycznego $p$ (ściany pęcherzyka), lecz wyłącznie od czystego ścinania opisywanego dewiatorem $s_{ab}$.

Tensor naprężeń w rdzeniu leptonu ma strukturę:

$$\sigma_{ab}^{\text{lepton}} = s_{ab}, \qquad s_{cc} = 0 \quad \text{(brak ciśnienia hydrostatycznego)} \tag{7.18}$$

#### 7.9.2.2. Kąt ścinania 45° i wewnętrzna macierz obrotu

Dla prostego splotu w 4-wymiarowej osnowie kierunki główne dewiatora naprężeń $s_{ab}$ nie są dowolne – są sztywno wyznaczone przez topologię węzła. Okazuje się, że w przypadku splotu o liczbie $\mathcal{W}=1$, osie główne naprężeń ścinających są przekrzywione względem siebie o kąt $\theta_0 = 45^\circ$ ($\pi/4$) w przestrzeni wewnętrznej. Jest to kąt optymalny, przy którym energia sprężysta splotu jest zminimalizowana – wszelkie inne kąty prowadziłyby do większych naprężeń i szybkiego rozpadu. To właśnie ten kąt 45° leży u podstaw reguły Koidego.

#### 7.9.2.3. Macierz masowa leptonów

Niech $M$ będzie macierzą masową w przestrzeni zapachowej leptonów. W TSM macierz ta jest rzutem tensora odkształceń sprężystych na bazę stanów własnych chiralności (Rozdział 7.8.3). Dla leptonów, które są splotami o tej samej strukturze topologicznej ($\mathcal{W}=1$), różniącymi się jedynie poziomem wzbudzenia (harmoniczną), macierz $M$ przyjmuje postać:

$$M = m_0 \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \tag{7.19}$$

gdzie $m_0$ jest skalą masową wspólną dla całej rodziny leptonowej. Taka struktura macierzy oznacza, że stany własne nie są diagonalne w bazie zapachowej – masa wyłania się jako wynik superpozycji składowych.

Diagonalizacja tej macierzy daje trzy wartości własne:

$$\lambda_1 = 3m_0, \quad \lambda_2 = \lambda_3 = 0 \tag{7.20}$$

W rzeczywistości degeneracja $\lambda_2 = \lambda_3 = 0$ jest znoszona przez subtelne poprawki nieliniowe (sprzężenie z modami $x^4$ i szumem $T_{\text{sub}}$), co prowadzi do rozszczepienia i pojawienia się niezerowych mas mionu i taonu.

#### 7.9.2.4. Wyprowadzenie czynnika 2/3 z Laplasjanu Sferycznego

Matematyczny opis energii rotacyjnej węzła i jego orientacji względem osi $x^4$ definiuje operator Hamiltona na sferze konfiguracji $\mathbb{S}^2$:

$$E_{\text{rot}}(\theta) = E_0 + \frac{\hbar^2}{2I} \kappa \cos^2\theta \tag{7.21}$$

Gdzie $I$ jest efektywnym momentem bezwładności węzła, a $\kappa$ bezwymiarową stałą Substratu. Poddanie tego układu równaniu Schrödingera z Laplasjanem Sferycznym $\Delta_{\mathbb{S}^2}$:

$$-\hbar^2 \Delta_{\mathbb{S}^2} \Psi(\theta, \varphi) + V(\theta)\Psi(\theta, \varphi) = E \Psi(\theta, \varphi) \tag{7.22}$$

prowadzi do rozwiązań w postaci wielomianów Legendre'a. Dla stanu podstawowego splotu $\mathcal{W}=1$ wartości własne operatora orientacji wymuszają dyskretne kąty $\theta_n$, które spełniają warunki cyklotomiczne. Pierwiastki masowe mas leptonów $\sqrt{m_n}$ są bezpośrednio proporcjonalne do rzutów tych stanów orientacyjnych:

$$\sqrt{m_n} = \nu_0 \cdot \left[ 1 + \sqrt{2} \cos\left(\theta_0 + \frac{2n\pi}{3}\right) \right] \tag{7.23}$$

Dla $\theta_0 = \pi/4$ ($45^\circ$) otrzymujemy tożsamościowe spełnienie relacji masowej Koidego:

$$\frac{m_e + m_\mu + m_\tau}{\left(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau}\right)^2} = \frac{2}{3} \tag{7.24}$$

W przypadku kwarków, ich masy odbiegają od czystej relacji trygonometrycznej ze względu na dodatkowe przesunięcie energetyczne wywołane przez profil ciśnienia hydrostatycznego $p(r)$ wewnątrz pęcherzyka hadronowego. Kwark up stanowi przyścienny mod ścinający, podczas gdy kwark top staje się rezonansem objętościowym całego pęcherzyka.

## 7.10. Topologiczna hierarchia mas leptonów: Mion i Taon jako wzbudzenia splotowe wyższego rzędu i wskaźnik złożoności $\chi_{\text{top}}$

Jedną z największych zagadek Modelu Standardowego jest istnienie trzech generacji leptonów, które posiadają identyczne ładunki i spiny, lecz skrajnie różne masy. W TSM hierarchia ta jest naturalną konsekwencją topologicznego nakładania skrzyżowań i pętli w 0-Matrycy.

Elektron: Reprezentuje stan podstawowy – najprostszy stabilny węzeł fermionowy o niezerowej chiralności (trójlistnik z $\mathcal{W}=1$ z nieliniowym zabezpieczeniem). Jego spoczynkowa gęstość zmagazynowanej energii (masa) wynika z minimalnego naprężenia ścinającego niezbędnego do zamknięcia tego splotu w 4D.

Mion i Taon: To fizycznie ten sam podstawowy rdzeń węzła, lecz „przepompowany” kinetycznie podczas zderzeń wysokoenergetycznych, co wymusza powstanie na nim dodatkowych, niestabilnych pętli i skrzyżowań. Zgodnie z nieliniową sprężystością Matrycy, każde dodatkowe zagięcie topologiczne generuje drastyczny, wykładniczy wzrost lokalnego naciągu i ciśnienia osnowy.

Masa ciężkich leptonów jest ściśle powiązana z ich stopniem skomplikowania topologicznego, opisywanym przez niezmienniki węzłów (stopień wielomianu Jonesa $V(t)$ lub minimalną liczbę skrzyżowań $c(K)$). W pierwszym przybliżeniu elastodynamiki splotów, masa leptona $m_i$ wyraża się jako:

$$m_i c_{\text{lok}}^2 = E_{\text{baza}} + \kappa \cdot f(c(K_i)) \tag{7.25}$$

gdzie $\kappa$ to moduł sztywności skrętnej osnowy przy ekstremalnych zagięciach, a $f(c(K_i))$ to nieliniowa funkcja liczby skrzyżowań dla danej generacji. Parametr ten opisuje wskaźnik złożoności topologicznej ($\chi_{\text{top}}$), powiązany z minimalną liczbą skrzyżowań linii naprężeń warkocza oraz niezmiennikami wielomianowymi Jonesa.

Ponieważ mion i taon są uwięzionymi stanami o potężnym nadmiarze naprężenia sprężystego, są one wysoce niestabilne w zimnej (zrelaksowanej) 0-Matrycy. Szum termiczny $T_{\text{sub}}$ błyskawicznie "strząsa" z nich te dodatkowe, niechronione geometrycznie pętle.

Proces rozpadu mionu na elektron i neutrina ($\mu^- \to e^- + \bar{\nu}_e + \nu_\mu$) to w rzeczywistości mechaniczne rozplątanie dodatkowych skrzyżowań z powrotem do stanu podstawowego elektronu, czemu towarzyszy wyrzucenie nadmiaru energii w postaci propagujących się fal relaksacyjnych (neutrin).

### 7.10.1. Anomalia magnetyczna $g-2$: Pomiar „tarcia” topologicznego

W Modelu Standardowym anomalia magnetyczna mionu $a_\mu = (g-2)/2$ jest interpretowana jako wynik oddziaływań z wirtualnymi cząstkami (polaryzacja próżni). TSM zastępuje tę interpretację klasyczną fizyką ośrodków ciągłych. Anomalia $g-2$ to bezpośredni, mierzalny opór geometryczny (drag), jaki osnowa stawia dodatkowym skrzyżowaniom węzła mionowego podczas jego rotacji w polu magnetycznym.

Podczas rotacji mionu, jego dodatkowe pętle „przecinają” linie sił pola 0-Matrycy. Ponieważ 0-Matryca posiada skończoną efektywną sztywność $\mathcal{K}_{\text{eff}}$, generuje to moment hamujący (dyssypację). Anomalna część momentu magnetycznego $\Delta a_{\text{TSM}}$ jest w TSM funkcją sprzężenia tego oporu mechanicznego i wykazuje liniową korelację ze wskaźnikiem złożoności:

$$\Delta a_{\text{TSM}} = \eta \cdot \left( \frac{\mathcal{K}_{\text{eff}}}{\rho_0 c^2} \right) \cdot \chi_{\text{top}} \tag{7.26}$$

gdzie:

$\eta$ – stała sprzężenia topologicznego węzła z ośrodkiem,

$\mathcal{K}_{\text{eff}} / (\rho_0 c^2)$ – znormalizowana sztywność sieci (bezwymiarowy współczynnik interakcji),

$\chi_{\text{top}} = \frac{c(K_\mu) - c(K_e)}{c(K_e)}$ – wskaźnik nadmiarowej złożoności topologicznej mionu względem elektronu.

Wartość anomalii mionu, którą mierzymy w akceleratorach (np. Fermilab), jest w istocie najbardziej precyzyjnym pomiarem sztywności sprężystej 0-Matrycy, jakiego kiedykolwiek dokonano.


## 7.11. Oscylacje neutrin jako rotacja polaryzacji w przestrzeni 4D

W Modelu Standardowym neutrina są bezmasowe (lub mają masy wprowadzane ad hoc), a ich oscylacje opisuje macierz PMNS, analogiczna do CKM. MS nie wyjaśnia fizycznej przyczyny tego zjawiska.

W TSM neutrino nie jest klasyczną cząstką – to czysty, bezmasowy (lub prawie bezmasowy) mod falowy zanurzony w wymiarze $x^4$ (sekcja 7.7.3). Jego ładunek topologiczny $\mathcal{W}=0$, ale posiada wewnętrzną strukturę polaryzacyjną. Oscylacje neutrin są mechanistyczną manifestacją rotacji tej polaryzacji podczas propagacji w 4D.

### 7.11.1. Neutrino jako fala w $x^4$

Zapiszmy pole neutrina jako składową $\Psi_\nu$ formy $\beta$ (Rozdział 2.1.4), a konkretnie składową $\bar{\psi} = \beta_{i4} dx^i$, która reprezentuje polaryzację sprzężoną z kierunkiem ortogonalnym. Dla neutrina pole to propaguje się głównie w $x^4$, a nie w 3-brane:

$$\Psi_\nu(x^4, t) = \psi_0 \exp\left( i k_4 x^4 - i \omega t \right) \tag{7.27}$$

gdzie:

$k_4$ – wektor falowy w kierunku $x^4$ $[\text{m}^{-1}]$,

$\omega$ – częstość drgań własnych,

$\psi_0$ – wektor polaryzacji w przestrzeni 3D (dla obserwatora na branie).

### 7.11.2. Trzy zapachy jako trzy składowe polaryzacji

W przestrzeni 4D istnieją trzy niezależne kierunki polaryzacji ortogonalne do kierunku ruchu (w $\mathbb{R}^4$ fala poprzeczna ma 3 stany polaryzacyjne, a nie 2 jak w 3D). Te trzy stany są wzajemnie ortogonalne i tworzą bazę:

$$\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3 \quad \text{(wektory jednostkowe w przestrzeni 4D)} \tag{7.28}$$

Dla obserwatora na 3-branie rzuty tych trzech wektorów na rozmaitość 3D dają trzy różne stany oddziaływania – trzy zapachy neutrin: $\nu_e$, $\nu_\mu$, $\nu_\tau$.

Szerokość rozpadu "niewidzialnego" bozonu Z w detektorach odpowiada precyzyjnie 3 generacjom neutrin ($N_\nu = 3$). Grupa $SU(2)$ stanowi podwójne nakrycie przestrzennej grupy $SO(3)$. Jej trzy macierze generatorów ($T_1, T_2, T_3$) odpowiadają fizycznie rzutom na trzy ortogonalne płaszczyzny w izotropowej 3-brane. Rozpad tak gęstego wzbudzenia nie jest procesem probabilistycznym, lecz rygorystycznym rozplątywaniem sieci naprężeń ścinających (skein relations – relacje kłębiaste). Naprężenie ścinające węzła może uciec z rdzenia („wypromieniować niewidzialnie” w postaci bezmasowych modów neutrinowych) wyłącznie na trzy niezdegenerowane, prostopadłe stopnie swobody przestrzennej.

### 7.11.3. Rotacja polaryzacji w 4D = oscylacje

Podczas propagacji w 4D wektor polaryzacji $\psi_0$ nie jest statyczny. Gradienty naprężeń tła (resztki pierwotnego skręcenia 3-brany, Rozdział 0.5) działają jak ośrodek dwójłomny – powoli obracają płaszczyznę polaryzacji wokół osi $x^4$. Kąt obrotu narasta proporcjonalnie do przebytego dystansu $L$ w 4D:

$$\theta(L) = \theta_0 + \frac{\Delta m^2}{2 E} L \tag{7.29}$$

gdzie $\Delta m^2$ to efektywna różnica mas (energii sprężystych) między modami polaryzacyjnymi, wynikająca z nieliniowego sprzężenia z naprężeniami tła, a $E$ to energia neutrina.

Dla obserwatora na 3-branie oznacza to, że neutrino wyprodukowane jako $\nu_e$ (określony rzut polaryzacji) po przebyciu dystansu $L$ ma już inny rzut – może być zarejestrowane jako $\nu_\mu$ lub $\nu_\tau$. Prawdopodobieństwo oscylacji dane jest klasycznym wzorem Malusa dla obracającej się polaryzacji:

$$P(\nu_\alpha \to \nu_\beta) = |\mathbf{e}_\alpha \cdot \mathbf{e}_\beta(\theta(L))|^2 \tag{7.30}$$

### 7.11.4. Macierz PMNS jako macierz obrotu w 4D

Macierz mieszania neutrin (PMNS) jest w TSM macierzą obrotu w przestrzeni 4D między bazą produkcyjną (zdefiniowaną przez oddziaływanie słabe na 3-branie) a bazą propagacyjną (naturalne osie polaryzacji w 4D):

$$U_{\text{PMNS}} = R_{4D}(\theta_{12}, \theta_{23}, \theta_{13}, \delta) \tag{7.31}$$

Kąty mieszania ($\theta_{12} \approx 33^\circ$, $\theta_{23} \approx 45^\circ$, $\theta_{13} \approx 8^\circ$) to kąty między osiami głównymi naprężeń tła 4D a płaszczyzną 3-brany. Są one stałe, bo geometria Wielkiego Wydarzenia (Rozdział 0.5) wyznaczyła je raz na zawsze. Fazowy czynnik $\delta$ (łamanie CP w sektorze neutrin) odpowiada rzeczywistemu kątowi skręcenia bazy polaryzacyjnej wokół $x^4$ – jego niezerowa wartość jest przewidywana w TSM jako naturalna konsekwencja chiralności pierwotnego skręcenia.

### 7.12. Demistyfikacja eksperymentu Younga – efekt obserwatora jako zjawisko hydrodynamiczne

Eksperyment z dwiema szczelinami, uchodzący za manifestację dualizmu falowo-korpuskularnego, znajduje w TSM czysto mechaniczne wyjaśnienie.

### 7.12.1. Fala pilotująca

Elektron porusza się jako stabilny węzeł topologiczny, generując przed sobą sprężystą falę dziobową (pilotującą) w 0-Matrycy. Odkształcenie tła $\phi(\mathbf{x}, t)$ spełnia równanie falowe ze źródłem:

$$\nabla^2 \phi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \phi}{\partial t^2} = \mathcal{S}(\mathbf{x}_e, t) \tag{7.32}$$

gdzie $\mathcal{S}$ to człon źródłowy sprzężony z pozycją elektronu $\mathbf{x}_e$.

Wersja bez detektora: Elektron przechodzi przez jedną szczelinę, ale jego fala pilotująca przechodzi przez obie. Za przesłoną tworzy się klasyczna interferencja fal wtórnych:

$$I(\mathbf{x}) = |\phi_1 + \phi_2|^2 = |\phi_1|^2 + |\phi_2|^2 + 2|\phi_1||\phi_2|\cos(\Delta \theta) \tag{7.33}$$

W sprężystej Matrycy powstają fizyczne „korytarze” wysokiego i niskiego ciśnienia. Elektron, opuszczając szczelinę, jest przez swoją falę pilotującą deterministycznie spychany w miejsca maksimów, tworząc prążki interferencyjne.

### 7.12.2. Efekt obserwatora

Włączenie detektora przy szczelinach wymaga emisji fotonów lub przyłożenia pola – to brutalna, mechaniczna ingerencja, która generuje w rejonie szczelin stochastyczną turbulencję $\eta(\mathbf{x}, t)$. Ponieważ energia szumu detektora drastycznie przewyższa subtelną energię fali pilotującej:

$$\langle |\eta(\mathbf{x}, t)|^2 \rangle \gg 2|\phi_1||\phi_2| \tag{7.34}$$

człon interferencyjny zostaje zatarty przez dekoherencję mechaniczną. Fala pilotująca ulega destrukcji, a elektron kontynuuje lot balistyczny – prążki znikają. „Załamanie funkcji falowej” to klasyczne zniszczenie fali nośnej przez szum pomiarowy.

## 7.13. Łamanie CP jako skręcenie osi naprężeń w przestrzeni 4D

Jednym z najbardziej fundamentalnych odkryć fizyki cząstek jest łamanie symetrii CP w rozpadach neutralnych kaonów i mezonów B. Oznacza ono, że prawa fizyki nie są identyczne dla materii i antymaterii po odbiciu przestrzennym. Model Standardowy parametryzuje to zjawisko przez zespoloną fazę $\delta$ w macierzy CKM, ale nie wyjaśnia jej pochodzenia.

W TSM faza $\delta$ nie jest abstrakcyjną liczbą – to rzeczywisty kąt skręcenia przestrzeni wewnętrznej naprężeń, którego nie można sprowadzić do zera przez żadną przestrzenną rotację.

### 7.13.1. Dwie bazy, dwa kąty – dlaczego potrzebna jest faza

W sekcji 7.8.3 ustalono, że kwarki górne ($u, c, t$) i dolne ($d, s, b$) posiadają odmienną chiralność topologicznego skrętu warkocza, przez co ich osie główne naprężeń są przekrzywione. Macierz CKM to obrót między tymi dwiema bazami.

W standardowej parametryzacji trzy kąty Eulera $\theta_{12}, \theta_{23}, \theta_{13}$ opisują wzajemne nachylenie osi. Ale w 3-wymiarowej przestrzeni obroty są opisywane przez grupę SO(3), która ma tylko 3 kąty. Skąd zatem dodatkowa faza $\delta$?

Odpowiedź leży w fakcie, że węzły są tworami 4-wymiarowymi. Ich przestrzeń wewnętrzna naprężeń nie jest zwykłą $\mathbb{R}^3$, lecz zawiera dodatkowy stopień swobody związany z zanurzeniem w $x^4$. Dwie bazy – górna i dolna – nie są po prostu obrócone względem siebie w 3D; są one wzajemnie skręcone wokół osi $x^4$, co wprowadza kąt, którego nie można wyzerować.

### 7.13.2. Kąt skręcenia $\delta$ jako nieusuwalna faza geometryczna

Wyobraźmy sobie dwie trójki wektorów w 4D: $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ dla kwarków górnych i $\{\mathbf{d}_1, \mathbf{d}_2, \mathbf{d}_3\}$ dla dolnych. Każda z tych trójek definiuje 3-wymiarową hiperpłaszczyznę w $\mathbb{R}^4$. Te dwie hiperpłaszczyzny przecinają się wzdłuż pewnej płaszczyzny 2D, a kąt między nimi – kąt skręcenia – oznaczamy jako $\delta$.

W odróżnieniu od zwykłego kąta w 3D, którego zmiana o $\pi$ przywraca pierwotną konfigurację, skręcenie dwóch hiperpłaszczyzn w 4D jest zjawiskiem chiralnym. Odbicie przestrzenne (P) zmienia znak wszystkich współrzędnych $x^1, x^2, x^3$, ale nie $x^4$. Tymczasem kąt $\delta$ jest zdefiniowany właśnie przez orientację w $x^4$ – dlatego operacja P nie odwraca go, lecz zmienia w sposób, którego nie można skompensować przez przejście do antycząstek (C). Łączna operacja CP nie jest więc symetrią – Wszechświat „pamięta” pierwotne skręcenie.

### 7.13.3. Związek z Wielkim Wydarzeniem i asymetria barionowa

Skąd wzięło się to skręcenie? Zgodnie z Rozdziałem 0.5, 3-brana powstała przez przekręcenie zakleszczonej 0-Matrycy podczas Wielkiego Wydarzenia. To przekręcenie nie było idealnie symetryczne – miało określoną chiralność. Ta sama chiralność odcisnęła się na wszystkich później utworzonych węzłach.

Eksperymentalnie zmierzona wartość fazy $\delta$ w macierzy CKM wynosi ok. $68^\circ$ (kąt $\gamma$ trójkąta unitarności). W TSM wartość ta nie jest przypadkowa – to kąt między płaszczyzną pierwotnego skręcenia 3-brany a osią $x^4$, utrwalony w geometrii węzłów. Jest to warunek początkowy narzucony przez Wielkie Wydarzenie.

Ta pierwotna, chiralna asymetria rzutowania jest również bezpośrednim źródłem globalnej asymetrii materia-antymateria we Wszechświecie. Wielkie Wydarzenie wygenerowało mechanicznie więcej węzłów o jednej chiralności niż o przeciwnej, ponieważ samo pierwotne skręcenie było chiralne.

## 7.14. Fundament empiryczny i źródła danych

Model TSM opiera się na rygorystycznej interpretacji twardych i bezdyskusyjnych danych eksperymentalnych, które w Modelu Standardowym wymagają sztucznych postulatów ad hoc:

Anomalia czasu życia neutronu (Dowód na wpływ tła na stabilność węzła): Klasyczna fizyka nie potrafi wyjaśnić, dlaczego neutrony w locie ("wiązka") rozpadają się wolniej niż neutrony uwięzione w materialnym pojemniku ("butli"). W TSM rozpad nie jest wynikiem "magicznego prawdopodobieństwa", lecz mechanicznym rozerwaniem splotu przez sprężysty szum Matrycy. Ścianki naczynia modyfikują profil tego szumu poprzez echa falowe, skracając czas życia.

Źródło: Wietfeldt, F. E., & Greene, G. L. (2011). The neutron lifetime. Reviews of Modern Physics, 83(4), 1173.

Oscylacje neutrin (Dowód na propagację w naprężonym ośrodku): Dowód na to, że neutrina zmieniają zapach w locie, to w TSM dowód na to, że ten bezmasowy impuls falowy posiada strukturę polaryzacyjną i ulega ciągłemu obrotowi (dwójłomności) w naprężonej osnowie 4D.

Źródło: Fukuda, Y. et al. (Super-Kamiokande Collaboration) (1998). Evidence for Oscillation of Atmospheric Neutrinos. Physical Review Letters, 81(8), 1562.

Maksymalne złamanie parzystości (Dowód na chiralność tła): Faworyzowanie lewoskrętności w rozpadach słabych to geometryczny skutek wrodzonego, lewoskrętnego zwoju samej 3-brany. Rozpadający się węzeł ulega rozwłóknieniu wzdłuż tego naturalnego skrętu osnowy.

Źródło: Wu, C. S. et al. (1957). Experimental Test of Parity Conservation in Beta Decay. Physical Review, 105(4), 1413.

Termiczna temperatura szumu 0-Matrycy (CMB): TSM odrzuca CMB jako "echo Wielkiego Wybuchu". Jest to po prostu empirycznie mierzona, aktualna temperatura termodynamiczna (2,7 K) nieustannych kolizji 0-cząstek tworzących Matrycę. Ten wszechobecny szum termiczny jest motorem rozpadów stochastycznych.

Źródło: Fixsen, D. J. (2009). The Temperature of the Cosmic Microwave Background. The Astrophysical Journal, 707(2), 916.

Idealna płynność plazmy kwarkowo-gluonowej: Dane z RHIC i LHC dowodzą, że plazma zachowuje się jak niemal doskonała, silnie sprzężona ciecz o minimalnej lepkości, co bezpośrednio potwierdza hydrodynamiczną, a nie gazową ontologię wnętrza pęcherzyków kawitacyjnych hadronów w TSM.

## 7.15. Testy eksperymentalne i falsyfikowalność TSM w fizyce subatomowej

### 7.15.1. Rezonator Matrycy – kontrolowane wzbudzanie drgań osnowy

Ponieważ 0-Matryca posiada cechy nieliniowego ośrodka sprężystego, możliwe jest wymuszenie sztucznych, makroskopowych drgań. Protokół zakłada konstrukcję nadprzewodzącej wnęki rezonansowej, wewnątrz której generowane jest zmienne, ultraintensywne pole magnetyczne:

$$B(t) = B_0 + \delta B \sin(2\pi f_{\text{mod}} t) \tag{7.35}$$

Częstotliwość $f_{\text{mod}}$ przestrajana jest w zakresie 1 MHz – 100 GHz. Gdy $f_{\text{mod}}$ zrówna się z częstotliwością własną lokalnej geometrii 0-Matrycy, nastąpi rezonans topo-harmoniczny. Efektywna stała sprzężenia $\kappa$ wzrośnie o czynnik dobroci $Q$ wnęki. Sygnatury:

Skok opóźnienia fazowego wiązki laserowej w interferometrze (Aneks B).

Emisja koherentnego promieniowania wtórnego.

Lokalna modulacja masy efektywnej cząstek testowych.

### 7.15.2. Analiza tensorowa zdarzeń 3-jetowych (LHC)

Zgodnie z modelem węzła $3_1$, destrukcja protonu w zderzeniach wysokoenergetycznych musi zachodzić wzdłuż trzech pierwotnych osi geometrycznych. Generuje to sygnaturę trzech twardych dżetów. Analiza przy użyciu tensora sferyczności:

$$S^{\alpha\beta} = \frac{\sum_i p_i^\alpha p_i^\beta}{\sum_i |p_i|^2} \tag{7.36}$$

po diagonalizacji daje wartości własne $\lambda_1 \ge \lambda_2 \ge \lambda_3$, definiujące sferyczność $S = \frac{3}{2}(\lambda_2+\lambda_3)$ i planarność $A = \frac{3}{2}\lambda_3$. Dla idealnie planarnego rozpadu węzła $3_1$ o symetrii $120^\circ$: $S = 0.75$, $A = 0$.

Wskaźnik asymetrii trzech strumieni:

$$\mathcal{A} = \frac{|p_{T,1}-p_{T,2}| + |p_{T,2}-p_{T,3}| + |p_{T,3}-p_{T,1}|}{p_{T,1}+p_{T,2}+p_{T,3}} \tag{7.37}$$

TSM przewiduje, że rozkład zdarzeń na wykresie Dalitza w przestrzeni $(S, A)$ nie będzie gładki (jak w stochastycznej QCD), lecz ujawni anomalne zagęszczenia – „wyspy” odpowiadające geometrycznemu pękaniu węzła. Analiza otwartych danych CMS/ATLAS powinna ujawnić te struktury przy odpowiedniej czułości statystycznej. Ich brak stanowi kryterium falsyfikacji modelu.

## 7.16. Podsumowanie Rozdziału 7

Rozdział 7 dostarcza kompletnego, mechanicznego obrazu fizyki subatomowej w ramach TSM, zastępując abstrakcyjne postulaty Modelu Standardowego rygorystyczną dynamiką 4-wymiarowego ośrodka sprężystego.

Hadrony jako pęcherzyki kawitacyjne: Proton i neutron to pęcherzyki kawitacyjne w 0-Matrycy stabilizowane przez węzeł trójlistny $3_1$. Morze partoniczne to turbulencja akustyczna wewnątrz pęcherzyka, a masa hadronu to w $99\%$ energia powierzchniowa jego ściany (nieliniowy gradient naprężeń zdefiniowany profilem ciśnienia $p(r)$).

Confinement i swoboda asymptotyczna: Uwięzienie kwarków to mechanika rozciągania i pękania szyjki sprężystej osnowy (hadronizacja). Swoboda asymptotyczna wynika z niskich naprężeń w zrelaksowanym wnętrzu pęcherzyka.

Rozpad beta jako stochastyczna relaksacja: Rozpad neutronu zachodzi, gdy termo-akustyczny szum sprężysty tła 0-Matrycy $T_{\text{sub}}$ rezonuje z częstotliwością relaksacji splotu $f_n$. Stałą rozpadu $\lambda_n$ definiuje całka nakrywania gęstości widmowej szumu i funkcji rezonansowej.

Zatrzask Fazowy: Splątane w jądru nukleony tworzą destruktywną interferencję szumu tła, wygaszając częstotliwości degradujące neutron i czyniąc go stabilnym. Anomalia czasu życia neutronu (pułapka vs wiązka) to bezpośredni dowód na wpływ sprężystego echa ścian naczynia na lokalne widmo szumu tła Matrycy.

Bozony W i Z jako mody naprężeniowe: To przejściowe rezonanse sprężyste, a nie autonomiczne cząstki. Kąt Weinberga $\theta_W$ oraz stała $g$ to makroskopowe parametry materiałowe osnowy wyprowadzone z uniwersalnej sztywności Substratu $\mathcal{K}$.

Reguła Koidego: Współczynnik $2/3$ w relacji mas leptonów zostaje ściśle wyprowadzony jako geometryczny niezmiennik macierzy obrotu o optymalny kąt ścinania $45^\circ$ w prostym splocie $\mathcal{W}=1$. Rozwiązanie Laplasjanu Sferycznego na sferze $\mathbb{S}^2$ dla energii rotacyjnej daje dyskretne kąty orientacyjne determinujące widmo mas leptonów.

Topologiczna hierarchia mas leptonów: Mion i taon to wyższe harmoniczne splotu elektronowego ($\mathcal{W}=1$). Ich potężna masa to energia zmagazynowana w dodatkowych, wymuszonych pętlach i skrzyżowaniach opisywanych wskaźnikiem $\chi_{\text{top}}$. Rozpad to mechaniczne rozwęźlanie pętli z emisją neutrin. Anomalia magnetyczna $g-2$ to bezpośredni pomiar oporu hydrodynamicznego (tarcia) dodatkowych pętli o sieć 0-Matrycy, wykazujący korelację z $\chi_{\text{top}}$.

Oscylacje neutrin: Są manifestacją rotacji płaszczyzny polaryzacji bezmasowych fal poprzeczno-ortogonalnych rozchodzących się w wymiarze $x^4$. Macierz PMNS to macierz obrotu w 4D.

Złamanie parzystości i chiralność: Asymetria w rozpadzie beta (Wu 1957) wynika bezpośrednio z wrodzonego, lewoskrętnego zwoju samej 3-brany, który narzuca uprzywilejowany kierunek pękania i relaksacji splotu.

Łamanie CP i asymetria barionowa: Zespolona faza $\delta$ to fizyczny kąt skręcenia wokół osi $x^4$ między hiperpłaszczyznami naprężeń kwarków górnych i dolnych w 4D. Kąt ten ($68^\circ$) oraz przewaga materii nad antymaterią zostały utrwalone w geometrii osnowy jako warunki początkowe pierwotnego, chiralnego skręcenia 3-brany podczas Wielkiego Wydarzenia.