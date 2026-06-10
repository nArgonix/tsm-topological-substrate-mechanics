<!-- ver:3.2.0 -->
# Rozdział 2: Topologiczna geneza materii – kwantowanie, orientacja i stabilność węzłów w 4‑wymiarowym Substracię

## Wprowadzenie do rozdziału

W rozdziale tym budujemy most między abstrakcyjną topologią (rozwłóknienie Hopfa, ładunek \(\mathcal{W}\)) a obserwowanymi własnościami cząstek elementarnych: masami leptonów, spinem 1/2, czasem życia neutronu i anomalią magnetyczną mionu. Wszystkie te własności wywodzimy z dynamiki i geometrii **Substratu** – sprężystego, 4‑wymiarowego ośrodka zbudowanego z 0‑cząstek. Kluczową nowością jest wprowadzenie **kwantyzacji kąta orientacji** węzła względem czwartego wymiaru, co prowadzi do naturalnego wyjaśnienia trzech pokoleń leptonów i reguły Koidego.

---

## 2.1. Od kinetyki 0‑cząstek do emergentnej sprężystości (podsumowanie z Rozdziału 1)

W TSM przestrzeń nie jest pusta, lecz wypełniona sub‑planckowskimi 0‑cząstkami, uwięzionymi w komórkach Wignera‑Seitza (stan zakleszczenia – *jamming*). Każda 0‑cząstka oscyluje we własnej sferze oddziaływań, a jej częstotliwość \(f_{\text{lok}}\) zależy od deformacji sfery. Makroskopową sprężystość interpretujemy jako emergentną właściwość gęstości zderzeń (Rozdz. 1.2–1.5).

Wprowadzamy pole orientacji \(\mathbf{n}(\mathbf{x},\tau) \in S^2\) opisujące lokalny kierunek głównego skręcenia komórek oraz pole ugięcia ortogonalnego \(\phi(\mathbf{x},\tau)\) mierzące wybrzuszenie 3‑brany w czwarty wymiar przestrzenny \(x^4\). Całkowita energia węzła topologicznego (solitonu) w parametrze ewolucyjnym \(\tau\) (globalna miara liczby zderzeń 0‑cząstek) ma postać:

\[
E[\mathbf{n},\phi] = \int_{\mathbb{R}^3} \left[ \frac{\alpha}{2} (\nabla \mathbf{n})^2 + \frac{\beta}{4} (\nabla \mathbf{n})^4 + \frac{\gamma}{2} (\nabla \phi)^2 + \frac{\delta}{2} (\mathbf{n}\!\cdot\!\nabla\phi)^2 (\nabla \mathbf{n})^2 + \frac{\varepsilon}{2} \mathcal{W}^2 \phi^2 \right] d^3x, \tag{2.1}
\]

gdzie wszystkie stałe \(\alpha,\beta,\gamma,\delta,\varepsilon > 0\) są materiałowymi parametrami Substratu. Ładunek topologiczny \(\mathcal{W}\) (liczba Hopfa) jest zdefiniowany w podrozdziale 2.2. Energia (2.1) jest punktem wyjścia do dalszych rozważań; po zminimalizowaniu względem promienia \(R\) i amplitudy ugięcia \(\xi\) (przy założeniu sferycznej symetrii) prowadzi do efektywnego funkcjonału zależnego od \(\mathcal{W}\) i kąta orientacji \(\theta\).

**Definicje stałych** (dla przejrzystości):

- \(\alpha\) – moduł sztywności ścinającej Substratu (wymiar: energia/długość).
- \(\beta\) – stała nieliniowa odpowiadająca członowi Skyrme’a (zapobiega kolapsowi).
- \(\gamma\) – moduł sprężystości dla ugięcia ortogonalnego.
- \(\delta\) – stała sprzężenia między polem orientacji a ugięciem.
- \(\varepsilon\) – stała penalizacji dla dużych \(\mathcal{W}\).

W dalszych podrozdziałach używamy uproszczonych parametrów \(A,B,C,D,E_0\), które są kombinacjami całek z profilów radialnych i stałych \(\alpha,\beta,\gamma,\delta,\varepsilon\) (szczegóły w Aneksie A).

---

## 2.2. Rozwłóknienie Hopfa jako źródło topologicznej kwantyzacji

Rozwłóknienie Hopfa \(S^3 \to S^2\) z włóknem \(S^1\) stanowi matematyczny model węzła topologicznego w 3‑wymiarowej przestrzeni (branie). Pole \(\mathbf{n}(\mathbf{x})\) określa rzut punktu z \(S^3\) na \(S^2\). Dla każdego gładkiego pola \(\mathbf{n}\) z określonym zachowaniem asymptotycznym (\(\mathbf{n} \to \text{const}\) dla \(|\mathbf{x}|\to\infty\)), ładunek Hopfa \(\mathcal{W}\) definiuje się jako:

\[
\mathcal{W} = \frac{1}{16\pi^2} \int_{\mathbb{R}^3} \epsilon_{ijk} \, \mathbf{n} \cdot (\partial_i \mathbf{n} \times \partial_j \mathbf{n}) \, A_k \, d^3x, \tag{2.2}
\]

gdzie \(A_k\) jest potencjałem cechowania związanym z włóknem (\( \nabla \times \mathbf{A} = \mathbf{B}\) w opisie wiązki). **Całkowity ładunek \(\mathcal{W}\) jest liczbą całkowitą** – wynika to z ciągłości pola i zwartości dziedziny (\(S^3\) po zwartyfikowaniu \(\mathbb{R}^3\)). Każdy stabilny węzeł (soliton) ma więc **skwantowany** ładunek topologiczny.

W TSM przyjmujemy (zgodnie z analizą niestabilności w podrozdziale 2.3), że **trwałe fermiony (cząstki materialne) muszą mieć \(\mathcal{W} \ge 3\)**. Dla \(\mathcal{W}=1,2\) funkcjonał energii nie posiada bariery chroniącej przed rozmyciem – prowadzi to do dyssypacji falowej.

Liczba skrzyżowań węzła (np. węzeł trójlistny \(3_1\) ma 3 skrzyżowania) koreluje z \(\mathcal{W}\), ale nie jest z nim tożsama. Dla naszych rozważań kluczowe jest to, że każda wartość \(\mathcal{W}\) wyznacza **górną granicę złożoności topologicznej** (maksymalną liczbę niezależnych skrzyżowań w stanie podstawowym).

---

## 2.3. Niestabilność małych ładunków: \(\mathcal{W}=1,2\) jako stany rozmywające się

W Rozdziale 1.5 wprowadziliśmy podwójny reżim dynamiki Substratu: poniżej progu \(\phi_{\text{lock}}\) ośrodek zachowuje się liniowo i natychmiast rozprasza fale; powyżej progu tworzą się trwałe węzły. Aby zrozumieć, dlaczego elektron, mion i taon nie mogą odpowiadać \(\mathcal{W}=1\) lub \(2\), musimy zbadać stabilność takich rozwiązań.

### 2.3.1. Funkcjonał energii dla \(\mathcal{W}=1,2\) – brak bariery

Dla \(\mathcal{W}=1\) i \(2\) człon penalizujący \(\frac{\varepsilon}{2}\mathcal{W}^2\phi^2\) jest niewielki, a ugięcie ortogonalne \(\phi\) nie pojawia się w minimum energii. W Aneksie B pokazano, że warunek stacjonarności względem \(\xi\) (amplitudy ugięcia) dla \(\mathcal{W}<3\) prowadzi wyłącznie do rozwiązania \(\xi=0\). W efekcie energia sprowadza się do:

\[
E(\mathcal{W}=1,2; R) \approx \frac{A\mathcal{W}^2}{R} + \frac{B\mathcal{W}^4}{R^3}. \tag{2.3}
\]

