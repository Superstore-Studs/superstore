from env import host, username, password
import os
import pandas as pd 
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from datetime import date

################################  acquire  ################################## 

def get_superstore_data(use_cache=True):
    '''This function returns the data from the superstore database in Codeup Data Science Database. 
    In my SQL query I have joined all necessary tables together, so that the resulting dataframe contains all the 
    information that is needed
    '''
    if os.path.exists('superstore.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('superstore.csv')
    print('Acquiring data from SQL database')

    database_url_base = f'mysql+pymysql://{username}:{password}@{host}/'
    query = '''
    SELECT * FROM orders 
    JOIN customers USING (`Customer ID`)
    JOIN products USING(`Product ID`)
    JOIN categories USING (`Category ID`)
    JOIN regions USING (`Region ID`);             
        
    '''
    df = pd.read_sql(query, database_url_base + 'superstore_db')
    df.to_csv('superstore.csv', index=False)
    return df
