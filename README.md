# Product_Sales_Predictions
----------------------------------------------------------------------------
Improving product sales by predicting what influences them. 

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/8affcf03-e60d-450d-9467-cec5d0190dcf)
<sup>https://www.mageplaza.com/blog/where-to-sell-your-product.html</sup>

Author:  *Christina Brockway*
--------------------------------------------------------------------------------------------------
### What influences the sales of a product?  Is it shelf placement, the type of store, maybe visibility?  These are just an example of variables to look at when predicting product sales.  This project uses a dataset with these product variables and a few more.  
### By identifiying features that influence product sales, an establishment should be able to increase sales based on those features.  

The goal of this project is to design a model that will predict the sales of  products based on available features, and to be able to use those predictions to increase sales.

## DataSource
https://datahack.analyticsvidhya.com/contest/practice-problem-big-mart-sales-iii/

For this dataset, there were 8523 records(rows) and 12 features(columns).

### Data Dictionary
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

## Methods
In order to prepare the data for machine learning, it needs to be cleaned and inspected. This anaylsis was done using the CRISP_DM for Machine Learning.  

The following processes were performed after cleaning:
1.  Exploratory Data Analysis
2.  Explanatory Visualization
3.  Machine Learning

### Exploratory Data Analysis and Explanitory Visualiztion
In this step each feature is looked at and compared to the Sales Price.  Using boxplots, histograms, and countplots the data is displayed in a clear and concise way to understand it. A heat map was also used to look for correlations.  

The following graphs illustrate the sales amount for products in the stores.  Examples would be meats,  dairy, electronics.... The graph shows a count of the number of products in order from most to least.  The boxplot below the first graph is another way of showing the distribution of the number of products. The boxplot is a good way of identifying the presence of outlier data numbers.  These outliers can then be dealt with to avoid skewing the model.

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/e4b7c8e8-a6e7-45f7-a8f1-81bc8494fa7d)


Each feature is then evaluated for the impact it will have on sales.  The following graph shows the four types of supermarkets and how much those supermarkets have sold in dollars.  Supermarket types 1 and 3 have consistantly sold the largest amount.  Looking at what these markets sell and how they market thier products is one way of improving sales.

![image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/15ee170c-9ce9-4318-aba9-3fdc2504ad62)

###  Machine Learning
The following models were used:
-  Linear Regression Model
-  Random Forest Regressor Model
-  Decision Tree Regressor Model

## Looking at Feature Importance

**The top 3 most impactful features using this model are Outlet_Identifier, Item_Type, and Item_MRP.**

  -  Outlet_Identifier: This is the unique identifier for each outlet. This feature is the most impactful on predeicting Outlet_Item_Sales. Depending on the Outlet, some are better than others at producing high sales numbers.

  -  Item_Type: This is the type of item that is being sold. This feature is made up of values like seafood, dairy, meats, etc... Seafood and Starchy food seem to be the best at producing high sales numbers.

  -  Item_MRP: This is the maximum retail price of the object. As this value goes up, the sales numbers will increase by 10.

![Top 5 DT image](https://github.com/SeeBee8/Product_Sales_Predictions/assets/141530991/2fce6414-862c-4508-96ab-89bfcb7b8610)
**The top most importance features according to this model are the Item_MRP, Outlet_Type, Outlet_Identifier, Item_Visibilty, and Item_Weight.**

These features show they are important in the ability for both the Linear Regression Model and the Decision Tree Model.  Outlet_Type and Outlet_Identifier have a high number of values that are used for the model and came up multiple times in the importance.  It may be worth keeping these features, but possibly spitting them into smaller subsets.

----------------------------------------------------------
## Evaluation

Each model was evaluated for performance using a comparison of statistics for the default model and the prediction model (R2 score, MAE, and MSE metrics). The data was then further looked at for the impact each feature had on the model.

In this case the Decision Tree Regressor Model out performed the other models.  Looking at the R2 score the Decision Tree model was able to predict 60%  of the prices correctly. The MSE shows the Decistion Tree model's ability to predict the price is much more accurate than other models.  This model was able to predict product sales within $700. 

**What ways could I improve this project**
  - *After looking at the important features, I would remove some of the other features that have a high cardinality.  With these features eliminated there may be a different dynamic to the dataset.*  
  - *I would consider dividing up some of the features with high cardinality into sub-groups to see how they truly impact the Item_Outlet_Sales.*
  - *There could be other ways to tune the model to change the bias*
  - *If the features that have a lot of NaN values that show little impact on predictions, consider dropping those columns, as there is a lot of missing information in this dataset.*

## **Overall Recommendations**

1.  Look at Outlets OUT27, OUT13, OUT17 to see how they differ from OUT10 and OUT19
  -  These differences should show why one outlet type outperforms the another

2.  Stock more items types that are bought more often the top 5 are:
  -  Dairy
  -  Starchy foods
  -  Fruits and Vegetables
  -  Snack foods
  -  Frozen foods

3.  Look at item with higher maximum retail prices.  These items will increase sales numbers by approximately 10. Having more items with high retail prices will increase sales.

4.  Look at supermarket types 1 and 3 and see how their products differ from types 2 and 4.
  - Similar to looking at outlet types, these differences should show why one supermarket type outperforms another.

5.  Continue to evaluate features with the model to monitor changes and see how they influence sales. 


