from env import host, username, password
import os
import pandas as pd 
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from datetime import date

def wrangle_superstore():
    '''
    Implements acquisition, preparation, pre-processing, and splitting for superstore. Dummies have not been created and will be made following the EDA cycle, and then retroactively applied to the splits.
    '''
    df = prepare_superstore(acquire_superstore_data())
    train, validate, test = split_superstore_data(df)
    return train, validate, test

# -------------------------------------------------

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

def prepare_superstore(df):
    '''
    '''
    # First obtain the DataFrame and define the variable. 
    df = acquire_superstore_data()
    # Next convert column names to snake_case
    df.columns = [col.lower().replace(" ","_").replace("-","_") for col in df.columns]
    # drop redundant columns
    df = df.drop(['region_id', 'category_id', 'country'], axis=1)
    # Convert columns to date_time
    df['order_date']= pd.to_datetime(df['order_date'])
    df['ship_date']= pd.to_datetime(df['ship_date'])
    # Calculate days between shipment and order placement
    df['days_bw_shipment'] = df['ship_date'] - df['order_date']
    # Sort index by order date
    df = df.set_index('order_date').sort_index()
    # Create columns for month and year
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    # get the DF
    return df

def split_superstore_data(df):
    '''
   Using methods gleaned from Codeup's Time Series Analysis lessons,
   splits the Superstore DF into Train Validate and Split; .5/.3/.2 respectively.
   Subsequently returns each.
    '''
    print('Dataframe Input received: Splitting Data .5/.3/.2.')
    train_size = int(len(df) * .5)
    validate_size = int(len(df) * .3)
    test_size = int(len(df) - train_size - validate_size)
    validate_end_index = train_size + validate_size

    # split into train, validation, test
    train = df[: train_size]
    validate = df[train_size : validate_end_index]
    test = df[validate_end_index : ]
    print(f'Train: {train.shape}, Validate {validate.shape}, and Test {test.shape} are ready.\
    \n Proceed with EDA.')
    return train, validate, test