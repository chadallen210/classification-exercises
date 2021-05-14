import numpy as np
import pandas as pd

def prep_iris(df):
    
    df = df.drop(columns=['species_id', 'measurement_id'])
    
    df.rename(columns={'species_name': 'species'}, inplace=True)
    
    df = pd.get_dummies(df, columns=['species'], drop_first=True)
    
    return df