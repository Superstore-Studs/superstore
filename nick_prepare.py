from env import host, username, password
import os
import pandas as pd 
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from datetime import date

import nick_acquire as get 

def prepare_superstore(df):
    '''
    '''
    # First obtain the DataFrame and define the variable. 
    df = get.acquire_superstore_data()
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
    
    