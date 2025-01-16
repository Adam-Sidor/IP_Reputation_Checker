# IP_Reputation_Checker
Projekt mający na celu sprawdzenie reputacji danych adresów IP.

---

## Spis treści
1. [Opis projektu](#opis-projektu)  
2. [Wymagania](#wymagania)  
3. [Instalacja](#instalacja)  
4. [Użycie](#użycie)  
5. [Funkcjonalności](#funkcjonalności)  
6. [Licencja](#licencja)  
7. [Kontakt](#kontakt)  

---

## Opis projektu
- Projekt zawiera skrypt w języku Python, który sprawdza reputacje danego adresu lub adresów IP. Projekt wykorzystuje do swojego działania API virustotal.com.

---

## Wymagania
- Oprogramowanie:  
  - Zainstalowany interpreter Python
- Pliki projektu:  
  - `Checker.py` - główny skrypt projektu.
  - `ip_list.txt` - domyślny plik z adresami IP.   

---

## Instalacja
Instrukcja krok po kroku, jak skonfigurować i uruchomić projekt:  
1. Sklonowanie repozytorium:  
   ```bash
   git clone https://github.com/Adam-Sidor/IP_Reputation_Checker
   ```
2. Zalogowanie się na stronie [VirusTotal.com](https://www.virustotal.com/gui/my-apikey) i uzyskanie klucza API.
3. Przypisanie w/w klucza do `API_KEY` w `Checker.py`

---

## Użycie
  1. Wybierz sposób użycia skryptu:
      1. Jeśli chcesz używać domyślnego pliku:
          - Wpisz adresy IP do pliku `ip_list.txt` (każdy adres IP w osobnym wierszu).
          - Uruchom terminal lub odpowienik np. Windows PowerShell.
          - W terminalu wpisz:
            ```bash
            python ścieżka_do_pliku_Checker.py
            ```
      2. Jeśli chcesz używać własnego pliku:
          - Wpisz adresy IP do własnego pliku np. `IP_to_check.txt` (każdy adres IP w osobnym wierszu).
          - Uruchom terminal lub odpowienik np. Windows PowerShell.
          - W terminalu wpisz:
            ```bash
            python ścieżka_do_pliku_Checker.py -f nazwa_pliku.txt
            ```
      3. Jeśli chcesz sprawdzić pojedynczy adres IP:
          - Uruchom terminal lub odpowienik np. Windows PowerShell.
          - W terminalu wpisz:
            ```bash
            python ścieżka_do_pliku_Checker.py -ip adres_IP
            ```
  2. Otwórz plik `output.csv` i sprawdź wyniki.  

Uwaga! w zależności od zainstalowanego interpretera Python w poleceniach z w/w punktów może być wymagane użycie `python3` zamiast `python`.

---

## Funkcjonalności
- Sprawdzanie reputacji adresów IP
- Możliwość tworzenia własnych plików z adresami IP
- Możliwośc sprawdzenia adresu IP podanego jako parametr

---

## Licencja
Wszystkie prawa zastrzeżone. Projekt został udostępniony wyłącznie w celach demonstracyjnych i edukacyjnych.  
- Możesz korzystać z tego projektu do użytku osobistego i edukacyjnego.  
- Wykorzystanie komercyjne lub redystrybucja projektu w całości lub w części wymaga wyraźnej pisemnej zgody autora.

---

## Kontakt
- Autor: Adam Sidor  
- E-mail: sidoadsi1@gmail.com  
- LinkedIn: [Mój profil](https://www.linkedin.com/in/adam-sidor-088a56341)  
