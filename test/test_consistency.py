import pytest
import pandas as pd

def test_train_target_col(data_train):
    """Test that the train dataframe has a 'target' column"""
    assert 'TARGET' in data_train.columns, "'TARGET' column is missing in train data"

def test_train_test_sizes(data_train, data_test):
    """Check that train and test dataframe have the same columns (except target)"""
    train_columns = set(data_train.columns) - {'TARGET'}
    test_columns = set(data_test.columns)
    assert train_columns == test_columns, "Train and Test data columns do not match"