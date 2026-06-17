<!-- ver:2.9.7 -->

# 1. Formalizm Mechaniki Substratu Topologicznego – czas emergentny, dynamika i kinematyka relatywistyczna

Zgodnie z aksjomatami sformułowanymi w Rozdziale 0, fundamentalna przestrzeń to 4‑wymiarowa, skończona bańka wypełniona zakleszczonymi 0‑cząstkami. Zanim przejdziemy do opisu oddziaływań i struktur materialnych, konieczne jest rygorystyczne zdefiniowanie czasu oraz dynamiki samej osnowy. Model TSM całkowicie odrzuca koncepcję absolutnego czasu newtonowskiego oraz relatywistycznej czasoprzestrzeni jako bytu pierwotnego. Czas, podobnie jak przestrzeń, jest zjawiskiem w pełni emergentnym.

## 1.1. Czas w ujęciu TSM – od lokalnej gęstości osnowy do mierzonego upływu zjawisk

### 1.1.1. Granica poznania i eliminacja fluktuacji sub-planckowskich

0-Matryca w swoim stanie podstawowym charakteryzuje się permanentnymi, mikroskopijnymi drganiami cząstek osnowy wokół ich położeń równowagi, co generuje niekoherentny szum tła (temperaturę Substratu $T_{\text{sub}}$). Zgodnie z zasadą rygoru empirycznego, model TSM kategorycznie odrzuca próbę definiowania czasu poprzez te pierwotne oscylacje.

Wszelkie efekty falowe oraz lokalne zmiany częstotliwości zachodzące bezpośrednio na pojedynczych elementach sieci mają charakter sub-planckowski (poniżej długości $10^{-35}$ m). Próba ich operacyjnego definiowania z naszego, makroskopowego punktu widzenia jest pozbawiona sensu mierzalnego.

W konsekwencji model TSM rezygnuje z postulowania mikroskopijnych zależności częstotliwościowych pojedynczych 0-cząstek, przenosząc cały ciężar formalizmu na makroskopowe uśrednianie hydrodynamiczne.

### 1.1.2. Matematyczny formalizm uśredniania – Efektywna Gęstość Substratu

Aby powiązać dyskretną, sub-planckowską strukturę osnowy z mierzalnymi zjawiskami makroskopowymi, wprowadza się operator splotu (filtrowania) z funkcją okna o skali odcięcia równej skali Plancka ($\Lambda_{\text{Planck}}$). Operator ten wygładza lokalne, nieciągłe anomalie gęstości wokół pojedynczych defektów strukturalnych, dając w wyniku ciągłe pole efektywne.

Fundamentalna gęstość upakowania jest funkcją 4-wymiarową: $\phi(\mathbf{X}) = \phi(x^1, x^2, x^3, x^4)$. Pełna forma operatora uśredniania to:

$$\langle\phi(\mathbf{X})\rangle_{\text{macro}} = \int_{\mathbb{R}^4} \phi(\mathbf{X}') \, W(\mathbf{X} - \mathbf{X}', \Lambda_{\text{Planck}}) \, d^4\mathbf{X}' \tag{1.1.2.1}$$

Obserwowalna gęstość na 3-branie ugiętej do $x^4 = w(\mathbf{x})$ to rzut tej całki:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} = \left.\langle\phi(\mathbf{X})\rangle_{\text{macro}}\right|_{x^4 = w(\mathbf{x})} \tag{1.1.2.2}$$

