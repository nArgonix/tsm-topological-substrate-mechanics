<!-- ver:2.4.0 -->
# Rozdział 6: Grawitacja jako ortogonalny naciąg – wymiar 4D, Plazmoidy i nieliniowa dynamika kontinuum

W Mechanice Substratu Topologicznego (TSM) odrzucamy abstrakcję geometryczną, która przypisuje grawitacji status czystego zakrzywienia niematerialnej czasoprzestrzeni. Grawitacja zostaje tu zdefiniowana jako rzeczywiste naprężenie ortogonalne (naciąg poprzeczny) sprężystej 3-brany w kierunku czwartego wymiaru przestrzennego ($x^4$). Niniejszy rozdział przedstawia pełen formalizm matematyczny opisujący zachowanie osnowy zarówno w reżimie liniowym, jak i w skrajnie nieliniowych warunkach astrofizycznych, zastępując aparaturę Ogólnej Teorii Względności (OTW) klasyczną elastodynamiką ośrodków ciągłych.

Zgodnie z Rozdziałem 1.1, wszystkie procesy dynamiczne zachodzą w lokalnym czasie $t$, emergentnym z gęstości upakowania $\phi$. Grawitacja – jako deformacja brany – modyfikuje tę gęstość, a tym samym tempo upływu czasu, co zostało formalnie opisane w (1.1.5)–(1.1.6).

---

## 6.1. Ontologia grawitacji i limit liniowy (Równanie Laplace’a)

Nasz obserwowalny Wszechświat funkcjonuje jako izotropowa, trójwymiarowa membrana (3-brana) uformowana z globalnie zakleszczonych 0-cząstek (Rozdział 0.5). Zgodnie z rozkładem modów wprowadzonym w Rozdziale 2.1.4, składowe polaryzacji skierowane ortogonalnie do brany reprezentują lokalne ugięcia osnowy.

Gdy lokalne sprzężenie pól elektromagnetycznych i torsyjnych formuje stabilny splot topologiczny (fermion) o określonej gęstości energii, 3-brana reaguje na to skupisko wymuszeniem przemieszczenia wzdłuż osi $x^4$. Ten fizyczny gradient naprężenia osnowy na zewnątrz splotu jest przez obiekty testowe odbierany jako pole grawitacyjne.

Dla słabych i średnich gęstości energii (limit newtonowski), membrana dąży do minimalizacji swojej powierzchni i wyrównania naprężeń, zachowując się jak idealnie cienka, naciągnięta błona sprężysta. Równanie równowagi statycznej dla izotropowej membrany poddanej punktowemu obciążeniu poprzecznemu $q(r)$ sprowadza się do trójwymiarowego równania Laplace’a:

$$\nabla^2 w(\mathbf{r}) = 0, \quad \text{dla } r > 0 \tag{6.1.1}$$

gdzie $w(\mathbf{r})$ oznacza wielkość ugięcia (przemieszczenia) membrany w osi $x^4$ w punkcie $\mathbf{r} = (x^1, x^2, x^3)$.

Zakładając idealną symetrię sferyczną układu, operator Laplace’a we współrzędnych sferycznych redukuje się do postaci:

$$\frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{dw}{dr} \right) = 0 \tag{6.1.2}$$

Całkując powyższe równanie dwukrotnie, otrzymujemy jawne rozwiązanie na profil ugięcia w funkcji odległości $r$ od centrum splotu:

$$w(r) = \frac{C}{r} + C_2 \tag{6.1.3}$$

Przyjmując warunek brzegowy w nieskończoności $w(r \to \infty) = 0$, stała integracji $C_2$ zeruje się. Stała $C$ jest wprost proporcjonalna do całkowitej energii splotu (masy $M$) oraz odwrotnie proporcjonalna do napięcia powierzchniowego brany $T_b$: $C = - \frac{G M}{T_b}$.

Siła grawitacyjna $\mathbf{F}_g$ działająca na cząstkę testową o masie $m$ wewnątrz brany jest bezpośrednim gradientem energii potencjalnej $V_g(r)$, zdefiniowanej sztywno poprzez pracę wykonaną przeciwko napięciu osnowy jako $V_g(r) = T_b m w(r)$. Stąd:

$$\mathbf{F}_g = - \nabla V_g(r) = - T_b m \nabla w(r) = - \frac{G M m}{r^2} \hat{\mathbf{r}} \tag{6.1.4}$$

W ten sposób prawo odwrotnych kwadratów Newtona zostaje wyprowadzone nie z postulatu wymiany hipotetycznych cząstek (grawitonów), lecz jako bezpośredni rzut geometryczny poprzecznego, trójwymiarowego profilu ugięcia kontinuum sprężystego.

---

## 6.2. Sformalizowana elastodynamika 3-brany: Nieliniowe ugięcie w $\mathbb{R}^4$

Aby poprawnie opisać drastyczne ugięcie trójwymiarowego kontinuum osnowy w kierunku ortogonalnym (wymiar $x^4$), klasyczna liniowa teoria sprężystości musi zostać zastąpiona ścisłym formalizmem dużych odkształceń. W modelu TSM 3-brana nie jest dwuwymiarową powłoką, lecz pełnoprawną trójwymiarową przestrzenią izotropową zanurzoną w $\mathbb{R}^4$.

### 6.2.1. Tensor odkształceń Green-St Venanta dla 3-brany

Niech $\mathbf{x} = (x^1, x^2, x^3)$ oznacza współrzędne wewnątrz płaskiej 3-brany, $u_a(\mathbf{x})$ wektor przemieszczeń wewnątrzbranowych, a $w(\mathbf{x})$ skalarne ugięcie membrany w kierunku czwartego wymiaru $x^4$. Ścisłą miarą deformacji geometrycznej uwzględniającą sprzężenie wymiarów jest skończony tensor odkształceń Green-St Venanta $E_{ab}$ (gdzie indeksy $a, b \in \{1, 2, 3\}$):

$$E_{ab} = \frac{1}{2} (\partial_a u_b + \partial_b u_a + \partial_a w \partial_b w) \tag{6.2.1}$$

gdzie:
- $u_a$ – składowe przemieszczeń wewnątrz brany $[\text{m}]$,
- $w$ – ugięcie brany w kierunku $x^4$ $[\text{m}]$,
- $\partial_a$ – pochodna cząstkowa po współrzędnej $x^a$.

To równanie rygorystycznie definiuje fakt, że każde fizyczne „wypchnięcie” osnowy w wymiar $x^4$ (reprezentowane przez gradient $\partial_a w$) automatycznie i nieliniowo rozciąga 3-branę w jej własnych wymiarach przestrzennych.

### 6.2.2. Trójwymiarowe równania kompatybilności i uogólniony operator Monge’a-Ampère’a

W trójwymiarowej 3-brane wprowadzanie skalarnej funkcji naprężeń Airy'ego (właściwej dla 2D) jest matematycznie niewystarczające. Aby zagwarantować ciągłość ośrodka (brak fizycznych rozerwań Matrycy), tensor odkształceń $E_{ab}$ musi bezwzględnie spełniać trójwymiarowe równania kompatybilności Saint-Venanta.

Korzystając z trójwymiarowego symbolu Leviego-Civity $\epsilon^{acd}$, warunek ten zapisujemy ściśle jako:

$$\epsilon^{acd} \epsilon^{bef} \partial_c \partial_e E_{df} = 0 \tag{6.2.2}$$

Podstawiając do tego równania naszą definicję nieliniowego tensora $E_{ab}$, pochodne przemieszczeń wewnątrzbranowych ($u_a$) tożsamościowo znikają. Pozostaje jedynie nieliniowy człon sprzęgający, który definiuje ścisły, trójwymiarowy odpowiednik nawiasu Monge'a-Ampère'a dla 3-brany, reprezentowany przez tensor źródeł skręcenia $S^{ab}[w]$:

$$S^{ab}[w] = - \frac{1}{2} \epsilon^{acd} \epsilon^{bef} \partial_c \partial_e w \partial_d \partial_f w \tag{6.2.3}$$

### 6.2.3. Tensor naprężeń Beltramiego i pełen układ sprzężony

