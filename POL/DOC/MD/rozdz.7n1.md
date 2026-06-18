

# Rozdział 7: Oddziaływania subatomowe – hadrony jako pęcherzyki kawitacyjne, oddziaływanie słabe jako rozwęźlanie, hierarchia leptonów i determinizm kwantowy w TSM

W modelu Mechaniki Substratu Topologicznego (TSM) zjawiska subatomowe nie są opisane przez abstrakcyjne zbiory probabilistyczne i punktowe, bezwymiarowe cząstki zawieszone w próżni. Dynamika cząstek elementarnych to w istocie mechanika nieliniowych odkształceń, węzłów topologicznych oraz rezonansów falowych propagujących się w 4-wymiarowym, sprężystym kontinuum – 0-Matrycy. Niniejszy rozdział redefiniuje kluczowe zjawiska fizyki wysokich energii, sprowadzając je do rygorystycznych procesów z zakresu mechaniki ośrodków ciągłych, spójnych z czasem lokalnym $t$ (Rozdział 1.1) i topologicczną naturą materii (Rozdział 2).

## 7.1. Czas lokalny i formalizm elasto-dynamiczny Substratu

Wszystkie procesy opisywane w tym rozdziale – oscylacje kwarków, rozpady słabe, rezonanse i hierarchie masowe – zachodzą w lokalnym czasie własnym $t$, który wyłania się bezpośrednio z uśrednionej gęstości upakowania 0-Matrycy:

$$dt = dN \cdot T_0 \cdot \frac{\langle\phi\rangle_{\text{macro}}}{\phi_0} \tag{7.1.1}$$

Mikroskopowy stan przed-zakleszczeniowy (pre-jamming) i skończona sztywność objętościowa sieci Wignera-Seitza w 4D pozwalają na zdefiniowanie fundamentalnych pól opisujących stan deformacji osnowy. Stan ten reprezentowany jest przez znormalizowane pole wektorowe $\mathbf{n}(\mathbf{x})$ na trójwymiarowej brane oraz skalarną funkcję ugięcia ortogonalnego $\phi(\mathbf{x})$:

$$\mathbf{n}(\mathbf{x}) \in \mathbb{S}^2, \quad |\mathbf{n}| = 1 \tag{7.1.2}$$

$$\phi(\mathbf{x}) = \frac{\partial \mathbf{n}}{\partial x^4} \tag{7.1.3}$$

Gdzie $\phi(\mathbf{x})$ reprezentuje ugięcie (deformację) kontinuum wzdłuż dodatkowego, czwartego wymiaru przestrzennego $x^4$. Opór mechaniczny, jaki 0-Matryca stawia lokalnemu odkształceniu, określa Uniwersalna Stała Sztywności Substratu ($\mathcal{K}$), definiowana za pomocą jednostek Plancka:

$$\mathcal{K} = \frac{c^4}{G} \tag{7.1.4}$$

Wymiarowo stała $\mathcal{K}$ odpowiada sile Plancka (lub zintegrowanemu ciśnieniu Plancka $P_P$ na powierzchni kwadratu długości Plancka $l_P^2$). Kąt Weinberga $\theta_W$ oraz stała sprzężenia słabego $g$ stanowią makroskopowe parametry materiałowe tej osnowy, bezpośrednio wynikające ze sztywności $\mathcal{K}$.

Winside pęcherzyków kawitacyjnych oraz w pobliżu silnie skompresowanych rdzeni leptonowych efektywna gęstość $\langle\phi\rangle_{\text{macro}}$ drastycznie odbiega od wartości referencyjnej $\phi_0$. Oznacza to, że lokalne tempo upływu czasu (tempo relaksacji i cykli $dN$) jest przestrzennie niejednorodne. W zrelaksowanym wnętrzu hadronu czas płynie relatywnie szybciej niż na jego nieliniowej, silnie naprężonej ścianie granicznej lub w gęstym, wielokrotnie skręconym rdzeniu mionu.

## 7.2. Ontologia oddziaływania silnego i stabilność stanu podstawowego $\mathcal{W}=1$