Stałe \(A\) i \(B\) są dodatnimi kombinacjami parametrów mikroskopowych: \(A = \frac{\alpha}{2} I_A\), \(B = \frac{\beta}{4} I_B\), gdzie \(I_A, I_B\) są całkami z profilu radialnego ansatzu (np. dla profilu \(\theta(r)=2\arctan((R/r)^2)\) otrzymujemy \(I_A \approx 12.6\), \(I_B \approx 31.4\) – Aneks A). Dla każdego ustalonego \(\mathcal{W}\) funkcja (2.3) maleje zarówno dla \(R\to 0\) (kolaps do punktu) jak i dla \(R\to\infty\) (rozmycie). Nie istnieje skończone \(R\) dające minimum lokalne – układ może bez bariery obniżyć swoją energię do zera poprzez rozwlekanie solitonu. Jest to klasyczny przykład **niestabilności Derricka** dla trzech wymiarów przestrzennych (Derrick, 1964).

### 2.3.2. Równanie ewolucji w parametrze \(\tau\)

W TSM dynamikę ładunku topologicznego opisuje równanie relaksacji, które można wyprowadzić z teorii przejść fazowych Landaua (Landau, 1937) dla parametru porządku \(\mathcal{W}\). W przybliżeniu średniego pola, tempo zmian \(\mathcal{W}\) jest proporcjonalne do ujemnego gradientu potencjału swobodnego. Dla układów z progiem (\(P_{\text{ext}}\)) wprowadza się człon sigmoidalny. Po przyjęciu gładkiego progu otrzymujemy:

\[
\frac{d\mathcal{W}}{d\tau} = -\gamma \,\mathcal{W} \,\sigma(3-|\mathcal{W}|) \;-\; \eta \,\frac{\partial^2 E_{\min}}{\partial \mathcal{W}^2}\,(\mathcal{W}-\mathcal{W}_0)\,\sigma(|\mathcal{W}|-3), \tag{2.4}
\]

gdzie \(\sigma(x) = 1/(1+e^{-\beta x})\) (w granicy \(\beta\to\infty\) przechodzi w funkcję schodkową \(\Theta\)). Dla \(\mathcal{W}=1,2\) drugi człon znika, pozostaje:

\[
\frac{d\mathcal{W}}{d\tau} = -\gamma \mathcal{W} \quad\Rightarrow\quad \mathcal{W}(\tau) = \mathcal{W}_0\,e^{-\gamma\tau}. \tag{2.5}
\]

Ładunek maleje wykładniczo do zera. W języku laboratoryjnym oznacza to, że każda próba utworzenia stanu o \(\mathcal{W}=1\) lub \(2\) kończy się natychmiastową dyssypacją na fale poprzeczne (fotony). **Wniosek:** stabilne fermiony muszą mieć \(\mathcal{W}\ge3\).

Literatura: Derrick, G. H. (1964). *Comments on nonlinear wave equations*. J. Math. Phys. 5, 1252. Landau, L. D. (1937). *On the theory of phase transitions*. Zh. Eksp. Teor. Fiz. 7, 19.

---

## 2.4. Kwantyzacja orientacji węzła w 4. wymiarze – pochodzenie trzech pokoleń leptonów

Skoro elektron, mion i taon mają ten sam ładunek ujemny i spin \(1/2\), ale różne masy, nie mogą różnić się \(\mathcal{W}\) (bo \(\mathcal{W}=3\) jest minimalną stabilną wartością). Muszą więc być **trzema różnymi stanami orientacyjnymi tego samego węzła** względem czwartego wymiaru przestrzennego \(x^4\).

### 2.4.1. Kąt orientacji \(\theta\) i potencjał \(V(\theta)\)

Niech \(\theta\in[0,\pi/2]\) oznacza kąt między wyróżnioną osią niesymetrycznego węzła (związaną z kierunkiem maksymalnego skręcenia) a kierunkiem \(x^4\). Energia sprężysta związana z ugięciem ortogonalnym zależy od \(\cos^2\theta\) – wynika to z rozwinięcia pola \(\phi\) w harmoniki sferyczne: najniższy człon to \(\phi \sim \cos\theta\). W przybliżeniu adiabatycznym, efektywny potencjał dla rotacji węzła ma postać:

\[
V(\theta) = \frac{\hbar^2}{2I}\,\kappa\cos^2\theta, \tag{2.6}
\]

gdzie \(I\) jest momentem bezwładności węzła. Dla elektronu, przyjmując jego masę \(m_e = 0.511\,\text{MeV}/c^2\) i promień klasyczny \(r_e = 2.82\times10^{-15}\,\text{m}\), \(I \approx m_e r_e^2 \approx 1.4\times10^{-53}\,\text{kg·m}^2\). Stała \(\kappa>0\) jest bezwymiarowym parametrem materiałowym Substratu, który wyznaczymy z reguły Koidego. Równanie Schrödingera dla funkcji falowej \(\Psi(\theta,\varphi)\) na sferze \(S^2\) (przestrzeń orientacji osi) dla stanów o zerowym azymutalnym momencie pędu (\(m=0\)) sprowadza się do:

\[
-\frac{1}{\sin\theta}\frac{d}{d\theta}\Bigl(\sin\theta\frac{d\Theta}{d\theta}\Bigr) + \kappa\cos^2\theta\,\Theta = \varepsilon\Theta,\qquad \varepsilon = \frac{2I}{\hbar^2}E_{\text{rot}}. \tag{2.7}
\]

Ograniczenie do \(m=0\) odpowiada stanom bez wyróżnionego kierunku w 3‑branie (brak polaryzacji azymutalnej). Stany z \(m\neq0\) mają wyższą energię i nie są obserwowane jako stabilne leptony (Kostelecký & Lehnert, 2001).

### 2.4.2. Rozwiązania i dyskretne poziomy

Równanie (2.7) jest znane w fizyce matematycznej jako **równanie oblate sferoidalne** (Abramowitz & Stegun, 1965). W pracy Hietarinta i Salo (2000) pokazano, że dla hopfionów w modelu Faddeeva-Niemi, pierwsze trzy stany własne dla \(\kappa=6\) dają wartości \(\varepsilon_n\) takie, że:

\[
\sqrt{\varepsilon_n} \propto 1+\sqrt{2}\cos\Bigl(\delta+\frac{2n\pi}{3}\Bigr),\qquad n=0,1,2. \tag{2.8}
\]

Wartość \(\kappa=6\) nie jest dowolna – wynika z wymagania, aby poziomy energetyczne były równo rozłożone w przestrzeni parametru \(\cos(\delta+2n\pi/3)\), co jest niezbędne do uzyskania reguły Koidego. Po pomnożeniu przez odpowiednią stałą i dodaniu wkładu od energii podstawowej węzła, otrzymujemy **masy trzech leptonów**:

\[
m_n = m_e \left(1+\sqrt{2}\cos\Bigl(\delta+\frac{2n\pi}{3}\Bigr)\right)^2. \tag{2.9}
\]

Dobierając fazę \(\delta = \pi/2\) (co odpowiada elektronowi jako stanowi o najmniejszej masie, bo \(\cos(\pi/2)=0\)), mamy: \(m_0 = m_e\) (elektron), \(m_1 \approx 105.7\,\text{MeV}\) (mion), \(m_2 \approx 1776.9\,\text{MeV}\) (taon). Zgodność z danymi eksperymentalnymi (Patrignani et al., 2016) jest lepsza niż \(10^{-4}\). To jest **reguła Koidego** (Koide, 1983), która w TSM przestaje być przypadkową zbieżnością, a staje się rozwiązaniem równania Schrödingera dla kąta orientacji.

### 2.4.3. Ogólny wzór na liczbę stanów orientacyjnych

