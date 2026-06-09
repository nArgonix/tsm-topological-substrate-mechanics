import os
import json
import re

# ==============================================================================
# TABELA PROGÓW RÓŻNICOWYCH
# ==============================================================================
PROGI_SYSTEMOWE = [
    {"max_diff": 0,  "status": "🟢 Actual"},
    {"max_diff": 10,  "status": "🔵 Small change"},
    {"max_diff": 0, "status": "🟡 Medium change"},
    {"max_diff": float('inf'), "status": "🔴 Critical change"}
]

def pobierz_wersje_z_pliku(sciezka_pliku):
    """Wyciąga wersję z tagu ver"""
    if not os.path.exists(sciezka_pliku) or os.path.isdir(sciezka_pliku):
        return None
        
    try:
        with open(sciezka_pliku, 'r', encoding='utf-8') as f:
            tresc_pliku = f.read()
        
        # Konstrukcja odporna na masowe Find & Replace w edytorach
        czesc_otwierajaca = "<" + "!--"
        czesc_zamykajaca = "--" + ">"
        wzorzec_szukany = czesc_otwierajaca + r'\s*ver:(\d+)\.(\d+)\.(\d+)\s*' + czesc_zamykajaca
        
        dopasowanie = re.search(wzorzec_szukany, tresc_pliku)
        if dopasowanie:
            return (int(dopasowanie.group(1)), int(dopasowanie.group(2)), int(dopasowanie.group(3)))
    except Exception as e:
        print(f"Błąd podczas odczytu pliku {sciezka_pliku}: {e}")
        
    return False

def konwertuj_wersje_na_int(krotka_wersji):
    if not krotka_wersji or isinstance(krotka_wersji, bool):
        return None
    major, minor, patch = krotka_wersji
    return (major * 100) + (minor * 10) + patch

def konwertuj_wersje_na_str(krotka_wersji):
    if krotka_wersji is None: return "---"
    if krotka_wersji is False: return "no VERSION tag found"
    return f"{krotka_wersji[0]}.{krotka_wersji[1]}.{krotka_wersji[2]}"

def wyznacz_status_tlumaczenia(v_pl, v_eng):
    if v_pl is None: return "❌ No original found (POL)"
    if v_pl is False: return "⚠️ TAG error POL"
    if v_eng is None: return "🔴 No translation found (ENG)"
    if v_eng is False: return "⚠️ TAG error ENG"
    
    punkty_pl = konwertuj_wersje_na_int(v_pl)
    punkty_eng = konwertuj_wersje_na_int(v_eng)
    
    roznica = punkty_pl - punkty_eng
    if roznica < 0: return "🟢 Actual (ENG newer)"
        
    for regula in PROGI_SYSTEMOWE:
        if roznica <= regula["max_diff"]:
            return regula["status"]
            
    return "🔴 Critical change"

def main():
    sciezka_mapy = '.github/scripts/translation_map.json'
    
    if not os.path.exists(sciezka_mapy):
        print(f"Błąd: Brak pliku mapowania {sciezka_mapy}")
        return

    with open(sciezka_mapy, 'r', encoding='utf-8') as f:
        mapowanie_plików = json.load(f)

    katalog_pl = 'POL/DOC'
    katalog_eng = 'ENG/DOC'
    
    # KROK 1: Rozbudowa nagłówka oraz separatorów wyrównania o kolumnę 'Plik ENG'
    linie_tabeli = [
        "| Rozdział (PL) | Wersja POL | Status / Typ zmiany | Version ENG | File name (ENG) |",
        "| :--- | :---: | :--- | :---: | :--- |"
    ]
    
    for plik_pl, plik_eng in mapowanie_plików.items():
        if not plik_pl.strip() or not plik_eng.strip():
            continue
            
        pelna_sciezka_pl = os.path.join(katalog_pl, plik_pl)
        pelna_sciezka_eng = os.path.join(katalog_eng, plik_eng)
        
        wer_pl = pobierz_wersje_z_pliku(pelna_sciezka_pl)
        wer_eng = pobierz_wersje_z_pliku(pelna_sciezka_eng)
        
        status_koncowy = wyznacz_status_tlumaczenia(wer_pl, wer_eng)
        str_pl = konwertuj_wersje_na_str(wer_pl)
        str_eng = konwertuj_wersje_na_str(wer_eng)
        
        # KROK 2: Dodanie zmiennej plik_eng na końcu wiersza tabeli
        linie_tabeli.append(f"| {plik_pl} | **{str_pl}** | {status_koncowy} | {str_eng} | `{plik_eng}` |")
        
    zawartosc_tabeli = "\n".join(linie_tabeli)
    
    sciezka_docelowa = 'UPDATE_CHK.md'
    if not os.path.exists(sciezka_docelowa):
        print(f"Błąd: Nie znaleziono pliku {sciezka_docelowa}")
        return

    with open(sciezka_docelowa, 'r', encoding='utf-8') as f:
        stara_zawartosc = f.read()
        
    ZNACZNIK_START = "<!-- TAB_START -->"
    ZNACZNIK_STOP = "<!-- TAB_STOP -->"
    
    if ZNACZNIK_START in stara_zawartosc and ZNACZNIK_STOP in stara_zawartosc:
        czesc_przed = stara_zawartosc.split(ZNACZNIK_START)[0]
        czesc_po = stara_zawartosc.split(ZNACZNIK_STOP)[1]
        nowa_zawartosc = f"{czesc_przed}{ZNACZNIK_START}\n\n{zawartosc_tabeli}\n\n{ZNACZNIK_STOP}{czesc_po}"
        
        with open(sciezka_docelowa, 'w', encoding='utf-8') as f:
            f.write(nowa_zawartosc)
        print(f"Plik {sciezka_docelowa} został pomyślnie zaktualizowany.")
    else:
        print(f"Błąd: W pliku {sciezka_docelowa} brakuje znaczników komentarza bota.")

if __name__ == '__main__':
    main()