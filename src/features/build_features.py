import pandas as pd
from sklearn.model_selection import train_test_split

from src.features.transformations import (
    hour_of_day,
)
from src.utils.store import AssignmentStore


def main():
    store = AssignmentStore()

    dataset = store.get_processed("dataset.csv")
    dataset = apply_feature_engineering(dataset)

    store.put_processed("transformed_dataset.csv", dataset)



if __name__ == "__main__":
    main()
