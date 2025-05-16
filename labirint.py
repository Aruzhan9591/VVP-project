import pandas as pd
import numpy as np
from collections import deque  # (ochered)
from PIL import Image


# -Ruční spuštění jednoho souboru (maze_1.csv)-
# file_path = 'maze_1.csv'


# Načtení bludiště ze souboru CSV
def load_maze(file_path):
    df = pd.read_csv(file_path, header=None)
    return df.values.astype(bool)


# Funkce pro získání sousedů (nahoru, dolů, vlevo, vpravo)
def find_neighbors(x, y, n):
    # levo,vpravo,verh,vniz
    for step_x, step_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
        nx, ny = x + step_x, y + step_y
        if 0 <= nx < n and 0 <= ny < n:
            yield nx, ny


# Algoritmus BFS pro hledání nejkratší cesty
def Bfs(maze):
    n = maze.shape[0]  # shape vernet 1(pervoe) chislo
    start = (0, 0)
    end = (n-1, n-1)

    visited = set([start])
    queue = deque([start])
    parent = {
        start: None
    }
    while queue:
        x, y = queue.popleft()  # s leva vikidyvaet element
        if (x, y) == end:
            break
        for nx, ny in find_neighbors(x, y, n):
            if (nx, ny) not in visited and not maze[nx][ny]:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    path = []
    cur = end  # budto by prishli k itogu
    while cur in parent and cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    if path and path[0] == start:
        return path
    return []


# Vykreslení výsledného obrázku s cestou
def generate_image(maze, path, out):
    n = maze.shape[1]
    img = np.zeros((n, n, 3), dtype=np.uint8)
    img[maze] = [0, 0, 0]  # black
    img[~maze] = [255, 255, 255]  # white
    for x, y in path:
        img[x, y] = [255, 0, 0]  # red

    Image.fromarray(img).save(out)


# -Ruční spuštění jednoho souboru (maze_1.csv)-
# out = "maze_1.png"
# file_path = "maze_1.csv"
# maze = load_maze(file_path)
# print(maze)
# path1 = Bfs(maze)
# generate_image(maze, path1, out)


# Automatické zpracování všech souborů maze_1.csv až maze_5.csv

for i in range(1, 6):
    file_path = f"maze_{i}.csv"
    out = f"maze_{i}.png"

    maze = load_maze(file_path)
    path = Bfs(maze)
    generate_image(maze, path, out)
    print(f"[OK] maze_{i}.csv → maze_{i}.png")