from env import host, username, password
import os
import pandas as pd 
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from datetime import date

def wrangle_superstore():
    '''
    Implements acquisition, preparation, pre-processing, and splitting for superstore. Dummies have not been created and will be made following the EDA cycle, and then retroactively applied to the splits. We implement a human-based approach to splitting, because the
    cut-off dates are more exact, and the sizes are still approximately .7/.3. Train would only have an additional 24 rows if the percentage-based method is used, while causing visual confusion. 
    '''
    df = prepare_superstore(acquire_superstore_data())
    train = df[:'2016'] # includes 2016
    test = df['2017']
    return train, test

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

def reorder_df(df):
    '''
    Since the Dataframe only visualizes the first and last ten columns
    I have restructuted the DataFrame column order based on what is
    most pertinent to see easily. 
    '''
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

def prepare_superstore(df):
    '''
    Acquires from MySql, converts columns to snakecase, drops redundant foreign keys
    Creates date_time columns, feature engineers days between shipment, isolates month 
    and year, creates profit and sales per product, sets order_date as the index
    and then reorders the columns so that the most captivating and informative columns
    can always be seen when calling the DF. 
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