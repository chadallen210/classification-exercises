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

##### ACQUIRE TELCO_CHURN DATA #####

def new_telco_data():
    '''
    gets telco_churn information from CodeUp db and creates a dataframe
    '''

    # SQL query
    telco_query = '''SELECT * FROM customers
                JOIN contract_types USING (contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN payment_types USING (payment_type_id)'''
    
    # reads SQL query into a DataFrame            
    df = pd.read_sql(telco_query, get_db_url('telco_churn'))
    
    return df

def get_telco_data():
    '''
    checks for existing telco_churn csv file and loads if present,
    otherwise runs new_telco_data function to acquire data
    '''
    
    # checks for existing file and loads
    if os.path.isfile('telco_churn.csv'):
        
        df = pd.read_csv('telco_churn.csv', index_col=0)
        
    else:
        
        # pull in data and creates csv file if not already present
        df = new_telco_data()
        
        df.to_csv('telco_churn.csv')
    
    return df