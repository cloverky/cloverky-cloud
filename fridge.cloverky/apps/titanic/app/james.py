from fastapi import FastAPI

from pathlib import Path
from titanic.app.walter import Walter

app = FastAPI(title="Titanic (James)")
_DATA_DIR = Path(__file__).resolve().parent
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.joblib"

class James:
    def __init__(self):
        pass


    def get_data(self):
        w = Walter()
        return w.get_data()

    def get_count(self):
        w = Walter()
        return w.get_count()    

    def get_count_survived(self):
        w = Walter()
        return w.get_count_survived()

    def get_count_not_survived(self):
        w = Walter()
        return w.get_count_not_survived()

    def has_decision_tree_model(self):
        return _MODEL_PATH.exists()

