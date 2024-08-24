import os
import pytest
import pandas as pd

@pytest.fixture(scope='module')
def data_train():
    """Get customers processed train data to feed into the tests"""
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, '../data/train_feature_engineering.csv.gz')
    return pd.read_csv(file_path, compression='gzip')
    
@pytest.fixture(scope='module')
def data_test():
    """Get customers processed test data to feed into the tests"""
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, '../data/test_feature_engineering_sampled.csv.gz')
    return pd.read_csv(file_path, compression='gzip')
    