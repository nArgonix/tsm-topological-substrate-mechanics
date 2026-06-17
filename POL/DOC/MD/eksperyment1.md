### 8.X Laboratoryjne ograniczenia anizotropii Substratu w reżimie niskich pól

Astrofizyczna weryfikacja Mechaniki Substratu Topologicznego (TSM), oparta na profilach polaryzacyjnych magnetarów (takich jak 4U 0142+61), dostarcza silnych przesłanek numerycznych dla istnienia anizotropii ośrodka. Niemniej jednak, interpretacja danych z misji IXPE jest inherentnie obarczona niepewnościami modelowymi, wynikającymi ze skomplikowanej dynamiki zdegenerowanej plazmy elektronowo-jonowej w atmosferze gwiazdy neutronowej. Aby jednoznacznie odseparować geometryczną odpowiedź 0-Matrycy od efektów barionowych, konieczne jest skonfrontowanie formalizmu TSM z wynikami ziemskich eksperymentów fizyki silnych pól, realizowanych w warunkach kontrolowanej, ultrawysokiej próżni laboratoryjnej.

Kluczowym punktem odniesienia w reżimie niskich pól ($B \ll B_{\mathrm{QED}}$, gdzie $B_{\mathrm{QED}} \approx 4.4 \times 10^9\text{ T}$ oznacza pole Schwingera) są współczesne dane elipsometryczne. Spośród nich najbardziej rygorystyczne ograniczenia nakłada eksperyment PVLAS (Ferrara, Włochy), wykorzystujący polarymetr o wysokiej czułości z wnęką rezonansową Fabry-Perota o dobroci $\mathcal{F} \approx 10^5$. Najnowsze laboratoryjne pomiary magnetycznej dwułomności próżni (VMB) wyznaczyły różnicę współczynników załamania światła dla modów ortogonalnych na poziomie:

$$\Delta n_{\mathrm{exp}} = (12 \pm 17) \times 10^{-23} \quad \text{przy indukcji pola } B = 2.5\text{ T}$$

#### Mapowanie parametrów TSM na mierzalne wielkości laboratoryjne

W klasycznej elektrodynamice kwantowej (QED), w oparciu o efektywny Lagrangian Heisenberga-Eulera, różnica współczynników załamania $\Delta n$ dla fali próbnej w obecności zewnętrznego, statycznego pola magnetycznego $B$ jest ściśle zdeterminowana przez uniwersalne stałe fizyczne i skaluje się liniowo z gęstością energii pola:

$$\Delta n_{\mathrm{QED}} = 3 A_e B^2 = \frac{2\alpha_{\mathrm{fine}}^2}{45 \mu_0} \left( \frac{\hbar}{m_e c} \right)^3 \frac{B^2}{\mu_0}$$

Dla pola $B = 2.5\text{ T}$ teoretyczna wartość QED wynosi $\Delta n_{\mathrm{QED}} \approx 2.5 \times 10^{-23}$, co plasuje wynik eksperymentu PVLAS na granicy mierzalności (czynnik błędu ~5).

W formalizmie TSM makroskopowa dwułomność kontinuum nie wynika z polaryzacji wirtualnych par lepton-antylepton, lecz stanowi bezpośredni przejaw magneto-sprężystej anizotropii sieci sfer oscylacji 0-cząstek. Na obecnym etapie rozwoju teorii odpowiedź ta jest parametryzowana fenomenologicznie za pomocą dwóch zmiennych wolnych: różnicy podatności topologicznej układu węzłów $(\kappa_{\parallel} - \kappa_{\perp})$ oraz szerokości strefy dyssypacji energii rezonansowej $\Delta E$. W reżimie niskich pól i dla częstotliwości optycznych dalekich od punktu rezonansowego ($E_{\mathrm{laser}} \ll E_{\mathrm{res}}$), ogólne równanie falowe TSM redukuje się do formy asymptotycznej, gdzie $\Delta n$ zależy wprost od lokalnego odkształcenia postaciowego sieci:

$$\Delta n_{\mathrm{TSM}} \approx (\kappa_{\parallel} - \kappa_{\perp}) \cdot \frac{B^2}{2\mu_0} \cdot f\left(\frac{E_{\mathrm{laser}}}{\Delta E}\right)$$

Gdzie $f$ jest bezwymiarową funkcją odpowiedzi strukturalnej, która w warunkach laboratoryjnych (niska gęstość energii wzbudzenia) przyjmuje wartość bliską jedności.

#### Zestawienie i bilans parametrów: TSM vs. Model Standardowy

Konfrontacja obu podejść na płaszczyźnie metodologicznej obnaża odmienne rozłożenie złożoności parametrycznej w zależności od skali układu:

1. **Poziom fundamentalny (Próżnia):** QED wykazuje wyższą spójność teoretyczną w ujęciu Brzytwy Ockhama, wprowadzając 0 parametrów wolnych – efekt dwułomności jest zablokowany przez sztywne stałe ($m_e, e, \alpha_{\mathrm{fine}}$). TSM wprowadza na tym poziomie 2 parametry wolne [$(\kappa_{\parallel} - \kappa_{\perp})$ oraz $\Delta E$], które muszą być wyznaczane fenomenologicznie z dopasowań numerycznych.
2. **Poziom aplikacyjny (Astrofizyka):** Aby odtworzyć profil polaryzacji magnetaru, Model Standardowy (QED + Atmosfera) musi zostać rozbudowany o 7 do 10 parametrów *ad hoc* (skład chemiczny plazmy, wielopolowe skręcenia pola $B_{\mathrm{tor}}$, gradienty termiczne warstw optycznych). TSM osiąga zbieżność numeryczną przy użyciu zaledwie 5 parametrów całkowitych (w tym tylko 2 fizycznych parametrów ośrodka), drastycznie upraszczając globalny model układu.

Zestawienie numeryczne dla warunków laboratoryjnych ($B = 2.5\text{ T}$, próżnia) przedstawia się następująco:

| Model teoretyczny | Liczba parametrów wolnych w laboratorium | Przewidywana wartość $\Delta n$ ($2.5\text{ T}$) | Status weryfikacji eksperymentalnej (PVLAS) |
| --- | --- | --- | --- |
| **QED (Heisenberg-Euler)** | 0 (wartość sztywna) | $\approx 2.5 \times 10^{-23}$ | Zgodny w granicach błędu $1\sigma$ |
| **TSM (Krok B)** | 2 (wyznaczone z magnetarów) | $\le (\kappa_{\parallel} - \kappa_{\perp}) \cdot U_B$ | Zgodny (narzuca górne ograniczenie) |

#### Analiza krytyczna i luki strukturalne formalizmu TSM

Wprowadzenie danych PVLAS do równań TSM pozwala na sformułowanie twardego, laboratoryjnego ograniczenia górnego (upper limit) dla anizotropii sprężystej 0-Matrycy. Aby wartość $\Delta n_{\mathrm{TSM}}$ nie przekroczyła eksperymentalnego pułapu błędu PVLAS, maksymalna dopuszczalna różnica podatności węzłów musi spełniać warunek:

$$(\kappa_{\parallel} - \kappa_{\perp}) \le 9.6 \times 10^{-24} \text{ m}^3/\text{J}$$

Wartość ta wyznacza krytyczny punkt odniesienia dla dalszych prac nad teorią, ujawniając jednocześnie dwie istotne luki formalne:

* **Brak mikroskopowego potencjału sieci (Luka A):** TSM nie posiada obecnie wyprowadzonego matematycznego pomostu łączącego makroskopowy tensor sprężystości kontinuum z mikroskopową geometrią sfer oscylacji. Stała podatności sprężystej powinna wynikać bezpośrednio z sił interakcji topologicznej między sąsiadującymi 0-cząstkami (odpowiednik potencjału Lennarda-Jonesa w fizyce ciała stałego) pod wpływem rotacji zcentrowanej (pola $B$). Bez tego wyprowadzenia wartość $(\kappa_{\parallel} - \kappa_{\perp})$ pozostaje wyłącznie parametrem dopasowania numerycznego, pozbawionym uzasadnienia z pierwszych zasad (first principles).
* **Problem ontologii tłumienia (Luka B):** Obecność niezerowej szerokości dyssypacji $\Delta E$ w funkcjach opisujących stan sieci implikuje istnienie mechanizmu tłumienia (mikrolepkości) wewnątrz Substratu. Jeśli 0-Matryca u podstaw jest definiowana jako idealny, bezstratny nośnik falowy, wprowadzenie parametru rozmycia rezonansu $\Delta E > 0$ bez sformułowania dedykowanej mechaniki statystycznej fluktuacji sieciowej stanowi wewnętrzną sprzeczność logiczną, która wymaga usunięcia.

#### Perspektywy weryfikacji w reżimie wysokich pól (BIREF@HIBEF)

Ostatecznym testem różnicującym dla TSM nie będą jednak pomiary w reżimie niskich pól (gdzie przewidywania TSM i QED asymptotycznie się pokrywają), lecz nadchodzące wyniki z eksperymentu BIREF w instytucie HIBEF (European XFEL, Hamburg). Wykorzystanie ultraintensywnych laserów petawatowych jako pompy oraz twardego promieniowania rentgenowskiego jako sondy pozwoli na zbadanie próżni w warunkach ekstremalnej gęstości energii.

Dla standardowej QED zależność $\Delta n \propto B^2$ pozostaje niezmienna aż do osiągnięcia progu Schwingera. Dla TSM, jako teorii ściśle mechanicznej, przewiduje się pojawienie efektów nieliniowych wyższego rzędu ($B^4, B^6$) wynikających z anharmoniczności wychyleń sfer oscylacji oraz zjawiska wysycenia topologicznego (geometrycznego limitu upakowania sieci). Wykazanie w eksperymentach typu Pump-Probe odchyleń od parabolicznego trendu QED lub wykrycie profilu rezonansowego dla konkretnych częstotliwości wzbudzenia będzie stanowiło jednoznaczną falsyfikację Modelu Standardowego na rzecz Mechaniki Substratu Topologicznego.