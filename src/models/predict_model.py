import numpy as np
import pandas as pd

from src.features.build_features import apply_feature_engineering
from src.utils.guardrails import validate_prediction_results
from src.utils.store import AssignmentStore


@validate_prediction_results
def main():
    store = AssignmentStore()

    df_test = store.get_raw("test_data.csv")
    df_test = apply_feature_engineering(df_test)

    model = store.get_model("saved_model.pkl")
    df_test["score"] = model.predict(df_test)


if __name__ == "__main__":
    main()
