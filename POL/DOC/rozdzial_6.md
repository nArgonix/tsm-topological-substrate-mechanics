<!-- ver:2.0.0 -->
# Rozdział 6: Grawitacja jako ortogonalny naciąg. Wymiar 4D, Plazmoidy i nieliniowa dynamika kontinuum

W Topologicznej Geometrodynamice Substratu (TSM) odrzucamy abstrakcję geometryczną, która przypisuje grawitacji status czystego zakrzywienia niematerialnej czasoprzestrzeni. Grawitacja zostaje tu zdefiniowana jako rzeczywiste naprężenie ortogonalne (naciąg poprzeczny) sprężystej 3-brany w kierunku czwartego wymiaru przestrzennego ($x^4$). Niniejszy rozdział przedstawia pełen formalizm matematyczny opisujący zachowanie osnowy zarówno w reżimie liniowym, jak i w skrajnie nieliniowych warunkach astrofizycznych, zastępując aparaturę Ogólnej Teorii Względności (OTW) klasyczną elastodynamiką ośrodków ciągłych.

## 6.1. Ontologia grawitacji i limit liniowy (Równanie Laplace'a)

Nasz obserwowalny Wszechświat funkcjonuje jako izotropowa, trójwymiarowa membrana (3-brana) uformowana z gęsto upakowanych 0-cząstek. Zgodnie z rozkładem modów wprowadzonym w Rozdziale 2, składowe polaryzacji skierowane ortogonalnie do brany reprezentują lokalne ugięcia osnowy.

Gdy lokalne sprzężenie pól elektromagnetycznych i torsyjnych formuje stabilny splot topologiczny (fermion) o określonej gęstości energii, 3-brana reaguje na to skupisko wymuszeniem przemieszczenia wzdłuż osi $x^4$. Ten fizyczny gradient naprężenia osnowy na zewnątrz splotu jest przez obiekty testowe odbierany jako pole grawitacyjne.

Dla słabych i średnich gęstości energii (limit newtonowski), membrana dąży do minimalizacji swojej powierzchni i wyrównania naprężeń, zachowując się jak idealnie cienka, naciągnięta błona sprężysta. Równanie równowagi statycznej dla izotropowej membrany poddanej punktowemu obciążeniu poprzecznemu $q(r)$ sprowadza się do trójwymiarowego równania Laplace'a:

$$\nabla^2 w(\mathbf{r}) = 0, \quad \text{dla } r > 0$$

gdzie $w(\mathbf{r})$ oznacza wielkość ugięcia (przemieszczenia) membrany w osi $x^4$ w punkcie $\mathbf{r} = (x^1, x^2, x^3)$. Zakładając idealną symetrię sferyczną układu, operator Laplace'a we współrzędnych sferycznych redukuje się do postaci:

$$\frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{dw}{dr} \right) = 0$$

Całkując powyższe równanie dwukrotnie, otrzymujemy jawne rozwiązanie na profil ugięcia w funkcji odległości $r$ od centrum splotu:

$$w(r) = \frac{C}{r} + C_2$$

Przyjmując warunek brzegowy w nieskończoności $w(r \to \infty) = 0$, stała integracji $C_2$ zeruje się. Stała $C$ jest wprost proporcjonalna do całkowitej energii splotu (masy $M$) oraz odwrotnie proporcjonalna do napięcia powierzchniowego brany $T_b$: $C = - \frac{G M}{T_b}$. Siła grawitacyjna $\mathbf{F}_g$ działająca na cząstkę testową o masie $m$ wewnątrz brany jest bezpośrednim gradientem energii potencjalnej $V_g(r)$, zdefiniowanej sztywno poprzez pracę wykonaną przeciwko napięciu osnowy jako $V_g(r) = T_b m w(r)$. Stąd:

$$\mathbf{F}_g = - \nabla V_g(r) = - T_b m \nabla w(r) = - \frac{G M m}{r^2} \hat{\mathbf{r}}$$

W ten sposób prawo odwrotnych kwadratów Newtona zostaje wyprowadzone nie z postulatu wymiany hipotetycznych cząstek (grawitonów), lecz jako bezpośredni rzut geometryczny poprzecznego, trójwymiarowego profilu ugięcia kontinuum sprężystego.

