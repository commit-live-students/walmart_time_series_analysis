# Parameter Selection
We will be using Seasonal ARIMA method for time series forecasting.
(https://otexts.org/fpp2/seasonal-arima.html,
https://people.duke.edu/~rnau/seasarim.htm)

In this task, we will try to select the parameters for the model using AIC score.
(https://coolstatsblog.com/2013/08/14/using-aic-to-test-arima-models-2/)

## Write a function `q03_parameter_selection` that:
1. Takes the dataframe returned from q01_preprocessing, pdq and seasonal_pdq as parameters(pdq and s_pdq already pre-calculated in the notebook)
2. Iterates over the two lists pdq and s_pdq as order and seasonal_order parameters of SARIMAX(https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html) respectively
3. Finds the lowest AIC score among all the iterations.
4. Returns the pdq and s_pdq element associated with the lowest AIC

Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |              |  Dataframe to be loaded        |
| variable  |list            | compulsory    |               |  All the different possible combinations of order parameter of SARIMAX        |
| variable  |list            | compulsory    |               |  All the different possible combinations of seasonal_order parameter of SARIMAX        |


Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | list | Variable containing the optimum order(p,d,q) value for SARIMAX |
| variable | list | Variable containing the optimum seasonal_order(P,D,Q) value for SARIMAX |



