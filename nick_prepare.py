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
    # add minutes to the order_date to avoid duplicate values
    df['order_date_anew'] = df['order_date'] + pd.to_timedelta(df.groupby('order_date').cumcount(), unit='h')
    # Sort index by order date
    df = df.set_index('order_date_anew').sort_index()
    # drop the old order date
    df = df.drop(['order_date'], axis=1)
    # Create columns for month and year
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    # Create product-based columns
    df['profit_per_product'] = df.profit / df.quantity
    # add sales per product
    df['sales_per_product'] = df.sales / df.quantity
    # create column for brands, only first six letters. 
    brands = df[['product_name']]
    split = pd.DataFrame(brands.product_name.str.split(' ', expand=True))
    split = split[[0]]
    split = split.rename(columns={0: 'brand'})
    split = pd.DataFrame(split.brand.str[0:6])
    df = pd.concat([df, split], axis=1) 
    # get the DF
    return df

def reorder_df(df):
    # Reordered month in df
    df_columns = [col for col in df.columns if col != 'month']
    df_columns.insert(8, 'month')
    df = df[df_columns]
    
    # Reordered year in df
    df_columns = [col for col in df.columns if col != 'year']
    df_columns.insert(0, 'year')
    df = df[df_columns]
    
    # Reordered month in df
    df_columns = [col for col in df.columns if col != 'month']
    df_columns.insert(0, 'month')
    df = df[df_columns]
    
    # Reordered customer_name in df
    df_columns = [col for col in df.columns if col != 'customer_name']
    df_columns.insert(10, 'customer_name')
    df = df[df_columns]
    
    # Reordered region_name in df
    df_columns = [col for col in df.columns if col != 'region_name']
    df_columns.insert(2, 'region_name')
    df = df[df_columns]
    
    # Reordered sales in df
    df_columns = [col for col in df.columns if col != 'sales']
    df_columns.insert(21, 'sales')
    df = df[df_columns]
    
    # Reordered profit in df
    df_columns = [col for col in df.columns if col != 'profit']
    df_columns.insert(19, 'profit')
    df = df[df_columns]
    
    # Reordered quantity in df
    df_columns = [col for col in df.columns if col != 'quantity']
    df_columns.insert(18, 'quantity')
    df = df[df_columns]
    
    # Reordered discount in df
    df_columns = [col for col in df.columns if col != 'discount']
    df_columns.insert(18, 'discount')
    df = df[df_columns]
    
    return df
    
    