Ponieważ grubość 3-brany w kierunku $x^4$ jest rzędu $l_P$ (Sekcja 6.2, Równanie 6.2.7), całkowanie po $x^{4'}$ jest asymptotycznie zlokalizowane w otoczeniu Planckowym brany, co pozwala zdefiniować efektywną gęstość powierzchniową:

$$\phi_{\text{eff}}(\mathbf{x}') \equiv \int_{-\infty}^{+\infty} \phi(\mathbf{x}', x^{4'}) \, W_4\!\left(w(\mathbf{x}') - x^{4'}, \Lambda_{\text{Planck}}\right) dx^{4'} \tag{1.1.2.3}$$

gdzie $W_4$ jest jednoczynnikową składową okna w osi ortogonalnej. Obserwowalna 3D gęstość makroskopowa przyjmuje wtedy postać:Fundamentalna gęstość upakowania jest polem 4-wymiarowym, zdefiniowanym na pełnej przestrzeni 0-Matrycy: $\phi(\mathbf{X}) = \phi(x^1, x^2, x^3, x^4)$. Pełny operator uśredniania makroskopowego obejmuje wszystkie cztery wymiary przestrzenne:

$$\langle\phi(\mathbf{X})\rangle_{\text{macro}} = \int_{\mathbb{R}^4} \phi(\mathbf{X}') \, W(\mathbf{X} - \mathbf{X}', \Lambda_{\text{Planck}}) \, d^4\mathbf{X}' \tag{1.1.2.4}$$

gdzie:
- $\mathbf{X} = (x^1, x^2, x^3, x^4)$ – 4-wektor pozycji w 0-Matrycy,
- $\phi(\mathbf{X}')$ – surowa, mikroskopijna gęstość lokalna osnowy w pełnej przestrzeni 4D,
- $W$ – normalizowana 4-wymiarowa funkcja przejścia (okno filtracyjne), eliminująca szum sub-planckowski,
- $\Lambda_{\text{Planck}}$ – skala odcięcia przestrzennego.
  
**Redukcja do obserwowanej gęstości 3D na 3-branie.**
Ponieważ wszystkie makroskopowe przyrządy pomiarowe (zegary atomowe, detektory) są strukturami węzłów topologicznych uwięzionymi wewnątrz 3-brany (Sekcja 1.5 Rozdziału 0), bezpośrednio dostępna jest wyłącznie wartość $\langle\phi(\mathbf{X})\rangle_{\text{macro}}$ zrestryktowana do hiperpowierzchni 3-brany. W stanie niezakłóconym brana zajmuje hiperpowierzchnię $x^4 = 0$; w obecności odkształceń grawitacyjnych jest ugięta do $x^4 = w(\mathbf{x})$ (Rozdział 6). Obserwowalna makroskopowa gęstość upakowania w punkcie $\mathbf{x} = (x^1, x^2, x^3)$ jest zatem rzutem:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} \equiv \left.\langle\phi(\mathbf{X})\rangle_{\text{macro}}\right|_{x^4 = w(\mathbf{x})} \tag{1.1.2.5}$$

Funkcja okna $W$ jest separowalna względem składowych brany i wymiaru ortogonalnego: $W(\mathbf{X}-\mathbf{X}', \Lambda_P) = W_3(\mathbf{x}-\mathbf{x}', \Lambda_P) \cdot W_4(x^4 - x^{4'}, \Lambda_P)$. Definiujemy efektywną gęstość powierzchniową 3D jako całkę $W_4$-ważoną wzdłuż osi ortogonalnej:

$$\phi_{\text{eff}}(\mathbf{x}') \equiv \int_{-\infty}^{+\infty} \phi(\mathbf{x}', x^{4'}) \, W_4\!\left(w(\mathbf{x}') - x^{4'}, \, \Lambda_{\text{Planck}}\right) dx^{4'} \tag{1.1.2.6}$$

Ponieważ charakterystyczna grubość 3-brany w kierunku $x^4$ jest rzędu skali Plancka $h \sim l_P$ (por. Sekcja 6.2, Równanie 6.2.01), a $W_4$ eliminuje wkłady spoza tego zakresu, całkowanie w (3) jest asymptotycznie zlokalizowane w otoczeniu Planckowym brany. Wyniki obserwowalne nie zależą od szczegółów struktury 0-Matrycy poza tą strefą. Ostateczna, operacyjna forma efektywnej gęstości makroskopowej na 3-branie przyjmuje postać:

$$\langle\phi(\mathbf{x})\rangle_{\text{macro}} = \int_{\mathbb{R}^3} \phi_{\text{eff}}(\mathbf{x}') \, W_3(\mathbf{x} - \mathbf{x}', \Lambda_{\text{Planck}}) \, d^3\mathbf{x}' \tag{1.1.2.7}$$

W płaskiej, niezakłóconej 3-branie ($w \equiv 0$, $\phi$ niezależne od $x^4$ w skali Planckowej) zachodzi $\phi_{\text{eff}}(\mathbf{x}') \equiv \phi(\mathbf{x}', 0)$, a równanie (4) redukuje się do standardowego 3D splotu gęstości osnowy z funkcją wygładzającą.

**Uwaga o spójności grawitacyjno-temporalnej:** Zależność $\phi_{\text{eff}}$ od ugięcia brany $w(\mathbf{x})$ (przez argument $W_4$) stanowi mechanistyczne uzasadnienie grawitacyjnej dylatacji czasu (Sekcja 1.1.5): węzeł topologiczny indukujący ugięcie $w > 0$ lokalnie przesuwa punkt próbkowania funkcji $W_4$ w obszar osnowy o wyższym ciśnieniu topologicznym, podnosząc $\phi_{\text{eff}}$ i zwalniając lokalny czas własny $dt$ zgodnie z równaniem kanonicznym (Sekcja 1.1.3). Zależność (1.1.5) jest więc limitem liniowym tego mechanizmu, a nie niezależnym założeniem.

### 1.1.3. Kanoniczna definicja czasu makroskopowego

Czas nie jest pierwotnym wymiarem ani samodzielną areną ewolucji układów. Czas mierzony w skali makroskopowej przez dowolne przyrządy pomiarowe (które same stanowią struktury złożone z miliardów węzłów topologicznych) jest parametrem operacyjnym ewolucji strukturalnej, ściśle zależnym od efektywnej gęstości osnowy.

Przyrost lokalnego czasu własnego $dt$ wyraża się równaniem:

<span id="eq-r1b">$$dt = dN \cdot T_0 \cdot \frac{\phi_0}{\langle\phi\rangle_{\text{macro}}} \tag{1.1.3.1}$$</span>

gdzie:
- $dt$ – przyrost lokalnego czasu własnego [s],
- $dN$ – liczba cykli makroskopowego procesu okresowego (np. oscylacji atomowych w zegarze),
- $T_0$ – okres referencyjny w niezaburzonej, stacjonarnej osnowie, 
- $\phi_0$ – podstawowa gęstość upakowania 0-Matrycy w Stanie Zero,
- $\langle\phi\rangle_{\text{macro}}$ – uśredniona hydrodynamicznie gęstość osnowy w obszarze zajmowanym przez układ pomiarowy.

Wyższa uśredniona gęstość $\langle\phi\rangle_{\text{macro}}$ generuje większy opór ośrodka dla makroskopowych procesów relaksacyjnych i propagacji sygnałów. Przekłada się to na zmniejszenie przyrostu lokalnego czasu własnego ($dt$ maleje dla stałej liczby cykli $dN$) względem płaskiego tła, co obserwujemy jako spowolnienie tempa upływu procesów fizycznych. Z perspektywy zewnętrznego obserwatora lokalna sekunda ulega rozciągnięciu, ponieważ aparat matematyczny rygorystycznie wiąże gęstość z mianownikiem operatora przyrostu czasu.

### 1.1.4. Kinematyczna dylatacja czasu jako izotropowe spiętrzenie osnowy

Ruch makroskopowego obiektu fizycznego w 0-Matrycy nie polega na mechanicznym przesuwaniu litej bryły, która spycha przed sobą ośrodek, lecz na bezstratnej propagacji kolektywnego wzoru węzłów-solitonów przez zakleszczony Substrat.

Materia o strukturze makroskopowej zachowuje się jak porowata siatka o dużych oczkach poruszająca się w ośrodku – Substrat swobodnie przenika przez strukturę makroskopową, a lokalna sieć stale przepływa przez obiekt. Podczas ruchu układu z prędkością współrzędnościową $v$, na każdym pojedynczym węźle siatki dochodzi do mikroskopijnych, lokalnych spiętrzeń. Ponieważ efekty te są sub-planckowskie, ich jednostkowe definiowanie nie wprowadza lokalnej anizotropii kierunkowej dla pojedynczych atomów.

Jednak w skali makroskopowej, wewnątrz całej objętości zajmowanej przez poruszające się ciało, następuje konstruktywna akumulacja tych mikro-odkształceń. Obecność poruszającej się struktury materii ogranicza swobodną relaksację osnowy, zamykając podwyższoną gęstość wewnątrz obwiedni obiektu. Generuje to całkowicie jednorodne i izotropowe (wielokierunkowe) spiętrzenie uśrednionej osnowy w całym ciele:

<span id="eq-r1c">$$\langle\phi(v)\rangle_{\text{macro}} = \phi_0 \cdot \gamma = \frac{\phi_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} \tag{1.1.4.1}$$</span>

Dzięki temu, że spiętrzenie $\langle\phi(v)\rangle_{\text{macro}}$ przyjmuje formę jednorodnego pola skalarnego wewnątrz obwiedni poruszającego się układu:

1.  Wszystkie zegary wewnątrz tego obiektu – bez względu na to, czy są zorientowane równolegle, czy prostopadle do wektora prędkości – doświadczają identycznego spowolnienia czasu. Eliminacja gradientu kierunkowego dla tempa upływu czasu w skali makro zapewnia pełną zgodność TSM z fizyką doświadczalną (eksperymenty Kennedy’ego-Thorndike’a oraz Michelsona-Morleya).
2.  Czynnik Lorentza $\gamma$ zostaje rygorystycznie wyprowadzony jako bezpośrednia, hydrodynamiczna konsekwencja nieliniowej sprężystości i oporu falowego (sztywności ścinania $\mu$) 0-Matrycy, gdy prędkość propagacji makroskopowej obwiedni zbliża się do granicznej prędkości fal poprzecznych $c_{\perp}$.

*Uwaga o asymetrii manifestacji:* Chociaż pole gęstości wewnątrz obwiedni jest makroskopowym skalarem (co gwarantuje izotropię dylatacji czasu), sam proces kontrakcji geometrycznej (opisany w Sekcji 1.7) jest efektem czysto dynamicznym, wywołanym jednostronnym oporem frontu fali wzdłuż wektora pędu układu.

### 1.1.5. Dylatacja grawitacyjna – związek z potencjałem $\Phi$

W Rozdziale 0.5 określono, że grawitacja to odkształcenie 3‑brany w czwarty wymiar, wywołane obecnością węzłów topologicznych. Odkształcenie to powoduje radialny gradient gęstości upakowania – im bliżej źródła, tym większa kompresja i większe $\phi$.

W słabym polu grawitacyjnym przyjmujemy liniową zależność gęstości efektywnej od modułu potencjału:

<span id="eq-r1d">$$\phi(\mathbf{x}) \approx \phi_0 \left(1 + \frac{|\Phi(\mathbf{x})|}{c_{\perp}^2}\right) \tag{1.1.5.1}$$</span>

gdzie $\Phi(\mathbf{x})$ to newtonowski potencjał grawitacyjny ($\Phi \le 0$), a $c_{\perp}$ to prędkość poprzecznych fal ścinających (światła).

### 1.1.6. Matematyczna spójność z czasem tła

Podstawiając zależność gęstościową (1.1.5) do kanonicznej relacji czasu (1.1.3), przyrost lokalnego czasu własnego $dt$ w stosunku do niezaburzonego czasu płaskiego tła $dt_{\text{flat}}$ (gdzie $\phi = \phi_0$) przyjmuje postać:

<span id="eq-r1e">$$\frac{dt}{dt_{\text{flat}}} = \frac{\phi_0}{\phi(\mathbf{x})} \approx \left(1 + \frac{|\Phi|}{c_{\perp}^2}\right)^{-1} \tag{1.1.6.1}$$</span>

Stosując rozwinięcie w szereg Taylora dla słabych pól ($\frac{|\Phi|}{c_{\perp}^2} \ll 1$), otrzymujemy:

<span id="eq-r1f">$$\frac{dt}{dt_{\text{flat}}} \approx 1 - \frac{|\Phi|}{c_{\perp}^2} \tag{1.1.6.2}$$</span>

Daje to poprawne empirycznie przybliżenie dylatacji grawitacyjnej, rygorystycznie zgodne co do znaku i rzędu wielkości z klasyczną formułą doświadczalną oraz danymi z systemów GPS i eksperymentu Pounda-Rebki. Wzrost gęstości osnowy jednoznacznie implikuje proporcjonalny spadek wartości $dt$.

## 1.2. Elastodynamika 4D osnowy i mikroskopowa geneza prędkości światła

Aby wyeliminować metodologiczny zarzut wprowadzenia bariery prędkości falowej $c$ jako założenia ad hoc, model TSM wyprowadza stałą prędkość światła (identyfikowaną jako prędkość poprzecznych fal ścinających $c_{\perp} \equiv c$) jako wielkość emergentną. Wyprowadzenie to realizowane jest dwuetapowo: poprzez rygorystyczny opis kontinuum elasto-dynamicznego, a następnie sprzężenie go z sub-planckowską kinetyką 0-cząstek.

### 1.2.1. Tensor odkształceń i równanie falowe w 4-Matrycy

Rozpatrzmy stan podstawowy Substratu przed sformowaniem brany. Jako 4-wymiarowy, izotropowy ośrodek sprężysty o gigantycznym zagęszczeniu kolizyjnym, 4-Matryca podlega uogólnionym równaniom Naviera-Cauchy’ego dla przemieszczeń $\mathbf{u}(x^1, x^2, x^3, x^4)$. Wprowadzamy 4-wymiarowy tensor odkształceń Cauchy’ego-Greena w postaci:

$$u_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x^j} + \frac{\partial u_j}{\partial x^i} + \frac{\partial u_k}{\partial x^i} \frac{\partial u_k}{\partial x^j} \right) \tag{1.2.1.1}$$

Gdzie indeksy $i, j, k \in \{1, 2, 3, 4\}$. Zakładając liniowy reżim sprężysty (w którym nieliniowe gradienty kwadratowe są pomijalne przed przekroczeniem progu blokady topologicznej), gęstość energii sprężystej $\mathcal{U}$ dana jest klasycznym wzorem Lamégo rozszerzonym do 4 wymiarów:

$$\mathcal{U} = \frac{1}{2} \lambda (u_{kk})^2 + \mu u_{ij} u_{ij} \tag{1.2.1.2}$$

Gdzie $\lambda$ oraz $\mu$ to makroskopowe współczynniki Lamégo charakteryzujące odpowiednio sprężystość objętościową (opór przeciw ściskaniu) oraz sprężystość postaciową (opór przeciw ścinaniu) Substratu. Równanie ruchu elementu objętości osnowy w czasie płaskiego tła $t_{\text{flat}}$ przyjmuje postać:

$$\rho_{\text{eff}} \frac{\partial^2 u_i}{\partial t_{\text{flat}}^2} = (\lambda + \mu) \frac{\partial u_k}{\partial x^i \partial x^k} + \mu \frac{\partial^2 u_i}{\partial x^k \partial x^k} \tag{1.2.1.3}$$

Gdzie $\rho_{\text{eff}}$ to efektywna makroskopowa gęstość falowa 4-Matrycy. Stosując rozkład Helmholtza na składową podłużną ($\nabla \cdot \mathbf{u}$) oraz poprzeczną ($\nabla \times \mathbf{u}$), wyodrębniamy prędkość propagacji fali poprzecznej (ścinającej):

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_{\text{eff}}}} \tag{1.2.1.4}$$

Ponieważ 3-brana jest zdefiniowana jako makroskopowe skręcenie uwięzione wzdłuż czwartego wymiaru ($x^4$), wszelkie interakcje elektromagnetyczne w naszym świecie są falami poprzecznymi tej struktury. Prędkość $c_{\perp}$ jest zatem tożsama z prędkością światła $c$ w próżni. Wektor falowy $\mathbf{k} = (k_1, 0, 0, k_4)$ prowadzi do relacji dyspersyjnej $\omega^2 = c_{\perp}^2 (k_1^2 + k_4^2)$. Maksymalna prędkość rzutu fali poprzecznej na obserwowalną przestrzeń 3D zachodzi dla $k_4 = 0$ i wynosi dokładnie $c_{\perp}$.

### 1.2.2. Dynamiczny opór relaksacyjny i sprzężenie skal prędkości

Równanie (1.2.1.4) opisuje zachowanie fali w makroskali, jednak moduł ścinania $\mu$ oraz efektywna bezwładność $\rho_{\text{eff}}$ nie są stałymi fundamentalnymi, lecz wyłaniają się z mikroskopowej kinetyki 0-cząstek. Kluczem do sprzężenia absolutnej prędkości sub-planckowskiej $v$ ze stałą makroskopową $c_{\perp}$ jest potężna dysproporcja skal geometrycznych.

Zdefiniujmy bezwymiarowy stosunek $\xi$ między stałą sieci osnowy $a$ (skala sub-Planckowska, $a < 1{,}6 \times 10^{-35}$ m) a długością fali mierzalnego zaburzenia makroskopowego $\lambda$:

$$\xi = \frac{a}{\lambda} \ll 1 \tag{1.2.2.1}$$

| Rodzaj promieniowania | Przykładowa $\lambda$ | Górne ograniczenie $\xi \leq l_P/\lambda$ |
| --- | --- | --- |
| Radiowa | $\sim 1$ m | $\lesssim 2 \times 10^{-35}$ |
| Widzialna | $\sim 5 \times 10^{-7}$ m | $\lesssim 3 \times 10^{-29}$ |
| Rentgenowska | $\sim 10^{-10}$ m | $\lesssim 2 \times 10^{-25}$ |

Niezależnie od pasma widma, parametr $\xi$ spełnia rygorystycznie $\xi \ll 1$. Pojedyncza komórka Wignera-Seitza o objętości $V_{4D} \sim a^4$ nie doświadcza makroskopowego ugięcia fali jako zjawiska kierunkowego w sposób natychmiastowy.

Zgodnie z Aksjomatem II, w stanie izotropowym (niezaburzonym) energia kinetyczna 0-cząstek, poruszających się z prędkością $v$, jest rozłożona równomiernie na 4 stopnie swobody przestrzennej. Z ekwipartycji pędu wynika, że moduł sprężystości postaciowej (ścinania) $\mu$ jest wprost proporcjonalny do pierwotnej gęstości statycznej tła $\rho_0$ oraz wariancji prędkości ortogonalnej do kierunku rozchodzenia się fali:

$$\mu = \rho_0 \langle v_{\perp}^2 \rangle = \rho_0 \frac{v^2}{4} \tag{1.2.2.2}$$

Gdy fala makroskopowa wymusza koherentne przemieszczenie, komórki 4D stawiają opór o charakterze bezwładności żyroskopowej. Ultra-szybkie oscylacje w 4 osiach działają jak stabilizator położenia. Front fali wymusza zmianę stanu tych oscylacji, co napotyka na opór wynikający z konieczności kaskadowej redystrybucji pędu. Powoduje to, że efektywna gęstość bezwładna $\rho_{\text{eff}}$, jaką „widzi” fala, jest zwielokrotniona względem gęstości statycznej tła $\rho_0$.

Definiujemy makroskopowy parametr dynamicznego tłumienia geometrycznego $\Gamma_{4D}$:

$$\Gamma_{4D} \equiv \frac{v}{2c_{\perp}} \tag{1.2.2.3}$$

Określa on, że efektywna masa bezwładna w równaniu falowym rośnie z kwadratem tego uwięzionego, żyroskopowego oporu tła:

$$\rho_{\text{eff}} = \rho_0 \cdot \Gamma_{4D}^2 \tag{1.2.2.4}$$

**Weryfikacja spójności kinetyki z continuum.**
Aby sprawdzić, czy kinetyczne postulaty stanu podstawowego są zgodne z makroskopowym równaniem falowym wyznaczonym w (1.2.1.4), podstawiamy relacje (1.2.2.2) i (1.2.2.4) do wzoru na $c_{\perp}$:

$$c_{\perp} = \sqrt{\frac{\mu}{\rho_{\text{eff}}}} = \sqrt{\frac{\rho_0 \frac{v^2}{4}}{\rho_0 \Gamma_{4D}^2}} = \sqrt{\frac{v^2}{4 \Gamma_{4D}^2}} = \frac{v}{2\Gamma_{4D}} \tag{1.2.2.5}$$

Podstawiając definicję $\Gamma_{4D}$ ze wzoru (1.2.2.3), uzyskujemy:

$$c_{\perp} = \frac{v}{2 \left( \frac{v}{2c_{\perp}} \right)} = c_{\perp} \tag{1.2.2.6}$$

Tożsamość zostaje spełniona w sposób absolutnie ścisły i matematycznie zamknięty. Prędkość fali na 3-branie staje się bezwzględnie zablokowana przez stosunek $v/\Gamma_{4D}$. Zgodnie z aksjomatem dynamiki sub-planckowskiej sformułowanym w Rozdziale 0, pierwotne oscylacje zachodzą z prędkością $v \gg c_{\perp}$. Podstawienie tej relacji do definicji (1.2.2.3) dowodzi jednoznacznie:

$$v \gg c_{\perp} \implies \Gamma_{4D} \gg 1 \tag{1.2.2.7}$$

Wniosek jest rygorystyczny: w czasie, gdy front fali makroskopowej przemieszcza się o jeden sub-planckowski skok $a$, pierwotne 0-cząstki wykonują $\Gamma_{4D}$ cykli zderzeniowych (drgań). Ośrodek stawia tak gigantyczny żyroskopowy opór bezwładny, że prędkość propagacji zaburzeń (światła) zwalnia do wielkości minimalnej w stosunku do pierwotnej dynamiki substratu.

### 1.2.3. Zachowawczy charakter propagacji falowej i brak dyssypacji energii

Zdefiniowanie potężnego oporu żyroskopowego rodzi zasadnicze pytanie: w jaki sposób w medium zdominowanym przez procesy kaskadowych kolizji stabilność energetyczna fali nie ulega natychmiastowej dyssypacji na ciepło? W skali kosmologicznej prowadziłoby to do niefizycznego wygasania fotonów. Model TSM eliminuje dyssypację poprzez dwa warunki ontologiczne:

1. **Brak sub-poziomu strukturalnego:** Zderzenia 0-cząstek są twarde, niepodzielne i bezwzględnie sprężyste (współczynnik restytucji wynosi 1). Ponieważ nie istnieje "wnętrze" 0-cząstki, energia nie ma jak ulec termalizacji do niższych wymiarów czy wewnętrznego tarcia. Chaos termiczny substratu ($T_{\text{sub}}$) jest stacjonarnym stanem bazowym tła.
2. **Czysto reaktywny charakter impedancji sieci:** Komórki sieciowe działają jak geometryczny akumulator energii. Na przednim zboczu fali pochłaniają pęd makroskopowy, co manifestuje się chwilowym, sprężystym zaburzeniem oscylacji 4D. Na tylnym zboczu fali komórka powraca do stanu izotropowego, w pełni i bezstratnie oddając 100% zmagazynowanej energii.

Całkowity bilans energetyczny transferu pędu w jednym pełnym cyklu falowym dla dowolnej komórki sieci wynosi dokładnie zero:

$$\Delta E_{\text{net}} = \int_{\text{front}}^{\text{tył}} \frac{\partial E_{\text{int}}}{\partial t} dt = 0 \tag{1.2.3.1}$$

Dlatego też redshift (przesunięcie ku czerwieni) obserwowany w kosmologii nie jest efektem tarcia fotonu o osnowę, lecz wynika ze zmiennej, uśrednionej gęstości substratu pomiędzy obszarem emisji a obszarem detekcji, zgodnie z definicją emergentnego czasu relatywistycznego.

### 1.2.4 Status fali podłużnej: Superluminalne fale gęstości 4D i fluktuacje czasu

Rozkład Helmholtza pola przemieszczeń w 4-Matrycy ujawnia istnienie drugiego, niezależnego modu falowego – fali podłużnej (dylatacyjnej), której prędkość propagacji wynosi:

$$c_{\parallel} = \sqrt{\frac{\lambda + 2\mu}{\rho_{\text{eff}}}} \tag{1.2.4.1}$$

Zgodnie z wyprowadzeniem z Podrozdziału 0.2, komórki kinetyczne 0-Matrycy stawiają potężny, asymptotyczny opór przeciwko ściskaniu objętościowemu, podczas gdy opór ścinania (rotacji) pozostaje skończony i mniejszy. W języku makroskopowych modułów sprężystości oznacza to rygorystyczną nierówność $\lambda \gg \mu$. Konsekwencją tego mechanizmu jest fakt, że prędkość fali podłużnej o wiele rzędów wielkości przekracza prędkość fal poprzecznych (światła):

$$c_{\parallel} \gg c_{\perp} \tag{1.2.4.2}$$

Istnienie superluminalnych zaburzeń nie narusza kinematyki relatywistycznej. W modelu TSM cała obserwowalna materia i oddziaływania elektromagnetyczne wynikają z uwięzienia węzłów topologicznych w defekcie 3-brany, a ich mechanika opiera się na transferze pędu ścinającego ($c_{\perp}$). Fala podłużna jest natomiast czysto objętościową falą ciśnienia rozchodzącą się swobodnie w pełnej przestrzeni Bulk 4D.

Fizyczna manifestacja fali podłużnej uwięzionej na 3-branie ma fundamentalne znaczenie. Ponieważ fala ta polega na sferycznym zagęszczaniu i rozrzedzaniu układu komórek, powoduje ona chwilowe, przestrzenne oscylacje ułamka upakowania osnowy ($\phi$). Zgodnie z równaniem kanonicznym czasu (Rozdział 1.1), lokalna zmiana gęstości $\phi$ wprost determinuje tempo procesów fizycznych. Fale podłużne rozchodzące się w 0-Matrycy to zatem w istocie sub-planckowskie **fale dylatacji czasu**.

Z punktu widzenia makroskopowych detektorów materii (opartych na polach EM, czyli naprężeniach ścinających), fale te są niewidoczne jako klasyczne promieniowanie. Generują one jednak nieustanne, sub-planckowskie fluktuacje tempa upływu lokalnego czasu w całej przestrzeni 3-brany, co w fizyce eksperymentalnej obserwowane jest jako tło szumu kwantowego (energia próżni) i może stanowić mechanistyczne podłoże dla zjawiska nielokalnego splątania kwantowego.

## 1.3. Ośrodek i przestrzeń: Globalne zakleszczenie i izotropowa 3‑brana

Mając zdefiniowany czas lokalny, możemy formalnie opisać strukturę przestrzenną. Zgodnie z opisem strukturalnym, fundamentalna przestrzeń $\mathcal{M}^4$ jest 4‑wymiarową, skończoną bańką wypełnioną 0‑cząstkami w stanie globalnego zakleszczenia (jamming).

### 1.3.1. Stan globalnego zakleszczenia

W całej objętości $\mathcal{M}^4$ ułamek upakowania przekracza wartość krytyczną:

<span id="eq-r1l">$$\phi \ge \phi_c \quad \text{(globalnie w 4D)} \tag{1.3.1.1}$$</span>

0‑cząstki są trwale uwięzione w komórkach Wignera‑Seitza i nie mają swobody translacyjnej. Ośrodek posiada pełny tensor sztywności i może przenosić fale poprzeczne we wszystkich czterech wymiarach. W absolutnym Stanie Zero, przed Wielkim Wydarzeniem, makroskopowe naprężenie ścinające wynosi $\sigma_{ab} = 0$, a jedyną dynamikę stanowi niekoherentny szum termiczny $T_{\text{sub}}$.

### 1.3.2. Izotropowa 3‑brana jako defekt topologiczny

Wielkie Wydarzenie – pierwotne zaburzenie spoza zakresu TSM – spowodowało lokalne plastyczne skręcenie osnowy. Powstały trwały defekt topologiczny to właśnie nasza 3‑brana – trójwymiarowa hiperpowierzchnia o wymiarze $D-1 = 3$. Z powodu statystycznego uśredniania kierunków na poziomie makroskopowym, 3‑brana zachowuje się jak idealnie ciągły, izotropowy, nieliniowy ośrodek sprężysty, zdolny do propagacji fal poprzecznych z prędkością $c_{\perp}$ (światło).

Obszar 4D poza 3‑braną pozostaje sztywnym, niezakłóconym szkłem topologicznym. Ponieważ jest idealnie sprężysty i w równowadze, nie generuje żadnych dodatkowych sił działających na branę.

## 1.4. Kinematyka nieliniowa: Emergencja metryki $g_{ab}$ z odkształcenia

W TSM metryka przestrzenna $g_{ab}$ nie jest bytem pierwotnym abstrakcyjnej geometrii; jest ona fizycznym **rzutem** stanu odkształcenia Substratu. W płaskiej, niezakłóconej 3‑brane (daleko od węzłów) ośrodek opisuje płaska metryka euklidesowa $\delta_{ab}$.

Wprowadzamy fizyczne wektorowe pole przemieszczenia osnowy $u^a(\mathbf{x})$, opisujące odkształcenie elementu objętości od położenia równowagi. Metryka obserwowalna (Riemanna) wyłania się rygorystycznie z nieliniowych gradientów przemieszczenia:

<span id="eq-r1m">$$g_{ab} = \delta_{ab} + \nabla_a \phi_b + \nabla_b \phi_a + \delta_{cd} \nabla_a \phi^c \nabla_b \phi^d \tag{1.4.1}$$</span>

gdzie: 
- $g_{ab}$ – tensor metryczny (obserwowalna geometria przestrzeni), 
- $\delta_{ab}$ – płaska metryka euklidesowa (niezakłócona osnowa),
- $u^a$ – wektor przemieszczenia osnowy $[\text{m}]$,
- $\nabla_a$ – pochodna kowariantna w metryce tła $\delta_{ab}$.

Zakrzywienie przestrzeni i wynikająca z niego grawitacja to mechaniczne naciągnięcie lokalnych komórek 0‑cząstek, tworzące makroskopowy gradient gęstości upakowania $\phi$ w stronę czwartego wymiaru przestrzennego.

## 1.5. Dynamika falowa Substratu i równania pola

Mechanika Substratu podlega uogólnionemu formalizmowi Lagrange’a. Gęstość lagrangianu $\mathcal{L}$ izotropowej 3‑brany zdefiniowana jest przez jej całkowitą energię sprężystą, wykorzystując tensor modułów sprężystości $K^{abcd}$:

<span id="eq-r1n">$$\mathcal{L} = \frac{1}{2} K^{abcd} \epsilon_{ab} \epsilon_{cd} + \mathcal{O}(\epsilon^3) \tag{1.5.1}$$</span>

gdzie:
- $\mathcal{L}$ – gęstość lagrangianu $[\text{J} \cdot \text{m}^{-3}]$,
- $K^{abcd}$ – tensor modułów sprężystości $[\text{Pa}]$,
- $\epsilon_{ab}$ – tensor odkształcenia (bezwymiarowy), $\epsilon_{ab} = \frac{1}{2}(\nabla_a \phi_b + \nabla_b \phi_a)$.

Pochodna lagrangianu względem tensora odkształcenia jednoznacznie określa tensor naprężenia:

<span id="eq-r1o">$$\sigma^{ab} = \frac{\partial \mathcal{L}}{\partial \epsilon_{ab}} = K^{abcd} \epsilon_{cd} \tag{1.5.2}$$</span>

Drobne odkształcenia pola w 3‑brane spełniają równanie falowe w globalnym czasie odniesienia $t_{\text{flat}}$:

$$\nabla^2 \phi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \phi}{\partial t_{\text{flat}}^2} = \mathcal{S}(\mathbf{x}, t_{\text{flat}}) \tag{1.5.3}$$

