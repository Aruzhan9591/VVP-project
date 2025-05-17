import numpy as np
from collections import deque
from typing import Generator


def find_neighbors(
        x: int, 
        y: int, 
        n: int
        ) -> Generator[tuple[int, int], None, None]:
    """
    Vrátí všechny průchozí sousedy (nahoru, dolů, vlevo, vpravo).

    Args:
        x (int): řádek
        y (int): sloupec
        n (int): velikost bludiště

    Yields:
        tuple[int, int]: souřadnice sousední buňky
    """
    for step_x, step_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + step_x, y + step_y
        if 0 <= nx < n and 0 <= ny < n:
            yield nx, ny


def bfs(maze: np.ndarray) -> list[tuple[int, int]]:
    """
    Najde nejkratší cestu v bludišti pomocí BFS.

    Args:
        maze (np.ndarray): 2D bool matice bludiště

    Returns:
        list[tuple[int, int]]: seznam souřadnic cesty nebo prázdný seznam
    """
    n = maze.shape[0]
    start = (0, 0)
    end = (n-1, n-1)

    visited = set([start])
    queue = deque([start])
    parent = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for nx, ny in find_neighbors(x, y, n):
            if (nx, ny) not in visited and not maze[nx][ny]:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    path = []
    cur = end
    while cur in parent and cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path if path and path[0] == start else []