Zgodnie z Rozdziałem 3.5, oddziaływanie silne (jądrowe) nie jest nową siłą fundamentalną, lecz bezpośrednim efektem topologicznego splątania węzłów w czwartym wymiarze przestrzennym ($x^4$). Gdy dwa hadrony (nukleony) zbliżają się do siebie na odległość rzędu femtometra ($\sim 1\text{ fm}$), ich części zanurzone w czwartym wymiarze ulegają mechanicznemu zazębieniu.

Linie naprężeń jednego węzła przeplatają się z liniami drugiego w wyższym wymiarze Bulk. Splątanie to generuje potężny, krótkozasięgowy poprzeczny naciąg 3-brany, który fizyka makroskopowa interpretuje jako przyciąganie jądrowe. Zjawisko to cechuje się:

1. **Wysyceniem:** Jeden węzeł w 4D może splątać się z ograniczoną geometrycznie liczbą sąsiadów ze względu na limit koordynacyjny sieci.
2. **Niezależnością ładunkową:** Splątanie zależy od pełnej struktury 4D, a nie od jej trójwymiarowego rzutu fazowego (ładunku elektrycznego).
3. **Uwięzieniem (confinement) i swobodą asymptotyczną:** Rozpatrywanymi z perspektywy wewnętrznej mechaniki pojedynczego pęcherzyka.

Tradycyjne ujęcie funkcjonalu energii solitonu oparte na modelach gradientowych sugerowało, że minimalny ładunek topologiczny zapewniający stabilność statyczną to $\mathcal{W} \ge 3$, podczas gdy stany o niższym ładunku ulegałyby rozmyciu. W TSM ograniczenie to zostaje przezwyciężone poprzez uwzględnienie nieliniowego członu potencjału zakleszczenia (jamming) sfer interakcji 0-cząstek. Samozakleszczenie samych cząstek jest fizycznie niemożliwe; nieliniowej blokadzie ulegają wyłącznie ich geometryczne sfery oddziaływań.

Pełny efektywny funkcjonał energii $E[\mathbf{n}]$ dla solitonowego węzła topologicznego o ładunku $\mathcal{W}$ przyjmuje postać:

$$E[\mathbf{n}] = \int_{\mathbb{R}^3} \left[ \frac{A}{2} (\nabla \mathbf{n})^2 + \frac{B}{2} (\nabla \mathbf{n})^4 + \frac{\mathcal{K}}{2} \phi(\mathbf{x})^2 + V_{\text{jam}}(\phi) \right] d^3x \tag{7.2.1}$$

Gdzie człon $(\nabla \mathbf{n})^2$ to klasyczna energia gradientowa, $(\nabla \mathbf{n})^4$ stanowi człon stabilizacyjny typu Skyrme'a zapobiegający kolapsowi punktowemu, natomiast kluczowy człon potencjału zakleszczenia sfer interakcji $V_{\text{jam}}(\phi)$ definiujemy jako:

$$V_{\text{jam}}(\phi) = \frac{D \cdot \mathcal{W}^2}{\left(1 - \left(\frac{\phi}{\phi_{\max}}\right)^2\right)^n} \tag{7.2.2}$$

Gdzie $D$ to stała sprzężenia mikroskopowego, $\phi_{\max}$ to graniczne ugięcie ortogonalne odpowiadające maksymalnemu dopuszczalnemu zagęszczeniu (zakleszczeniu) sfer interakcji 0-cząstek, a $n \ge 2$ jest wykładnikiem nieliniowości strukturalnej. Wprowadzenie $V_{\text{jam}}(\phi)$ modyfikuje równanie ewolucji ładunku w globalnym parametrze zderzeniowym $\tau$:

$$\frac{dW}{d\tau} = -\frac{\delta E[\mathbf{n}]}{\delta \mathbf{n}} \tag{7.2.3}$$

Dnia dzięki obecności bieguna asymptotycznego w $V_{\text{jam}}(\phi)$ przy $\phi \rightarrow \phi_{\max}$, dla stanu podstawowego $\mathcal{W}=1$ redukcja wariacyjna generuje głębokie, stabilne minimum lokalne. Uniemożliwia to relaksację ładunku do zera, czyniąc go asymptotycznie trwałym. Stan ten odpowiada podstawowej cząstce materii – elektronowi.

