# SARIMAX model implementation
In this task we will try to implement the model and validate it

## Write a function `q04_model_data` that :
- Takes the dataframe returned from q01_preprocessing, pdq and s_pdq returned from q03_parameter_selection as parameters
- Fits the model with data of ['Weekly_Sales'] till '2011-02-01'
- Predicts the data for remaining dates(using .get_prediction)
- Returns the RMSE of the predicted data and actual data




Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |              |  Dataframe to be loaded        |
| variable  |list element    | compulsory    |                |  Variable containing the optimum order(p,d,q) value for SARIMAX|
| variable  |list element    | compulsory    |                |  Variable containing the optimum seasonal order(P,D,Q) value for SARIMAX|


Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | float | RMSE between the true and predicted value of Weekly Sales |
| variable | SARIMAXResultsWrapper| Sarimax model which was fit upon the data|

