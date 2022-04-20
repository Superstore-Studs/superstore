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