## 6.2. Sformalizowana elastodynamika 3-brany: Nieliniowe ugięcie w $\mathbb{R}^4$

Aby poprawnie opisać drastyczne ugięcie trójwymiarowego kontinuum osnowy w kierunku ortogonalnym (wymiar $x^4$), klasyczna liniowa teoria sprężystości musi zostać zastąpiona ścisłym formalizmem dużych odkształceń. W modelu TSM 3-brana nie jest dwuwymiarową powłoką, lecz pełnoprawną trójwymiarową przestrzenią izotropową zanurzoną w $\mathbb{R}^4$.

**1. Tensor odkształceń Green-St Venanta dla 3-brany**
Niech $\mathbf{x} = (x^1, x^2, x^3)$ oznacza współrzędne wewnątrz płaskiej 3-brany, $u_a(\mathbf{x})$ wektor przemieszczeń wewnątrzbranowych, a $w(\mathbf{x})$ skalarne ugięcie membrany w kierunku czwartego wymiaru $x^4$. Ścisłą miarą deformacji geometrycznej uwzględniającą sprzężenie wymiarów jest skończony tensor odkształceń Green-St Venanta $E_{ab}$ (gdzie indeksy $a, b \in \{1, 2, 3\}$):

$$E_{ab} = \frac{1}{2} (\partial_a u_b + \partial_b u_a + \partial_a w \partial_b w)$$

To równanie rygorystycznie definiuje fakt, że każde fizyczne "wypchnięcie" osnowy w wymiar $x^4$ (reprezentowane przez gradient $\partial_a w$) automatycznie i nieliniowo rozciąga 3-branę w jej własnych wymiarach przestrzennych.

**2. Trójwymiarowe równania kompatybilności i uogólniony operator Monge'a-Ampère'a**
W trójwymiarowej 3-brane wprowadzanie skalarnej funkcji naprężeń Airy'ego (właściwej dla 2D) jest matematycznie niewystarczające. Aby zagwarantować ciągłość ośrodka (brak fizycznych rozerwań Matrycy), tensor odkształceń $E_{ab}$ musi bezwzględnie spełniać trójwymiarowe równania kompatybilności Saint-Venanta.

Korzystając z trójwymiarowego symbolu Leviego-Civity $\epsilon^{acd}$, warunek ten zapisujemy ściśle jako:

$$\epsilon^{acd} \epsilon^{bef} \partial_c \partial_e E_{df} = 0$$

Podstawiając do tego równania naszą definicję nieliniowego tensora $E_{ab}$, pochodne przemieszczeń wewnątrzbranowych ($u_a$) tożsamościowo znikają. Pozostaje jedynie nieliniowy człon sprzęgający, który definiuje ścisły, trójwymiarowy odpowiednik nawiasu Monge'a-Ampère'a dla 3-brany, reprezentowany przez tensor źródeł skręcenia $S^{ab}[w]$:

$$S^{ab}[w] = - \frac{1}{2} \epsilon^{acd} \epsilon^{bef} \partial_c \partial_e w \partial_d \partial_f w$$

**3. Tensor naprężeń Beltramiego i pełen układ sprzężony**
Aby spełnić warunek równowagi wewnętrznej $\partial_b \sigma^{ab} = 0$, w trójwymiarowej Matrycy zamiast funkcji skalarnej wprowadzamy symetryczny tensor funkcji naprężeń Beltramiego $\Phi_{cd}$, z którego generowane jest makroskopowe pole naprężeń wewnątrzbranowych:

$$\sigma^{ab} = \epsilon^{acd} \epsilon^{bef} \partial_c \partial_e \Phi_{df}$$

Integrując powyższe wyprowadzenia, uzyskujemy ostateczny, ścisły, trójwymiarowy odpowiednik równań Föppla-von Kármána opisujący grawitacyjny naciąg 3-brany:

$$D \nabla^4 w = \sigma^{ab} \partial_a \partial_b w + q(\mathbf{r})$$

$$\epsilon^{acd} \epsilon^{bef} \partial_c \partial_e (\mathbb{C}^{-1}_{dfpq} \sigma^{pq}) = S^{ab}[w]$$