gdzie:
- $\nabla^2$ – laplasjan w metryce tła $\delta_{ab}$,
- $c_{\perp}$ – prędkość propagacji poprzecznych fal ścinających (bazowa prędkość światła) $[\text{m} \cdot \text{s}^{-1}]$,
- $\mathcal{S}(\mathbf{x}, t_{\text{flat}})$ – funkcja źródła, reprezentująca obecność trwałych odkształceń topologicznych (węzłów).

Krzywizna geometryczna $g_{ab}$ jest bezpośrednim odzwierciedleniem tensora naprężenia tła, sprzężonym przez elastyczne stałe materiałowe Substratu.

## 1.6. Podwójny reżim elasto‑dynamiki: Fale sprężyste a nieliniowa blokada topologiczna

Wprowadzenie mechanizmu natychmiastowej relaksacji naprężeń poprzez geometryczne sfery odpychania kinetycznego generuje fundamentalny problem dynamiczny: w jaki sposób w idealnie sprężystym ośrodku, który z definicji błyskawicznie rozprasza wszelkie nadmiary ciśnienia, może uformować się i utrzymać stabilna, trwała struktura materialna (cząstka)? Rozwiązanie tego pozornego paradoksu wymaga rygorystycznego rozdzielenia dynamiki Substratu na dwa komplementarne reżimy, rozgraniczone krytycznym progiem ułamka upakowania $\phi_{\text{lock}}$ (progiem zamrożenia topologicznego).

