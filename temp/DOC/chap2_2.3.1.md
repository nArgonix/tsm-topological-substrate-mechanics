
### 2.3.1. Geometryczne pochodzenie spinu połówkowego

W klasycznej mechanice kwantowej oraz kwantowej teorii pola spin połówkowy jest postulowany jako wewnętrzny, niefizyczny moment pędu cząstek elementarnych, opisywany za pomocą abstrakcyjnego formalizmu spinorów Diraca i generatorów algebry $su(2)$. W ramach Mechaniki Substratu Topologicznego (TSM) pojęcie to zostaje pozbawione mistycznego charakteru i sprowadzone do czystej elastodynamiki oraz topologii więzów geometrycznych ośrodka ciągłego w przestrzeni $\mathbb{R}^4$. Spin $1/2$ wyłania się jako bezpośrednia konsekwencja trójwymiarowego uwięzienia pola orientacji strukturalnej komórek Wignera-Seitza Substratu wokół centrum topologicznego defektu (solitonu), zakotwiczonego w ortogonalnym wymiarze Bulk ($x^4$).

Aby sformułować rygorystyczny dowód matematyczny tego zjawiska, wprowadźmy lokalne pole orientacji osnowy, reprezentowane przez macierz obrotu $R(\mathbf{x}) \in SO(3)$, która definiuje przestrzenne skierowanie osi drgań i sfer oddziaływań 0-cząstek w każdym punkcie $\mathbf{x}$ trójwymiarowej membrany (3-brany). Alternatywnie, stan ten możemy opisać za pomocą jednostkowego wektora orientacji fazowej $\mathbf{n}(\mathbf{x}) \in \mathbb{S}^2$.

Rozpatrzmy proces ciągłej, makroskopowej rotacji układu współrzędnych wokół ustalonej osi obrotu, zdefiniowanej przez jednostkowy wektor $\mathbf{u} = (u_1, u_2, u_3)$. Niech $\alpha \in [0, 2]$ będzie parametrem ewolucyjnym określającym kąt obrotu $\theta(\alpha) = \pi \alpha$. Droga w przestrzeni konfiguracji grupy rotacji $SO(3)$ generowana przez ten obrót tworzy zamkniętą pętlę $\gamma(\alpha)$ dla $\alpha \in [0, 2]$, co odpowiada pełnemu obrotowi o kąt $2\pi$.

Z punktu widzenia topologii algebraicznej grupa $SO(3)$ jest wielokrotnością niespójną topologicznie, a jej grupa fundamentalna wynosi:

$$\pi_1(SO(3)) \cong \mathbb{Z}_2 = \{0, 1\}$$

Oznacza to, że w przestrzeni obrotów trójwymiarowych istnieją dokładnie dwie klasy pętli homotopijnych: pętle ściągalne (trywialne, klasa $0$) oraz pętle nieściągalne (nietrywialne, klasa $1$). Pętla odpowiadająca obrotowi o kąt $2\pi$ jest generatorem grupy $\pi_1(SO(3))$ i reprezentuje klasę nietrywialną. Nie można jej w sposób ciągły zdeformować do punktu bez rozerwania kontinuum.

Przejście do reprezentacji spinorowej (grupy nakrywającej) realizujemy poprzez uniwersalne podwójne nakrycie:

$$\text{Ad} : \text{Spin}(3) \cong SU(2) \longrightarrow SO(3)$$

Dowolny element grupy $SU(2)$ reprezentujący lifting topologiczny obrotu o kąt $\theta$ wokół osi $\mathbf{u}$ kodujemy za pomocą macierzy unitarnych $U(\theta) \in SU(2)$, wykorzystując macierze Pauliego $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$:

$$U(\theta) = \exp\left(-i \frac{\theta}{2} \mathbf{u} \cdot \boldsymbol{\sigma}\right) = I \cos\left(\frac{\theta}{2}\right) - i (\mathbf{u} \cdot \boldsymbol{\sigma}) \sin\left(\frac{\theta}{2}\right)$$

