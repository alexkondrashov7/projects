
from joblib import load
import pandas as pd
import numpy as np


class FinalModel:
    def __init__(self, path_selector, path_main_model):
        self.selector = load(path_selector)
        self.model = load(path_main_model)

    def predict(self,X):
        self.get_features(X)
        return self.model.predict(self.dataset)

    def predict_proba(self,X):
        self.get_features(X)
        return self.model.predict_proba(self.dataset)[:,1]
        
    def get_features(self,X):
        X = self.selector.transform(X)
        self.dataset = pd.DataFrame(X, columns = self.selector.get_feature_names_out())