### 1.6.1. Reżim I: Liniowa relaksacja akustyczna ($\phi < \phi_{\text{lock}}$)

Dopóki lokalna kompresja sieci nie przekracza krytycznego progu stabilności geometrycznej klatek Wignera‑Seitza, Substrat zachowuje się jak idealne, liniowe continuum sprężyste. W tym stanie:

- Odkształcenia są zachowawcze. Sfery odpychania kinetycznego ulegają deformacji, ale 0‑cząstki rygorystycznie zachowują macierz swoich dotychczasowych sąsiadów. Nie dochodzi do zmiany lokalnej topologii sieci.
- Nadmiar efektywnego ciśnienia $P_{\text{eff}}$ jest transferowany symetrycznie na zewnątrz na zasadzie kaskady brzegowej. Ośrodek relaksuje energię poprzez propagację fal poprzecznych z prędkością $c_{\perp}$ oraz fal podłużnych. Rozpraszanie zjawisk zaburzających jest natychmiastowe i całkowite.

### 1.6.2. Reżim II: Nieliniowa blokada topologiczna ($\phi \ge \phi_{\text{lock}}$)

Sytuacja zmienia się drastycznie, gdy na skutek ekstremalnej koncentracji energii układ zostaje skompresowany poza granicę plastyczności $\phi_{\text{lock}}$.

