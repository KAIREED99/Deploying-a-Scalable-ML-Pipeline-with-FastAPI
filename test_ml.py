import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from ml.data import process_data
from ml.model import compute_model_metrics


data = pd.read_csv("data/census.csv")

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


def test_process_data_return_type():
    """
    Test that process_data returns numpy arrays.
    """
    X, y, encoder, lb = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)


def test_compute_model_metrics():
    """
    Test that metric values are between 0 and 1.
    """
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])

    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= f1 <= 1


def test_train_test_data_size():
    """
    Test that train and test datasets have expected sizes.
    """
    train, test = train_test_split(
        data,
        test_size=0.20,
        random_state=42,
    )

    assert len(train) > 0
    assert len(test) > 0
    assert len(train) + len(test) == len(data)