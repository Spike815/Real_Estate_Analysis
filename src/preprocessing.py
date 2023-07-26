import json
import pandas as pd
import joblib

input = {
    "data": {
        "type of property":"HOUSE",
         "subtype of property":"MIXED_USE_BUILDING",
         "number of bedrooms":3,
         "living area":120,
         "furnished": True,
         "terrace":True,
         "terrace area":15,
         "garden":True,
         "garden area":30,
         "total property area":500,
         "total land area":800,
         "number of facades":2,
         "swimming pool":False,
         "state of the building":"GOOD",
         "Province": "Oost-Vlaanderen",
         "kitchen":"Not equipped",
         "postalcode":9010}
  }
def _convert(n):
    return int(n/100)

def preprocess_new_data(input):
    """this function takes the input and returns a dataframe object which fits the machine learning model"""
  #convert the input to a dictionary
    df = pd.DataFrame([input["data"]])
  #take the first two digits of postalcode
    df["postalcode"]=df["postalcode"].agg(_convert)
    df.replace([True, False],[1,0])
    df.rename(columns={"postalcode":"digit"},inplace=True)
    return df.to_numpy()

X = preprocess_new_data(input)
