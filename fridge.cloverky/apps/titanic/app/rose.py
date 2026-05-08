from pathlib import Path

import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.joblib"


class rose:
    def __init__(self):
        pass

    def save_decision_tree_model(self):
        df = pd.read_csv(_CSV_PATH)

        feature_cols = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
        target_col = "Survived"
        model_df = df[feature_cols + [target_col]].copy()

        # 문자열 결측값 보정
        model_df["Embarked"] = model_df["Embarked"].fillna("Unknown")
        model_df["Sex"] = model_df["Sex"].fillna("unknown")

        # 수치형 결측값은 중앙값으로 보정
        for col in ["Age", "Fare"]:
            model_df[col] = model_df[col].fillna(model_df[col].median())

        X = pd.get_dummies(model_df[feature_cols], drop_first=False)
        y = model_df[target_col].astype(int)

        model = DecisionTreeClassifier(random_state=42, max_depth=5)
        model.fit(X, y)

        payload = {
            "model": model,
            "feature_columns": X.columns.tolist(),
        }
        joblib.dump(payload, _MODEL_PATH)

        return str(_MODEL_PATH)