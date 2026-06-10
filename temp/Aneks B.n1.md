## Aneks B (wersja 2.1) – Elasto‑dynamiczna zmiana prędkości światła w polu magnetycznym

W aneksie tym wyprowadzamy zależność prędkości światła od stałego pola magnetycznego $B$, wynikającą z nieliniowej odpowiedzi 0‑Matrycy na naprężenie torsyjne. Głównym celem jest ilościowe określenie stałej materiałowej $\kappa$, która moduluje przenikalność elektryczną jako $\epsilon_{\text{eff}} = \epsilon_0(1+\kappa B^2)$. W odróżnieniu od wcześniejszych prób, nie wyprowadzamy $\kappa$ z innych modułów sprężystości (np. z Aneksu E) – traktujemy ją jako niezależny parametr Substratu, zgodnie z postulatami Rozdziału 1.8. Jego dolną granicę wyznaczamy z warunku uwięzienia dwóch elektronów w skali femtometrowej, co prowadzi do wartości $\kappa \approx 10^{-30}\,\text{T}^{-2}$. Na tej podstawie obliczamy przewidywane przesunięcie fazowe w interferometrze Macha‑Zehndera oraz dyskutujemy (nie)wykonalność rezonansowego testu eksperymentalnego.

### B.1. Gęstość energii pola magnetycznego jako naprężenie torsyjne 0‑Matrycy

W modelu TSM pole magnetyczne $\mathbf{B}$ jest makroskopowym przejawem wirowości (skręcenia) 3‑brany. Gęstość energii tego odkształcenia, wyrażona w jednostkach elektrodynamiki, wynosi:

$$
u_B = \frac{B^2}{2\mu_0}, \tag{B.1.1}
$$

gdzie $\mu_0$ jest przenikalnością magnetyczną próżni – parametrem materiałowym Substratu w Stanie Zero. W obecności pola magnetycznego naprężenie torsyjne modyfikuje lokalne stałe sprężyste ośrodka. Dla izotropowego kontinuum, w najniższym rzędzie nieliniowości, przenikalność elektryczna $\epsilon$ ulega zmianie proporcjonalnej do $u_B$:

$$
\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \kappa B^2\right), \qquad \kappa = \frac{\alpha}{2\mu_0}, \tag{B.1.2}
$$

gdzie $\kappa$ jest stałą materiałową 0‑Matrycy (wymiar $\text{T}^{-2}$), a $\alpha$ – bezwymiarowym współczynnikiem nieliniowym. W poniższych rozważaniach pomijamy ewentualną zmianę $\mu$, ponieważ w omawianych zjawiskach dominuje efekt elektryczny (zgodnie z Rozdziałem 1.8).

---

### B.2. Prędkość światła w polu magnetycznym

Z definicji prędkości fazowej fali elektromagnetycznej w ośrodku o przenikalności $\epsilon_{\text{eff}}$ i stałej $\mu_0$:

$$
c_{\text{mag}} = \frac{1}{\sqrt{\epsilon_{\text{eff}} \mu_0}} = \frac{1}{\sqrt{\epsilon_0 (1+\kappa B^2) \mu_0}} = \frac{c_0}{\sqrt{1+\kappa B^2}}, \tag{B.2.1}
$$

gdzie $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ to prędkość światła w Stanie Zero (brak pola). Dla słabych pól ($\kappa B^2 \ll 1$) stosujemy rozwinięcie Taylora:

$$
c_{\text{mag}} = c_0 \left(1 - \frac{1}{2}\kappa B^2 + \frac{3}{8}\kappa^2 B^4 - \dots\right) \approx c_0 \left(1 - \frac{1}{2}\kappa B^2\right). \tag{B.2.2}
$$

---

### B.3. Wyznaczenie dolnej granicy $\kappa$ z warunku uwięzienia dwóch elektronów

W Rozdziale 3.5 postulowano, że oddziaływanie silne (uwięzienie nukleonów) jest skrajną nieliniową manifestacją elektromagnetyzmu, gdy człony $\propto \kappa \nabla(\mathbf{E}^2)\times\mathbf{B}$ stają się porównywalne z liniowym prawem Coulomba. Aby znaleźć wymaganą wartość $\kappa$, rozpatrujemy dwa elektrony (węzły topologiczne $\mathcal{W}=3$) w odległości $r = 1\,\text{fm}$ – skali, przy której efekty silne zaczynają dominować.

