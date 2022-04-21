from turtle import pd
import pandas as pd
import numpy as np
import matt_acquire

################################  prep  ################################## 

# combine everything into a prepare function
def prep_superstore():
    '''
    '''
    # First obtain the DataFrame and define the variable. 
    df = matt_acquire.get_superstore_data()
    # Next convert column names to snake_case
    print('Data acquired: Initializing Preparatory Stage...')
    df.columns = [col.lower().replace(" ","_").replace("-","_") for col in df.columns]
    # drop redundant columns
    df = df.drop(['region_id', 'category_id', 'country', 'unnamed:_0'], axis=1)
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
    print('Preparation complete. DF ready to be split for EDA.')
    # get the DF
    return df



    ################################  split  ################################## 

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

    ################################  acquire  ################################## 

def wrangle_superstore_data(df):
    '''
    Implements acquisition, preparation, pre-processing, and splitting for superstore. Dummies have not been created and will be made following the EDA cycle, and then retroactively applied to the splits. We implement a human-based approach to splitting, because the
    cut-off dates are more exact, and the sizes are still approximately .7/.3. Train would only have an additional 24 rows if the percentage-based method is used, while causing visual confusion. 
    '''
    
    train = df[:'2016'] # includes 2016
    test = df['2017']
    return train, test

    ################################  acquire  ################################## 



    ################################  acquire  ################################## 