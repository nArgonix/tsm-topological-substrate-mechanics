import re
import os

# --- KONFIGURACJA ---
FILES_TO_PROCESS = ['rozdzial 0.md', 'rozdzial 1.md', 'rozdzial 2.md', 'rozdzial 3.md', 'rozdzial 4.md', 'rozdzial 5.md', 
                    'rozdz.7.md','rozdz.7.md','rozdz.8.md','rozdz.9.md','rozdz.10.md',
                    'rozdz.11.md','rozdz.12.md','rozdz.13.md','rozdz.13.md']


OUTPUT_FILE = 'MASTER_TOC.md'
DETAILS_LEVEL = 2  # Od poziomu ## zaczynamy grupowanie

def generate_master_toc():
    # Regex wyciągający nagłówki (hashy i tytuł osobno)
    pattern = re.compile(r'^(#{1,4})\s+(.*)')
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        f_out.write("# Spis Treści\n\n")
        
        for file_path in FILES_TO_PROCESS:
            if not os.path.exists(file_path): continue
            
            in_details = False
            
            with open(file_path, 'r', encoding='utf-8') as f_in:
                for line in f_in:
                    match = pattern.match(line)
                    if match:
                        hashes, title = match.groups()
                        level = len(hashes)
                        
                        # 1. Logika dla głównych nagłówków (poziom 1)
                        if level < DETAILS_LEVEL:
                            if in_details:
                                f_out.write("</details>\n\n")
                                in_details = False
                            f_out.write(f"- {title}\n")
                        
                        # 2. Logika dla podrozdziałów
                        else:
                            if not in_details:
                                f_out.write("<details>\n<summary>Podrozdziały</summary>\n\n")
                                in_details = True
                            # title jest już "czyste" dzięki regex, nie dodajemy hashes
                            f_out.write(f"  - {title}\n")
            
            # Zamknij ostatni tag po zakończeniu pliku
            if in_details:
                f_out.write("</details>\n")
            f_out.write("\n")
    
    print(f"Sukces: Czysty spis treści zapisano w {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_master_toc()