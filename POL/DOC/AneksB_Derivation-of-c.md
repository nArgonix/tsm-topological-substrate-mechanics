<!-- ver:0.5.0 -->
# Aneks B: Rygorystyczne wyprowadzenie elasto-dynamicznej zmiany prędkości światła w polu magnetycznym

Poniższe wyprowadzenie stanowi matematyczny fundament dla **Aksjomatu 1.5** oraz priorytetowego testu rezonansowego opisanego w **Rozdziale 11.1**. Pokazuje ono, w jaki sposób wirowość (skręcenie) przestrzeni przekłada się na mierzalne opóźnienie fazowe fali poprzecznej.

**Krok 1. Gęstość energii pola magnetycznego jako naprężenie torsyjne Matrycy**

Zgodnie z ujęciem elektrodynamiki torsyjnej (Rozdział 4), pole magnetyczne $B$ nie jest bytem abstrakcyjnym, lecz fizyczną wirowością izotropowej 3-brany. W zrelaksowanej 0-Matrycy (Stanie Zero) generuje ono naprężenie ścinające o gęstości energii:

$$u_B = \frac{B^2}{2\mu_0}$$

Zgodnie z mechaniką nieliniową, naprężenie to modyfikuje poprzeczną przepustowość falową ośrodka (przenikalność elektryczną). W najprostszym, liniowym przybliżeniu dla małych odkształceń $u_B$:

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \alpha u_B\right) = \epsilon_0 \left(1 + \alpha \frac{B^2}{2\mu_0}\right)$$

Wygodniej jest wprowadzić uniwersalną stałą elastyczności skrętnej $\kappa$ o wymiarze $\text{T}^{-2}$:

$$\epsilon_{\text{eff}} = \epsilon_0 \left(1 + \kappa B^2\right), \quad \text{gdzie} \quad \kappa = \frac{\alpha}{2\mu_0}$$

**Krok 2. Prędkość światła w ośrodku o zmodyfikowanej przenikalności**

Z równań Maxwella (które w TGM są jedynie makroskopowym przybliżeniem dynamiki sprężystej kontinuum) prędkość fazowa fali ścinającej (elektromagnetycznej) wynosi:

$$c = \frac{1}{\sqrt{\epsilon \mu_0}}$$

Podstawiając nieliniowy człon $\epsilon_{\text{eff}}$ do tego równania, otrzymujemy lokalną prędkość światła w obszarze skręconym:

$$c_{\text{mag}} = \frac{1}{\sqrt{\epsilon_0 (1 + \kappa B^2) \mu_0}} = \frac{c_0}{\sqrt{1 + \kappa B^2}}$$

gdzie $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ to prędkość światła w idealnie zrelaksowanym Stanie Zero (brak pola).

**Krok 3. Rozwinięcie szeregu dla słabego pola ($\kappa B^2 \ll 1$)**

Ponieważ Matryca jest ośrodkiem o ekstremalnej sztywności, stała $\kappa$ jest bardzo mała. Stosujemy rozwinięcie w szereg Taylora postaci $(1+x)^{-1/2} = 1 - \frac{1}{2} x + \frac{3}{8} x^2 - \dots$
Dla parametru $x = \kappa B^2$:

$$c_{\text{mag}} = c_0 \left(1 - \frac{1}{2} \kappa B^2 + \frac{3}{8} \kappa^2 B^4 - \dots\right)$$

W praktyce eksperymentalnej, nawet przy potężnym polu rzędu $B = 10\text{ T}$ i zakładanej górnej granicy $\kappa \lesssim 10^{-6}\text{ T}^{-2}$, człon kwadratowy jest rzędu $10^{-12}$ i staje się całkowicie pomijalny. Równanie redukuje się do kluczowej, mierzalnej postaci:

$$\boxed{ c_{\text{mag}} \approx c_0 \left(1 - \frac{1}{2} \kappa B^2\right) }$$

**Krok 4. Opóźnienie fazowe w eksperymencie interferometrycznym**

W interferometrze Macha-Zehndera z ramieniem testowym o długości $L$ umieszczonym w stałym polu $B$, różnica czasu przejścia fotonów między ramieniem testowym a referencyjnym wynosi:

$$\Delta t = \frac{L}{c_{\text{mag}}} - \frac{L}{c_0} \approx \frac{L}{c_0} \cdot \frac{1}{2} \kappa B^2$$

Mechaniczne przesunięcie fazowe dla lasera o długości fali $\lambda$ to $\Delta \Phi = \frac{2\pi c_0}{\lambda} \Delta t$, co daje ostateczny wzór:

$$\Delta \Phi = \frac{\pi L}{\lambda} \kappa B^2$$

**Znaczenie i granice falsyfikacji:**
Zjawisko to jest bezpośrednio mierzalne. Gdybyśmy przyjęli przykładowe parametry: $L = 2\text{ m}$, $\lambda = 632\text{ nm}$, $\kappa = 10^{-6}\text{ T}^{-2}$ oraz pole z magnesu nadprzewodzącego $B = 10\text{ T}$, przesunięcie fazowe wyniosłoby:

$$\Delta \Phi \approx \frac{\pi \cdot 2}{632 \times 10^{-9}} \cdot 10^{-6} \cdot 100 \approx \frac{6{,}28}{6{,}32 \times 10^{-7}} \cdot 10^{-4} \approx 10^3\text{ rad}$$

Tak ogromne przesunięcie byłoby widoczne gołym okiem (tysiące prążków interferencyjnych). Ponieważ w dotychczasowych, klasycznych obserwacjach go nie wykryto, wartość empiryczna statycznego $\kappa$ musi być znacznie niższa ($\kappa \ll 10^{-6}\text{ T}^{-2}$).
To rygorystyczne ograniczenie matematyczne bezwzględnie uzasadnia konieczność zastosowania **wariantu rezonansowego** (opisanego w Rozdziale 11.1), w którym modulacja $\delta B(t)$ uderza we własną częstotliwość topo-harmoniczną Matrycy, sztucznie potęgując parametr do wartości efektywnej $\kappa_{\text{eff}} = \kappa Q$, omijając w ten sposób statyczną sztywność tła.

---