Gdzie $\nabla^4 = (\partial_1^2 + \partial_2^2 + \partial_3^2)^2$ jest trójwymiarowym operatorem biharmonicznym, $\mathbb{C}^{-1}$ to tensor podatności sprężystej 0-Matrycy, a $q(\mathbf{r})$ to obciążenie ortogonalne generowane przez splot. Sztywność giętna objętości 3-brany $D$ jest jawnym parametrem materiałowym zdefiniowanym strukturalnie jako:

$$D = \frac{E h^3}{12(1-\nu^2)}$$

gdzie $E$ reprezentuje moduł Younga czystej osnowy, a $\nu$ to współczynnik Poissona.

W celu zachowania pełnej kowalencji i możliwości obliczeniowych, tensor podatności sprężystej $\mathbb{C}^{-1}_{dfpq}$ dla izotropowej 0-Matrycy zostaje jawnie wyznaczony poprzez rzutowanie na tensor metryczny grawitacyjnego tła $g_{df}$, co redukuje lewą stronę równania kompatybilności do postaci:

$$\mathbb{C}^{-1}_{dfpq} \sigma^{pq} = \frac{1+\nu}{E} \sigma_{df} - \frac{\nu}{E} \sigma^c_c g_{df}$$

gdzie $\sigma^c_c = \text{Tr}(\sigma)$ reprezentuje ślad tensora naprężeń (ciśnienie hydrostatyczne osnowy).

Z kolei niezmiennik $J_2$, sterujący nieliniowym usztywnieniem modułu ścinania $\mu_{\text{eff}}$, jest zdefiniowany jako drugi niezmiennik dewiatora naprężeń $s^{ab}$:

$$J_2 = \frac{1}{2} s_{ab} s^{ab}$$

gdzie tensor dewiatora $s^{ab}$ reprezentuje czyste naprężenia ścinające, odizolowane od ciśnienia wszechstronnego, zdefiniowane jako:

$$s^{ab} = \sigma^{ab} - \frac{1}{3} \sigma^c_c g^{ab}$$

Parametr $h$ występujący w definicji sztywności giętnej $D$ zyskuje w trójwymiarowym formalizmie $\mathbb{R}^4$ głęboką interpretację: nie jest on grubością fizycznej powłoki, lecz szerokością funkcji lokalizacji energii 3-brany w kierunku ortogonalnym $x^4$. Skala ta jest ściśle powiązana z gęstością upakowania 0-cząstek w komórce Wignera-Seitza i odpowiada skali Plancka $l_{\text{P}}$.

Nieliniowe sprzężenie narzuca asymptotyczne usztywnienie tła. W miarę wzrostu lokalnych ciśnień, gdy drugi niezmiennik dewiatora naprężeń ($J_2$) zbliża się do wartości krytycznej $J_{2,\text{crit}}$, efektywny moduł sprężystości poprzecznej $\mu_{\text{eff}}$ rośnie nieliniowo według relacji:

$$\mu_{\text{eff}}(J_2) = \frac{\mu_0}{1 - \left(\frac{J_2}{J_{2,\text{crit}}}\right)^2}$$

Gdy $J_2 \to $ $J_{2,\text{crit}}$, opór materiałowy 0-Matrycy dąży do nieskończoności ($\mu_{\text{eff}} \to \infty$). Oznacza to, że continuum stawia absolutny opór przed dalszym wyciąganiem, co wymusza istnienie minimalnego promienia krzywizny $R_{\text{min}}$ dla dowolnego skupiska energii. Matematyczna osobliwość typu $1/r$ o nieskończonej gęstości grawitacyjnej jest w TSM fizycznie niemożliwa.

## 6.3. Plazmoidy Topologiczne zamiast Czarnych Dziur