**Parametry:**
- Ładunek elektronu $e = 1{,}602\times10^{-19}\,\text{C}$.
- Moment magnetyczny elektronu $\mu_B = e\hbar/(2m_e) = 9{,}274\times10^{-24}\,\text{J/T}$.
- Pole elektryczne w odległości $r$: $E = \dfrac{e}{4\pi\epsilon_0 r^2}$.
- Pole magnetyczne od dipola (dla zgodnej orientacji spinów): $B \approx \dfrac{\mu_0}{4\pi} \dfrac{\mu_B}{r^3}$.

**Gęstości energii:**
- Liniowa energia Coulomba: $u_C = \frac{1}{2}\epsilon_0 E^2$.
- Nieliniowa energia sprzężenia: $u_{\text{nl}} \sim \epsilon_0 \kappa B^2 E^2$ (wynika z członu $\kappa B^2$ w $\epsilon_{\text{eff}}$).

Stosunek:

$$
\frac{u_{\text{nl}}}{u_C} \sim 2\kappa B^2. \tag{B.3.1}
$$

Podstawiając wartości liczbowe:

$$
B = 10^{-7} \cdot \frac{9{,}274\times10^{-24}}{(10^{-15})^3} = 10^{-7} \cdot 9{,}274\times10^{21} = 9{,}274\times10^{14}\,\text{T},
$$

$$
B^2 \approx 8{,}60\times10^{29}\,\text{T}^2.
$$

Stąd

$$
\frac{u_{\text{nl}}}{u_C} \sim 2\kappa \cdot 8{,}60\times10^{29} = 1{,}72\times10^{30}\,\kappa. \tag{B.3.2}
$$

Przyjmujemy, że uwięzienie (przejście w reżim silny) zachodzi, gdy $u_{\text{nl}}/u_C \gtrsim 1$. Otrzymujemy **dolną granicę**:

$$
\kappa_{\text{th}} \gtrsim 5{,}8\times10^{-31}\,\text{T}^{-2}. \tag{B.3.3}
$$

Dla bezpieczeństwa, uwzględniając czynniki geometryczne i niejednorodność pól, przyjmujemy:

$$
\boxed{\kappa \approx 10^{-30}\,\text{T}^{-2}}. \tag{B.3.4}
$$

Wartość ta jest zgodna z górną granicą eksperymentalną $\kappa \lesssim 10^{-6}\,\text{T}^{-2}$ (Rozdział 3.3) i pozwala na opis uwięzienia w skali fm. Jednocześnie dla pól rzędu 10 T mamy $\kappa B^2 \sim 10^{-28}$, co tłumaczy brak obserwowalnych statycznych efektów magneto‑optycznych.

---

### B.4. Związek z formalizmem Rozdziału 1.8

W Rozdziale 1.8 stała $\kappa$ została wprowadzona jako fundamentalny parametr materiałowy 0‑Matrycy, opisujący nieliniową modulację przenikalności elektrycznej przez pole magnetyczne:

$$
\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \kappa B^2 + \lambda \frac{\Phi}{c_\perp^2} + \dots\right), \tag{B.4.1}
$$

gdzie $\lambda$ odpowiada za sprzężenie grawitacyjne, a $c_\perp$ to prędkość fal poprzecznych. Powyższe oszacowanie $\kappa \approx 10^{-30}\,\text{T}^{-2}$ jest **pierwszym ilościowym przewidywaniem** tej stałej wynikającym z warunku stabilności materii (uwięzienia dwóch elektronów w skali femtometrowej). Jest ono zgodne z górną granicą eksperymentalną i pozwala zachować spójność między elektrodynamiką liniową (obserwowaną makroskopowo) a nieliniowym reżimem odpowiedzialnym za siły jądrowe.