Geometryczne pochodzenie spinu połówkowego wyłania się bezpośrednio z definicji spinu hopfionu w TSM, opisywanego relacją:

$$s = \mathcal{W} - 2 \tag{7.2.4}$$

Dla elektronu o ładunku topologicznym $\mathcal{W}=1$ otrzymujemy $s = 1 - 2 = -1/2$, co precyzyjnie odtwarza połówkowy charakter spinu i statystykę Fermiego-Diraca (znak ujemny definiuje lewoskrętną chiralność stanu podstawowego).

## 7.3. Model kawitacyjny hadronu a Głębokie Rozpraszanie Nieelastyczne (DIS)

### 7.3.1. Hadron jako pęcherzyk kawitacyjny w 0-Matrycy

W TSM hadron (proton, neutron, mezon) to nie zbiór punktowych kwarków utrzymywanych w próżni, lecz lokalny obszar 4-wymiarowej 0-Matrycy, w którym gęstość naprężeń strukturalnych osiąga stan krytyczny, tworząc zamkniętą domenę – pęcherzyk kawitacyjny. Na zewnątrz pęcherzyka panuje podstawowe, wysokie ciśnienie zewnętrzne Matrycy ($\langle\phi\rangle_{\text{macro}} \approx \phi_0$), natomiast wewnątrz występuje stan częściowej relaksacji falowej ($\langle\phi\rangle_{\text{macro}} < \phi_0$).

Ściana pęcherzyka to stromy, wysoce nieliniowy gradient naprężeń – kinetyczna bariera fazowa, która fizycznie izoluje wnętrze hadronu od reszty osnowy. Stabilność struktury hadronowej jest wyznaczana przez równowagę pomiędzy wewnętrznym napięciem powierzchniowym splotów a profilem ciśnienia hydrostatycznego pęcherzyka $p(r)$. Dla nukleonu o promieniu granicznym $r_0 \approx 0.84\, \text{fm}$ profil ciśnienia opisuje funkcja:

$$p(r) = P_{\text{sub}} \cdot \left[1 - \exp\left(-\frac{(r-r_0)^2}{\alpha^2}\right)\right] - P_{\text{max}} \cdot \operatorname{sech}^2\left(\frac{r}{\alpha}\right) \tag{7.3.1}$$

Gdzie $P_{\text{sub}}$ to ciśnienie tła Substratu, $P_{\text{max}}$ to maksymalne ciśnienie na sztywnej ściance granicznej pęcherzyka, a $\alpha$ stanowi stałą materiałową osnowy. Ciśnienie maleje od ścianki do geometrycznego centrum pęcherzyka, działając jako operator zaburzenia masowego dla zlokalizowanych w nim modów drgań.

Szkielet topologiczny struktury stabilizowany jest przez fundamentalny defekt topologiczny – węzeł trójlistny ($3_1$), który w rzucie na 3-branę posiada trzy główne skrzyżowania (pętle naprężeń), odpowiadające trzem kwarkom walencyjnym. Wewnątrz pęcherzyka panuje intensywna turbulencja akustyczno-sprężysta – tzw. morze partoniczne, stanowiące zbiór wyższych harmonicznych drgań samego węzła oraz uwięzionych fal stojących 0-Matrycy.

### 7.3.2. Interpretacja wyników DIS

Eksperymenty Głębokiego Rozpraszania Nieelastycznego (DIS) badają strukturę hadronów za pomocą sondy elektronowej o zmiennym przekazie pędu $Q^2$. W TSM wyniki te zyskują czysto hydrodynamiczną interpretację:

1. **Niskie $Q^2$ (długa fala sondująca):** Fala elektronu o niskiej energii nie jest w stanie rozróżnić drobnych turbulencji wewnątrz pęcherzyka. Widzi tylko trzy główne żyły szkieletu węzła $3_1$ i rozprasza się na kwarkach walencyjnych.
2. **Wysokie $Q^2$ (krótka fala sondująca):** Sonda o wysokiej energii wnika głęboko w mikrostrukturę pęcherzyka, rozpraszając się na gęstej pianie turbulentnych fluktuacji sprężystych. Ewolucja funkcji rozkładu partonów (PDF) opisywana równaniami DGLAP nie odzwierciedla kreacji wirtualnych cząstek w próżni, lecz zmianę skali rozdzielczości widma drgań nieliniowego ośrodka sprężystego.

## 7.4. Uwięzienie topologiczne (Confinement) i asymptotyczna swoboda

W ontologii TSM uwięzienie kwarków nie wynika z wymiany gluonów, lecz z mechaniki nieliniowego rozciągania ośrodka sprężystego. Kwarki są otwartymi fragmentami splotów (warkoczami), które z jednej strony tworzą rdzeń węzła $3_1$, a z drugiej – są fizycznie zakotwiczone w ścianie pęcherzyka kawitacyjnego, domykając obwód naprężeń wewnątrz hadronu.

Próba wyciągnięcia kwarka z pęcherzyka powoduje lokalne odkształcenie plastyczne ściany i wyciągnięcie jej w szyjkę – wydłużony strumień o ekstremalnym naprężeniu ścinającym. Energia potrzebna do rozciągania tej struktury rośnie liniowo z dystansem $r$:

$$E_{\text{conf}}(r) = \sigma \cdot r \tag{7.4.1}$$

Gdzie $E_{\text{conf}}$ to energia uwięzienia $[\text{J}]$, $\sigma$ to napięcie struny topologicznej $[\text{N}]$, będące bezpośrednią funkcją modułu sztywności 0-Matrycy, a $r$ to odległość między kwarkiem a resztą hadronu $[\text{m}]$. Gdy zgromadzona energia sprężysta przekroczy próg plastyczności (równy $2 m_q c_{\perp}^2$), dochodzi do topologicznego pęknięcia kontinuum. Szyjka ulega relaksacji, tworząc dwa nowe, zamknięte pęcherzyki – parę kwark-antykwark. Jest to mechaniczny obraz hadronizacji i powstawania dżetów.

Asymptotyczna swoboda (słabnięcie oddziaływań na małych dystansach) wynika bezpośrednio z geometrii pęcherzyka kawitacyjnego. W miarę jak kwarki zbliżają się do środka hadronu, oddalają się od nieliniowej ściany naprężeń. Ponieważ wnętrze pęcherzyka jest obszarem zrelaksowanym, efektywne naprężenie między warkoczami dąży lokalnie do zera. Obserwowany spadek stałej sprzężenia przy wysokich energiach to bezpośrednia konsekwencja wchodzenia sondy w obszar obniżonego ciśnienia wewnątrz pęcherzyka.

## 7.5. Masy hadronów i brak wolnych gluonów

Masa hadronu to całkowita energia odkształcenia sprężystego i kinetycznego uwięziona w geometrii pęcherzyka:

$$m_{\text{hadron}} = \frac{1}{c_{\perp}^2} \left( \oint_{\text{ściana}} \sigma_{ab} \, dS^{ab} + \sum_{\text{warkocze}} E_{\text{kin}} \right) \tag{7.5.1}$$

Gdzie $m_{\text{hadron}}$ to masa spoczynkowa hadronu $[\text{kg}]$, $c_{\perp}$ to prędkość fal poprzecznych $[\text{m} \cdot \text{s}^{-1}]$, $\sigma_{ab}$ to tensor naprężeń na ścianie pęcherzyka $[\text{Pa}]$, $dS^{ab}$ to element powierzchni ściany $[\text{m}^2]$, a $E_{\text{kin}}$ to energia kinetyczna drgań warkoczy $[\text{J}]$. Głównym nośnikiem masy ($\sim 99\%$) jest energia powierzchniowa ściany – nieliniowy gradient naprężeń utrzymywany przeciwko ciśnieniu zewnętrznemu Matrycy.

