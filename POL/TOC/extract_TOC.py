import re
import argparse
import os

def extract_headings_to_md(input_file, output_file=None):
    # Jeśli output_file nie został podany, stwórz domyślną nazwę
    if output_file is None:
        file_name, file_ext = os.path.splitext(input_file)
        output_file = f"TOC_{file_name}{file_ext}"
    
    pattern = re.compile(r'^(#{1,4})\s+(.*)')
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            with open(output_file, 'w', encoding='utf-8') as f_out:
                f_out.write(f"# Spis treści dla: {os.path.basename(input_file)}\n\n")
                
                for line in f_in:
                    match = pattern.match(line)
                    if match:
                        hashes, title = match.groups()
                        indent = '  ' * (len(hashes) - 1)
                        f_out.write(f"{indent}- **{hashes} {title}**\n")
        
        print(f"Sukces: Spis został zapisany w '{output_file}'")
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{input_file}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ekstrakcja nagłówków do pliku .md")
    parser.add_argument("wejsciowy", help="Plik źródłowy .md")
    # nargs='?' sprawia, że argument jest opcjonalny
    parser.add_argument("wyjsciowy", nargs='?', help="Plik wynikowy (opcjonalny)")
    
    args = parser.parse_args()
    extract_headings_to_md(args.wejsciowy, args.wyjsciowy)