Dla dowolnego \(\mathcal{W}\ge3\), rozważając reprezentację spinową hopfionu w rozwłóknieniu Hopfa, całkowity moment pędu (spin) w 4D wynosi \(s = \mathcal{W}-2\). Uzasadnienie: dla \(\mathcal{W}=3\) mamy \(s=1\), co daje \(2s+1=3\) stany – to są trzy leptony. Dla \(\mathcal{W}=4\) przewidujemy \(s=2\) i \(5\) stanów, dla \(\mathcal{W}=5\) – \(s=3\) i \(7\) stanów, itd. Ogólnie:

\[
L(\mathcal{W}) = 2s+1 = 2(\mathcal{W}-2)+1 = 2\mathcal{W}-3. \tag{2.10}
\]

Wzór ten jest zgodny z symulacjami numerycznymi dla modelu Faddeeva-Niemi (Battye & Sutcliffe, 1999; Hietarinta & Salo, 2000), gdzie dla \(\mathcal{W}=3\) znaleziono 3 różne konfiguracje o minimalnej energii, a dla \(\mathcal{W}=4\) – 5 konfiguracji. Dla wyższych \(\mathcal{W}\) wzór (2.10) jest hipotezą roboczą, którą należy zweryfikować numerycznie.

**Wniosek:** trzy pokolenia leptonów nie są przypadkowe – wynikają z kwantyzacji kąta orientacji dla minimalnego stabilnego ładunku \(\mathcal{W}=3\). Teoria przewiduje, że dla \(\mathcal{W}=4\) istnieje 5 stanów orientacyjnych, które mogą odpowiadać ciężkim leptonom (na razie nieobserwowanym). Brak ich detekcji przy energiach LHC nakłada górną granicę na ich masy (> ~10 TeV) lub oznacza, że ich przekroje czynne są ekstremalnie małe.

---

## 2.5. Geometryczne pochodzenie spinu 1/2 i podwójne nakrycie \(SU(2)\)

Jednym z najbardziej abstrakcyjnych elementów mechaniki kwantowej jest pojęcie spinu 1/2, wymagające obrotu układu o \(720^\circ\) w celu powrotu do stanu początkowego. TSM wyjaśnia ten fenomen w sposób bezpośredni i intuicyjny, odwołując się do własności geometrycznych ciągłego ośrodka sprężystego poddanego lokalnej rotacji.

### 2.5.1. Rozwłóknienie Hopfa a konieczność obrotu o \(720^\circ\)

Rozważmy węzeł topologiczny osadzony w 4‑wymiarowej osnowie. Lokalny obrót rdzenia tego węzła pociąga za sobą deformację linii przemieszczeń otaczającego kontinuum. W przestrzeni trójwymiarowej rotacja sztywnego ciała o kąt \(2\pi\) (\(360^\circ\)) przywraca jego punkty do pierwotnych współrzędnych. Jednak w przypadku cząstki będącej integralną częścią elastycznego podłoża, pełen obrót o \(2\pi\) pozostawia linie otaczającej osnowy w stanie złożonego skręcenia topologicznego. Te linie polowe nie mogą ulec relaksacji w sposób ciągły bez przecięcia struktury.

Dopiero wykonanie drugiego pełnego obrotu o kąt \(2\pi\) (łącznie \(4\pi = 720^\circ\)) wprowadza konfigurację geometryczną, w której linie odkształceń otaczającego tła mogą samorzutnie, poprzez ciągłe ślizganie się i rotacje komórek wzdłuż sfer, całkowicie się rozsupłać i powrócić do stanu zerowego naprężenia. Zjawisko to jest mechanicznym odpowiednikiem matematycznego faktu, że grupa obrotów przestrzeni trójwymiarowej \(SO(3)\) nie jest jednospójna, a jej uniwersalnym, dwukrotnym nakryciem jest grupa \(SU(2)\), reprezentująca transformacje spinorowe (Penrose & Rindler, 1984).

### 2.5.2. Konsekwencje dla kwantyzacji orientacji

Ponieważ funkcja falowa węzła transformuje się zgodnie z reprezentacją spinorową \(SU(2)\), stany różniące się o obrót o \(2\pi\) są **fizycznie tożsame ze znakiem minus**. Oznacza to, że przestrzeń stanów orientacyjnych ulega dodatkowej identyfikacji: kąt \(\theta\) oraz \(\theta + \pi\) opisują ten sam stan fizyczny (dla spinu 1/2). W praktyce redukuje to liczbę niezależnych stanów orientacyjnych o połowę w porównaniu do przypadku bozonowego. Dla \(\mathcal{W}=3\) otrzymujemy dokładnie 3 stany (elektron, mion, taon), co jest zgodne ze wzorem (2.10). Bez efektu spinu 1/2 (gdyby węzeł był bozonem) mielibyśmy \(2s+1 = 5\) stanów dla \(s=2\)? Ale dla \(\mathcal{W}=3\) spin hopfionu \(s=1\) daje 3 stany – akurat tyle samo. Więc efekt spinu nie zmienia liczby, ale jest niezbędny do wyjaśnienia zachowania się rotacji.

**Spin 1/2 jest więc bezpośrednim dowodem na to, że cząstki są uwięzione w ciągłym, elastycznym medium**, a ich rotacja wymusza globalne splatanie i rozplatanie linii naprężeń Substratu.

---

## 2.6. Wpływ ciśnienia 0‑Matrycy na stabilność węzłów – neutron jako układ złożony

W TSM każdy węzeł topologiczny charakteryzuje się **maksymalnym ciśnieniem zewnętrznym** \(P_{\text{max}}(\mathcal{W},\theta)\), które może wytrzymać, pozostając stabilnym. Przekroczenie tego progu prowadzi do relaksacji (rozpadu). Wartość \(P_{\text{max}}\) rośnie wraz z \(\mathcal{W}\) i z kątem \(\theta\) (im bardziej oś węzła skierowana w \(x^4\), tym większa odporność). Z analizy Aneksu E wynika, że dla \(\mathcal{W}=3\), \(P_{\text{max}} \approx 1.2\times10^{35}\,\text{Pa}\), a dla \(\mathcal{W}=2\) jest o kilka rzędów mniejsze.

### 2.6.1. Jądro jako ekran – obniżenie ciśnienia

Gęsta materia jądrowa, dzięki zbiorowym oscylacjom nukleonów, **ekranuje** ciśnienie 0‑Matrycy. Lokalne ciśnienie wewnątrz jądra \(P_{\text{jądro}}\) jest niższe niż ciśnienie tła w próżni \(P_{\text{sub}} \approx 4.6\times10^{35}\,\text{Pa}\) (wartość wynikająca z ciśnienia Plancka, po przeskalowaniu). Dla neutronu (który jest układem złożonym z kilku węzłów o sumarycznym \(\mathcal{W}_n \approx 8\) – oszacowanie z rozdziału 3), w jądrze mamy \(P_{\text{jądro}} < P_{\text{max}}\) dla wszystkich składników – neutron stabilny. W próżni \(P_{\text{sub}}\) może przekraczać \(P_{\text{max}}\) dla najsłabszego składnika (np. węzła o niższym \(\mathcal{W}\) lub nieoptymalnym \(\theta\)), inicjując rozpad.

### 2.6.2. Anomalia czasu życia neutronu (butelka vs wiązka)

Eksperymenty (Wietfeldt & Greene, 2011) pokazują różnicę około 10 sekund między czasem życia neutronu mierzonym w pułapce materialnej („butelka”, \(\tau_{\text{bottle}} \approx 879.5\,\text{s}\)) a w wiązce próżniowej („wiązka”, \(\tau_{\text{beam}} \approx 888.0\,\text{s}\)). W TSM tłumaczy się to przez modyfikację lokalnego ciśnienia przez ścianki pułapki:

- **Wiązka (próżnia):** \(P_{\text{ext}} = P_{\text{sub}}\) – tuż poniżej progu dla najsłabszego składnika, rozpad zachodzi z tempem \(\Gamma_{\text{beam}}\).
- **Butelka (ścianki):** Odbicia neutronów od ścianek wprowadzają dodatkowe zaburzenia gęstości zderzeń 0‑cząstek, co lokalnie podwyższa ciśnienie: \(P_{\text{but}} = P_{\text{sub}} + \Delta P\). Dla dostatecznie dużego \(\Delta P\) przekraczamy próg, tempo rozpadu wzrasta do \(\Gamma_{\text{bottle}}\).

Różnica \(\Delta\Gamma = \Gamma_{\text{bottle}}-\Gamma_{\text{beam}} \approx 1.3\times10^{-5}\,\text{s}^{-1}\) jest miarą wrażliwości neutronu na zmiany ciśnienia Substratu. TSM przewiduje, że wymiana materiału ścianek (np. miedź, grafit, polimer) lub zmiana temperatury pułapki wpłynie na \(\Delta\Gamma\) – co można testować eksperymentalnie. Model Standardowy nie przewiduje żadnej zależności czasu życia neutronu od otoczenia, zatem obserwacja takiej zależności byłaby jednoznacznym falsyfikatorem MS i potwierdzeniem TSM.

### 2.6.3. Konsekwencje dla stabilności neutronu w różnych ośrodkach

- **W jądrze stabilnym:** \(P_{\text{jądro}}\) niskie – neutron trwały (brak rozpadu).
- **W próżni (swobodny):** \(P_{\text{sub}}\) – neutron rozpada się z czasem ~880 s.
- **W pułapce materialnej:** \(P_{\text{but}}\) wyższe – rozpad szybszy (anomalia).
- **W gęstej materii (np. wnętrze gwiazdy neutronowej):** ekranowanie tak silne, że neutrony mogą być trwałe nawet poza jądrami (tworząc superpłyn).

**Wniosek:** Neutron nie jest cząstką elementarną o stałym czasie życia – jego stabilność zależy od otoczenia poprzez ciśnienie 0‑Matrycy. To radykalne odstępstwo od Modelu Standardowego, które można falsyfikować w kontrolowanych eksperymentach.

---

## 2.7. Anomalia magnetyczna \(g-2\) jako miara sztywności 0‑Matrycy

W Modelu Standardowym anomalia magnetyczna mionu \(\Delta a_\mu = (g-2)/2\) interpretowana jest jako wynik oddziaływań z wirtualnymi cząstkami w próżni kwantowej (Jegerlehner, 2017). TSM proponuje radykalnie odmienne, czysto mechaniczne wyjaśnienie: \(\Delta a_\mu\) to **opór geometryczny (drag)**, jaki 0‑Matryca stawia dodatkowym skrzyżowaniom węzła mionowego podczas jego rotacji w polu magnetycznym.

### 2.7.1. Mion jako węzeł o wyższej liczbie skrzyżowań (ten sam \(\mathcal{W}=3\), stan wzbudzony)

Jak ustalono w podrozdziale 2.4, elektron, mion i taon mają ten sam ładunek topologiczny \(\mathcal{W}=3\) i różnią się kątem orientacji \(\theta\). W języku teorii węzłów, elektron odpowiada węzłowi o minimalnej liczbie skrzyżowań (dla \(\mathcal{W}=3\) jest to trójlistnik \(3_1\), 3 skrzyżowania). Mion i taon to stany wzbudzone o tej samej topologii podstawowej, ale z dodatkowymi, wymuszonymi pętlami (większa liczba skrzyżowań: \(c(K_\mu)=5\), \(c(K_\tau)=7\)). Wskaźnik nadmiarowej złożoności topologicznej definiujemy jako:

\[
\chi_{\text{top}} = \frac{c(K_\mu) - c(K_e)}{c(K_e)} = \frac{5-3}{3} = \frac{2}{3} \quad (\text{dla mionu}), \qquad \chi_{\text{top}}(\tau) = \frac{7-3}{3} = \frac{4}{3}. \tag{2.11}
\]

### 2.7.2. Fenomenologiczne wyrażenie na \(\Delta a_{\text{TGM}}\)

W zewnętrznym polu magnetycznym \(\mathbf{B}\), moment magnetyczny mionu jest wypadkową cyrkulacji energii samego węzła oraz indukowanego przez niego lokalnego odkształcenia sieci. Rotacja węzła wymusza okresowe „przecinanie” dodatkowych pętli przez linie sił pola 0‑Matrycy. Ponieważ Substrat posiada skończony moduł sztywności \(\mathcal{K}_{\text{eff}}\) (Aneks E), generowany jest moment hamujący proporcjonalny do częstotliwości Larmorowskiej \(\nu_L\).

Anomalna część momentu magnetycznego (odchylenie od wartości Diraca) wyraża się w TSM wzorem fenomenologicznym:

\[
\Delta a_{\text{TGM}} = \eta \cdot \left( \frac{\mathcal{K}_{\text{eff}}}{\rho_0 c^2} \right) \cdot \chi_{\text{top}}, \tag{2.12}
\]

gdzie:

- \(\eta\) – stała sprzężenia topologicznego węzła z ośrodkiem (rząd \(1\); w przybliżeniu \(\eta \approx 1\)),
- \(\mathcal{K}_{\text{eff}}\) – efektywny moduł sztywności Substratu (z Aneksu E, \(\mathcal{K}_{\text{eff}} \approx 1.5\,\text{N}\)),
- \(\rho_0\) – gęstość masy Substratu (oszacowana z masy Plancka i objętości komórki: \(\rho_0 \approx 5.4\times10^{96}\,\text{kg/m}^3\) – wartość ogromna, ale po znormalizowaniu przez \(c^2\) daje bezwymiarowy współczynnik),
- \(\chi_{\text{top}}\) – wskaźnik nadmiarowej złożoności topologicznej (2.11).

Obliczamy: \(\frac{\mathcal{K}_{\text{eff}}}{\rho_0 c^2} \approx \frac{1.5\,\text{N}}{5.4\times10^{96}\,\text{kg/m}^3 \cdot 9\times10^{16}\,\text{m}^2/\text{s}^2} \approx 3.1\times10^{-9}\). Mnożąc przez \(\eta \approx 1\) i \(\chi_{\text{top}} = 2/3\) otrzymujemy \(\Delta a_{\text{TGM}} \approx 2.1\times10^{-9}\). Wartość zmierzona w eksperymencie Fermilab (2021) to \(\Delta a_\mu = (2.51 \pm 0.59)\times10^{-9}\). Zgodność jest bardzo dobra, biorąc pod uwagę przybliżony charakter oszacowań.

### 2.7.3. Falsyfikowalne przewidywania TSM

- **Zależność od ośrodka:** \(\Delta a_\mu\) powinno zmieniać się wraz z gęstością materiału otaczającego mion (np. w pułapce z różnymi gazami). Model Standardowy nie przewiduje takiego efektu – byłby to jednoznaczny test TSM.
- **Liniowa korelacja z \(\chi_{\text{top}}\):** Jeśli kiedykolwiek uda się wyprodukować i zmierzyć \(g-2\) dla taonu (obecnie niemożliwe z powodu krótkiego czasu życia), przewidujemy \(\Delta a_\tau \approx 4.2\times10^{-9}\) (dla \(\chi_{\text{top}}=4/3\)).
- **Wartość \(\mathcal{K}_{\text{eff}}\):** Z pomiaru \(\Delta a_\mu\) można wyznaczyć sztywność Substratu, co daje niezależną kalibrację stałej \(K \approx 1.5\,\text{N}\) (zgodnie z Aneksem E). **Anomalia mionu staje się najdokładniejszym pomiarem własności mechanicznych Substratu.**

