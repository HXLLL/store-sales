# Let's design a Python library that encapsulates the functionality of training and predicting sales using the Prophet model.
# The library will consist of a `Model` class with methods for training, predicting, and updating the model with new data.

# First, we'll define the Model class with the necessary imports and methods.
# Since fbprophet and pandas are not directly executable in this environment, we will assume their availability for the purpose of this code.

# Note: Function and method calls will be commented out to adhere to the guidelines.

"""
import pandas as pd
from fbprophet import Prophet

class SalesModel:
    def __init__(self):
        # Initialize the model without any data
        self.model = None
        self.holidays = None

    def preprocess_data(self, sales_data, holidays_data, oil_data):
        # Convert date columns to datetime
        sales_data['date'] = pd.to_datetime(sales_data['date'])
        holidays_data['date'] = pd.to_datetime(holidays_data['date'])
        oil_data['date'] = pd.to_datetime(oil_data['date'])

        # Create a holidays dataframe for Prophet
        self.holidays = holidays_data[['date', 'type']].rename(columns={'date': 'ds', 'type': 'holiday'})

        # Merge oil prices into sales data
        sales_data = sales_data.merge(oil_data, on='date', how='left')
        sales_data['dcoilwtico'].fillna(method='ffill', inplace=True)
        sales_data['promotion'] = sales_data['onpromotion'].apply(lambda x: 1 if x > 0 else 0)
        return sales_data

    def train(self, sales_data, holidays_data, oil_data):
        # Preprocess data
        processed_data = self.preprocess_data(sales_data, holidays_data, oil_data)
        
        # Prepare the data for Prophet
        prophet_data = processed_data[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})

        # Initialize and fit the model
        self.model = Prophet(holidays=self.holidays)
        self.model.fit(prophet_data)

    def predict(self, periods):
        # Make future predictions
        future = self.model.make_future_dataframe(periods=periods, include_history=False)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat']]

    def update(self, new_sales_data, new_holidays_data, new_oil_data):
        # Preprocess new data
        processed_data = self.preprocess_data(new_sales_data, new_holidays_data, new_oil_data)
        
        # Update the model with new data
        new_prophet_data = processed_data[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})
        self.model.fit(new_prophet_data)

# Example usage (commented out):
# sales_data = pd.read_csv('sales_data.csv')
# holidays_data = pd.read_csv('holidays_data.csv')
# oil_data = pd.read_csv('oil_data.csv')
# model = SalesModel()
# model.train(sales_data, holidays_data, oil_data)
# predictions = model.predict(30)  # Predict next 30 days
# model.update(new_sales_data, new_holidays_data, new_oil_data)
"""

# This code snippet provides a class `SalesModel` with methods to train a model using historical sales data, predict future sales, and update the model with new data.
# The methods for preprocessing data ensure that the sales data, holidays, and oil prices are formatted correctly for use with the Prophet model.
# The `train` method initializes and fits the Prophet model with preprocessed data.
# The `predict` method uses the trained model to forecast future sales for a specified number of days.
# The `update` method allows for retraining the model with new data, accommodating changes in trends or additional information.