Konsekwencją załamania się osobliwości jest redefinicja obiektów kompaktowych. Pojęcie "Czarnej Dziury" jako geometrycznej dziury w czasoprzestrzeni zostaje zastąpione pojęciem **Plazmoidu Topologicznego**. Plazmoid to skończony, stabilny i ultra-gęsty obiekt fizyczny, w którym 0-cząstki pod wpływem skrajnych ciśnień grawitacyjnych osiągnęły stan absolutnego zakleszczenia strukturalnego (*jamming*). Stan ten nie wynika z wewnętrznego, izolowanego samozakleszczenia ruchu pojedynczych 0-cząstek, lecz jest mechanicznym efektem drastycznego, przestrzennego ograniczenia ich sfer interakcji wewnątrz skrajnie skompresowanej sieci.

* **Horyzont Zdarzeń jako krawędź fazowa:** Horyzont nie jest matematyczną kurtyną bez powrotu, lecz fizyczną granicą przejścia fazowego osnowy. Na zewnątrz tej krawędzi 0-Matryca zachowuje pełne właściwości sprężyste, umożliwiając swobodną propagację fal. Wewnątrz granicy, z powodu skrajnego upakowania, osnowa przechodzi w stan sztywnego układu quasikrystalicznego. Światło (fala poprzeczna) wkraczając w tę strefę nie wpada do osobliwości, lecz ulega natychmiastowemu, całkowitemu rozproszeniu na ekstremalnych gradientach naprężeń oraz konwersji w wibracje sieciowe Plazmoidu.
* **Mechanizm dżetów galaktycznych:** Ponieważ Plazmoid jest dynamicznym, ściśniętym splotem, nieustannie dochodzi w nim do fluktuacji naprężeń. Gdy lokalne ciśnienie wewnętrzne przewyższy wytrzymałość topologicznego zamka, 0-Matryca gwałtownie uwalnia nadmiar zgromadzonej energii potencjalnej. Uwolnienie to następuje w sposób wysoce anizotropowy – poprzez wyrzut skompresowanej materii i modów podłużnych wzdłuż osi najmniejszego oporu mechanicznego (osi rotacji układu), co teleskopy rejestrują jako dżety galaktyczne.

## 6.4. Dynamika galaktyczna: Torsyjne Wleczenie i eliminacja Ciemnej Materii

Wprowadzenie Plazmoidu jako rotującego, fizycznego splotu o gigantycznym momencie pędu pozwala rozwiązać kluczowe anomalie dynamiczne w skalach makroskopowych bez konieczności wprowadzania egzotycznych cząstek Ciemnej Materii.

### 6.4.1. Torsyjne Wleczenie i płaskie krzywe rotacji gwiazd

W klasycznej astrofizyce prędkość liniowa gwiazd na peryferiach galaktyk powinna maleć wraz z odległością $r$ zgodnie z dynamiką keplerowską ($v \propto 1/\sqrt{r}$). Obserwacje wykazują jednak, że krzywa rotacji stabilizuje się na stałym poziomie ($v \approx \text{const}$).

W TSM zjawisko to jest bezpośrednią konsekwencją Torsyjnego Wleczenia (hydro-elastodynamicznego odpowiednika efektu Lense-Thirringa). Rotujący z ogromną prędkością centralny Plazmoid, z racji ekstremalnej lepkości topologicznej układu, dosłownie "wkręca" otaczającą go 0-Matrycę, generując makroskopowe, rotacyjne pole ścinania $\bar{\beta}$. Pole to rozchodzi się w głąb 3-brany, a jego bezpośrednim kinematycznym przejawem jest lokalny profil prędkości kątowej osnowy $\Omega(r)$. Gwiazdy znajdujące się na obrzeżach galaktyki nie są utrzymywane wyłącznie przez radialną siłę naciągu poprzecznego $\mathbf{F}_g = -\nabla w$, ale poruszają się wewnątrz rotującego wiru samej osnowy. Wypadkowa prędkość liniowa gwiazdy $v_{\text{total}}$ stanowi superpozycję jej lokalnej prędkości orbitalnej oraz prędkości dryfu unoszącego ją tła.

Aby jawnie wyprowadzić składową prędkości dryfu $v_{\text{drift}}(\bar{\beta})$, rozpatrujemy równanie równowagi pędu dla składowej sferycznej (wzdłużnej $\theta$) w warunkach stacjonarnych. Rotujący z prędkością kątową $\Omega_0$ centralny Plazmoid o promieniu krytycznym $R_{\text{min}}$ narzuca pole prędkości kątowej osnowy $\Omega(r)$. Równanie transmisji momentu pędu przez lepko-sprężystą strukturę 0-Matrycy przyjmuje postać:

$$\frac{d}{dr} \left( r^3 \mu_{\text{eff}}(r) \frac{d\Omega(r)}{dr} \right) = 0$$

Gdzie $\mu_{\text{eff}}(r)$ jest radialnym profilem nieliniowego modułu ścinania, indykowanym przez ugięcie grawitacyjne gęstego centrum. W strefie bliskiej, gdzie dominują naprężenia nieliniowe, profil $\mu_{\text{eff}}(r)$ wykazuje spadek potęgowy, co wymusza powolne wygasanie prędkości kątowej tła. Rozwiązanie tego równania definiuje pole dryfu tła jako:

$$v_{\text{drift}}(r) = r \Omega(r) = r \left( \Omega_0 - \int_{R_{\text{min}}}^{r} \frac{C_{\text{torsion}}}{x^3 \mu_{\text{eff}}(x)} dx \right)$$

Gdzie $C_{\text{torsion}}$ jest stałą całkowania zależną od momentu pędu Plazmoidu. Na peryferiach galaktyki, funkcja ta w doskonały sposób kompensuje keplerowski spadek prędkości orbitalnej splotów testowych ($v_{\text{orb}} \propto 1/\sqrt{r}$), wymuszając asymptotyczną stabilizację wypadkowej prędkości liniowej gwiazd ($v_{\text{total}} = v_{\text{orb}} + v_{\text{drift}} \approx \text{const}$). Spadek przestrzenny nieliniowego pola rotacyjnego $\bar{\beta}$ w sprężystej membranie idealnie znosi ubytek klasycznego przyciągania radialnego, co całkowicie eliminuje potrzebę wprowadzania hipotetycznych cząstek Ciemnej Materii.

### 6.4.2. Zachowanie gwiazd w pobliżu centrum galaktyki (Orbita S2)

Nieliniowy reżim TSM znajduje bezpośredmie potwierdzenie w trajektoriach gwiazd krążących w bezpośrednim sąsiedztwie centralnego Plazmoidu Sgr A*, takich jak gwiazda S2. Podczas zbliżania się gwiazdy do perycentrum, układ opuszcza limit liniowy Laplace'a i wchodzi w strefę opisywaną równaniami Föppla-von Kármána.

Z powodu nieliniowego sztywnienia osnowy ($\mu_{\text{eff}} \to \infty$), rzeczywisty potencjał grawitacyjny staje się głębszy, a siła przyciągania zyskuje dodatkowy człon elastyczny $\delta \mathbf{F}(\mu_{\text{eff}})$, odchylając się od czystej zależności $1/r^2$. Jawna postać wektora wypadkowej siły grawitacyjnej w tym nieliniowym obszarze przyjmuje postać:

$$\mathbf{F}_{\text{TGM}}(r) = - \left( \frac{G M m}{r^2} + \frac{\mathcal{A}_{\text{nielin}}(J_2)}{r^4} \right) \hat{\mathbf{r}}$$

gdzie $\mathcal{A}_{\text{nielin}}$ jest nieliniowym współczynnikiem sprzężenia sprężystego, wyznaczanym bezpośrednio z lokalnego gradientu inwariantu $J_2$ oraz ewolucji modułu $\mu_{\text{eff}}$. Zgodnie z mechaniką klasyczną, każda wyższa korekta potęgowa potencjału Newtona narusza twierdzenie Bertranda, co wymusza gwałtowną precesję apsydalną orbity. Ruch rozetowy gwiazdy S2 oraz precesja jej peryhelium są w TSM naturalnym skutkiem nieliniowego oporu materiałowego naprężonej sieci, a nie czysto relatywistyczną korektą metryczną.

## 6.5. Alternatywa dla ekspansji: Redshift jako dystansowa dyspersja falowa (Zgodność z Postulatem 0.7)

