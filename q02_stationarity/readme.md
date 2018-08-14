# Test for Stationarity

A stationary time series is one whose statistical properties such as mean, variance, autocorrelation, etc. are all constant over time. 

Most statistical forecasting methods are based on the assumption that the time series can be rendered approximately stationary 

In the previous question, you plotted the 'Weekly Sales' and may have noticed the trend around Dec.(Sales peak) but overall the graph is approximately stationary

In this we will try to analyze the stationarity of Weekly_Sales column using both plotting and Dickey-Fuller Test(https://machinelearningmastery.com/time-series-data-stationary-python/)



## Write a function `q02_stationarity` that :
- Makes use of the previously created dataframe from q01_preprocessing.
- Plot the 'Weekly Sales' column and analyze it(particularly notice if there is any trend or seasonal trend)
- Use the rolling window method(with window=12) for mean and standard deviation and plot them to see whether the statistical properties are stationary 
- Use adfuller() function on Weekly_Sales column (use autolag='AIC') and store the result in pandas series with index
  ['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used']
- Prints the above created series(Make sure to loop out the final list)


Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| variable | dataframe | compulsory | | Dataframe to be loaded |

Returns:
There is no return parameter for the function. The plot should be similar to (link to be pasted)

#### Things to ponder upon
Although mostly flat, there is a a very small upward trend in mean

Also, the test statistic is a little different than the critical values owing to the trend mentioned above


#### Note:
Though in this particular task, we don't really need to make the data stationary, you can check out the different ways to make it stationary with this link-


