Concerning the Database's Categories:

The superstore carries three categories: Furniture, Office Supplies and Technology      
There are 17 total sub-categories

Furniture has four: Bookcases, Chairs, Furnishings, Tables       
Office Supplies consist of nine: Appliances, Art, Binders, Envelopes, Fasteners, Labels, Paper, Storage, Supplies        
Technology has the final four: Accessories, Copiers, Machines, Phones         

Subcompartmentalizing these should serve to be highly useful. Creating dummies for the categories would be a breeze, and only
add one extra column, as 'Category" will be dropped along with the first dummy. 
Creating dummies based on the 17 sub labels will only be confusing in exploration, but after we have selected the, let's say,
top 7-or-so sub-categories, then dummies would be useful. 

There are time gaps among our splits:         
Time gaps for Train:         
Number of rows: 310         
Number of days between first and last day: 874 days         
           
Time gaps for Validate:         
Number of rows: 159           
Number of days between first and last day: 387 days          
          
Time gaps for Test:          
Number of rows: 103          
Number of days between first and last day: 198 days          
          
These present gaps among our index indicate that the current datetime data is not continuous, which may be tricky to work with. To resolve these temporal discrepancies, we could use the average daily sales values per month instead, using the start of each month as the timestamp. A resampling would accomplish this but may also cause distortions. Additionally, the implications for how that would change the index are massive, so I'm not sure what to make of it. It's something that requires deeper understanding and further research. Time may not permit this, but if it does and the outcomes are desirable, then we can apply the same resampling method to the validate and test sets as well.
          
As of 1 p.m. I am still in the early stages of exploration and have not applied any statistical tests to the big three questions, which are          
### Which products are most profitable?          
### Which products had outstanding sales volumes?          
### Does product type vary by customer/region?          
          
##### Bear in Mind
#### Each of these Sales are on U.S. territory
So we can apply our knowledge of major sales days or trends in months 
##### Take for example: 
* January 1st New Year's Day Sales (typically runs for 2-4 days) 
* President's Day (3rd Monday of February)
* Memorial Day (Last Monday in May)
* Jun 21st Amazon Prime Day
* July 4th Independence Day
* August 8th National Bargain Hunting Week
* Labor Day (1st Monday in September)
* Columbus Day (1st Monday in October)
* Oct 12 Fair Trade Month
* November 25th-ish Black Friday (the day after Thanksgiving)
* November 28th-ish Cyber Monday (Monday following Black Friday)

We can anticipate these days will have discounts applied. Perhaps sometimes excessively, other times maybe less competitively than needed. 

##### Speaking of Competition
For certain products, months such as March Madness (and the beginning of the year more generally) as well as October represent tremendous opportunities
for sales fluctuations in accordance with marketing trends as they pertain to sports. 

# Some remarks on distribution: Absolute Frequencies

### If March Madness was worth consideration, it does not reflect in our sales. The three months with the least sales are
* March ~6%
* January ~4%
* February ~3%

The months we have the greatest number of sales are:
* December ~14%
* November and September ~ 13%
* April ~9%
The drop in October is curious, 7% 

### There's been a rise in sales between 2014 and 2016. 
2014 accounts for 27% of the dataframe; 2015 30%; and 
2016 ~43%. 

### We sell the most in the East and Western regions
.320 and .319 respectively. Central sees .213 and the South lags with .148. 

### We primarily ship Standard Class at ~.55%
Same day delivery is rare, at 5%

#### Most of our sales are Consumer segmented .563
Corporate .269, home offivce .168

#### We are primarily selling Office Supplies: 60% of our sales
Furniture comprises 20% of train and Technology is about 19%
Even so, the dispersions among sub categories is interesting. 

    Column: sub_category
    Binders 0.147
    Paper 0.128
    Storage 0.099
    Furnishings 0.090
    Phones 0.086
    Accessories 0.082
    Art 0.082
    Chairs 0.058
    Appliances 0.039
    Labels 0.037
    Tables 0.036
    Envelopes 0.030
    Fasteners 0.028
    Supplies 0.019
    Bookcases 0.019
    Machines 0.013
    Copiers 0.006
 
 ### We mostly sell quantities from 2-5 and rarely sell 10 or more.
     Column: quantity
     2.0 0.241
     3.0 0.240
     4.0 0.126
     5.0 0.112
     1.0 0.082
     6.0 0.065
     7.0 0.064
     8.0 0.027
     9.0 0.024
     10.0 0.006
     14.0 0.005
     13.0 0.003
     12.0 0.003
     11.0 0.

### Discounts rarely make a difference, and are rarely given, except for at 20% 

    Column: discount
    0.00 0.472
    0.20 0.379
    0.70 0.049
    0.80 0.026
    0.40 0.023
    0.30 0.019
    0.60 0.011
    0.50 0.009
    0.10 0.006
    0.15 0.002
    0.45 0.002
    0.32 0.002

### Mid-week sells are considerably less common

    Column: day
    Monday 0.197
    Sunday 0.183
    Saturday 0.180
    Friday 0.177
    Thursday 0.129
    Tuesday 0.099
    Wednesday 0.036



