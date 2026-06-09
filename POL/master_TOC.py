import re
import os

# --- KONFIGURACJA ---
FILES_TO_PROCESS = ['rozdzial 0.md', 'rozdzial 1.md', 'rozdzial 2.md', 'rozdzial 3.md', 'rozdzial 4.md', 'rozdzial 5.md', 'rozdzial 6.md',
                    'rozdz.7.md','rozdz.8.md','rozdz.9.md','rozdz.10.md','rozdz.11.md','rozdz.12.md','rozdz.13.md']

OUTPUT_FILE = 'MASTER_TOC.md'
VISIBLE_LEVELS = 2  # Ile poziomów ma być stale WIDOCZNYCH. 
                    # Jeśli 1: poziomy 1 (#) są widoczne, a podrozdziały (##, ###) są w <details>.
                    # Jeśli 2: poziomy 1 (#) i 2 (##) są widoczne, a od poziomu 3 (###) zwijamy.

def generate_master_toc():
    pattern = re.compile(r'^(#{1,4})\s+(.*)')
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        f_out.write("# Spis Treści\n\n")
        
        for file_path in FILES_TO_PROCESS:
            if not os.path.exists(file_path): continue
            
            # Reprezentacja struktury pliku jako drzewa (lista krotek: (level, title))
            nodes = []
            with open(file_path, 'r', encoding='utf-8') as f_in:
                for line in f_in:
                    match = pattern.match(line)
                    if match:
                        hashes, title = match.groups()
                        nodes.append((len(hashes), title.strip()))
            
            # Renderowanie struktury z podglądem "w przód"
            for i, (level, title) in enumerate(nodes):
                indent = '  ' * (level - 1)
                
                # Sprawdzamy, czy ten nagłówek ma podrozdziały (dzieci)
                has_children = (i + 1 < len(nodes) and nodes[i+1][0] > level)
                
                # CZY TO JEST POZIOM, KTÓRY MA BYĆ "ROZWIJACZEM" (Ostatni widoczny poziom, posiadający dzieci)
                if level == VISIBLE_LEVELS and has_children:
                    f_out.write(f"{indent}- <details>\n")
                    f_out.write(f"{indent}  <summary><b>{title}</b></summary>\n\n")
                
                # ZWYKŁY ELEMENT (Widoczny lub będący liściem głęboko w strukturze)
                else:
                    # Jeśli element jest wewnątrz zwiniętej sekcji, dodajemy mu dodatkowe wcięcie
                    current_indent = indent
                    if level > VISIBLE_LEVELS:
                        # Wyrównanie wcięcia dla elementów wewnątrz <details>
                        current_indent = '  ' * (level)
                    f_out.write(f"{current_indent}- {title}\n")
                
                # DOMYKANIE TAGU <details>
                # Zamykamy, jeśli następny element wraca do poziomu VISIBLE_LEVELS (lub wyżej), albo to koniec pliku
                if level >= VISIBLE_LEVELS:
                    next_level = nodes[i+1][0] if i + 1 < len(nodes) else 0
                    if next_level <= VISIBLE_LEVELS and level >= VISIBLE_LEVELS:
                        # Musimy domknąć blok dla bieżącej sekcji
                        # Szukamy jak głęboko musimy się cofnąć w strukturze
                        for close_level in range(level, VISIBLE_LEVELS, -1):
                            if next_level <= close_level - 1:
                                close_indent = '  ' * (close_level - 1)
                                f_out.write(f"\n{close_indent}</details>\n")
                                
            f_out.write("\n---\n\n")
            
    print(f"Sukces: Spis treści (VISIBLE_LEVELS={VISIBLE_LEVELS}) zapisano w {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_master_toc()