Gluony nie istnieją jako autonomiczne cząstki. Są one wyłącznie wewnętrznymi modami plazmowymi – falami podłużnymi i poprzecznymi wzbudzonymi wewnątrz zrelaksowanego ośrodka pęcherzyka. Ich propagacja poza barierę fazową jest niemożliwa, ponieważ na zewnątrz 0-Matryca znajduje się w stanie wysokiego naprężenia, co powoduje wykładnicze tłumienie amplitudy fali (mechanizm analogiczny do efektu Proca dla pól masywnych). Gluon wygasa na dystansie subatomowym, co klasyczna fizyka interpretuje jako uwięzienie.

## 7.6. Stabilizacja neutronu w jądrze atomowym

W stanie wolnym neutron jest pęcherzykiem kawitacyjnym o podwyższonym naprężeniu wewnętrznym, co prowadzi do jego rozpadu słabego ze średnim czasem życia $\sim 880\text{ s}$. Jednak wewnątrz stabilnego jądra atomowego zachodzi mechanizm geometrycznego zatrzasku fazowego (phase latch).

Klastrowanie nukleonów w geometrycznie zwarte struktury sieciowe sprawia, że ściany pęcherzyków nakładają się i rezonują. Centrum geometryczne każdego neutronu staje się węzłem fali stojącej dla częstotliwości zagrażających przetrwaniu splotu neutronu ($f_n$). Oznacza to drastyczne wygaszenie i wyzerowanie lokalnego szumu degradującego neutron:

$$\rho_{\text{wewn}}(f_n) \approx 0 \implies \lambda_{n,\text{jądro}} \approx 0 \tag{7.6.1}$$

Wskutek tego stała rozpadu dąży do zera, a czas życia neutronu w zatrzasku fazowym dąży do nieskończoności. Odchylenia od pełnej symetrii geometrycznej klastra (w izotopach niestabilnych) wprowadzają przecieki fal szumu, przywracając skończone prawdopodobieństwo rozpadu beta.

## 7.7. Oddziaływanie słabe jako mechaniczne rozwęźlanie i bozony W/Z

W TSM oddziaływanie słabe nie jest wymianą bozonów rozumianych jako fundamentalne cząstki punktowe. Jest to proces mechanicznego rozwęźlania nietrwałych konfiguracji topologicznych – rekonfiguracji warkoczy wewnątrz pęcherzyka, która prowadzi do zmiany ładunku i masy hadronu.

W przypadku rozpadu beta neutronu ($n \to p + e^- + \bar{\nu}_e$), pod wpływem wewnętrznej turbulencji lub fluktuacji termicznej dochodzi do mechanicznego pęknięcia skrzyżowania węzła: warkocz reprezentujący kwark $d$ przekształca się w warkocz kwarka $u$. Nadmiar energii sprężystej zostaje wypromieniowany jako para: elektron (nowy, prosty węzeł o ładunku topologicznym $\mathcal{W}=1$) oraz antyneutrino (bezmasowy mod falowy, $\mathcal{W}=0$, zanurzony i rozchodzący się w wymiarze $x^4$).

Bozony $W^\pm$ i $Z^0$ stanowią krótkożyjące, silnie nieliniowe rezonanse naprężeniowe 0-Matrycy, wzbudzane w momencie gwałtownej rekonfiguracji węzłów. Ich masa ($\sim 80-91\text{ GeV}$) to całkowita praca mechaniczna wykonywana przeciwko pełnemu 4-wymiarowemu ciśnieniu hydrostatycznemu Matrycy dążącej do kolapsu pęcherzyka. Niezwykle krótki czas życia ($\sim 10^{-25}\text{ s}$) to czas relaksacji tego skrajnego odkształcenia w sprężystym ośrodku.

### 7.7.1. Macierz CKM jako obrót osi naprężeń

