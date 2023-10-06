# Product_Sales_Predictions
----------------------------------------------------------------------------
Using a variety of data to make predictions that will improve product sales 

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/8affcf03-e60d-450d-9467-cec5d0190dcf)
<sup>https://www.mageplaza.com/blog/where-to-sell-your-product.html</sup>

Author:  *Christina Brockway*
--------------------------------------------------------------------------------------------------
###What influences the sales of a product?  Is it shelf placement, type of store, visibility?  These are just a sample of variables to look at when predicting product sales.  This project uses a dataset with these variables and a few more.  By identifiying features that influence product sales, an establishment should be able to increase sales based on those features.  

The goal of this project is to design a model that will predict the sales of certain products, and to be able to use those predictions to increase sales overall.

###DataSource
https://datahack.analyticsvidhya.com/contest/practice-problem-big-mart-sales-iii/
For this dataset, there were 8523 records(rows) and 12 features(columns).

####Data Dictionary
| **Feature Name**          | **Description**                                                                                                                                                                                               | **Other info** |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Item_Identifier           | Product ID                                                                                                                                                                                                    | --             |
| Item_Weight               | Weight of Product                                                                                                                                                                                             | numeric (g)    |
| Item_Fat_Content          | Is the product: Low Fat or Regular                                                                                                                                                                            | nominal        |
| Item_Visibility           | Total display area of all products in the store allocated to the particular product                                                                                                                           | numeric (%)    |
| Item_Type                 | The category to which the product belongs: Dairy, Soft Drinks, Meat, Fruits&Vegatables, Household, Frozen Foods, Canned, Baking, Health&Hygiene, Breads, Hard Drinks, Starchy Food, Breakfast, Seafood, Other | nominal        |
| Item_MRP                  | Maximum Retail Price(list price) of the product                                                                                                                                                               | numeric        |
| Outlet_Identifier         | Store ID                                                                                                                                                                                                      | --             |
| Outlet_Establishment_Year | The year in which the store was established                                                                                                                                                                   | --             |
| Outlet_Size               | The size of the store in terms of ground area covered                                                                                                                                                         | numeric        |
| Outlet_Type               | Grocery Store, Supermarket Type 1, 2 or 3                                                                                                                                                                     | nominal        |
| Item_Outlet_Sales         | Sales of the product in the particular store.  This is the target variable to be predicted.                                                                                                                   | numeric        |
|                           |                                                                                                                                                                                                               |                |



-----------------------------------------------------------------------------------------------

##Methods
In order to prepare the data for machine learning, it needs to be cleaned and inspected. This anaylsis was done using the CRISP_DM for Machine Learning.  

The following processes were performed after cleaning:
1.  Exploratory Data Analysis
2.  Explanatory Visualization
3.  Machine Learning

####Exploratory Data Analysis and Explanitory Visualiztion
In this step each feature is looked at and compared to the Sales Price.  Using boxplots, histograms, and countplots the data is displayed in a clear and concise way to understand it. A heat map was also used to look for correlations.  Each feature is then evaluated for the impact it will have on sales.

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/e4b7c8e8-a6e7-45f7-a8f1-81bc8494fa7d)

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/5431206d-a4c7-4f48-a4b0-68fecd231503)

Each feature is then evaluated for the impact it will have on sales.

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/15ee170c-9ce9-4318-aba9-3fdc2504ad62)

####Machine Learning
The following models were used:
-  Linear Regression Model
-  Decision Tree Regressor Model
-  Random Forest Regressor Model

Each model was evaluated for performance.  In this case the Random Forest Regressor Model out performed the other models.  Looking at the R2 score the Random Forest model was able to predict 93%  of the  prices correct. The MSE shows the Random Forest model's ability to predict the price is much more accurate than in the Linear Regression model.  This model was able to predict product sales within $700. 
