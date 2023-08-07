import pandas as pd




def preprocess_new_data(input):
    """this function takes the input and returns a dataframe object which fits the machine learning model"""
  # convert the input to a dictionary
    df = pd.DataFrame([input])
    X=df.to_numpy()
    return X