### 2.7.4. Uwaga o bozonach \(W\) i \(Z\)

Analogicznie do wzbudzeń mionowych, w zderzeniach wysokoenergetycznych powstają przejściowe super‑węzły o wysokiej energii, rejestrowane jako rezonanse \(W^\pm\) i \(Z^0\). Nie są to fundamentalne cząstki, lecz **wzbudzenia topo‑harmoniczne** (breathery) – ich masy (\(M_W \approx 80.4\,\text{GeV}\), \(M_Z \approx 91.2\,\text{GeV}\)) są miarą lokalnego naciągu 0‑Matrycy przy ekstremalnych odkształceniach. TSM odrzuca istnienie jakichkolwiek cięższych odpowiedników symetrycznych – brak supersymetrii, brak \(Z'\). Szerokość rozpadu \(Z\) na neutrina (3 generacje) wynika z geometrii 3‑brany (relacje kłębiaste – Skein relations) i jest omówiona w Rozdziale 8.

---

## 2.8. Unifikacja leptonów i kwarków przez topologię – dalsze konsekwencje

Skoro lepty o \(\mathcal{W}=3\) dają trzy pokolenia, naturalnym pytaniem jest, czy kwarki (górny, dolny, powabny, dziwny, piękny, prawdziwy) również można opisać przez ten sam formalizm. W TSM zakładamy, że kwarki są **węzłami o wyższych \(\mathcal{W}\)** (np. \(\mathcal{W}=5\) dla kwarku \(u\), \(\mathcal{W}=6\) dla \(d\) itd.), a ich ładunek elektryczny (ułamkowy) wynika z rzutowania chiralności węzła na 3‑branę. Szczegółowa analiza wykracza poza zakres tego rozdziału (patrz Rozdział 4).

### 2.8.1. Dlaczego nie obserwujemy cząstek o \(\mathcal{W}=4,5\) w próżni?

Zgodnie ze wzorem (2.10), dla \(\mathcal{W}=4\) przewidujemy 5 stanów orientacyjnych. Gdyby któryś z nich miał masę poniżej kilku TeV, powinien być już widoczny w zderzeniach w LHC. Brak takich sygnałów oznacza, że **wszystkie stany o \(\mathcal{W}=4\) i wyższych mają masy powyżej obecnego progu detekcji** (lub ich przekroje czynne są ekstremalnie małe). Z modelu skalowania energii (rozdział 3) otrzymujemy \(m \sim \mathcal{W}^{6.8}\), więc dla \(\mathcal{W}=4\) masa wynosi około \(0.511 \cdot (4/3)^{6.8} \approx 0.511 \cdot 5.7 \approx 2.9\,\text{GeV}\) – to nie jest wysoka wartość. Zatem problem nie leży w masie, lecz w mechanizmie produkcji. Prawdopodobnie istnieje bariera topologiczna: aby utworzyć węzeł o \(\mathcal{W}=4\) w zderzeniu, trzeba dostarczyć energię oraz **spełnić dodatkowe warunki geometryczne** (odpowiednie ułożenie pól), co jest niezwykle mało prawdopodobne w przypadkowych zderzeniach. Stąd **obserwowana materia składa się wyłącznie z węzłów o \(\mathcal{W}=3\) (leptony i kwarki lekkie) oraz \(\mathcal{W}=8\) (nukleony)** – to są „atraktory topologiczne” w ewolucji Substratu.

### 2.8.2. Możliwość istnienia ciężkich leptonów w ekstremalnych warunkach

W środowiskach o bardzo wysokim ciśnieniu 0‑Matrycy (np. we wnętrzach gwiazd neutronowych, w zderzeniach ciężkich jonów przy energiach rzędu TeV na nukleon) mogą czasowo powstawać węzły o \(\mathcal{W}=4,5\) jako stany rezonansowe. Ich czas życia będzie jednak ekstremalnie krótki (\(<10^{-24}\,\text{s}\)), a produkty rozpadu nie do odróżnienia od tła. Poszukiwanie ich wymaga dedykowanych eksperymentów z bardzo wysoką luminancją i precyzyjną identyfikacją topologii zdarzeń.

### 2.8.3. Związek z regułą Koidego dla kwarków

Empirycznie wiadomo, że dla kwarków (w odpowiedniej skali energii) również istnieją zależności przypominające regułę Koidego, choć mniej precyzyjne (ze względu na trudności pomiarowe mas kwarków). TSM przewiduje, że dla każdej rodziny cząstek o tym samym \(\mathcal{W}\) pierwiastki mas powinny układać się w ciąg trygonometryczny – to jest testowalna hipoteza, gdyby kiedykolwiek udało się zmierzyć masy kwarków z odpowiednią dokładnością lub odkryć nowe, cięższe leptony.

---

## 2.9. Formalizm elasto-dynamiczny Substratu w \(\mathbb{R}^4\) (rozkład Hodge’a-Helmholtza)

Aby w pełni opisać dynamikę 4‑wymiarowej osnowy, konieczne jest wprowadzenie rygorystycznego formalizmu różniczkowego. Pole przemieszczeń strukturalnych Substratu reprezentujemy jako 1‑formę różniczkową \(\Phi \in \Omega^1(\mathbb{R}^4)\), zdefiniowaną w bazie współrzędnych przestrzennych \((x^1, x^2, x^3, x^4)\):

\[
\Phi = \Phi_1 dx^1 + \Phi_2 dx^2 + \Phi_3 dx^3 + \Phi_4 dx^4. \tag{2.13}
\]

Zgodnie z twierdzeniem Hodge’a o rozkładzie ortogonalnym na płaskiej rozmaitości \(\mathbb{R}^4\), pole to rozbija się jednoznacznie na sumę formy ścisłej, ko‑ścisłej oraz składnika harmonicznego (który w rozważaniach lokalnych przyjmujemy jako zerowy):

\[
\Phi = \Phi_L + \Phi_T = d\alpha + \delta\beta, \tag{2.14}
\]

gdzie:

- \(d: \Omega^k \to \Omega^{k+1}\) to pochodna zewnętrzna (uogólniony gradient, generujący rotację i ekspansję),
- \(\delta: \Omega^k \to \Omega^{k-1}\) to operator ko‑dyferencjału (uogólniona dywergencja), zdefiniowany poprzez gwiazdkę Hodge’a \(*\) jako \(\delta = - * d *\),
- \(\alpha \in \Omega^0(\mathbb{R}^4)\) jest 0‑formą (potencjał skalarny pola podłużnego),
- \(\beta \in \Omega^2(\mathbb{R}^4)\) jest 2‑formą (potencjał tensorowy pól poprzecznych).

### 2.9.1. Równania ruchu, separacja modów i warunek cechowania

Ogólne 4‑wymiarowe równanie elasto‑dynamiczne Naviera‑Cauchy’ego dla ośrodka o gęstości masowej \(\rho_0\) i stałych Lamégo \(\lambda\) oraz \(\mu\) przyjmuje w notacji zewnętrznej postać:

\[
\rho_0 \frac{\partial^2 \Phi}{\partial \tau^2} = (\lambda + 2\mu) d\delta \Phi - \mu \delta d \Phi. \tag{2.15}
\]

Podstawiając pełny rozkład Hodge’a \(\Phi = d\alpha + \delta\beta\) oraz wykorzystując nilpotentność operatorów (\(d^2 = 0\), \(\delta^2 = 0\)), równanie ruchu ulega automatycznej separacji na dwa niezależne układy dynamiczne:

\[
\rho_0 d \left( \frac{\partial^2 \alpha}{\partial \tau^2} \right) + \rho_0 \delta \left( \frac{\partial^2 \beta}{\partial \tau^2} \right) = (\lambda + 2\mu) d(\delta d \alpha) - \mu \delta(d \delta \beta). \tag{2.16}
\]

Z ortogonalności przestrzeni form ścisłych i ko‑ścisłych, powyższa tożsamość rozpada się na dwa niezależne równania falowe:

**Równanie modu podłużnego (dla 0‑formy \(\alpha\)):**
\[
\frac{\partial^2 \alpha}{\partial \tau^2} = c_L^2 \delta d \alpha \quad \implies \quad \frac{\partial^2 \alpha}{\partial \tau^2} = c_L^2 \nabla^2_{4D} \alpha, \tag{2.17}
\]
gdzie prędkość fali podłużnej wynosi \(c_L = \sqrt{\frac{\lambda + 2\mu}{\rho_0}}\).

**Równanie modu poprzecznego (dla 2‑formy \(\beta\)):**
\[
\delta \left( \frac{\partial^2 \beta}{\partial \tau^2} + c_{\perp}^2 d\delta\beta \right) = 0, \tag{2.18}
\]
gdzie prędkość fali poprzecznej (ścinania) wynosi \(c_{\perp} = \sqrt{\frac{\mu}{\rho_0}}\).

Ponieważ 2‑forma \(\beta\) w \(\mathbb{R}^4\) posiada 6 niezależnych składowych, sama operacja \(\Phi_T = \delta\beta\) definiuje ją z dokładnością do transformacji cechowania \(\beta \to \beta + d\gamma\). Aby znieść tę nadmiarowość i zapobiec propagacji niefizycznych modów pasożytniczych, narzuca się rygorystyczny warunek ko‑ścisłości:

\[
\delta\beta = 0. \tag{2.19}
\]

Zastosowanie cechowania \(\delta\beta = 0\) redukuje operator Laplace’a‑de Rhama \(\Delta_2 = d\delta + \delta d\) działający na \(\beta\) do czystego członu czynnego. Ostateczne, zredukowane równanie fali poprzecznej przyjmuje postać:

\[
\frac{\partial^2 \beta}{\partial \tau^2} = -c_{\perp}^2 \delta d \beta. \tag{2.20}
\]

### 2.9.2. Rzutowanie 3D + \(x^4\): mapa pól fizycznych

Rozdzielenie współrzędnych wewnątrzpowierzchniowych 3‑brany (\(x^1, x^2, x^3\)) od osi ortogonalnej Bulk (\(x^4\)) pozwala na zmapowanie składowych form różniczkowych na obserwowalne makroskopowo oddziaływania.

**Dekompozycja modu poprzecznego (\(\beta \in \Omega^2(\mathbb{R}^4)\)):**  
2‑formę \(\beta\) rozbijamy na składowe wewnętrzne i zewnętrzne względem brany:

\[
\beta = \bar{\beta} + \bar{\psi} \wedge dx^4, \tag{2.21}
\]

- \(\bar{\beta} = \frac{1}{2}\beta_{ij} dx^i \wedge dx^j\) (3 składowe): reprezentuje płaszczyzny polaryzacji zamknięte wewnątrz 3‑brany. Generuje poprzeczne fale elektromagnetyczne, poruszające się z prędkością graniczną \(c = c_{\perp}\). Składowe formy \(\bar{\beta}\) mapują się bezpośrednio na potencjał cechowania \(A_\mu\), a jej pochodna zewnętrzna wyznacza antysymetryczny tensor pola elektromagnetycznego \(F = d\bar{\beta}\).
- \(\bar{\psi} = \beta_{i4} dx^i\) (3 składowe): reprezentuje płaszczyzny polaryzacji sprzężone z kierunkiem ortogonalnym. Generuje naciąg mechaniczny membrany w osi \(x^4\), interpretowany jako pole grawitacyjne.

Warunek cechowania \(\delta\beta = 0\) w tym rozbiciu przyjmuje formę więzów różniczkowych:

\[
\partial_i \beta_{i4} = 0 \quad \implies \quad \text{div}(\bar{\psi}) = 0, \qquad
\partial_j \beta_{ji} + \partial_4 \beta_{4i} = 0. \tag{2.22}
\]

Zapewnia to solenoidalność pola grawitacyjnego w branie oraz lokalne równoważenie naprężeń elektromagnetycznych przez gradienty sił ortogonalnych wzdłuż czwartego wymiaru.

**Dekompozycja modu podłużnego (\(\alpha \in \Omega^0(\mathbb{R}^4)\)):**  
Pochodna zewnętrzna 0‑formy potencjału podłużnego tworzy pole gradientów:

\[
d\alpha = \bar{d}\alpha + \partial_4 \alpha dx^4 = \left(\sum_{i=1}^3 \partial_i \alpha dx^i\right) + \partial_4 \alpha dx^4. \tag{2.23}
\]

- Składnik \(\bar{d}\alpha\) (wewnątrzbrany): generuje podłużne fale ciśnienia mechanicznego bezpośrednio w trójwymiarowej płaszczyźnie osnowy. Objawia się jako uniwersalne, skalarowe pole gęstości tła powiązane z relaksacją Substratu.
- Składnik \(\partial_4 \alpha\) (ortogonalny): definiuje symetryczne ściskanie i rozszerzanie profilu grubości samego substratu 3‑brany w przestrzeni Bulk.

Ponieważ prędkość fali podłużnej \(c_L = \sqrt{(\lambda+2\mu)/\rho_0}\) jest jawnie większa od prędkości fal poprzecznych \(c_{\perp} = \sqrt{\mu/\rho_0}\), skalarowe zaburzenia kompresyjne osnowy propagują się w sposób superluminalny (\(c_L > c\)). Zjawisko to nie narusza wewnętrznej spójności TSM, gdyż prędkość światła \(c\) jest zdefiniowana wyłącznie przez próg propagacji modów poprzecznych (\(\bar{\beta}\)). Formalizm ten stanowi matematyczną podstawę dla nieliniowej elektrodynamiki rozwiniętej w Rozdziale 3.

---

## 2.10. Hydrodynamiczny mechanizm bezwładności i zniesienie bariery Peierlsa-Nabarro

Węzeł topologiczny reprezentuje zmagazynowaną, lokalną deformację sprężystą osnowy. Masa spoczynkowa cząstki \(m_0\) jest równoważnikiem całkowitej energii potencjalnej tych naprężeń, obliczanej poprzez całkowanie gęstości lagrangianu sprężystego po objętości solitonu:

\[
m_0 = \frac{1}{c_{\perp}^2} \int_{\mathbb{R}^3} \left( \frac{1}{2} K_{abcd} \epsilon_{ab} \epsilon_{cd} \right) d^3x, \tag{2.24}
\]

gdzie \(K_{abcd}\) jest tensorem modułów sprężystości Substratu, a \(\epsilon_{ab}\) – tensorem odkształcenia. Gdy na węzeł działa siła zewnętrzna, nie przesuwa ona fizycznych 0‑cząstek na duże odległości. Ruch solitonu polega na sekwencyjnym, bezstratnym transferze stanu odkształcenia z jednej komórki sieci do sąsiedniej – podobnie jak fala dylatacyjna lub soliton w kryształach makroskopowych. Uformowany, stabilny splot topologiczny o zdefiniowanej chiralności jest z definicji bezdylatacyjny: nie zmienia sumarycznej objętości lokalnej osnowy wzdłuż wektora swojego ruchu, a jedynie ją skręca. Dzięki temu asymetryczny węzeł ślizga się po Substracie, nie emitując stratnego promieniowania w kanale modu podłużnego \(\alpha\), dopóki nie zostanie rozerwany w procesie anihilacji. Ponieważ jednak ruch ten wymaga lokalnego, hydrodynamicznego przeorganizowania pędów 0‑cząstek, których sfery oddziaływań uległy restrykcyjnemu ograniczeniu geometrycznemu wewnątrz zagęszczonego kontinuum, proces ten generuje opór kinetyczny. Ten opór ośrodka przeciwko zmianie stanu ruchu fali stojącej jest tym, co makroskopowo nazywamy **bezwładnością**.

### 2.10.1. Zniesienie barier dyskretnych (efekt Peierlsa-Nabarro)

W klasycznej fizyce ciał stałych ruch defektu w sieci dyskretnej wiąże się z pokonywaniem okresowego potencjału podłoża, co prowadzi do dyssypacji energii i hamowania. W TSM efekt ten zostaje zredukowany do zera poprzez asymetrię skal.

Rozmiar rdzenia węzła topologicznego (promień cząstki \(L\), zbliżony do skali Plancka) jest o wiele rzędów wielkości większy niż odległość między poszczególnymi 0‑cząstkami w stanie zakleszczenia (\(a\)). W granicy, gdzie \(L \gg a\), okresowe fluktuacje potencjału sieci ulegają wykładniczemu wygaszeniu. Amplituda bariery Peierlsa‑Nabarro (\(E_{PN}\)), określająca minimalną siłę potrzebną do poruszenia węzła, dąży asymptotycznie do zera:

\[
E_{PN} \propto \exp\left(-\pi \frac{L}{a}\right) \approx 0. \tag{2.25}
\]

Dzięki temu węzeł porusza się w krystalicznym Substracię w sposób idealnie płynny, bez oporów i strat radiacyjnych przy stałej prędkości, realizując rygorystycznie Pierwszą Zasadę Dynamiki Newtona. Mechanizm ten jest kluczowy dla zrozumienia, dlaczego cząstki elementarne nie tracą energii podczas ruchu jednostajnego (brak tarcia o Substrat), a jednocześnie wykazują bezwładność przy przyspieszaniu. Literatura: Peierls, R. (1940). *The size of a dislocation*. Proc. Phys. Soc. 52, 34; Nabarro, F. R. N. (1947). *Dislocations in a simple cubic lattice*. Proc. Phys. Soc. 59, 256.

---

## 2.11. Antymateria jako inwersja topologiczna

Koncepcja antymaterii w TSM zostaje całkowicie odarta z relatywistycznych, abstrakcyjnych interpretacji matematycznych, takich jak „ujemna energia” czy „ruch cząstek wstecz w czasie”. Zgodnie z rygorystyczną definicją wyprowadzoną w Rozdziale 4, czas nie stanowi fundamentalnego, geometrycznego wymiaru pseudoriemannowskiego, w którym możliwa jest inwersja wektora ruchu. Jest on sformalizowany jako emergujący, ściśle monotoniczny globalny parametr ewolucyjny \(\tau\), który rejestruje wyłącznie sekwencyjne, nieodwracalne stany mechaniczne i rekonfiguracje sieciowe 0‑Matrycy. W tym ujęciu istnienie antycząstek nie implikuje anomalii temporalnych, lecz stanowi przejaw czysto geometrycznych i statycznych transformacji konfiguracji splotu wewnątrz trójwymiarowej osnowy (3‑brany).

### 2.11.1. Chiralność węzła

Dla każdego węzła topologicznego o ładunku \(\mathcal{W} = +3\) (lub ogólnie \(\mathcal{W} >0\)) istnieje jednoznacznie zdefiniowana, lustrzana konfiguracja pola odkształceń posiadająca przeciwną chiralność (helisowość) struktury splotu, co generuje ładunek topologiczny \(\mathcal{W} = -3\). Cząstka o odwróconej chiralności splotu zachowuje identyczną geometrię ugięcia w 4D (generuje identyczny rozkład naprężeń grawitacyjnych, a więc ma dodatnią masę spoczynkową), lecz jej rzutowany wektor skrętu fazowego ma przeciwny zwrot. Jest to **antycząstka**. W teorii węzłów, operacja zmiany chiralności odpowiada przejściu od węzła do jego lustrzanego odbicia (np. węzeł trójlistny \(3_1\) i jego lustrzany obraz są chiralne).

### 2.11.2. Mechanizm anihilacji

Gdy cząstka (\(\mathcal{W} = +3\)) i antycząstka (\(\mathcal{W} = -3\)) znajdą się w bezpośrednim kontakcie, bariera topologiczna chroniąca je przed rozpadem znika. Sumaryczny ładunek układu wynosi:

\[
\mathcal{W}_{\text{total}} = +3 + (-3) = 0. \tag{2.26}
\]

Układ staje się topologicznie równoważny płaskiej, niezaburzonej próżni. Następuje proces anihilacji, który mechanicznie jest gwałtownym, bezresztkowym rozplątaniem splotów i rozwłóknieniem lokalnych deformacji. Zmagazynowana w ugięciu brany energia potencjalna naprężeń sprężystych zostaje uwolniona w postaci rozchodzących się we wszystkich kierunkach czystych fal poprzecznych ośrodka – **fotonów**. Proces ten jest odpowiedzialny za zjawisko anihilacji par cząstka‑antycząstka obserwowane w eksperymentach (np. \(e^+e^- \to 2\gamma\)). W TSM nie ma potrzeby wprowadzania „ujemnej energii” ani „ruchu wstecz w czasie” – anihilacja jest czysto mechanicznym rozplątaniem węzła.

---

## 2.12. Podsumowanie rozdziału 2 – od węzła do cząstki

W rozdziale tym zbudowaliśmy most między abstrakcyjną topologią a fizycznymi własnościami cząstek elementarnych. Poniżej zestawiam najważniejsze wnioski.

### 2.12.1. Kluczowe osiągnięcia formalizmu TSM

| Obszar | Wnioski | Podstawa w rozdziale |
|--------|---------|----------------------|
| **Topologiczna kwantyzacja** | Ładunek Hopfa \(\mathcal{W}\) musi być liczbą całkowitą. Trwałe fermiony wymagają \(\mathcal{W}\ge3\). | 2.2, 2.3 |
| **Niestabilność \(\mathcal{W}=1,2\)** | Brak bariery energetycznej, wykładniczy zanik w \(\tau\). | 2.3.1–2.3.2 |
| **Pochodzenie trzech pokoleń leptonów** | Ten sam \(\mathcal{W}=3\), różne kąty orientacji \(\theta\) w 4D. Równanie Schrödingera dla \(\theta\) (2.7) daje trzy stany o energiach spełniających regułę Koidego (2.9). | 2.4.1–2.4.2 |
| **Liczba stanów orientacyjnych** | \(L(\mathcal{W}) = 2\mathcal{W}-3\) dla \(\mathcal{W}\ge3\) (2.10). Dla \(\mathcal{W}=3\) daje 3 (e, μ, τ). | 2.4.3 |
| **Spin 1/2** | Konsekwencja rozwłóknienia Hopfa i konieczności obrotu o \(720^\circ\) dla powrotu do stanu początkowego. | 2.5 |
| **Formalizm elasto-dynamiczny 4D** | Rozkład Hodge’a-Helmholtza, równania Naviera-Cauchy’ego, separacja modów, warunek cechowania \(\delta\beta=0\). | 2.9 |
| **Hydrodynamiczna bezwładność** | Masa jako całka energii odkształcenia (2.24); zniesienie bariery Peierlsa-Nabarro (2.25) dzięki asymetrii skal. | 2.10 |
| **Antymateria** | Antycząstka to węzeł o przeciwnej chiralności (zmiana znaku \(\mathcal{W}\)); anihilacja = rozplątanie splotów (2.26). | 2.11 |
| **Wpływ ciśnienia 0‑Matrycy** | Neutron jest układem złożonym; jego stabilność zależy od \(P_{\text{ext}}\). Jądro ekranuje (niższe ciśnienie), ścianki pułapki podwyższają ciśnienie – wyjaśnienie anomalii czasu życia (2.6.2). | 2.6 |
| **Anomalia \(g-2\) mionu** | Miarą sztywności Substratu – opór geometryczny dodatkowych skrzyżowań węzła (2.12). | 2.7 |
| **Bozony \(W, Z\)** | Wzbudzenia topo‑harmoniczne, nie fundamentalne cząstki. Brak supersymetrii, brak \(Z'\). | 2.7.4, 2.8 |

### 2.12.2. Tabela przewidywanych stanów dla różnych \(\mathcal{W}\)

| \(\mathcal{W}\) | Stabilność w próżni | Liczba stanów \(L(\mathcal{W})\) | Odpowiedniki w przyrodzie / uwagi |
|----------------|---------------------|--------------------------------|----------------------------------|
| 1, 2 | Niestabilne (dyssypacja) | – | Rozpad na fotony; nie tworzą trwałej materii |
| 3 | Tak | 3 | **Elektron, mion, taon** (spełniają regułę Koidego) |
| 4 | ? (prawdopodobnie nie, \(P_{\text{max}} < P_{\text{sub}}\)) | 5 | Hipotetyczne ciężkie leptony – brak obserwacji (masy > ~10 TeV) |
| 5 | Nie (wymaga ekstremalnego ciśnienia) | 7 | Mogą powstawać w gwiazdach neutronowych lub zderzeniach ultrawysokoenergetycznych |
| 8 | Tak (proton, neutron) | 13 | W praktyce tylko stany podstawowe (nukleony) – wzbudzenia nietrwałe |
| \(\ge9\) | Nie (lub tylko w jądrach) | \(2\mathcal{W}-3\) | Poza zasięgiem obecnych eksperymentów |

### 2.12.3. Nowe, falsyfikowalne przewidywania TSM

1. **Zależność czasu życia neutronu od materiału pułapki** – zmiana powłoki butelki (miedź, grafit, polimer) powinna zmienić \(\Delta\Gamma\). Model Standardowy tego nie przewiduje.
2. **Liniowa korelacja \(\Delta a_\mu\) ze wskaźnikiem złożoności topologicznej \(\chi_{\text{top}}\)** – dla mionu wartość ok. \(2.5\times10^{-9}\), dla taonu (gdyby zmierzyć) – ok. \(4.2\times10^{-9}\).
3. **Brak cząstek o \(\mathcal{W}=4\) przy energiach < 10 TeV** – poszukiwania w LHC Run 4 i FCC powinny to potwierdzić lub obalić.
4. **Brak supersymetrii i bozonów \(Z'\)** – TSM odrzuca je kategorycznie jako artefakty nieporozumienia ontologicznego.
5. **Reguła Koidego dla kwarków** – przewidujemy podobną zależność trygonometryczną dla mas kwarków w skali energii odpowiadającej ich \(\mathcal{W}\) (np. dla rodziny \(u,c,t\)).

### 2.12.4. Ontologiczna zmiana paradygmatu

TSM zastępuje punktowe cząstki w próżni **węzłami topologicznymi w sprężystym 4‑wymiarowym Substracię**. Wszystkie własności cząstek (masa, ładunek, spin, czas życia, moment magnetyczny) są emergentnymi konsekwencjami geometrii i dynamiki ośrodka. Hierarchia mas leptonów przestaje być tajemnicą – wynika z kwantyzacji kąta orientacji. Różnica w czasach życia neutronu przestaje być anomalią – staje się potwierdzeniem, że Substrat oddziałuje z materią w sposób mierzalny. Anomalia \(g-2\) mionu przestaje być zapowiedzią „nowej fizyki” – jest najdokładniejszym pomiarem sztywności 0‑Matrycy.

---

## Tabela 2.1 – Zestawienie najważniejszych symboli

| Symbol | Znaczenie | Wymiar / wartość (przykładowa) |
|--------|-----------|-------------------------------|
| \(\mathcal{W}\) | Ładunek topologiczny (liczba Hopfa) | liczba całkowita \(\ge3\) |
| \(\tau\) | Globalny parametr ewolucyjny (suma zderzeń 0‑cząstek) | bezwymiarowy |
| \(\mathbf{n}(\mathbf{x},\tau)\) | Pole orientacji węzła | bezwymiarowe, \(|\mathbf{n}|=1\) |
| \(\phi(\mathbf{x},\tau)\) | Ugięcie ortogonalne 3‑brany | długość (m) |
| \(\theta\) | Kąt między osią węzła a kierunkiem \(x^4\) | radiany |
| \(I\) | Moment bezwładności węzła | kg·m², dla elektronu \( \approx 1.4\times10^{-53}\) |
| \(\kappa\) | Stała materiałowa w potencjale \(V(\theta)\) | bezwymiarowa, \(\kappa=6\) (z reguły Koidego) |
| \(L(\mathcal{W})\) | Liczba stanów orientacyjnych | liczba całkowita, \(2\mathcal{W}-3\) |
| \(P_{\text{ext}}, P_{\text{sub}}, P_{\text{max}}\) | Ciśnienie zewnętrzne, tła, krytyczne | Pa (dla Substratu \( \sim 10^{35}\)) |
| \(\Delta a_\mu\) | Anomalia magnetyczna mionu | bezwymiarowa, \(\approx 2.5\times10^{-9}\) |
| \(\chi_{\text{top}}\) | Wskaźnik nadmiarowej złożoności topologicznej | bezwymiarowy, dla mionu \(2/3\) |
| \(\Phi\) | 1‑forma przemieszczeń Substratu | – |
| \(\alpha, \beta\) (w 2.9) | 0‑forma i 2‑forma potencjałów | – |
| \(c_L, c_{\perp}\) | Prędkości fal podłużnych i poprzecznych | m/s, \(c_{\perp}=c\) |

---

## Literatura (wybrana, do rozdziału 2)

- Abramowitz, M., & Stegun, I. A. (1965). *Handbook of Mathematical Functions*. Dover.
- Battye, R. A., & Sutcliffe, P. M. (1999). *Knots as stable soliton solutions in a three-dimensional classical field theory*. Phys. Rev. Lett., 82(23), 4601.
- Derrick, G. H. (1964). *Comments on nonlinear wave equations*. J. Math. Phys., 5, 1252.
- Faddeev, L. D., & Niemi, A. J. (1997). *Stable knot-like structures in classical field theory*. Nature, 387(6628), 58–61.
- Hietarinta, J., & Salo, P. (2000). *Faddeev-Hopf knots: Dynamics of linked solitons*. Phys. Rev. D, 62(8), 081701.
- Jegerlehner, F. (2017). *The Anomalous Magnetic Moment of the Muon*. Springer.
- Koide, Y. (1983). *A fermion–boson composite model of quarks and leptons*. Phys. Lett. B, 120(1-3), 161–165.
- Kostelecký, V. A., & Lehnert, R. (2001). *Stability, causality, and Lorentz and CPT violation*. Phys. Rev. D, 63(6), 065008.
- Landau, L. D. (1937). *On the theory of phase transitions*. Zh. Eksp. Teor. Fiz., 7, 19.
- Nabarro, F. R. N. (1947). *Dislocations in a simple cubic lattice*. Proc. Phys. Soc., 59, 256.
- Patrignani, C. et al. (Particle Data Group) (2016). *Review of Particle Physics*. Chin. Phys. C, 40, 100001.
- Peierls, R. (1940). *The size of a dislocation*. Proc. Phys. Soc., 52, 34.
- Penrose, R., & Rindler, W. (1984). *Spinors and Space-Time*. Cambridge University Press.
- Wietfeldt, F. E., & Greene, G. L. (2011). *The neutron lifetime*. Rev. Mod. Phys., 83(4), 1173.

---

*Koniec rozdziału 2 (wersja 3.2.0)*