W Modelu Standardowym macierz CKM opisuje mieszanie zapachów kwarków podczas oddziaływań słabych. TSM definiuje ją jako klasyczną transformację bazy tensora odkształceń w przestrzeni 3D. Ponieważ kwarki górne (ładunek $+2/3$) i dolne ($-1/3$) stanowią odmienne orientacje chiralne i geometryczne splotów, ich wewnętrzne osie naprężeń sprężystych nie są idealnie współliniowe. Są one tworami 4-wymiarowymi, a ich przestrzeń wewnętrzna naprężeń zawiera dodatkowy stopień swobody związany z zanurzeniem w $x^4$. Macierz CKM reprezentuje geometryczną macierz obrotu, dopasowującą osie odkształceń podgrup kwarkowych podczas procesu rozwęźlania i rekonfiguracji strukturalnej.

## 7.8. Hierarchia mas leptonów i reguła Koidego

W TSM elektron, mion i taon dzielą ten sam elementarny ładunek topologiczny $\mathcal{W}=1$. Ich zróżnicowanie masowe wynika z wewnętrznej złożoności splotu geometrycznego – mion i taon stanowią wyższe, wzbudzone harmoniczne podstawowego splotu elektronowego. Ich potężna masa to energia zmagazynowana w dodatkowych, wymuszonych pętlach i skrzyżowaniach wewnętrznych, opisywanych wskaźnikiem złożoności topologicznej $\chi_{\text{top}}$.

Ta geometryczna zależność przejawia się w empirycznej relacji Koidego dla mas leptonów naładowanych:

$$\frac{m_e + m_\mu + m_\tau}{\left(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau}\right)^2} = \frac{2}{3} \tag{7.8.1}$$

Wartość tej relacji obliczona empirycznie wynosi dokładnie $0{,}6666\dots$ z odchyleniem mniejszym niż $10^{-4}$. W TSM reguła Koidego przestaje być numerologiczną zagadką, stając się bezpośrednią konsekwencją geometrii odkształceń sprężystych.

Matematyczny opis energii rotacyjnej węzła i jego orientacji względem osi $x^4$ definiuje operator Hamiltona na sferze konfiguracji $\mathbb{S}^2$:

$$E_{\text{rot}}(\theta) = E_0 + \frac{\hbar^2}{2I} \kappa \cos^2\theta \tag{7.8.2}$$

Gdzie $I$ jest efektywnym momentem bezwładności hydrodynamicznej chmury osnowy, $\kappa$ to moduł sztywności skrętnej przy ekstremalnych zagięciach, a $\theta$ to dyskretne kąty orientacyjne wyznaczane przez rozwiązanie Laplasjanu Sferycznego na sferze $\mathbb{S}^2$. Rzutowanie tych dyskretnych stanów energii na 3-branę daje dokładnie trzy dozwolone wartości masowe spełniające czynnik sprzężenia geometrycznego $2/3$. Masa danej generacji wyraża się jako:

$$m_i c_{\text{lok}}^2 = E_{\text{baza}} + \kappa \cdot f(\chi_{\text{top}}(K_i)) \tag{7.8.3}$$

Gdzie $f(\chi_{\text{top}}(K_i))$ to nieliniowa funkcja zależna od wskaźnika złożoności topologicznej splotu, powiązana z minimalną liczbą skrzyżowań linii naprężeń warkocza. Rozpad mionu lub taonu to mechaniczne rozwęźlanie tych dodatkowych pętli, wywołane interakcją z szumem tła Substratu ($T_{\text{sub}}$), z emisją neutrin. Anomalia magnetyczna $g-2$ stanowi bezpośredni pomiar oporu hydrodynamicznego (tarcia) tych dodatkowych pętli podczas ruchu w sieci 0-Matrycy.

## 7.9. Oscylacje neutrin i złamanie parzystości

Neutrina są w TSM bezmasowymi, ortogonalnymi falami poprzecznymi rozchodzącymi się wzdłuż czwartego wymiaru przestrzennego $x^4$. Trzy generacje neutrin ($\nu_e, \nu_\mu, \nu_\tau$) odpowiadają trzem niezależnym rzutom polaryzacji na ortogonalne płaszczyzny w izotropowej 3-brane, co wyjaśnia, dlaczego szerokość niewidzialnego rozpadu bozonu $Z$ precyzyjnie wskazuje liczbę generacji $N_\nu = 3$. Grupa $SU(2)$, stanowiąca podwójne nakrycie grupy $SO(3)$, generuje te stany poprzez swoje trzy macierze generatorów ($T_1, T_2, T_3$), odpowiadające fizycznie rzutom na trzy ortogonalne płaszczyzny w izotropowej 3-brane.