Podrozdział ten kategorycznie znosi pojęcie "rozszerzania się przestrzeni" oraz powiązaną z nim hipotezę Ciemnej Energii. Zgodnie z Postulatem 0.7, Wszechświat nigdy nie przeszedł przez akt pierwotnej osobliwości, ani nie znajduje się w stanie globalnego, po-wybuchowego odprężania naprężeń. Kosmiczna 0-Matryca jako całość stanowi układ zamknięty o stałej objętości 4D, pozostający w stanie makroskopowej równowagi ciśnień dynamicznych.

Skoro fizyczne odległości między węzłami sieci w skali kosmologicznej są średnio stacjonarne, obserwowane przesunięcie ku czerwieni (redshift) linii widmowych dalekich galaktyk musi być interpretowane jako zjawisko czysto materiałowe – dyspersja dystansowa fal poprzecznych wewnątrz lepko-sprężystego continuum.

### 6.5.1. Mechanizm wiskotycznej utraty pędu fali

Żaden rzeczywisty ośrodek posiadający dyskretną, ziarnistą strukturę (sieć 0-cząstek) nie jest środowiskiem idealnie bezstratnym dla propagacji zaburzeń falowych na ekstremalnych dystansach. Przekazywanie odkształcenia ścinającego (transmisja fotonu reprezentowanego przez mod $\beta$) między kolejnymi komórkami Wignera-Seitza wiąże się z mikroskopowym, lepko-sprężystym oporem osnowy.

W miarę pokonywania drogi $r$ przez pakiet falowy, jego energia $E$ (a w konsekwencji częstotliwość $\nu$) ulega powolnej, systematycznej dyssypacji na skutek skończonej podatności materiałowej tła. Przebieg tego procesu opisuje różniczkowe równanie tłumienia strukturalnego:

$$\frac{dE}{dr} = - \zeta E$$

gdzie $\zeta$ jest stałą tłumienia przestrzennego, determinowaną przez wewnętrzną lepkość objętościową i moduł ścinania 0-Matrycy. Całkowanie tego równania wzdłuż drogi optycznej fotonu od odległego źródła do obserwatora daje zależność wykładniczą:

$$\nu_{\text{obs}} = \nu_{\text{em}} \exp(-\zeta r)$$

Dla odległości lokalnych (w skali kilkudziesięciu megaparseków), gdzie całkowite tłumienie jest niewielkie ($\zeta r \ll 1$), rozwinięcie funkcji wykładniczej w szereg Taylora do pierwszego wyrazu niezerowego daje relację liniową:

$$\frac{\nu_{\text{em}} - \nu_{\text{obs}}}{\nu_{\text{obs}}} = \exp(\zeta r) - 1 \approx \zeta r$$

Definiując standardowy parametr przesunięcia ku czerwieni $z = \frac{\lambda_{\text{obs}} - \lambda_{\text{em}}}{\lambda_{\text{em}}} = \frac{\nu_{\text{em}} - \nu_{\text{obs}}}{\nu_{\text{obs}}}$, otrzymujemy bezpośrednią zależność:

$$z \approx \zeta r$$

Klasyczne prawo Hubble'a zostaje w tym miejscu całkowicie pozbawione podłoża kinematycznego (brak ucieczki galaktyk). Stała Hubble'a $H_0$ staje się parametrem stricte materiałowym, opisującyn jednostkową zdolność tłumienia fal poprzecznych przez 0-Matrycę: $H_0 = \zeta c_{\perp}$, gdzie $c_{\perp}$ to krytyczna prędkość propagacji w branie.

### 6.5.2. Obalenie Ciemnej Energii i konwersja między-modowa fal

Wykładniczy charakter tłumienia $\exp(-\zeta r)$ staje się kluczem do wyjaśnienia anomalii jasności Supernowych typu Ia bez wprowadzania Ciemnej Energii. Światło podróżujące z obiektów położonych na skrajnych dystansach kosmologicznych (miliardy lat świetlnych) wchodzi w nieliniowy reżim tłumienia wykładniczego. Spadek energii fotonów zachodzi tam szybciej niż liniowa ekstrapolacja prawa Newtona-Hubble'a, przez co supernowe docierają do ziemskich detektorów jako ciemniejsze i silniej przesunięte ku czerwieni. Kosmologia standardowa, błędnie interpretując ten fakt jako przyspieszenie kinematyczne, zmuszona jest do postulowania ciemnej energii. W TSM jest to czysty efekt nieliniowego oporu ośrodka.

