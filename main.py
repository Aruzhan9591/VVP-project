from maze_lib.loader import load_maze
from maze_lib.bfs_solver import bfs
from maze_lib.visualizer import generate_image

for i in range(1, 6):
    file_path = f"maze_{i}.csv"
    out = f"maze_{i}.png"

    maze = load_maze(file_path)
    path = bfs(maze)
    generate_image(maze, path, out)
    print(f"[OK] {file_path} → {out}")