Aby spełnić warunek równowagi wewnętrznej $\partial_b \sigma^{ab} = 0$, w trójwymiarowej Matrycy zamiast funkcji skalarnej wprowadzamy symetryczny tensor funkcji naprężeń Beltramiego $\Phi_{cd}$, z którego generowane jest makroskopowe pole naprężeń wewnątrzbranowych:

$$\sigma^{ab} = \epsilon^{acd} \epsilon^{bef} \partial_c \partial_e \Phi_{df} \tag{6.2.4}$$

Integrując powyższe wyprowadzenia, uzyskujemy ostateczny, ścisły, trójwymiarowy odpowiednik równań Föppla-von Kármána opisujący grawitacyjny naciąg 3-brany:

$$D \nabla^4 w = \sigma^{ab} \partial_a \partial_b w + q(\mathbf{r}) \tag{6.2.5}$$

$$\epsilon^{acd} \epsilon^{bef} \partial_c \partial_e (\mathbb{C}^{-1}_{dfpq} \sigma^{pq}) = S^{ab}[w] \tag{6.2.6}$$

Gdzie:
- $\nabla^4 = (\partial_1^2 + \partial_2^2 + \partial_3^2)^2$ – trójwymiarowy operator biharmoniczny,
- $\mathbb{C}^{-1}$ – tensor podatności sprężystej 0-Matrycy $[\text{Pa}^{-1}]$,
- $q(\mathbf{r})$ – obciążenie ortogonalne generowane przez splot $[\text{N} \cdot \text{m}^{-3}]$.

Sztywność giętna objętości 3-brany $D$ jest jawnym parametrem materiałowym zdefiniowanym strukturalnie jako:

$$D = \frac{E h^3}{12(1-\nu^2)} \tag{6.2.7}$$

gdzie $E$ reprezentuje moduł Younga czystej osnowy $[\text{Pa}]$, $\nu$ to współczynnik Poissona (bezwymiarowy), a $h$ to szerokość funkcji lokalizacji energii 3-brany w kierunku $x^4$, ściśle powiązana ze skalą Plancka.

W celu zachowania pełnej kowariancji, tensor podatności sprężystej $\mathbb{C}^{-1}_{dfpq}$ dla izotropowej 0-Matrycy zostaje jawnie wyznaczony poprzez rzutowanie na tensor metryczny tła $g_{df}$:

$$\mathbb{C}^{-1}_{dfpq} \sigma^{pq} = \frac{1+\nu}{E} \sigma_{df} - \frac{\nu}{E} \sigma^c_c g_{df} \tag{6.2.8}$$

gdzie $\sigma^c_c = \text{Tr}(\sigma)$ reprezentuje ślad tensora naprężeń (ciśnienie hydrostatyczne osnowy).

Drugi niezmiennik dewiatora naprężeń $J_2$, sterujący nieliniowym usztywnieniem modułu ścinania $\mu_{\text{eff}}$, jest zdefiniowany jako:

$$J_2 = \frac{1}{2} s_{ab} s^{ab} \tag{6.2.9}$$

gdzie tensor dewiatora $s^{ab} = \sigma^{ab} - \frac{1}{3} \sigma^c_c g^{ab}$ reprezentuje czyste naprężenia ścinające.

Nieliniowe sprzężenie narzuca asymptotyczne usztywnienie tła. W miarę wzrostu lokalnych ciśnień, gdy $J_2$ zbliża się do wartości krytycznej $J_{2,\text{crit}}$, efektywny moduł sprężystości poprzecznej $\mu_{\text{eff}}$ rośnie nieliniowo:

$$\mu_{\text{eff}}(J_2) = \frac{\mu_0}{1 - \left(\frac{J_2}{J_{2,\text{crit}}}\right)^2} \tag{6.2.10}$$

Gdy $J_2 \to J_{2,\text{crit}}$, opór materiałowy 0-Matrycy dąży do nieskończoności ($\mu_{\text{eff}} \to \infty$). Oznacza to, że continuum stawia absolutny opór przed dalszym wyciąganiem, co wymusza istnienie minimalnego promienia krzywizny $R_{\text{min}}$ dla dowolnego skupiska energii. Matematyczna osobliwość typu $1/r$ o nieskończonej gęstości grawitacyjnej jest w TSM fizycznie niemożliwa.

---

