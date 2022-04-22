import plotly.express as px
from env import host, username, password
import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.model_selection import train_test_split
from datetime import date
import nick_wrangle as get
import plotly.express as px

def superstore_over_time(df):
    '''
    Take in the superstore dataframe and separate into categories,
    then display the profit and sales information for each category.
    '''
    office_supplies = df.loc[df['category'] == 'Office Supplies']
    furniture = df.loc[df['category'] == 'Furniture']
    technology = df.loc[df['category'] == 'Technology']
    
    fig, axes = plt.subplots(nrows=3, ncols=2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    
    plt.rcParams["figure.figsize"] = (20,10)
    
    plt.subplot(3, 2, 1)
    y = technology.profit
    
    ax = y.groupby(y.index.year).mean().plot.bar(width=.6, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Profit by Year TECHNOLOGY ONLY', xlabel='', ylabel='Annual Gains/Losses')
    
    plt.subplot(3, 2, 2)
    y2 = technology.sales
    
    ax = y2.groupby(y2.index.year).mean().plot.bar(width=.6, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Sales by Year TECHNOLOGY ONLY', xlabel='', ylabel='Annual Sales TECHNOLOGY')
    
    # Checking profit and sales in office supplies side by side
    plt.rcParams["figure.figsize"] = (14,7)
    
    plt.subplot(3, 2, 3)
    y = office_supplies.profit
    
    ax = y.groupby(y.index.year).mean().plot.bar(width=.6, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Profit by Year OFFICE SUPPLIES', xlabel='', ylabel='Annual Gains/Losses')
    
    plt.subplot(3, 2, 4)
    y2 = office_supplies.sales
    
    ax = y2.groupby(y2.index.year).mean().plot.bar(width=.6, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Sales by Year OFFICE SUPPLIES', xlabel='', ylabel='Annual Sales OFFICE SUPPLIES')
    
    # Checking overall profit and sales in furniture side by side
    plt.rcParams["figure.figsize"] = (14,7)
    
    plt.subplot(3, 2, 5)
    y = furniture.profit
    
    ax = y.groupby(y.index.year).mean().plot.bar(width=.6, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Profit by Year FURNITURE ONLY', xlabel='Year', ylabel='Annual Gains/Losses')
    
    plt.subplot(3, 2, 6)
    y2 = furniture.sales
    
    ax = y2.groupby(y2.index.year).mean().plot.bar(width=.6, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Sales by Year FURNITURE ONLY', xlabel='Year', ylabel='Annual Sales FURNITURE')
    
    plt.show()
    
def products_furn_and_tech(df):
    '''
    Takes in a df and creates subsets used to display the profit margins for technology and furniture.
    '''
    furniture_df = df.loc[df['category'] == 'Furniture']
    technology_df = df.loc[df['category'] == 'Technology']
    
    fig, ax = plt.subplots(1,2)
    fig.suptitle('Side by Side Comparison of Product Profitability')
    sns.barplot(data= technology_df, x = 'sub_category', y= 'profit', hue = 'region_name', ci = None, estimator = np.sum, ax=ax[0]).set_title('Technology Products')

    sns.barplot(data= furniture_df, x = 'sub_category', y= 'profit', hue = 'region_name', ci = None, estimator = np.sum, ax=ax[1]).set_title('Furniture Products')
    
    
    def create_top_bottom_dfs(df): 
    ''' 
    Takes in superstore DataFrame and creates multiple subsets, sorted by profit-per-product
    in descendening order to show top products for each sub-categories, and ascending for the least
    profitable. Returns best and worst products dataframes.
    '''
    #Accessories, Copiers, Machines, Phones  
    technology_df = df.loc[df['category'] == 'Technology']
    
    # subsetting by sub-category
    accessories = technology_df.loc[technology_df['sub_category'] == 'Accessories']
    copiers = technology_df.loc[technology_df['sub_category'] == 'Copiers']
    machines = technology_df.loc[technology_df['sub_category'] == 'Machines']
    phones = technology_df.loc[technology_df['sub_category'] == 'Phones']
    
    # top 3 profitable products per category, per product
    top3_accessories = accessories.sort_values(by='profit_per_product', ascending=False).head(3)
    top3_copiers = copiers.sort_values(by='profit_per_product', ascending=False).head(3)
    top3_machines = machines.sort_values(by='profit_per_product', ascending=False).head(3)
    top3_phones = phones.sort_values(by='profit_per_product', ascending=False).head(3)
    
    # data frame containing all 12 rows with top 3 products
    top3_df = pd.concat([top3_accessories, top3_copiers], axis=0)
    top3_df = pd.concat([top3_df, top3_machines], axis=0)
    top3_df = pd.concat([top3_df, top3_phones], axis=0)
    
    # the three least profitable products per category, per product
    bottom3_accessories = accessories.sort_values(by='profit_per_product', ascending=True).head(3)
    bottom3_copiers = copiers.sort_values(by='profit_per_product', ascending=True).head(3)
    bottom3_machines = machines.sort_values(by='profit_per_product', ascending=True).head(3)
    bottom3_phones = phones.sort_values(by='profit_per_product', ascending=True).head(3)
    
    # data frame containing all 12 rows with bottom 3 products 
    bottom3_df = pd.concat([bottom3_accessories, bottom3_copiers], axis=0)
    bottom3_df = pd.concat([bottom3_df, bottom3_machines], axis=0)
    bottom3_df = pd.concat([bottom3_df, bottom3_phones], axis=0)
    
    return top3_df, bottom3_df

def top_product_lines(df):
    '''
    Takes in the superstore dataframe and selects the best products
    as identified by the previous function, and then collects all observations involving each product_name under that brand.
    '''
    
    #Accessories, Copiers, Machines, Phones  
    technology_df = df.loc[df['category'] == 'Technology']
    
    canon_df = technology_df.loc[technology_df['product_name'].str.startswith('Canon', na=False)]
    ativa_df = technology_df.loc[technology_df['product_name'].str.startswith('Ativa', na=False)]
    lexmark_df = technology_df.loc[technology_df['product_name'].str.startswith('Lexmark', na=False)]
    logitech_df = technology_df.loc[technology_df['product_name'].str.startswith('Logitech', na=False)]
    maxell_df = technology_df.loc[technology_df['product_name'].str.startswith('Maxell', na=False)]
    plantronics_df = technology_df.loc[technology_df['product_name'].str.startswith('Plantronics', na=False)]
    polycom_df = technology_df.loc[technology_df['product_name'].str.startswith('Polycom', na=False)]
    konftel_df = technology_df.loc[technology_df['product_name'].str.startswith('Konftel', na=False)]
    mitel_df = technology_df.loc[technology_df['product_name'].str.startswith('Mitel', na=False)]
    
    top_product_lines = pd.concat([canon_df, ativa_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, lexmark_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, logitech_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, maxell_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, plantronics_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, polycom_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, konftel_df], axis=0)
    top_product_lines = pd.concat([top_product_lines, mitel_df], axis=0)
    
    return top_product_lines

def show_top_brands(top_product_lines):
    '''
    Takes in the previously established brand-based DataFrame and returns
    two histogram plots via a groupby brand method. The first plot lists
    the product inventory collectively, and the second shows the profitabilty
    for each brand in descending order.
    '''
    
    plt.rcParams["figure.figsize"] = (14,7)
    fig, axes = plt.subplots(nrows=1, ncols=2)
    
    
    plt.subplot(1,2,1)
    ax = top_product_lines.groupby('brand').size().sort_values(ascending=False).plot.bar(width=.6, ec='black', color=['lightcoral', 'firebrick', 'lightsalmon', 'sienna', 'khaki', 'darkseagreen', 'turquoise', 'steelblue', 'yellow'])
    plt.xticks(rotation=0)
    ax.set(title='Brand Inventory Size', xlabel='', ylabel='Value Counts')
    
    plt.subplot(1,2,2)
    ax = top_product_lines.groupby('brand').profit_per_product.mean().sort_values(ascending=False).plot.bar(width=.6, ec='black', color=['yellow', 'lightsalmon', 'steelblue', 'turquoise', 'darkseagreen', 'khaki', 'firebrick', 'lightcoral', 'sienna'])
    plt.xticks(rotation=0)
    ax.set(title='Average Profit per Brand (Descending Order)', xlabel='Dollars Per Product', ylabel='Average Profit Per Brand Product')
    
    fig.suptitle('Avita, Canon, and Konftel invite considerable revenue gain')
    
    fig.tight_layout()

def show_office_inventory_bad_cats(df):
    '''
    Display the worst sub-categories for our office supplies business model. 
    Also includes the grouby function used to look at the sub-categories profit per product
    within the entire office supplies supply
    '''  
    office_supplies = df.loc[df['category'] == 'Office Supplies']
    noffice = office_supplies.loc[office_supplies['sub_category'] == 'Supplies']
    soffice = office_supplies.loc[office_supplies['sub_category'] == 'Art']
    bloffice = office_supplies.loc[office_supplies['sub_category'] == 'Fasteners']
    
    print(f"{office_supplies.groupby('sub_category').profit_per_product.mean().sort_values(ascending=False)}")
    
    office_things = pd.concat([noffice, soffice], axis=0)
    office_things = pd.concat([office_things, bloffice], axis=0)
    office_things
    
    plt.rcParams["figure.figsize"] = (10,5)
    fig, axes = plt.subplots(nrows=1, ncols=2)
    
    
    plt.subplot(1,2,1)
    ax = office_things.groupby('sub_category').size().sort_values(ascending=False).plot.bar(width=.6, ec='black', color=['lightcoral', 'firebrick', 'lightsalmon', 'sienna', 'khaki', 'darkseagreen', 'turquoise', 'steelblue', 'yellow'])
    plt.xticks(rotation=0)
    ax.set(title='Office Supplies Inventory Size', xlabel='', ylabel='Value Counts')
    
    plt.subplot(1,2,2)
    ax = office_things.groupby('sub_category').profit_per_product.mean().sort_values(ascending=False).plot.bar(width=.6, ec='black', color=['lightcoral', 'firebrick', 'salmon', 'turquoise', 'darkseagreen', 'khaki', 'firebrick', 'lightcoral', 'sienna'])
    plt.xticks(rotation=0)
    ax.set(title='Average Profit per Class', xlabel='Dollars Per Product', ylabel='Average Profit Per Sub Category')
    
    fig.suptitle('Least Profitable Classes Among Office Supplies')
    
    fig.tight_layout()