Aby model ten był spójny i odporny na klasyczne zarzuty stawiane teoriom "zmęczenia światła" (takie jak rozmycie obrazów odległych gwiazd na skutek rozproszenia), TSM wprowadza mechanizm **nieliniowej konwersji między-modowej**. Energia tracona przez falę poprzeczną (mod ścinania $\beta$) nie ulega rozproszeniu na chaotyczne drgania termiczne cząstek (co powodowałoby zniekształcenia frontu falowego), lecz zostaje – poprzez nieliniowe sprzężenia sieciowe – przetransformowana w ortogonalny, podłużny mod kompresyjny ($\alpha$).

W ten sposób energia "wytracana" przez światło zasila bezpośrednio składową ciśnienia tła w czwartym wymiarze, podtrzymując ciągłe fluktuacje i kreację nowych zniekształceń opisaną w Postulacie 0.7. Układ zamyka swój obieg energetyczny, pozostając makroskopowo statycznym i wiecznym.

## 6.6. Fizyczna natura stałej $c$ i fale naprężeniowe (LIGO)

W Topologicznej Geometrodynamice Substratu stała $c$ traci swój mistyczny status nienaruszalnej bariery geometrycznej samej czasoprzestrzeni. Zostaje ona sprowadzona do roli **krytycznej prędkości propagacji fal poprzecznych ($c_{\perp}$)** wewnątrz sprężystego continuum 3-brany.

### 6.6.1. Mechaniczne pochodzenie efektów relatywistycznych

Prędkość ta jest sztywno zdefiniowana przez parametry mechaniczne osnowy – jej lokalny moduł sztywności na ścinanie $\mu$ oraz gęstość bezwładnościową masową $\rho$:

$$c_{\perp} = \sqrt{\frac{\mu}{\rho}}$$

Każda cząstka elementarna (będąca lokalnym splotem/węzłem topologiczny) zachowuje swoją wewnętrzną spójność strukturalną dzięki ciągłej wymianie informacji naprężeniowych między tworzącymi ją 0-cząstkami. Gdy węzeł zostaje przyspieszony do prędkości bliskich $c_{\perp}$ wewnątrz 3-brany, zaczyna doganiać czoło własnej fali naprężeniowej. Ośrodek przed poruszającym się splotem ulega nieliniowemu zagęszczeniu i usztywnieniu, tworząc strukturalny odpowiednik stożka Macha.

Obserwowane wówczas klasyczne efekty relatywistyczne – pozorny asymptotyczny wzrost masy inercyjnej oraz dylatacja czasu – nie wynikają ze zmian abstrakcyjnej czasoprzestrzeni, lecz są **czystymi zjawiskami hydro-elastodynamicznymi**. Cząstka napotyka potężny opór falowy ośrodka, a wewnętrzne procesy oscylacyjne wewnątrz splotu ulegają spowolnieniu z powodu wydłużenia dróg propagacji naprężeń w zagęszczonej osnowie.

### 6.6.2. Superluminalność w 4D i rejestracje interferometryczne

Ponieważ ograniczenie prędkości do wartości $c_{\perp}$ wynika bezpośrednio z gęstości i sztywności ścinania wewnątrz trójwymiarowej brany, limit ten **nie obowiązuje w kierunku ortogonalnym ($x^4$)**. Wymiar $x^4$ (otaczający *Bulk*) wykazuje cechy nadciekłego kondensatu 0-cząstek, pozbawionego gęstej sieci splotów fermionowych, co pozwala na propagację modów podłużnych ($\alpha$) oraz ruch struktur z prędkościami znacznie przekraczającymi $c_{\perp}$. To, co w 3D rejestrujemy jako cząstkę relatywistyczną, jest jedynie rzutem (cieniem) nadrzędnego, czterowymiarowego procesu dynamicznego.