## 6.3. Plazmoidy Topologiczne zamiast Czarnych Dziur

Konsekwencją załamania się osobliwości jest redefinicja obiektów kompaktowych. Pojęcie „Czarnej Dziury” jako geometrycznej dziury w czasoprzestrzeni zostaje zastąpione pojęciem **Plazmoidu Topologicznego**. Plazmoid to skończony, stabilny i ultra-gęsty obiekt fizyczny, w którym 0-cząstki pod wpływem skrajnych ciśnień grawitacyjnych osiągnęły stan absolutnego zakleszczenia strukturalnego ($\phi \to \phi_{\text{max}}$, Rozdział 0.6).

- **Horyzont Zdarzeń jako krawędź fazowa:** Horyzont nie jest matematyczną kurtyną bez powrotu, lecz fizyczną granicą przejścia fazowego osnowy. Na zewnątrz tej krawędzi 0-Matryca zachowuje pełne właściwości sprężyste. Wewnątrz granicy osnowa przechodzi w stan sztywnego szkła topologicznego. Światło (fala poprzeczna) wkraczając w tę strefę nie wpada do osobliwości, lecz ulega konwersji w mody podłużne i zostaje włączone do energii wewnętrznej plazmoidu. **Informacja nie ulega zniszczeniu** – zostaje mechanicznie utrwalona w quasikrystalicznej geometrii zgniecionej sieci (Rozdział 4.5). Entropia spektralna wewnątrz plazmoidu spada do zera ($S_{\text{spec}} \to 0$).
- **Mechanizm dżetów galaktycznych:** Ponieważ Plazmoid jest dynamicznym, ściśniętym splotem, nieustannie dochodzi w nim do fluktuacji naprężeń. Gdy lokalne ciśnienie wewnętrzne przewyższy wytrzymałość topologicznego zamka, 0-Matryca gwałtownie uwalnia nadmiar zgromadzonej energii potencjalnej. Uwolnienie to następuje w sposób wysoce anizotropowy – poprzez wyrzut skompresowanej materii i modów podłużnych wzdłuż osi najmniejszego oporu mechanicznego (osi rotacji układu), co teleskopy rejestrują jako dżety galaktyczne.

---

## 6.4. Dynamika galaktyczna: Torsyjne Wleczenie i eliminacja Ciemnej Materii

Wprowadzenie Plazmoidu jako rotującego, fizycznego splotu o gigantycznym momencie pędu pozwala rozwiązać kluczowe anomalie dynamiczne w skalach makroskopowych bez konieczności wprowadzania egzotycznych cząstek Ciemnej Materii.

### 6.4.1. Torsyjne Wleczenie i płaskie krzywe rotacji gwiazd

W klasycznej astrofizyce prędkość liniowa gwiazd na peryferiach galaktyk powinna maleć wraz z odległością $r$ zgodnie z dynamiką keplerowską ($v \propto 1/\sqrt{r}$). Obserwacje wykazują jednak, że krzywa rotacji stabilizuje się na stałym poziomie ($v \approx \text{const}$).

W TSM zjawisko to jest bezpośrednią konsekwencją Torsyjnego Wleczenia (hydro-elastodynamicznego odpowiednika efektu Lense-Thirringa). Rotujący z ogromną prędkością centralny Plazmoid, z racji ekstremalnej lepkości topologicznej układu, dosłownie „wkręca” otaczającą go 0-Matrycę, generując makroskopowe, rotacyjne pole ścinania. Pole to rozchodzi się w głąb 3-brany, a jego bezpośrednim kinematycznym przejawem jest lokalny profil prędkości kątowej osnowy $\Omega(r)$. Gwiazdy znajdujące się na obrzeżach galaktyki nie są utrzymywane wyłącznie przez radialną siłę naciągu poprzecznego $\mathbf{F}_g = -\nabla w$, ale poruszają się wewnątrz rotującego wiru samej osnowy. Wypadkowa prędkość liniowa gwiazdy $v_{\text{total}}$ stanowi superpozycję jej lokalnej prędkości orbitalnej oraz prędkości dryfu unoszącego ją tła.

Równanie transmisji momentu pędu przez lepko-sprężystą strukturę 0-Matrycy przyjmuje postać:

$$\frac{d}{dr} \left( r^3 \mu_{\text{eff}}(r) \frac{d\Omega(r)}{dr} \right) = 0 \tag{6.4.1}$$

gdzie $\mu_{\text{eff}}(r)$ jest radialnym profilem nieliniowego modułu ścinania, indykowanym przez ugięcie grawitacyjne gęstego centrum.

Rozwiązanie definiuje pole dryfu tła:

$$v_{\text{drift}}(r) = r \Omega(r) = r \left( \Omega_0 - \int_{R_{\text{min}}}^{r} \frac{C_{\text{torsion}}}{x^3 \mu_{\text{eff}}(x)} dx \right) \tag{6.4.2}$$

gdzie:
- $\Omega_0$ – prędkość kątowa centralnego Plazmoidu $[\text{rad} \cdot \text{s}^{-1}]$,
- $R_{\text{min}}$ – promień Plazmoidu $[\text{m}]$,
- $C_{\text{torsion}}$ – stała całkowania zależna od momentu pędu Plazmoidu $[\text{N} \cdot \text{m}^2]$.

Na peryferiach galaktyki, funkcja ta w doskonały sposób kompensuje keplerowski spadek prędkości orbitalnej, wymuszając asymptotyczną stabilizację wypadkowej prędkości liniowej gwiazd. Spadek przestrzenny nieliniowego pola rotacyjnego w sprężystej membranie idealnie znosi ubytek klasycznego przyciągania radialnego, co całkowicie eliminuje potrzebę wprowadzania hipotetycznych cząstek Ciemnej Materii.

### 6.4.2. Zachowanie gwiazd w pobliżu centrum galaktyki (Orbita S2)

Nieliniowy reżim TSM znajduje bezpośrednie potwierdzenie w trajektoriach gwiazd krążących w bezpośrednim sąsiedztwie centralnego Plazmoidu Sgr A*, takich jak gwiazda S2. Podczas zbliżania się gwiazdy do perycentrum, układ opuszcza limit liniowy Laplace’a i wchodzi w strefę opisywaną równaniami Föppla-von Kármána.

Z powodu nieliniowego sztywnienia osnowy ($\mu_{\text{eff}} \to \infty$), rzeczywisty potencjał grawitacyjny staje się głębszy, a siła przyciągania zyskuje dodatkowy człon elastyczny. Jawna postać wektora wypadkowej siły grawitacyjnej w tym nieliniowym obszarze przyjmuje postać:

$$\mathbf{F}_{\text{TSM}}(r) = - \left( \frac{G M m}{r^2} + \frac{\mathcal{A}_{\text{nielin}}(J_2)}{r^4} \right) \hat{\mathbf{r}} \tag{6.4.3}$$

gdzie $\mathcal{A}_{\text{nielin}}$ jest nieliniowym współczynnikiem sprzężenia sprężystego, wyznaczanym bezpośrednio z lokalnego gradientu inwariantu $J_2$. Zgodnie z mechaniką klasyczną, każda wyższa korekta potęgowa potencjału Newtona narusza twierdzenie Bertranda, co wymusza gwałtowną precesję apsydalną orbity. Ruch rozetowy gwiazdy S2 oraz precesja jej peryhelium są w TSM naturalnym skutkiem nieliniowego oporu materiałowego naprężonej sieci, a nie czysto relatywistyczną korektą metryczną.

---

## 6.5. Redshift kosmologiczny a propagacja fal – rozwiązanie paradoksu zmiennego ośrodka

### 6.5.1. Globalna relaksacja Substratu a inwariantność przestrzenna

W skali kosmologicznej 3-brana podlega monotonicznemu, powolnemu procesowi relaksacji naprężeń szczątkowych po Wielkim Wydarzeniu. Konsekwencją tego procesu jest globalny, stopniowy spadek podstawowej gęstości upakowania 0-Matrycy w czasie absolutnym $\tau$:

$$\phi(\tau) \to \phi_0$$

Ponieważ relaksacja ta zachodzi w sposób wielokierunkowy i jednorodny w całej objętości obserwowalnego Wszechświata, w każdym punkcie ewolucji zachowana jest ścisła jednorodność przestrzenna kontinuum tła ($\nabla \phi_{\text{global}} = 0$).

