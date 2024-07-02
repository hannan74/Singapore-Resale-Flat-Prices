# Singapore-Resale-Flat-Prices
## Overview
This project aims to develop a machine learning model that predicts the resale prices of flats in Singapore. The model is deployed as a user-friendly web application, enabling users to estimate the resale value of flats based on various factors. The project benefits both potential buyers and sellers in the Singapore housing market by providing insights into market trends and helping them make informed decisions.

### Features
#### Data Collection and Preprocessing: 
Historical resale flat transaction data from the Singapore Housing and Development Board (HDB) for the years 1990 to the present.

#### Feature Engineering: 
Extracts relevant features including town, flat type, storey range, floor area, flat model, and lease commence date. Additional features are created to enhance prediction accuracy.

#### Model Selection and Training: 
Utilizes machine learning models such as linear regression, decision trees, or random forests to predict resale prices.

#### Model Evaluation: 
Assesses the model's performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.

#### Streamlit Web Application: 
Provides a user-friendly interface for users to input flat details and receive resale price predictions.

#### Deployment on Render: 
Ensures the application is accessible to users over the internet.

#### Testing and Validation: 
Validates the application’s functionality and prediction accuracy through thorough testing.

#### Evaluation Metrics
Mean Absolute Error (MAE): 14474.266 Mean Squared Error (MSE): 458336904.601 Root Mean Squared Error (RMSE): 21408.804 R-squared (R²) Score: 0.984

### Usage
Open the Streamlit web application in your browser.

Enter the details of the flat including town, flat type, storey range, floor area, flat model, and lease commence date.

Click the "Predict" button to get the estimated resale price of the flat.
