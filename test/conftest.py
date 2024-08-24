import pytest
import pandas as pd

@pytest.fixture(scope='module')
def data_train():
    """Get customers processed train data to feed into the tests"""
    return pd.read_csv('C:/Users/tykap/OneDrive/Bureau/P7_Credit_scoring/data/train_feature_engineering.csv.gz', compression='gzip')

@pytest.fixture(scope='module')
def data_test():
    """Get customers processed test data to feed into the tests"""
    return pd.read_csv('C:/Users/tykap/OneDrive/Bureau/P7_Credit_scoring/data/test_feature_engineering_sampled.csv.gz', compression='gzip')