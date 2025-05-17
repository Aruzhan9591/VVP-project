from maze_lib.loader import load_maze
from maze_lib.bfs_solver import bfs
from maze_lib.visualizer import generate_image
from maze_lib.generator import generate_maze

for i in range(1, 6):
    file_path = f"maze_{i}.csv"
    out = f"maze_{i}.png"

    maze = load_maze(file_path)
    path = bfs(maze)
    generate_image(maze, path, out)
    print(f"[OK] {file_path} → {out}")

# new generated maze
generated_maze = generate_maze(size=20, density=0.3)
generated_path = bfs(generated_maze)
generate_image(generated_maze, generated_path, "generated_maze.png")
print("[OK] Generated random maze → generated_maze.png")
