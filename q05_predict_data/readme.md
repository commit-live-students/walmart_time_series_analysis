# Make Predictions
In this assignment, we will try to make future predictions of the weekly sales

## Write a function `q05_predict_data` that:
- Takes the dataframe returned from q01_preprocessing and model returned from q04_model as parameters
- Creates a new dataframe with index starting from '2012-11-01' to '2013-10-01' and columns same as the passed dataframe
- Concat the new dataframe with the passed dataframe
- Add a new column 'forecast' with the concatted dataframe
- Store the prediction of the model from '2012-10-01' to '2013-10-01' in the 'forecast' column
- Plot both 'Weekly_Sales' and 'Forecast' together to visualise the future prediction

Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |              |  Dataframe to be loaded        |
| variable | SARIMAXResultsWrapper| compulsory|              |Sarimax model which was fit upon the data|


Returns:
This function returns nothing. The plot should look similar to https://github.com/commit-live-students/walmart_time_series_analysis/blob/master/images/forecast.png
