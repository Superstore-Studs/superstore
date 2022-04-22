
[[Data Dictionary](#dictionary)]
[[Project Description](#project_description)]
[[Project Planning](#project_planning)]
[[Project Acquisition](#project_acquisition)]
[[Project Preparation](#project_preparation)]
[[Project Exploration](#project_exploration)]


## Data Dictonary
<a name="dictionary"></a>
[[Back to top](#top)]

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| product_id | Unique-identifier for each product | object |  
| customer_id | Unique-identifier for each customer | object
| order_id | Unique-identifier for each order | object
| ship_date | Day the order was shipped | datetime64
| ship_mode | Shipping time window | object
| segment | Customer segment: home office, consumer, corporate | object
| city | City the order was placed from | object
| state | State the order was placed form | object
| postal_code | Postal code of shipment address | float64
| sales | Dollars spent to obtain the order | float64
| quantity | Total number of a particular product sold | float64
| discount | The discount amount of the order (as applicable) | float64
| profit | The money gained or loss per order | float64
| customer_name | Full name of the customer | object
| product_name | Full name of the product | object
| category | Identifies as Technology, Office Supplies, or Furniture | object
| sub_category | More detailed subsections within the aforementioned three | object
| region_name | East, West, South, Central | object
| days_bw_shipment | Time between order date and shipping date | int64
| month | Month the order was placed | object
| year | Year the order was placed | int64
| profit_per_product | Profit divided by quantity per order | float64
| sales_per_product | Sales divided by quantity per order | float64
| brand | Brand name extracted from product_name | object

## Project Description and Goals
<a name="project_description"></a>

- Project description:
    - Obtain the superstore database as a team, select from the following prompts a mission:
        - 1. CEO: Which customer segment is the best? 
            - If we were going to shift our company to focus more specifically on one customer segment, which one should it be?
        - 2. VP of Marketing: What should we market?
            - We want to launch a new marketing campaign in the near future. How should we target with this campaign? Would you recomend targeting a specific type of customer, product line, or anything else?
        - 3. VP of Sales: What should our sales goals for 2018 be?
            - Are there any additional metrics should we track?
        - 4. VP of Product: Which product line should we expand?
            - Is there a product category that is particularly profitable for us? Does one or another stand out in terms of sales volume? Does this vary by customer segment?
        - Data retrieved from Codeup's MySQL database using a query contained in pd.read_sql.

- Goals:
    - A python script or scripts that automate the data wrangling
    - A notebook or notebooks that include a summary of your data wrangling and exploration
    - A slide deck including an executive summary slide with your recomendations and rationale for them. This should include at least 2 visualizations suitable for presentation.
    - A 5 minute presentation explaining our recomendation


# Project Planning
## <a name="project_planning"></a>
[[Back to top](#top)]

 **Plan** -> Acquire -> Prepare -> Explore 

- Tasking out how we plan to work through the pipeline.
- We have elected to address the Vice President of Product's questions. 

### Target variable
- Profit/profit_per_product

### Initial Focus
- Find distinctions among the Furniture, Office Supplies, and Technology to see how the superstore is profiting from each; noticing trends with this approach will guide our process
- Feature-engineer variables on a product-by-product basis, to show how much profit or sales are made in accordance with the quantity per order
    - Ensure we observe whether or not a discount has been applied before considering a product or subcategory as a boon or blunder
- Of course check immediately for data cleanliness and adjust accordingly.


### Project Outline:
- It generally goes like this: 
- Acquisiton via Codeup Database
- Preparation and pre-preocessing data using Pandas
    - Remove features
        - too many nulls?
        - not helpful to the quest?
    - Create features as needed
    - Handle null values
        - are these fixable or should they just be deleted?
    - Handle outliers
    - Split Data before EDA (not the case for this project)
- Exploratory Data Analysis
     - Visualization using MatPlotLib and Seaborn
- Statistical Testing
- Conclude with the results.

### Hypotheses
- Technology is the most advantageous but underutilized category.
- Technological product lines will be across-the-board worth expanding
- Furniture has been a dangeous and failing pursuit for the superstore and may make its image suffer
- Although most sales happen under office supplies, the profit potential for technology exceeds it. 

# Project Acquisition
<a name="project_acquisition"></a>
[[Back to top](#top)]

 Plan -> **Acquire** -> Prepare -> Explore 

Functions used can be found in wrangle.py. 

1. Acquire the superstore data from the from Codeup's MySQL server, then convert it into a Pandas DataFrame.
```
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
```

2. Observe the initial information
    - TAKEAWAYS:
        - There are no nulls and the date-time columns need to be converted to be used
            - No major inconsistencies in the data, but the columns need to be renamed.
```
# Convert column names to snake_case
    df.columns = [col.lower().replace(" ","_").replace("-","_") for col in df.columns]
```

    - There are redundant columns. Removing them is optional. 
3. Used UDF describe data to closely inspect contents.


# Project Preparation
<a name="project_preparation"></a>
[[Back to top](#top)]

 Plan -> Acquire -> **Prepare** -> Explore -> Model & Evaluate -> Deliver

Functions used can be found in wrangle.py. 

1. Clean-up:
    - Take note of the engineered-features
```
# Calculate days between shipment and order placement
    df['days_bw_shipment'] = df['ship_date'] - df['order_date']
# add minutes to the order_date to avoid duplicate values
    df['order_date_anew'] = df['order_date'] + pd.to_timedelta(df.groupby('order_date').cumcount(), unit='h')
# Create product-based columns
    df['profit_per_product'] = df.profit / df.quantity
# add sales per product
    df['sales_per_product'] = df.sales / df.quantity

```
    - Extracting the brand name was tedious, but worked nevertheless. 
    - Initially we split the data before exploration, but later saw this was futile.
    - There was no modeling, and so we ultimately consolidated the test and train sets. 
        - Although retroactively you could see it as us simply ompting not to split. 
        
# Project Exploration
<a name="project_exploration"></a>
[[Back to top](#top)]

 Plan -> Acquire -> Prepare -> **Explore** 

1. Questions we sought to address within Exploration: 
    - Which product line should we expand? 
    - Is there a product category that is particularly profitable for us? 
    - Does one or another stand out in terms of sales volume? 
2. Hypothesis Testing
                We rejected the null for each. 
    - Is Furniture worth keeping under consideration? 
        - No. Furniture profit on average is less than the overall profit avg. 
    - Is Technology a worthwhile business venture? 
        - Absolutely. Technology profit on average is far greater than overall profit avg. 
 CONCLUSION       
3. Answers to the three questions. 
    - Technology under the brands Ativa, Canon, and Konftel
    - Technology invites a lot of room for business growth
    - Office Supplies in their entirety far exceed the other two categories


[[Back to top](#top)]
