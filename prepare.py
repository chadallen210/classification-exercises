##### IMPORTS #####

import numpy as np
import pandas as pd

import acquire

##### PREPARE IRIS #####

def prep_iris(df):
    
    df = df.drop(columns=['species_id', 'measurement_id'])
    
    df.rename(columns={'species_name': 'species'}, inplace=True)
    
    df = pd.get_dummies(df, columns=['species'], drop_first=True)
    
    return df

def prep_titanic(df):
    '''
    This function take in the titanic data acquired by get_titanic_data,
    Returns prepped train, validate, and test dfs with embarked dummy vars,
    deck dropped, and the mean of age imputed for Null values.
    '''
    
    # drop rows where embarked/embark town are null values
    df = df[~df.embarked.isnull()]
    
    # encode embarked using dummy columns
    titanic_dummies = pd.get_dummies(df.embarked, drop_first=True)
    
    # join dummy columns back to df
    df = pd.concat([df, titanic_dummies], axis=1)
    
    # drop the deck column
    df = df.drop(columns='deck')
    
    # split data into train, validate, test dfs
    train, validate, test = titanic_split(df)
    
    # impute mean of age into null values in age column
    train, validate, test = impute_mean_age(train, validate, test)
    
    return train, validate, test

def titanic_split(df):
    '''
    This function will take in the titanic data acquired by get_titanic_data,
    performs a split, and stratifies column.
    Returnd train, validate, and test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=0.2,
                            random_state=1221,
                            stratify=df.survived)
    train, validate = train_test_split(train_validate, test_size=0.3,
                                    random_state=1221,
                                    stratify=train_validate.survived)
    return train, validate, test
