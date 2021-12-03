After loading the data, we set out to compute the correlation coefficient among all the columns (variables) of our dataset.
A "color coded" table made for a much more easy visual analysis.
With a focus on SalePrice as the dependent variable, we observed the relationship between the other variables and SalePrice from the table generated.
The results varied among the other variables and SalePrice. 
Some showed a strong positive correlation like the case of OverallQual and SalePrice as well as GrLivArea and SalePrice with each having a correlation coefficeint > 0.7.
Others had a moderate positive relation like the case of YearRemodAdd and SalePrice as well as YearBuilt and SalePrice among others with each having a correlation coefficient between 0.5 and 0.7.
For the purposes of our analysis we classified each variable with respect to their relationship with SalePrice per their correlation coefficient as follow

<= –0.70: A strong negative relationship

Between –0.50 and -0.70: A moderate negative relationship

Between –0.30 nd -0.50: A weak negative relationship

Between 0.30 and 0.50: A weak positive relationship

Between 0.50 and 0.70: A moderate positive relationship

>= 0.70: A strongpositive relationship

Only correlation between a variable and itself (for example SalePrice and SalePrice or YearBuilt and YearBuilt showed a perfect positive correlation. Thus coefficient = 1)
There was no case of a perfect negative relationship (thus coefficient = -1) or no correlation (thus coefficient = 0).


We further set out to generate the graph of the relationship as well as their respective Ordinary Least Square Summary with appropriate Python codes to have a better understanding of the relationship between the selected variables and SalePrice.
The OLS summary gave further details including R-squared (the proportion of the variance for SalePrice that is explained by the respective independent variable being considered) among others.
It also showed the possibility of the existence of a strong multicollinearity or other numerical problems just by how large the "condition number" in the summary data is.

Going forward, we would conduct further analysis based on the output from the coefficient table generated with emphasis on variables with moderate to strong positive or negative relationship with SalePrice.
This will be aimed at better predicting the Sale Price of a house given those variables.