**Uwaga:** Wartość $\kappa$ nie jest wyprowadzana z innych stałych Substratu (np. z modułu sztywności $\mathcal{K}$ z Aneksu E), ponieważ te dotyczą innych typów odkształceń (topologicznych). W ramach TSM dopuszcza się istnienie wielu niezależnych stałych materiałowych, analogicznie jak w klasycznej mechanice ośrodków ciągłych (moduł Younga, moduł ścinania, moduł sprężystości objętościowej – wszystkie niezależne).

---

### B.5. Opóźnienie fazowe w interferometrze Macha‑Zehndera

Dla ramienia interferometru o długości $L$ umieszczonego w stałym polu $B$, różnica czasu przejścia światła między ramieniem testowym a referencyjnym:

$$
\Delta t = \frac{L}{c_{\text{mag}}} - \frac{L}{c_0} \approx \frac{L}{c_0} \cdot \frac{1}{2}\kappa B^2, \tag{B.5.1}
$$

gdzie wykorzystano przybliżenie $(1-x)^{-1/2} \approx 1+x/2$ dla małych $x$. Odpowiadające przesunięcie fazowe dla fali o długości $\lambda$:

$$
\Delta \Phi = 2\pi \frac{c_0}{\lambda} \Delta t = \frac{\pi L}{\lambda} \kappa B^2. \tag{B.5.2}
$$

Dla $\kappa = 10^{-30}\,\text{T}^{-2}$, $L=1\,\text{m}$, $\lambda=500\,\text{nm}$, $B=10\,\text{T}$:

$$
\Delta \Phi \approx \frac{\pi \cdot 1}{5\times10^{-7}} \cdot 10^{-30} \cdot 100 \approx 6\times10^{-22}\,\text{rad}.
$$

Jest to wartość **niewykrywalna** przy obecnej technologii interferometrycznej. Dlatego **statyczny pomiar $\kappa$ jest niemożliwy** – co pozostaje w zgodzie z dotychczasowymi eksperymentami (PVLAS, BMV).

---

### B.6. Implikacje dla proponowanego testu rezonansowego (Rozdział 11.1)

W wariancie rezonansowym, w którym modulowane pole $\delta B(t)$ wzbudza drgania własne 0‑Matrycy, efektywna stała nieliniowa zostaje wzmocniona przez dobroć $Q$ układu: $\kappa_{\text{eff}} = \kappa Q$. Aby osiągnąć $\Delta\Phi \sim 1\,\text{rad}$ (poziom mierzalny), potrzebne $Q \sim \Delta\Phi_{\text{target}} / \Delta\Phi_{\text{stat}} \sim 1 / 10^{-21} = 10^{21}$. Nawet w najwyższych dobrociach wnęk nadprzewodzących ($Q \sim 10^{12}$) jest to poza zasięgiem. **Należy więc uznać, że zaproponowany w Rozdziale 11.1 eksperyment nie jest wykonalny** przy tym oszacowaniu $\kappa$. Alternatywnie, trzeba poszukiwać innego mechanizmu sprzężenia (np. bezpośredniego oddziaływania z modami spinowymi o znacznie większym $\kappa$, co wymagałoby rewizji wartości w górę).

---

### B.7. Podsumowanie Aneksu B (wersja 2.1)

1. **Stała nieliniowa $\kappa$** jest niezależnym parametrem materiałowym 0‑Matrycy, wprowadzonym w Rozdziale 1.8.
2. Z warunku uwięzienia dwóch elektronów (skala fm) wyznaczono $\kappa \approx 10^{-30}\,\text{T}^{-2}$.
3. Wartość ta jest zgodna z górną granicą eksperymentalną i tłumaczy brak statycznych efektów magneto‑optycznych.
4. Statyczny efekt jest niewykrywalny ($\Delta\Phi \sim 10^{-22}\,\text{rad}$ dla $B=10\,\text{T}$).
5. Rezonansowy test z Rozdziału 11.1 jest niewykonalny przy tym $\kappa$ – należy go odłożyć lub szukać silniejszego sprzężenia.
6. **Nie wprowadza się zbędnych modułów pośrednich** (np. $\mathcal{K}_{\text{spin}}$), ponieważ $\kappa$ jest parametrem pierwotnym.

---

*Koniec Aneksu B (wersja 2.1)*