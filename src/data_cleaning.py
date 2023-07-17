import pandas as pd
import numpy as np
def cleaning(df):
    """Cleaning the dataframe by:
    1.replace True with 1, and False with 0\
    2.replace categorical data with number"""

    #get dummies for catagorical data:
    get_dummies = ["kitchen","type of property","postalCode","state of the building"]
    for prop in get_dummies:
        dummy_data=pd.get_dummies(df[prop])
        df = df.join(dummy_data)

    df.drop(columns=["fully equipped kitchen"],inplace=True)

    #replace True with 1, and False with 0, turn them into numerical data
    df.replace([True,False],[1,0],inplace=True)

    # fix the distributions of number of bedrooms
    df["number of bedrooms"] = np.log(df["number of bedrooms"] + 1)

    return df

def remove_outliners(df,columns,n_std):
    """function to remove outliners"""
    for col in columns:

        mean = df[col].mean()
        sd = df[col].std()
        df = df[(df[col] <= mean+(n_std*sd))]
        df = df[(df[col] >= mean-(n_std*sd))]
    return df

