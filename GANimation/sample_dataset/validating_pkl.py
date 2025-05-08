import pickle
from pathlib import Path

ROOT = Path(__file__).parent
DATASET_PATH = ROOT / "aus_openface.pkl"

with open(DATASET_PATH, "rb") as f:
    aus_data = pickle.load(f)

print("Exemplo de chave:", list(aus_data.keys())[:8])
print("Exemplo de valores:", list(aus_data.values())[:1])