Zjawisko oscylacji neutrin to przejaw rotacji płaszczyzny polaryzacji tych fal podczas ich propagacji w osnowie. Macierz PMNS opisująca to mieszanie staje się klasyczną macierzą obrotu geometrycznego w 4D.

Złamanie parzystości (chiralności) w oddziaływaniach słabych (eksperyment Wu 1957) wynika bezpośrednio z wrodzonego, lewoskrętnego zwoju samej 3-brany, który narzuca uprzywilejowany kierunek pękania i relaksacji splotu. Pierwotne Wielkie Wydarzenie wygenerowało globalny asymetryczny naciąg, co faworyzuje powstawanie i rozpad cząstek o określonej lewoskrętnej orientacji kinematycznej. Rozpady słabe jedynie ujawniają tę wbudowaną asymetrię strukturalną tła.

## 7.10. Determinizm kwantowy i weryfikacja empiryczna

TSM eliminuje potrzebę kolapsu funkcji falowej i probabilistycznego indeterminizmu, przywracając pełny determinizm mechaniczny w ujęciu teorii fali pilotującej.

### 7.10.1. Hydrodynamika fali pilotującej

Elektron porusza się w osnowie jako stabilny węzeł topologiczny, generując przed sobą sprężystą falę dziobową (pilotującą) w 0-Matrycy. Odkształcenie tła $\phi(\mathbf{x}, t)$ spełnia deterministyczne równanie falowe ze źródłem:

$$\nabla^2 \phi - \frac{1}{c_{\perp}^2} \frac{\partial^2 \phi}{\partial t^2} = \mathcal{S}(\mathbf{x}_e, t) \tag{7.10.1}$$

Gdzie $\mathcal{S}$ to człon źródłowy sprzężony z pozycją rdzenia cząstki. W eksperymencie Younga (z dwiema szczelinami) fala pilotująca przechodzi przez obie szczeliny, interferując ze sobą i modyfikując profil naprężeń tła. Rdzeń solitonu (cząstka), poruszając się wzdłuż linii najmniejszego oporu sprężystego osnowy, trafia w odpowiednie prążki interferencyjne. Interwencja detektora niszczy tę subtelną falę pilotującą za pomocą szumu, co eliminuje wzór interferencyjny bez konieczności odwoływania się do niefizycznego aktu kolapsu.

### 7.10.2. Kryteria falsyfikacji i dowody empiryczne

Model TSM dostarcza konkretnych, mierzalnych kryteriów, dzięki którym może zostać zweryfikowany lub sfałszowany:

1. **Rezonator Matrycy:** Możliwość laboratoryjnego, kontrolowanego wzbudzania lokalnych fal podłużnych w osnowie, co powinno prowadzić do mierzalnych anomalii bezwładnościowych cząstek testowych.
2. **Analiza tensorowa zdarzeń 3-jetowych w LHC:** Zgodnie z modelem węzła $3_1$, destrukcja protonu w zderzeniach wysokoenergetycznych musi zachodzić asymetrycznie wzdłuż trzech pierwotnych osi geometrycznych szkieletu topologicznego. Generuje to sygnaturę trzech dżetów o specyficznych korelacjach tensorowych i kątowych, co wykracza poza standardowe, izotropowe przybliżenia statystyczne QCD.
3. **Istniejące dane empiryczne:** Idealna płynność plazmy kwarkowo-gluonowej (będąca w TSM po prostu stanem stopionej, zrelaksowanej osnowy pęcherzyków), całkowity brak cząstek supersymetrycznych w pełnym zakresie energii LHC oraz rygorystyczna stabilność protonu (czas życia $> 1.6 \times 10^{34}$ lat ze względu na nieliniową barierę potencjału zakleszczenia sfer interakcji) stanowią silne dowody wspierające strukturę elasto-dynamiczną TSM względem teorii opartych na punktowych osobliwościach w próżni.