- Klatki kinetyczne zostają zniekształcone geometrycznie. Zgodnie z aksjomatem absolutnego uwięzienia, 0‑cząstki nie przemieszczają się fizycznie do sąsiednich komórek – drastycznej deformacji ulega geometryczny kształt samych klatek Wignera-Seitza.
- Nieliniowe skrócenie osi komórek powoduje trwałą rotację głównych kierunków naprężeń sprężystych. Wektory wewnętrznych sił kontaktowych krzyżują się pod niestandardowymi kątami wewnątrz silnie ściśniętego obszaru. Zamiast przekazywać pęd na zewnątrz w sposób symetryczny, linie naprężeń zamykają się, uniemożliwiając prostą, liniową relaksację fali.
- Następuje kinetyczne ograniczenie swobody sfer oddziaływań w formie splotu: pola naprężeń zapętlają się w samopodtrzymujący się, rotacyjny splot (wir solitonowy). Każda próba powrotu struktury do liniowego stanu geometrycznego jest blokowana przez napływające przesunięcie fazowe sąsiednich komórek uwięzionych w tej samej lokalnej anomalii.

W tym reżimie Substrat traci zdolność do uwalniania naprężeń przestrzennych poprzez zwykłą emisję akustyczną. Powstaje nieliniowy splot (soliton), który zyskuje stabilność, ponieważ rozplecenie tego węzła wymagałoby ponownego przejścia układu przez stan ekstremalnej kompresji, co stwarza potężną barierę energetyczną. Ośrodek doskonale propaguje fale sprężyste w swojej liniowej granicy, ale trwale więzi energię poprzez deformację geometryczną komórek i sprzężenie kierunków naprężeń w granicy topologicznej, dając początek skwantowanej materii.

