
import numpy as np
from numpy import ndarray
from maze_lib.bfs_solver import bfs


def generate_maze(
        size: int,
        density: float = 0.3,
        max_attempts: int = 100
        ) -> ndarray:
    """
    Vygeneruje náhodné bludiště, které má vždy řešení z [0,0] do [n-1,n-1].

    Args:
        size (int): Rozměr bludiště (size x size).
        density (float): Podíl zdí (mezi 0 a 1).
        max_attempts (int): Počet pokusů vygenerovat průchozí bludiště.

    Returns:
        ndarray: 2D matice True/False (True = zeď, False = volno).
    """
    for _ in range(max_attempts):
        maze = np.random.rand(size, size) < density
        maze[0, 0] = False
        maze[size-1, size-1] = False

        path = bfs(maze)
        if path:
            return maze

    raise ValueError("Nepodařilo se vygenerovat průchozí bludiště.")
