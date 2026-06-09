import os
import json
import re

# ==============================================================================
# TABELA PROGÓW RÓŻNICOWYCH (Dystans numeryczny między PL a ENG)
# Skrypt oblicza różnicę: Wartość_PL - Wartość_ENG
# Sprawdzanie następuje od góry do dołu, wybierając pierwszy pasujący próg.
# ==============================================================================
THRESHOLDS = [
    {"max_diff": 0,  "status": "🟢 Aktualna"},
    {"max_diff": 3,  "status": "🔵 Mała zmiana (0.0.x)"},
    {"max_diff": 12, "status": "🟡 Średnia zmiana (0.x.0)"},
    {"max_diff": float('inf'), "status": "🔴 Krytyczna zmiana (x.0.0)"}
]

def extract_version(filepath):
    """Wyciąga wersję z tagu """
    if not os.path.exists(filepath):
        return None
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'', content)
        if match:
            return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except Exception as e:
        print(f"Błąd podczas odczytu pliku {filepath}: {e}")
        
    return False

def version_to_int(v_tuple):
    """
    Wprowadzona formuła wagowa:
    Major * 100 + Minor * 10 + Patch
    """
    if not v_tuple or isinstance(v_tuple, bool):
        return None
    major, minor, patch = v_tuple
    return (major * 100) + (minor * 10) + patch

def version_to_str(v_tuple):
    if v_tuple is None: return "---"
    if v_tuple is False: return "Brak tagu ver"
    return f"{v_tuple[0]}.{v_tuple[1]}.{v_tuple[2]}"

def evaluate_status(v_pl, v_eng):
    """Wyznacza status na podstawie matematycznej różnicy wagowej"""
    if v_pl is None: return "❌ Brak oryginału PL"
    if v_pl is False: return "⚠️ Błąd tagu w PL"
    if v_eng is None: return "🔴 Brak tłumaczenia"
    if v_eng is False: return "⚠️ Błąd tagu w ENG"
    
    num_pl = version_to_int(v_pl)
    num_eng = version_to_int(v_eng)
    
    diff = num_pl - num_eng
    
    if diff < 0:
        return "🟢 Aktualna (ENG nowsza)"
        
    # Dopasowanie do zdefiniowanych progów punktowych
    for rule in THRESHOLDS:
        if diff <= rule["max_diff"]:
            return rule["status"]
            
    return "🔴 Krytyczna zmiana"

def main():
    map_file = '.github/scripts/translation_map.json'
    
    if not os.path.exists(map_file):
        print(f"Błąd: Brak pliku mapowania {map_file}")
        return

    with open(map_file, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    pol_dir = 'POL/DOC'
    eng_dir = 'ENG/DOC'
    
    # Układ kolumn: Rozdział | Wersja POL | Status / Typ zmiany | Wersja ANG
    table_lines = [
        "| Rozdział (PL) | Wersja POL | Status / Typ zmiany | Wersja ANG |",
        "| :--- | :---: | :--- | :---: |"
    ]
    
    for pol_file, eng_file in mapping.items():
        pol_path = os.path.join(pol_dir, pol_file)
        eng_path = os.path.join(eng_dir, eng_file)
        
        v_pl = extract_version(pol_path)
        v_eng = extract_version(eng_path)
        
        status = evaluate_status(v_pl, v_eng)
        v_pl_str = version_to_str(v_pl)
        v_eng_str = version_to_str(v_eng)
        
        table_lines.append(f"| {pol_file} | **{v_pl_str}** | {status} | {v_eng_str} |")
        
    table_content = "\n".join(table_lines)
    
    update_path = 'UPDATE_CHK.md'
    if not os.path.exists(update_path):
        print("Błąd: Nie znaleziono pliku UPDATE_CHK.md")
        return

    with open(update_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_marker = ""
    end_marker = ""
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = f"{before}{start_marker}\n\n{table_content}\n\n{end_marker}{after}"
        
        with open(update_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("UPDATE_CHK.md został zaktualizowany na podstawie wag liczbowych.")
    else:
        print("Błąd: Brak znaczników bota w UPDATE_CHK.md")

if __name__ == '__main__':
    main()