##### IMPORTS #####
import pandas as pd
import numpy as np
import os
from env import host, username, password

##### CONNECT TO CODEUP DB #####
def get_db_url(db, username=username, host=host, password=password):
    
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'



##### ACQUIRE TITANIC DATA FUNCTIONS #####

def new_titanic_data():
    
    sql_query_titanic = 'SELECT * FROM passengers'
    
    df = pd.read_sql(sql_query_titanic, get_db_url('titanic_db'))
    
    return df


def get_titanic_data(cached=False):
    
    if os.path.isfile('titanic_df.csv'):
        
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        
        df = new_titanic_data()
        
        df.to_csv('titanic_df.csv')
    
    return df


##### ACQUIRE IRIS DATA FUNCTIONS #####

def new_iris_data():
    
    sql_query_iris = 'SELECT * FROM measurements JOIN species USING (species_id)'
                
    df = pd.read_sql(sql_query_iris, get_db_url('iris_db'))
    
    return df


def get_iris_data(cached=False):
    
    if os.path.isfile('iris_df.csv'):
        
        df = pd.read_csv('iris_df.csv', index_col=0)
        
    else:
        
        df = new_iris_data()
        
        df.to_csv('iris_df.csv')
        
    return df
