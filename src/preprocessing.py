import pandas as pd
# test input
test = {
    "type_of_property": "HOUSE",
    "subtype_of_property": "VILLA",
    "number_of_bedrooms": 2,
    "living_area": 60,
    "furnished": 0,
    "terrace": 0,
    "terrace_area": 0,
    "garden": 1,
    "garden_area": 20,
    "total_property_area": 120,
    "total_land_area": 300,
    "number_of_facades": 2,
    "swimming_pool": 0,
    "state_of_the_building": "GOOD",
    "Province": "Oost-Vlaanderen",
    "kitchen": "Not equipped",
    "postalcode": 90
}


def _convert(n):
    return int(n/100)


def preprocess_new_data(input):
    """this function takes the input and returns a dataframe object which fits the machine learning model"""
  # convert the input to a dictionary
  # [input["data"]]
    df = pd.DataFrame([input])
  # take the first two digits of postalcode
    # df.replace([True, False],[1,0])
    # df.rename(columns={"postalcode": "digit"}, inplace=True)
    # df["digit"] = int(df["digit"]/100
    X=df.to_numpy()
    return X

# from src.prediction import predict_new_data
# print(predict_new_data(preprocess_new_data(test)))