Zgodnie z twierdzeniem Noether, niezmienniczość układu względem translacji przestrzennych nakłada rygorystyczne żądanie zachowania pędu falowego. Oznacza to, że podczas całej podróży fotonu przez relaksujący Substrat, jego bezwzględny wektor falowy $\mathbf{k}$ oraz bezwzględna (mierzona w metryce laboratoryjnej Staniu Zero) długość fali $\lambda_{\text{abs}}$ pozostają nienaruszone:

$$\frac{d\mathbf{k}}{d\tau} = 0 \implies \lambda_{\text{abs}}(\tau) = \lambda_{\text{em}} = \text{const}$$

Model TSM kategorycznie odrzuca zatem koncepcję kinematycznego „rozciągania” długości fali światła w locie. Foton nie traci energii w próżni ani nie podlega rozszerzaniu metrycznemu, ponieważ przestrzeń Substratu jest skończona i statyczna pod względem geometrycznym. Cały obserwowany efekt przesunięcia ku czerwieni jest rezultatem warunków brzegowych emisji oraz ewolucji lokalnych standardów pomiarowych.

### 6.5.2. Mechanizm emisji w zagęszczonej osnowie (Pamięć Gęstości)

Rozważmy proces emisji fotonu przez układ atomowy w odległej przeszłości (w momencie $\tau_{\text{em}}$), kiedy globalna gęstość osnowy wynosiła $\phi_{\text{em}} > \phi_0$.

Zgodnie z kanoniczną definicją czasu własnego (Podrozdział 1.1.3), lokalna sekunda $dt$ w gęstszym ośrodku trwa dłużej w ujęciu bezwzględnym z powodu wyższego oporu strukturalnego osnowy stawiającego opór makroskopowym procesom relaksacyjnym:

$$dt_{\text{em}} = dt_0 \cdot \frac{\phi_{\text{em}}}{\phi_0}$$

Dla lokalnego obserwatora w momencie $\tau_{\text{em}}$, częstotliwość konkretnego przejścia kwantowego wynosi $\nu_0$ (jest stałą cechą strukturalną danego układu wiązań solitonowych), co odpowiada lokalnemu okresowi fali $\Delta t_{\text{em}} = 1/\nu_0$. Przeliczając ten okres na dzisiejszy standard czasu (gdzie gęstość zrelaksowała do $\phi_0$, a zatem $dt_0 = dt_{\text{abs}}$), bezwzględny okres drgań emitowanej fali wynosi:

$$\Delta t_{\text{abs}} = \Delta t_{\text{em}} \cdot \frac{\phi_{\text{em}}}{\phi_0} = \frac{1}{\nu_0} \cdot \frac{\phi_{\text{em}}}{\phi_0}$$

Ponieważ bezwzględny okres fali jest dłuższy, jej bezwzględna częstotliwość drgań $\nu_{\text{em, abs}}$ w skali referencyjnej Stanu Zero jest proporcjonalnie niższa:

$$\nu_{\text{em, abs}} = \frac{1}{\Delta t_{\text{abs}}} = \nu_0 \cdot \frac{\phi_0}{\phi_{\text{em}}}$$

Materiałowa prędkość fal poprzecznych $c_{\perp} = \sqrt{\mu/\rho}$ jest fundamentalną niezmienniczą stałą elastyczną całego Substratu i nie ulega zmianie podczas globalnej relaksacji. W związku z tym, bezwzględna długość fali uformowana w punkcie emisji wynosi:

$$\lambda_{\text{em}} = \frac{c_{\perp}}{\nu_{\text{em, abs}}} = \frac{c_{\perp}}{\nu_0} \cdot \frac{\phi_{\text{em}}}{\phi_0} = \lambda_0 \cdot \frac{\phi_{\text{em}}}{\phi_0}$$

gdzie $\lambda_0 = c_{\perp}/\nu_0$ definiuje standardową długość fali tego samego przejścia atomowego, jaką mierzymy w laboratorium dzisiaj. Równanie to dowodzi, że foton opuszcza źródło w przeszłości z już wbudowaną, dłuższą bezwzględną długością fali ($\lambda_{\text{em}} > \lambda_0$), będącą bezpośrednim odzwierciedleniem dylatacji czasu uwarunkowanej pierwotną gęstością $\phi_{\text{em}}$.

