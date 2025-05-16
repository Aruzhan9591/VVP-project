# Hledání nejkratší cesty v bludišti

## Popis projektu
Tento projekt je součástí předmětu Vědecké výpočty v Pythonu a zaměřuje se na nalezení nejkratší cesty v bludišti pomocí algoritmu BFS. Bludiště je reprezentováno ve formě CSV souboru, kde `True` označuje neprůchozí cesta (zdi) a `False` průchozí cestu.

Startovací bod je vždy v levém horním rohu (`[0, 0]`) a cílový bod v pravém dolním rohu (`[n-1, n-1]`). Výstupem je obrázek (`.png`), kde:
- Černá = zdi
- Bílá = průchozí cesta
- Červená = nalezená nejkratší cesta

## Funkcionalita
- Načítání bludiště z CSV souboru
- Vyhledání nejkratší cesty pomocí BFS
- Vykreslení cesty do barevného PNG obrázku
- Podpora více bludišť (maze_1.csv až maze_5.csv)

## Použité knihovny
- `numpy`
- `pandas`
- `collections` (deque)
- `PIL` (`Pillow`)

## Spuštění souboru
- Projekt umožňuje spustit buď jeden konkrétní soubor ručně (maze_1.csv), nebo automaticky zpracovat více bludišť (maze_1.csv až maze_5.csv). Stačí zakomentovat nebo odkomentovat příslušný blok v labirint.py.

