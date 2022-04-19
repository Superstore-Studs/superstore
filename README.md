
[[Data Dictionary](#dictionary)]
[[Project Description](#project_description)]
[[Project Planning](#project_planning)]
[[Project Acquisition](#project_acquisition)]
[[Project Preparation](#project_preparation)]
[[Project Exploration](#project_exploration)]
[[Key Findings](#findings)]
[[Data Acquire, Prep, and Exploration](#wrangle)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]


## Data Dictonary
<a name="dictionary"></a>
[[Back to top](#top)]

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|  |  |  |  

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

 **Plan** -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

- Tasking out how I plan to work through the pipeline.

### Target variable
- ____

### Initial Focus
- _____
- _____
- _____


### Project Outline:
- Acquisiton via Codeup Database
- Preparation and pre-preocessing data using Pandas
    - Remove features
        - too many nulls?
        - not helpful to the quest?
    - Create features as needed
    - Handle null values
        - are these fixable or should they just be deleted?
    - Handle outliers
    - Split Data before EDA
- Exploratory Data Analysis
     - Visualization using MatPlotLib and Seaborn
- Statistical Testing
- Modeling: Primary focus is Regression in its many forms 
- Implementation via Test set
- Conclude with the results.

### Hypotheses
- ________
- ________
- ________
- ________

# Project Acquisition
<a name="project_acquisition"></a>
[[Back to top](#top)]

 Plan -> **Acquire** -> Prepare -> Explore -> Model & Evaluate -> Deliver

Functions used can be found in wrangle.py in git hub repo

1. Acquire the superstore data from the from Codeup's MySQL server, then convert it into a Pandas DataFrame.
```

```

2. Observe the initial information
    - TAKEAWAYS:
        -  
            - 
3. Used UDF describe data to closely inspect contents.


# Project Preparation
<a name="project_preparation"></a>
[[Back to top](#top)]

 Plan -> Acquire -> **Prepare** -> Explore -> Model & Evaluate -> Deliver

Functions used can be found in wrangle.py in git hub repo

1. Clean-up:
```

```

# Project Exploration
<a name="project_exploration"></a>
[[Back to top](#top)]

 Plan -> Acquire -> Prepare -> **Explore** -> Model & Evaluate -> Deliver

1. Separate train and use only that DF for EDA.
2. Correlation heatmaps 
    - 
    - 
    - 
3. Bi-variate and Multivariate visualizations via Seaborn


# Stat Tests
## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]