### 6.5.3. Ostateczny bilans optyczny i definicja stałej Hubble’a

Ponieważ – zgodnie z Sekcją 6.5.1 – długość fali nie ulega modyfikacji podczas propagacji przez jednorodny przestrzennie Substrat, foton dociera do dzisiejszego detektora z niezmienioną wartością bezwzględną:

$$\lambda_{\text{obs}} = \lambda_{\text{em}} = \lambda_0 \cdot \frac{\phi_{\text{em}}}{\phi_0}$$

Dzisiejszy obserwator rejestruje ten foton i porównuje jego długość fali ze swoim lokalnym, współczesnym wzorcem laboratoryjnym $\lambda_0$. Definiując bezwymiarowy parametr przesunięcia ku czerwieni $z$:

$$1 + z = \frac{\lambda_{\text{obs}}}{\lambda_0} = \frac{\lambda_0 \cdot \frac{\phi_{\text{em}}}{\phi_0}}{\lambda_0} = \frac{\phi_{\text{em}}}{\phi_0}$$

Po przekształceniu otrzymujemy ostateczną, ścisłą definicję redshiftu kosmologicznego w mechanice TSM:

$$z = \frac{\phi_{\text{em}}}{\phi_0} - 1$$

W ujęciu tym prawo Hubble’a przestaje być dowodem na ucieczkę galaktyk. Stała Hubble’a $H_0$ zostaje rygorystycznie przedefiniowana jako bezpośrednia miara logarytmicznego tempa historycznej relaksacji struktury Substratu w bieżącej epoce kosmologicznej:

$$H_0 = -\frac{1}{\phi_0} \left. \frac{d\phi}{d\tau} \right|_{\tau=\tau_0}$$

Dzięki takiemu sformułowaniu matematycznemu Podrozdział 6.5 wskazuje jednoznacznie: redshift jest efektem optycznym wynikającym ze stałego spadku gęstości tła Wszechświata, co w pełni wyjaśnia obserwacje astrofizyczne bez konieczności wprowadzania sprzecznych z mechaniką klasyczną pojęć, takich jak ekspansja samej przestrzeni czy ciemna energia.

---

## 6.6. Fizyczna natura stałej $c$ i fale naprężeniowe (LIGO)

W Mechanice Substratu Topologicznego stała $c$ traci swój mistyczny status nienaruszalnej bariery geometrycznej czasoprzestrzeni. Zostaje ona sprowadzona do roli **krytycznej prędkości propagacji fal poprzecznych ($c_{\perp}$)** wewnątrz sprężystego continuum 3-brany.

### 6.6.1. Mechaniczne pochodzenie efektów relatywistycznych

Prędkość ta jest sztywno zdefiniowana przez parametry mechaniczne osnowy – jej lokalny moduł sztywności na ścinanie $\mu$ oraz gęstość bezwładnościową masową $\rho$ (Rozdział 2.1.3):

$$c_{\perp} = \sqrt{\frac{\mu}{\rho}} \tag{6.6.1}$$

Każda cząstka elementarna (będąca lokalnym splotem/węzłem topologicznym) zachowuje swoją wewnętrzną spójność strukturalną dzięki ciągłej wymianie informacji naprężeniowych między tworzącymi ją 0-cząstkami. Gdy węzeł zostaje przyspieszony do prędkości bliskich $c_{\perp}$ wewnątrz 3-brany, zaczyna doganiać czoło własnej fali naprężeniowej. Ośrodek przed poruszającym się splotem ulega nieliniowemu zagęszczeniu i usztywnieniu, tworząc strukturalny odpowiednik stożka Macha.

Obserwowane wówczas klasyczne efekty relatywistyczne – pozorny asymptotyczny wzrost masy inercyjnej oraz dylatacja czasu – nie wynikają ze zmian abstrakcyjnej czasoprzestrzeni, lecz są **czystymi zjawiskami hydro-elastodynamicznymi**, spójnymi z wyprowadzeniem dylatacji kinematycznej w Rozdziale 1.1.6. Cząstka napotyka potężny opór falowy ośrodka, a jej gęstość wewnętrzna $\phi$ rośnie z czynnikiem Lorentza, co bezpośrednio spowalnia lokalny czas.

