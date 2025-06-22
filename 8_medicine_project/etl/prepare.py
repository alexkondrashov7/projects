
import pandas as pd

class PrepareData:
    def __init__(self, path, is_del_target = True):
        self.path = path
        self.del_target = is_del_target
    def transform_dataset(self):
        df = pd.read_csv(self.path)
        df.columns = self.prepare_cols(df.columns)
        ids = df['id'].copy() # Сохраняем id
        df.dropna(axis = 1, inplace = True, thresh=0.9*df.shape[0])
        df['diagnosis'] = df['diagnosis'].apply(lambda x: 1 if x == 'M' else 0)
        df.drop(['id','radius_mean','concavity_mean','texture_se','concavity_worst'], inplace = True, axis = 1)
        if self.del_target:
            df.drop('diagnosis', inplace = True, axis = 1)
            
        return df,ids
    @staticmethod
    def prepare_cols(cols):
       return list(col.strip().replace(' ','_') for col in cols)
