import numpy as np
from pathlib import Path

ROOT = Path(__file__).parent
DATASET_PATH = ROOT / "gray_face_0.csv"

data = np.genfromtxt(DATASET_PATH, delimiter=",", autostrip=True)
print("Shape:", data.shape)
print("Data (primeiras 5 linhas):\n", data[:5])