## 1.7. Aksjomat materii: Skwantowane węzły topologiczne i rygorystyczne rozdzielenie masy od ładunku

Pod wpływem ekstremalnej kompresji nieliniowej ($\phi(\mathbf{x}) \ge \phi_{\text{lock}}$), liniowe fluktuacje tracą zdolność relaksacji falowej. Komórki sieci zmuszone są do geometrycznego zapętlenia. W 4‑wymiarowym kontinuum formują one stabilne fale stojące (solitony), będące w istocie trwałymi węzłami topologicznymi, które fizyka makroskopowa identyfikuje jako fermiony. Węzły te są tworami w pełni 4‑wymiarowymi – ich struktura rozciąga się również w czwarty wymiar, co ma fundamentalne znaczenie dla grawitacji i oddziaływań jądrowych.

### 1.7.1. Matematyczna geneza kwantowania materii

Skwantowany charakter cząstek elementarnych nie jest w TSM założeniem dodanym ad hoc, lecz ścisłym wymogiem aparatury topologii algebraicznej. Stan odkształcenia (skręcenia) klatek kinetycznych opisujemy wektorowym polem orientacji osnowy $\mathbf{n}(\mathbf{x})$ (gdzie $|\mathbf{n}| = 1$). Aby węzeł utrzymywał stabilność, pole $\mathbf{n}$ z dala od rdzenia splotu musi płynnie asymptotycznie dążyć do niezaburzonego, jednorodnego stanu tła. To ograniczenie brzegowe wymusza zamknięcie przestrzeni parametrów na sfery.

