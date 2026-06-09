import re
import os
import argparse

# --- STAŁA KONFIGURACJA ---

# --- KONFIGURACJA ---
FILES_TO_PROCESS = ['rozdzial 0.md', 'rozdzial 1.md', 'rozdzial 2.md', 'rozdzial 3.md', 'rozdzial 4.md', 'rozdzial 5.md', 'rozdzial 6.md',
                    'rozdz.7.md','rozdz.8.md','rozdz.9.md','rozdz.10.md','rozdz.11.md','rozdz.12.md','rozdz.13.md']

DEFAULT_OUTPUT_FILE = 'MASTER_TOC.md'
VISIBLE_LEVELS = 2  # Poziomy stale widoczne

# Znaczniki do wstrzykiwania zawartości
TOC_START_TAG = "<!--TOCS-->"
TOC_END_TAG = "<!--TOCE-->"

def build_toc_string():
    """Generuje strukturę spisu treści jako jeden ciąg znaków (string)."""
    pattern = re.compile(r'^(#{1,4})\s+(.*)')
    toc_lines = []
    
    for file_path in FILES_TO_PROCESS:
        if not os.path.exists(file_path): 
            print(f"Pomijam: plik {file_path} nie istnieje.")
            continue
        
        nodes = []
        with open(file_path, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                match = pattern.match(line)
                if match:
                    hashes, title = match.groups()
                    nodes.append((len(hashes), title.strip()))
        
        for i, (level, title) in enumerate(nodes):
            indent = '  ' * (level - 1)
            has_children = (i + 1 < len(nodes) and nodes[i+1][0] > level)
            
            if level == VISIBLE_LEVELS and has_children:
                toc_lines.append(f"{indent}- <details>")
                toc_lines.append(f"{indent}  <summary><b>{title}</b></summary>\n")
            else:
                current_indent = indent
                if level > VISIBLE_LEVELS:
                    current_indent = '  ' * (level)
                toc_lines.append(f"{current_indent}- {title}")
            
            if level >= VISIBLE_LEVELS:
                next_level = nodes[i+1][0] if i + 1 < len(nodes) else 0
                if next_level <= VISIBLE_LEVELS:
                    for close_level in range(level, VISIBLE_LEVELS, -1):
                        if next_level <= close_level - 1:
                            close_indent = '  ' * (close_level - 1)
                            toc_lines.append(f"\n{close_indent}</details>")
                            
        toc_lines.append("\n---\n")
        
    return "\n".join(toc_lines)

def inject_into_file(target_file, toc_content):
    """Wstrzykuje wygenerowany TOC pomiędzy znaczniki w istniejącym pliku."""
    if not os.path.exists(target_file):
        print(f"Błąd: Plik docelowy '{target_file}' nie istnieje. Stwórz go najpierw.")
        return

    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Sprawdzenie czy znaczniki istnieją
    if TOC_START_TAG not in content or TOC_END_TAG not in content:
        print(f"Błąd: W pliku '{target_file}' brakuje znaczników:\n{TOC_START_TAG}\n{TOC_END_TAG}")
        print("Spis treści NIE został zaktualizowany.")
        return

    # Wyrażenie regularne podmieniające tekst między znacznikami
    pattern = re.compile(f"{re.escape(TOC_START_TAG)}.*?{re.escape(TOC_END_TAG)}", re.DOTALL)
    
    # KLUCZOWA POPRAWKA: Escapujemy backslashe w treści spisu treści, 
    # aby Python nie traktował np. \p jako błędnej komendy regex.
    safe_toc_content = toc_content.replace('\\', '\\\\')
    
    replacement = f"{TOC_START_TAG}\n\n{safe_toc_content}\n\n{TOC_END_TAG}"
    
    new_content = pattern.sub(replacement, content)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Sukces: Spis treści został pomyślnie wstrzyknięty do '{target_file}'")

def main():
    # Obsługa argumentów linii poleceń
    parser = argparse.ArgumentParser(description="Generator zbiorczego Spisu Treści (TOC).")
    parser.add_argument(
        'target_file', 
        nargs='?', 
        default=None, 
        help="Opcjonalny plik (np. README.md), do którego ma zostać wstrzyknięty TOC."
    )
    
    args = parser.parse_args()
    toc_content = build_toc_string()
    
    if args.target_file:
        # Scenariusz 1: Podano plik -> Wstrzykujemy do środka
        inject_into_file(args.target_file, toc_content)
    else:
        # Scenariusz 2: Brak argumentu -> Tworzymy nowy plik MASTER_TOC.md od zera
        with open(DEFAULT_OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
            f_out.write("# Spis Treści\n\n")
            f_out.write(toc_content)
        print(f"Sukces: Nowy spis treści zapisano w '{DEFAULT_OUTPUT_FILE}'")

if __name__ == "__main__":
    main()