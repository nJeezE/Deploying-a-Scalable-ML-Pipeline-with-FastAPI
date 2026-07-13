import pytest
# TODO: add necessary import
import numpy as np
import os
from ml.data import apply_label
from ml.model import train_model, save_model, load_model, compute_model_metrics

from sklearn.ensemble import RandomForestClassifier


# TODO: implement the first test. Change the function name and input as needed
def test_apply_label_input():
    """
    # testing that the input successfully maps 0 and 1
    """
    # force a 0 through the pipeline
    result_zero = apply_label(np.array([0]))
    assert result_zero == "<=50K"
    
    # force a 1 through the pipeline
    result_one = apply_label(np.array([1]))
    assert result_one == ">50K"

# TODO: implement the second test. Change the function name and input as needed
def test_model_save_load(tmp_path):
    """
    # tests that the model is saved and reloaded as a random forest classifier
    """
    # dummy dataset
    X_train = np.random.rand(15, 5)
    y_train = np.random.randint(0, 2, size=15)

    # train the model
    original_model = train_model(X_train, y_train)

    # create tmp_path
    temp_file_path = os.path.join(tmp_path, "model.pkl")

    # save the model
    save_model(original_model, temp_file_path)

    assert os.path.exists(temp_file_path)
    assert os.path.getsize(temp_file_path) > 0

    # loading the model back in for testing
    loaded_model = load_model(temp_file_path)

    # check that the model exists and is a random forest classifier
    assert isinstance(loaded_model, RandomForestClassifier)





# TODO: implement the third test. Change the function name and input as needed
def test_metrics_shape():
    """
    # test that the metrics return the correct values for perfect prediction
    """
    # dummy data
    y_true = np.array([0, 1, 0, 1])
    y_pred = np.array([0, 1, 1, 0])
    # calculate metrics
    metrics = compute_model_metrics(y_true, y_pred)
    # returns tuple of length 3
    assert isinstance(metrics, tuple)
    assert len(metrics) == 3