Rygorystyczne twierdzenia topologiczne dowodzą, że całka z gęstości takiego przestrzennego skręcenia może przyjmować wyłącznie wartości całkowite. Zjawisko to definiuje niezmienną liczbę splotu (ładunek topologiczny) $\mathcal{W} \in \mathbb{Z}$. Węzeł, który posiada ładunek $\mathcal{W} = 1$, nie może płynnie wypromieniować ułamka swojego splotu, ponieważ wymagałoby to globalnego, makroskopowego rozdarcia ciągłości krystalicznej sieci osnowy. Próg $\phi_{\text{lock}}$ działa jako mechanizm zapłonowy uwięzienia, ale to twarde reguły geometrii sfery wymuszają niepodzielną kwantyzację uformowanego solitonowego defektu.

Dzięki temu fundamentowi, TSM rygorystycznie oddziela pojęcie masy od ładunku:

- **Ładunek elektryczny (Rzut 3D):** Jest bezpośrednio mierzonym strumieniem wektora skrętu fazowego węzła zrzutowanym na płaszczyznę naszej 3‑brany. Ponieważ zamknięty skręt zawsze musi domknąć się do pełnego obrotu fazowego (stanowiąc wielokrotność geometryczną $2\pi$), ładunek ulega absolutnemu skwantowaniu do wartości $\pm 1e$, niezależnie od wewnętrznego skomplikowania węzła w wyższym wymiarze.
- **Masa spoczynkowa (Zanurzenie 4D):** Zdefiniowana jest jako makroskopowy ekwiwalent energii sprężystej zmagazynowanej w napiętej strukturze węzła. Odpowiada ona bezpośrednio głębokości, z jaką uformowany splot wybrzusza ortogonalnie 3‑branę w czwarty wymiar przestrzenny. Wyjaśnia to ostatecznie asymetrię mas: złożony, wielokrotny warkocz topologiczny (proton) wymusza znacznie głębszą deformację 4D i generuje nieporównywalnie silniejszy gradient naprężeń tła niż prosty splot (elektron), mimo posiadania identycznego rzutu ładunku $\pm 1e$.

### 1.7.2. Ruch płynny i asymptotyczne wygaszenie barier dyskretnych

Propagacja materii w przestrzeni nie polega na przepychaniu 0‑cząstek przez ośrodek, lecz na bezstratnym, falowym transferze samego stanu topologicznego splątania przez kolejne sfery oddziaływania.

Rozmiar przestrzenny rdzenia węzła ($L$) drastycznie przewyższa mikroskopowy rozmiar pojedynczej komórki Wignera‑Seitza ($a$). Ta fundamentalna asymetria skal powoduje, że okresowy potencjał oporu sieci krystalicznej ulega uśrednieniu przestrzennemu. Prowadzi to do wykładniczego wygaszenia dyskretnej bariery energetycznej Peierlsa‑Nabarro, określającej minimalną siłę potrzebną do przesunięcia defektu w ciele stałym:

<span id="eq-r1aa">$$E_{PN} \propto \exp\left(-\pi \frac{L}{a}\right) \approx 0 \tag{1.6.1} \qquad(16)$$</span>

W rezultacie, tak sformowany węzeł topologiczny ślizga się wewnątrz Substratu w sposób idealnie płynny, bez rozpraszania energii, co rygorystycznie i bezsiłowo realizuje Pierwszą Zasadę Dynamiki Newtona. Wypromieniowanie energii w postaci fal poprzecznych (fotonów) następuje wyłącznie przy odkształceniach węzła wynikających ze zderzeń lub gwałtownego przyspieszenia.

## 1.8. Wyprowadzenie kinematyki relatywistycznej z hydro‑elastyczności 0-Matrycy (substratu)

Transformacje Lorentza i zasada $E = mc^2$ są rygorystyczną konsekwencją oporu hydrodynamicznego podczas ruchu fal stojących (węzłów) w gęstym kontinuum. W TSM cała kinematyka relatywistyczna wynika z mechaniki ośrodka i lokalnej natury czasu.

### 1.8.1. Konstrukcja prędkości i kontrakcja długości

Ruch węzła topologicznego w osnowie musi być opisywany w odniesieniu do geometrycznego tła spoczywającej 0-Matrycy. Definiujemy dwie komplementarne reprezentacje prędkości makroskopowej:

1.  **Prędkość współrzędnościowa tła ($v$):** Mierzona względem lokalnie płaskiej, niezaburzonej osnowy przy użyciu globalnego czasu odniesienia $dt_{\text{flat}}$: $$v = \frac{dx}{dt_{\text{flat}}} \tag{1.7.1a}$$

2.  **Prędkość własna węzła ($\eta$):** Mierzona przez obserwatora poruszającego się wraz z węzłem, określająca przyrost odległości w przestrzeni tła na jednostkę lokalnego czasu własnego $dt$: $$\eta = \frac{dx}{dt} \tag{1.7.1b}$$

Ponieważ kanoniczne równanie czasu rygorystycznie wiąże oba przyrosty czasowe relacją $dt = dt_{\text{flat}} / \gamma$, zachodzi bezpośredni związek transformacyjny: <span id="eq-r1ab">$$\eta = \frac{dx}{\frac{dt_{\text{flat}}}{\gamma}} = \gamma \cdot v = \frac{v}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} \tag{1.7.1c} \qquad(17)$$</span>

Gdy prędkość współrzędnościowa obiektu dąży do granicznej prędkości fal poprzecznych ($v \to c_{\perp}$), czynnik Lorentza $\gamma \to \infty$, co powoduje, że prędkość własna $\eta \to \infty$. Rozróżnienie to eliminuje paradoks nieskończonej prędkości kinematycznej i zachowuje $c_{\perp}$ jako nieprzekraczalną barierę dla fizycznego ruchu falowego na płaszczyźnie 3-brany.

Rozważmy teraz węzeł poruszający się wzdłuż osi $x$ z prędkością współrzędnościową $v$. Ruch ten generuje przed obiektem front kompresji – efektywna gęstość wewnątrz węzła rośnie zgodnie z (1.1.7). Wprowadzając współrzędną uciekającą $u = x - vt_{\text{flat}}$, przekształcenie jednorodnego równania falowego (1.4.3) wymaga przeskalowania osi przestrzennej w celu zachowania niezmienniczości formy solitonu: <span id="eq-r1ac">$$x' = \frac{u}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} = \gamma (x - vt_{\text{flat}}) \tag{1.7.1d} \qquad(18)$$</span>

Kształt węzła ulega mechanicznej kompresji o czynnik geometryczny $\gamma$ pod wpływem jednostronnego oporu elastycznego kontinuum wzdłuż wektora pędu. Długość mierzona w kierunku ruchu ulega skróceniu: $L' = L / \gamma$.

### 1.8.2. Energia, pęd i masa relatywistyczna

Energia całkowita węzła poruszającego się z prędkością współrzędnościową $v$ składa się z energii spoczynkowej (sprężernej deformacji 4D) oraz energii kinetycznej (odpowiedzi osnowy na ruch). Całkowita energia odkształcenia osnowy w obecności poruszającego się węzła wynosi:

