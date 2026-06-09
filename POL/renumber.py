import re
import argparse
import sys

def renumber_markdown(file_path, start_number):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{file_path}'")
        return

    # Inicjalizacja liczników: pierwszy poziom zaczyna się od start_number
    # counters[0] to poziom '#', counters[1] to '##' itd.
    counters = [start_number - 1, 0, 0, 0]
    new_lines = []
    
    for line in lines:
        match = re.match(r'^(#{1,4})\s+(.*)', line)
        if match:
            hashes, title = match.groups()
            level = len(hashes) - 1
            
            # Jeśli zmieniamy poziom nagłówka, inkrementujemy licznik
            if level == 0:
                counters[0] += 1
                # Resetujemy podpoziomy
                for i in range(1, 4):
                    counters[i] = 0
            else:
                counters[level] += 1
                # Resetujemy podpoziomy głębsze niż obecny
                for i in range(level + 1, 4):
                    counters[i] = 0
            
            # Usuwamy starą numerację
            clean_title = re.sub(r'^(\d+(\.\d+)*)\.?\s+', '', title).strip()
            
            # Tworzymy nową numerację
            num_str = ".".join(str(counters[i]) for i in range(level + 1))
            new_lines.append(f"{hashes} {num_str}. {clean_title}\n")
        else:
            new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Sukces: Plik '{file_path}' został zaktualizowany, numeracja zaczyna się od {start_number}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatyczna numeracja rozdziałów w Markdown.")
    parser.add_argument("nazwa_pliku", help="Ścieżka do pliku .md")
    parser.add_argument("nr_rozdzialu", type=int, help="Numer początkowy głównego rozdziału (#)")
    
    args = parser.parse_args()
    renumber_markdown(args.nazwa_pliku, args.nr_rozdzialu)