### 6.6.2. Superluminalność w 4D i rejestracje interferometryczne

Ponieważ ograniczenie prędkości do wartości $c_{\perp}$ wynika bezpośrednio z gęstości i sztywności ścinania wewnątrz trójwymiarowej brany, limit ten **nie obowiązuje w kierunku ortogonalnym ($x^4$)**. Wymiar $x^4$ (otaczający *Bulk*) wykazuje cechy nadciekłego kondensatu 0-cząstek, pozbawionego gęstej sieci splotów fermionowych, co pozwala na propagację modów podłużnych ($\alpha$) z prędkościami znacznie przekraczającymi $c_{\perp}$. To, co w 3D rejestrujemy jako cząstkę relatywistyczną, jest jedynie rzutem (cieniem) nadrzędnego, czterowymiarowego procesu dynamicznego.

W tym ujęciu eksperymenty interferometryczne takie jak LIGO nie rejestrują „falowania samej pustej geometrii”, lecz rzeczywiste, potężne fronty fal uderzeniowych naprężeń poprzecznych (*stress-wave fronts*), rozchodzące się w osnowie z prędkością materiałową $c_{\perp}$. Fale te powstają podczas gwałtownych, nieliniowych reorganizacji strukturalnych – na przykład w trakcie fuzji dwóch Plazmoidów Topologicznych, gdy ich zablokowane strefy fazowe uderzają o siebie, generując makroskopowe „gromy naprężeniowe” w sprężystym tle Wszechświata.

---

## 6.7. Podsumowanie Rozdziału 6

- **Ontologia grawitacji jako naciągu sprężystego:** Grawitacja to mechaniczne odkształcenie i naciąg poprzeczny 3-brany w kierunku $x^4$. Równania Einsteina zastąpione są elastodynamiką ośrodków ciągłych, z prawem Newtona jako limitem liniowym.
- **Przejście w reżim nieliniowy (Föppla-von Kármána):** Silne pola grawitacyjne wymagają nieliniowych równań, w których sprzężenie zginania z rozciąganiem powoduje asymptotyczny wzrost $\mu_{\text{eff}}$ i blokuje kolaps grawitacyjny.
- **Eliminacja osobliwości na rzecz Plazmoidów:** W centrach galaktyk zamiast czarnych dziur istnieją Plazmoidy – stabilne struktury w stanie maksymalnego zakleszczenia ($\phi \to \phi_{\text{max}}$). Informacja wewnątrz nich jest zachowana w zamrożonej geometrii sieci ($S_{\text{spec}} \to 0$).
- **Demistyfikacja prędkości światła ($c$):** $c$ to materiałowa prędkość fal poprzecznych $c_{\perp} = \sqrt{\mu/\rho}$. Relatywistyczny wzrost masy to opór falowy ośrodka, a dylatacja czasu – skutek wzrostu gęstości $\phi$ w poruszającym się węźle.
- **Superluminalność w wymiarze ortogonalnym ($x^4$):** Ograniczenie $c_{\perp}$ dotyczy tylko 3-brany. W $x^4$ możliwa jest propagacja superluminalna modów podłużnych.
- **Redshift jako pamięć gęstości:** Przesunięcie ku czerwieni wynika z emisji światła w gęstszej osnowie w przeszłości ($z = \phi_{\text{em}}/\phi_0 - 1$), a stała Hubble'a jest miarą tempa historycznej relaksacji osnowy.
- **Natura fal grawitacyjnych (LIGO):** Rejestrowane fale to fronty naprężeń poprzecznych w osnowie, generowane przez gwałtowne procesy astrofizyczne, takie jak fuzje Plazmoidów.
- **Eliminacja Ciemnej Materii i Ciemnej Energii:** Płaskie krzywe rotacji tłumaczy Torsyjne Wleczenie Plazmoidów, a odchylenia SN Ia – ewolucja $G_{\text{eff}}$ i historyczna gęstość osnowy.