# Data loading and Preprocessing

- Feature preprocessing techniques have significant influence on forecasting accuracy, therefore are essential in a forecasting model. 


## Write a function `q01_preprocesssing` that :
- Takes the dataset and reformats the date column to '%Y-%m-%d'
- Creates Year, Month, Day columns from the date column
- Makes Date column the index and drops the date column
- Susbets the dataframe to only include data of Store '1'
- Resamples the data on monthly basis('MS')
(https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.resample.html,
http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases)
- Returns the new dataframe  


Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |               |  Dataframe to be loaded        |

Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe with above operations inculcated |
