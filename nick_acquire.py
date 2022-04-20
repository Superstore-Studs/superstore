from env import host, username, password
import os
import pandas as pd 
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from datetime import date

def get_db_url(database, username=username, host=host, password=password):
    return f"mysql+pymysql://{username}:{password}@{host}/{database}"

def acquire_superstore_data(use_cache=True):
    '''
    This function returns the Superstore database as a Pandas DataFrame. 
    When this SQL data is cached and extant in the os directory path, return the data as read into a df. 
    If csv is unavailable, aquisition proceeds regardless,
    reading the queried database elements into a dataframe, creating a cached csv file
    and lastly returning the dataframe for some sweet data science perusal.
    '''

    # If the cached parameter is True, read the csv file on disk in the same folder as this file 
    if os.path.exists('superstore.csv') and use_cache:
        print('Using cached CSV')
        return pd.read_csv('superstore.csv')

    # When there's no cached csv, read the following query from Codeup's MySQL database.
    print('CSV not detected.')
    print('Acquiring data from MySQL database instead.')
    df = pd.read_sql(
        '''
SELECT * FROM orders 
    JOIN customers USING (`Customer ID`)
    JOIN products USING(`Product ID`)
    JOIN categories USING (`Category ID`)
    JOIN regions USING (`Region ID`);             
        '''
                    , get_db_url('superstore_db'))
    
    
    
    print('Acquisition Complete. Dataframe available and is now cached for future use.')
    # create a csv of the dataframe for the sake of efficiency. 
    df.to_csv('superstore.csv', index=False)
    
    return df