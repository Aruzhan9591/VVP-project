import pandas as pd
import numpy as np


def load_maze(file_path: str) -> np.ndarray:
    """
    Načte bludiště ze souboru CSV.

    Args:
        file_path (str): Cesta k CSV souboru.

    Returns:
        np.ndarray: 2D matice bool (True = zeď, False = volná cesta).
    """
    df = pd.read_csv(file_path, header=None)
    return df.values.astype(bool)
