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