Gdzie $I$ jest macierzą jednostkową $2\times2$. Przeanalizujmy zachowanie transformacji pola orientacji $\mathbf{n}(\mathbf{x})$ przy zmianie kąta $\theta$:

1. Dla obrotu o pełny kąt geometryczny $\theta = 2\pi$ ($\alpha = 2$):

$$U(2\pi) = I \cos(\pi) - i (\mathbf{u} \cdot \boldsymbol{\sigma}) \sin(\pi) = -I$$



Podstawienie to wykazuje jawne odwrócenie znaku operatora ewolucji fazowej. W przestrzeni fizycznej Substratu transformacja ta indukuje inwersję wektora orientacji komórek osnowy:

$$\mathbf{n}(\mathbf{x}) \xrightarrow{\text{Obrót } 2\pi} -\mathbf{n}(\mathbf{x})$$

2. Dla obrotu o podwójny kąt geometryczny $\theta = 4\pi$ ($\alpha = 4$):

$$U(4\pi) = I \cos(2\pi) - i (\mathbf{u} \cdot \boldsymbol{\sigma}) \sin(2\pi) = I$$



Co przywraca pierwotny stan topologiczny pola:

$$\mathbf{n}(\mathbf{x}) \xrightarrow{\text{Obrót } 4\pi} \mathbf{n}(\mathbf{x})$$

W klasycznym trójwymiarowym kontinuum mechanicznym stan $\mathbf{n}$ oraz $-\mathbf{n}$ musiałby prowadzić do nieciągłości makroskopowych pól naprężeń. Jednakże w modelu TSM 3-brana jest zanurzona w czterowymiarowej przestrzeni $\mathbb{R}^4$. Elastyczne linie naciągu normalnego, łączące komórki brany z otaczającym środowiskiem Bulk, podczas obrotu o $2\pi$ ulegają nieliniowemu zakleszczeniu splotowemu (skręceniu) wzdłuż osi $x^4$. Stan ten charakteryzuje się lokalnym nagromadzeniem energii sprężystej ścinania, opisanej przez składowe tensora odkształceń potencjału $\beta_{i4}$.

Wprowadźmy tensor gęstości momentu skręcającego $\tau_{ijk}$, powiązany z gradientem pola orientacji:

$$\tau_{ijk} = \mu \left( R_{ia} \partial_k R_{ja} - R_{ja} \partial_k R_{ia} \right)$$

Gdzie $\mu$ jest modułem ścinania Substratu. Całkowita energia elastyczna splotu $E_{\text{twist}}$ związana z obrotem układu wokół centrum solitonu o kąt $\theta$ wynosi:

$$E_{\text{twist}} = \frac{1}{2} \int_{\mathbb{R}^3} \tau_{ijk} \tau_{ijk} d^3x$$

Ponieważ pętla $2\pi$ jest topologicznie nieściągalna w $SO(3)$, pole naprężeń $\tau_{ijk}$ nie może zrelaksować się do zera – linie sił są mechanicznie zablokowane przez ciągłość zakotwiczenia w wymiarze Bulk. Wykonanie kolejnego obrotu o $2\pi$ (łącznie $4\pi$) wprowadza drugą klasę skręcenia, która w przestrzeni czterowymiarowej tworzy układ pętli o przeciwnej klasie homotopii. Zgodnie z topologicznym prawem relaksacji więzów (czego makroskopowym modelem makietowym jest tzw. *Dirac belt trick*), pętla $4\pi$ jest w pełni ściągalna do stanu trywialnego ($\text{klasa } 0$). Oznacza to, że dodatkowy obrót pozwala na przestrzenne „przełożenie” linii naciągu wzdłuż osi $x^4$ i pełne rozplątanie węzła strukturalnego bez rozrywania osnowy.

Zjawisko to stanowi matematyczny i mechaniczny dowód, że cząstki o spinie połówkowym są rzeczywistymi, fizycznymi solitonami skrętnymi w Substracie, a ich kwantowa właściwość zmiany znaku funkcji falowej przy obrocie o $2\pi$ jest bezpośrednim odzwierciedleniem nieliniowej relaksacji elastodynamicznej w przestrzeni o wyższej wymiarowości.