W tym ujęciu eksperymenty interferometryczne takie jak LIGO nie rejestrują "falowania samej pustej geometrii", lecz rzeczywiste, potężne fronty fal uderzeniowych naprężeń poprzecznych (*stress-wave fronts*), rozchodzące się w osnowie z prędkością materiałową $c_{\perp}$. Fale te powstają podczas gwałtownych, nieliniowych reorganizacji strukturalnych – na przykład w trakcie fuzji dwóch Plazmoidów Topologicznych, gdy ich zablokowane strefy fazowe uderzają o siebie, generując makroskopowe "gromy naprężeniowe" w sprężystym tle Wszechświata.

Oto propozycja rygorystycznego, strukturyzowanego podsumowania Rozdziału 6 (dawnego 5), sformułowana w standardzie terminologicznym TSM (Topologicznej Geometrodynamiki Substratu) oraz w pełni spójna z formatem zakończenia Rozdziału 4:

## 6.7. Podsumowanie rozdziału 6

* **Ontologia grawitacji jako naciągu sprężystego:** Grawitacja zostaje odarta z relatywistycznej abstrakcji geometrycznej i zdefiniowana jako rzeczywiste, mechaniczne odkształcenie i naciąg poprzeczny trójwymiarowej osnowy (3-brany) skierowany ortogonalnie w stronę czwartego wymiaru przestrzennego ($x^4$). Równania Einsteina zostają w ten sposób zastąpione przez klasyczną elastodynamikę ośrodków ciągłych.
* **Przejście w reżim nieliniowy (Föppla-von Kármána):** O ile słabe pola grawitacyjne (limit newtonowski) poprawnie opisuje liniowe równanie Laplace’a ($\nabla^2 w = 0$), o tyle w pobliżu skrajnie gęstych splotów ugięcie membrany staje się tak potężne, że konieczne jest zastosowanie nieliniowych równań Föppla-von Kármána. Sprzężenie zginania z rozciąganiem wewnątrzbrany powoduje asymptotyczny wzrost efektywnej sztywności osnowy ($\mu_{\text{eff}}$), co skutecznie blokuje kolaps grawitacyjny.
* **Eliminacja osobliwości na rzecz Plazmoidów:** TSM kategorycznie odrzuca istnienie punktów o nieskończonej gęstości (czarnych dziur). W centrach galaktyk i zwiędłych gwiazd neutronowych, pod wpływem gigantycznego ciśnienia, powstają Topologiczne Plazmoidy – stabilne struktury o skończonym promieniu, znajdujące się w stanie maksymalnego mechanicznego zakleszczenia (*structural jamming*) komórek Wignera-Seitza.
* **Demistyfikacja prędkości światła ($c$):** Prędkość $c$ przestaje być uniwersalną stałą samej geometrii, a staje się materiałową prędkością dźwięku fal poprzecznych (ścinających) wewnątrz 3-brany. Asymptotyczny opór falowy przy zbliżaniu się do $c$ (klasyczny relatywistyczny wzrost masy) jest efektem czysto hydrodynamicznym – splot topologiczny poruszający się w Substracie dogania falę własnego naciągu, tworząc strukturalny odpowiednik akustycznego stożka Macha.
* **Superluminalność w wymiarze ortogonalnym ($x^4$):** Ponieważ ograniczenie prędkości do wartości $c_{\perp}$ wynika bezpośrednio ze sztywności ścinania trójwymiarowej osnowy, limit ten nie obowiązuje w kierunku prostopadłym. Otaczająca przestrzeń *Bulk* ($x^4$) wykazuje cechy nadciekłego kondensatu pozbawionego splotów fermionowych, co pozwala na propagację modów podłużnych ($\alpha$) oraz ruch struktur z prędkościami superluminalnymi ($v > c_{\perp}$).
* **Natura fal grawitacyjnych w interpretacji LIGO:** Eksperymenty interferometryczne nie rejestrują oscylacji pustej czasoprzestrzeni, lecz potężne, makroskopowe fronty fal uderzeniowych naprężeń poprzecznych (*stress-wave fronts*) rozchodzące się w Substracie z materiałową prędkością $c_{\perp}$ na skutek gwałtownych procesów reorganizacji splotów (np. zlewania się Plazmoidów). Podlega to potencjalnej falsyfikacji poprzez badanie anomalnego oporu hydrodynamicznego i nieliniowych odchyleń orbit ciasnych układów binarnych.