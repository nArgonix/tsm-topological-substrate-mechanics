import re
import os
import glob

# Ścieżka relatywna do katalogu z dokumentami
BASE_DIR = os.path.join("POL", "DOC", "MD")
OUTPUT_FILE_NAME = "_global_refs.md"

EQ_PATTERN = re.compile(r"(\$\$(?:(?!\$\$).)*?\$\$\s*\{\#eq[-:][^\}]+\})", re.DOTALL)
FIG_PATTERN = re.compile(r"(!\[.*?\]\(.*?\)\s*\{\#fig[-:][^\}]+\})")

def main():
    extracted_elements = []
    
    if not os.path.exists(BASE_DIR):
        print(f"BŁĄD KRYTYCZNY: Katalog '{BASE_DIR}' nie istnieje.")
        return

    search_path = os.path.join(BASE_DIR, "*.md")
    all_files = sorted(glob.glob(search_path))
    output_file_path = os.path.join(BASE_DIR, OUTPUT_FILE_NAME)
    
    files_processed = 0

    for full_path in all_files:
        file_name = os.path.basename(full_path)
        if file_name == OUTPUT_FILE_NAME:
            continue
            
        files_processed += 1
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                equations = EQ_PATTERN.findall(content)
                figures = FIG_PATTERN.findall(content)
                extracted_elements.extend(equations)
                extracted_elements.extend(figures)
        except Exception as e:
            print(f" -> Błąd podczas czytania pliku {file_name}: {e}")

    # ZAPIS PRZY UŻYCIU NATYWNYCH BLOKÓW PANDOC (Fenced Divs)
    # Ta składnia gwarantuje, że blok zamknie się sztywno w obrębie tego pliku
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write("\n\n")
        f.write("::: {style=\"display:none\"}\n\n")
        for element in extracted_elements:
            f.write(element + "\n\n")
        f.write(":::\n")
    
    print(f"Sukces: Zindeksowano łącznie {len(extracted_elements)} referencji w {output_file_path}")

if __name__ == "__main__":
    main()