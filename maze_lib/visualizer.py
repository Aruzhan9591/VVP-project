import numpy as np
from PIL import Image


def generate_image(
        maze: np.ndarray, 
        path: list[tuple[int, int]], 
        out: str) -> None:
    """
    Vygeneruje obrázek PNG s vykreslenou cestou.

    Args:
        maze (np.ndarray): 2D matice bludiště
        path (list[tuple[int, int]]): souřadnice cesty
        out (str): název výstupního souboru
    """
    n = maze.shape[1]
    img = np.zeros((n, n, 3), dtype=np.uint8)
    img[maze] = [0, 0, 0]         # černé zdi
    img[~maze] = [255, 255, 255]  # bílé cesty
    for x, y in path:
        img[x, y] = [255, 0, 0]   # červená cesta

    Image.fromarray(img).save(out)
