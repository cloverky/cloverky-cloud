from pathlib import Path

import pandas as pd
import numpy as np

class Walter:
    def __init__(self):
        pass

    def get_data(self, limit: int = 10):
        base_dir = Path(__file__).resolve().parent
        df = pd.read_csv(base_dir / "Titanic-Dataset.csv")

        # Starlette/FastAPI JSON 직렬화는 JSON 규격상 `nan/inf`를 허용하지 않아 500이 발생할 수 있습니다.
        # 따라서 NaN/±Inf를 JSON-compliant한 `None`으로 치환합니다.
        df = df.head(limit)
        df = df.replace([np.inf, -np.inf], np.nan)

        # dtype이 float인 상태에서는 None이 다시 nan으로 되돌려질 수 있어,
        # object로 바꾼 뒤 치환이 유지되도록 합니다.
        mask = pd.notna(df)
        df = df.astype(object).where(mask, None)

        return df.to_dict(orient="records")