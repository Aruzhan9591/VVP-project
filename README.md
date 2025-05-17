# Hledání nejkratší cesty v bludišti


## Popis projektu
Tento projekt byl vytvořen v rámci předmětu **Vědecké výpočty v Pythonu**. Cílem je načíst bludiště ze souboru CSV, nalézt nejkratší cestu pomocí algoritmu **BFS (Breadth-First Search)** a vykreslit výsledek do obrázku. Program podporuje zpracování více bludišť najednou.

Vstupem je 2D CSV matice, kde:
- `True` = zeď (neprůchozí),
- `False` = volná cesta (průchozí).

Startovací bod je vždy v levém horním rohu `[0, 0]`, cílový bod je v pravém dolním rohu `[n-1, n-1]`.

Výstupem je obrázek (`.png`), kde:
- **Černá** = zdi  
- **Bílá** = volné buňky  
- **Červená** = nalezená nejkratší cesta

---

## Funkcionalita

- Načítání bludiště z CSV (`loader.py`)
- Hledání nejkratší cesty pomocí BFS (`bfs_solver.py`)
- Vykreslení cesty do PNG obrázku (`visualizer.py`)
- Automatické zpracování více bludišť (`main.py`)
- Výstup: obrázky `maze_1.png` až `maze_5.png`

---

## Struktura projektu

- python_project/
- ├── maze_lib/
- │ ├── loader.py    # načtení CSV
- │ ├── bfs_solver.py   # BFS algoritmus
- │ ├── visualizer.py    # vykreslení PNG
- ├── main.py    # hlavní spouštěcí soubor
- ├── maze_1.csv až maze_5.csv
- ├── maze_1.png až maze_5.png
- ├── README.md

---

## Použité knihovny

- `numpy`
- `pandas`
- `collections` (deque)
- `Pillow` (`PIL`)

---

---

## Poznámka k prostředí

- Projekt je určen k běhu ve virtuálním prostředí (venv), zejména kvůli omezením v Pythonu 3.12

- Pro spuštění doporučujeme:

```bash
# vytvoření virtuálního prostředí
python3 -m venv venv

# aktivace prostředí
source venv/bin/activate

# instalace závislostí
pip install pandas pillow

# spuštění hlavního souboru
python main.py