<span id="eq-r1ad">$$E = \gamma E_0 = \frac{E_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} \tag{1.8.2.1}$$</span>

gdzie $E_0 = m_0 c_{\perp}^2$ to energia spoczynkowa węzła w układzie własnym, a $m_0$ to masa spoczynkowa (energia sprężysta splotu w 4D).

Masa relatywistyczna – jako miara całkowitej energii – wynosi:

<span id="eq-r1ae">$$m = \gamma m_0 = \frac{m_0}{\sqrt{1 - \frac{v^2}{c_{\perp}^2}}} \tag{1.8.2.2}$$</span>

Pęd węzła definiujemy jako strumień energii sprężystej w kierunku ruchu, powiązany z przyrostem lokalnego czasu własnego:

<span id="eq-r1af">$$p = m_0 \frac{dx}{dt} = m_0 \eta = \gamma m_0 v \tag{1.8.2.3}$$</span>

Równanie siły działającej na węzeł wewnątrz osnowy – po uwzględnieniu lokalnego czynnika dylatacji czasu ($dt = dt_{\text{flat}}/\gamma$) – ujawnia zjawisko asymptotycznego oporu falowego przy próbie zmiany stanu pędu:

<span id="eq-r1ag">$$F = \frac{dp}{dt_{\text{flat}}} = m_0 \gamma^3 \frac{d^2 x}{dt_{\text{flat}}^2} \tag{1.7.5} \qquad(22)$$</span>

Gdy prędkość współrzędnościowa węzła zbliża się do prędkości fal ścinających ($v \to c_{\perp}$), czynnik $\gamma \to \infty$. Opór falowy osnowy staje się nieskończony, co uniemożliwia solitonowi przekroczenie progu $c_{\perp}$ na płaszczyźnie 3‑brany.

### 1.8.3. Związek energii i pędu – relacja dyspersyjna

Z równań (1.8.2.1) i (1.8.2.3) natychmiast wynika relatywistyczna relacja dyspersyjna:

<span id="eq-r1ah">$$E^2 = (pc_{\perp})^2 + (m_0 c_{\perp}^2)^2 \tag{1.8.3.1}$$</span>

Dla fotonu – fali poprzecznej bez masy spoczynkowej ($m_0 = 0$) – energia i pęd są związane przez $E = pc_{\perp}$, co jest zgodne z klasyczną elektrodynamiką i mechaniką kwantową.

## 1.9. Zmienna propagacja fal (lokalne $c_{\perp}$) i stałe materiałowe

Prędkość światła nie jest stałą uniwersalną; wynika bezpośrednio z nieliniowego zjawiska akustoelastyczności gęstego kontinuum. W obszarze poddanym napięciu mechanicznemu ($\Sigma$), lokalna prędkość fal poprzecznych $c_{\perp,\text{lok}}$ modulowana jest przez sztywność nieliniową (stałe Murnaghana $\mathcal{A}$):

<span id="eq-r1i">$$c_{\perp,\text{lok}}^2 = \frac{\mu}{\rho_0} \left( 1 + \mathcal{A} \Sigma \right) \tag{1.9.1}$$</span>

gdzie:
- $\mu$ – moduł sztywności postaciowej osnowy $[\text{Pa}]$,
- $\rho_0$ – gęstość masy (bezwładnej) 0‑cząstek $[\text{kg} \cdot \text{m}^{-3}]$,
- $\mathcal{A}$ – stała nieliniowości Murnaghana $[\text{Pa}^{-1}]$,
- $\Sigma$ – ślad tensora naprężenia $[\text{Pa}]$.

W zapisie elektrodynamicznym przekłada się to bezpośrednio na efektywną przepustowość Substratu:

<span id="eq-r1j">$$c_{\perp,\text{lok}} = \frac{1}{\sqrt{\epsilon_{\text{eff}} \mu_0}} \tag{1.9.2}$$</span>

Parametr $\epsilon_{\text{eff}}$ zależy od lokalnych gradientów naprężeń wywołanych polami magnetycznymi lub grawitacyjnym ugięciem w kierunku czwartego wymiaru:

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \kappa B^2 + \lambda \frac{\Phi}{c_{\perp}^2} + \dots\right) \tag{1.9.3}$$

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

## 1.10. Podsumowanie Rozdziału

- **Czas jako funkcja gęstości osnowy:** Czas absolutny zostaje całkowicie odrzucony. Lokalny czas własny $t$ jest definiowany przez liczbę cykli procesów okresowych, spowalnianych przez uśrednioną makroskopowo gęstość upakowania $\phi$: $dt = dN \cdot T_0 \cdot \phi_0/\langle\phi\rangle_{\text{macro}}$. Dylatacja grawitacyjna i kinematyczna wynikają bezpośrednio ze zmian gęstości – wzrost lokalnego upakowania $\phi$ rygorystycznie minimalizuje przyrost $dt$, powodując spowolnienie procesów fizycznych. Zależność grawitacyjna została skorygowana liniowo ($dt/dt_{\text{flat}} \approx 1 - |\Phi|/c^2$), co zapewnia idealną zgodność z fizyką eksperymentalną.
- **Globalne zakleszczenie:** Cała 4‑wymiarowa bańka od początku znajduje się w stanie sztywnego szkła topologicznego. 3‑brana jest trwałym defektem – skręceniem hiperpowierzchni powstałym podczas Wielkiego Wydarzenia.
- **Podwójny reżim dynamiczny:** Rozwiązano paradoks natychmiastowej relaksacji Substratu poprzez wprowadzenie progu zamrożenia topologicznego $\phi_{\text{lock}}$. Poniżej tego progu kontinuum zachowuje się liniowo. Powyżej ($\phi \ge \phi_{\text{lock}}$) dochodzi do nieliniowej blokady geometrycznej i rotacji głównych kierunków naprężeń, formując trwałe węzły – 4‑wymiarowe solitony.
- **Rozwiązanie pułapki czasu własnego:** Wprowadzono rygorystyczne rozróżnienie na prędkość współrzędnościową tła ($v = dx/dt_{\text{flat}}$) podlegającą barierze $c_{\perp}$ oraz relatywistyczną prędkość własną węzła ($\eta = dx/dt = \gamma v$), która może dążyć do nieskończoności.
- **Rygorystyczna kwantyzacja i relatywizm falowy:** Stabilność i skwantowanie fermionów wyprowadzono z niezmienników topologicznych ($\mathcal{W} \in \mathbb{Z}$). Kinematyka relatywistyczna (kontrakcja Lorentza, $E = \gamma m_0 c_{\perp}^2$, bariera $c_{\perp}$) jest bezpośrednią konsekwencją oporu hydrodynamicznego osnowy przy odwrotnej zależności przyrostu czasu własnego ($dt \propto 1/\gamma$).
- **Materializacja stałych fizycznych:** Prędkość światła to prędkość poprzecznych fal ścinających ($c_{\perp}$), zależna od lokalnych naprężeń. Fundamentalne stałe ($c, e, G, \epsilon_0$) zyskują status parametrów materiałowych 4‑wymiarowego medium sprężystego.
