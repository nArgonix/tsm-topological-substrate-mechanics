import re
import os

# --- KONFIGURACJA ---
FILES_TO_PROCESS = ['rozdzial 0.md', 'rozdzial 1.md', 'rozdzial 2.md', 'rozdzial 3.md', 'rozdzial 4.md', 'rozdzial 5.md', 
                    'rozdz.7.md','rozdz.7.md','rozdz.8.md','rozdz.9.md','rozdz.10.md',
                    'rozdz.11.md','rozdz.12.md','rozdz.13.md','rozdz.13.md']
OUTPUT_FILE = 'MASTER_TOC.md'
DETAILS_LEVEL = 2  # Od tego poziomu (i głębiej) wstawiane będą <details>

def generate_master_toc():
    pattern = re.compile(r'^(#{1,4})\s+(.*)')
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        f_out.write("# Zbiorczy Spis Treści\n\n")
        
        for file_path in FILES_TO_PROCESS:
            if not os.path.exists(file_path):
                print(f"Uwaga: Plik {file_path} nie istnieje, pomijam.")
                continue
                
            f_out.write(f"## Źródło: {file_path}\n\n")
            
            with open(file_path, 'r', encoding='utf-8') as f_in:
                for line in f_in:
                    match = pattern.match(line)
                    if match:
                        hashes, title = match.groups()
                        level = len(hashes)
                        
                        # Logika tworzenia spisu
                        if level < DETAILS_LEVEL:
                            f_out.write(f"- {hashes} {title}\n")
                        else:
                            # Prosta implementacja zamykania w details
                            f_out.write(f"<details>\n<summary>{hashes} {title}</summary>\n\n")
                            # Tu można dodać logikę zamykania tagów, 
                            # jeśli struktura jest bardziej złożona
                            f_out.write("</details>\n")
                            
            f_out.write("\n---\n\n")
    
    print(f"Sukces: Zbiorczy spis zapisano w {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_master_toc()