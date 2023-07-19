import pandas as pd
import numpy as np
from sklearn import preprocessing
def _convert(n):
    """get the first two digits of postalcode"""
    return int(n/100)


def cleaning(df):
    """Cleaning the dataframe by:
    1.replace True with 1, and False with 0
    2.replace categorical data with number
    3.scale the data"""

    #drop Nan rows
    df.drop(df["kitchen"].isna().index)

    #remove the properties without coordinates
    lon_la = (df["latitude"].isna()) | (df["longitude"].isna())
    df.drop(df.loc[lon_la].index,inplace=True)

    #remove castles
    castle = df[df["subtype of property"]=="CASTLE"].index
    df.drop(castle,inplace=True)

    #remove fully equipped kitchen column
    df.drop(columns=["fully equipped kitchen"],inplace=True)

    # add a column for the first two digits of the postal code
    df["digit"]=df["postalCode"].agg(_convert)

    #get dummies for catagorical data:
    get_dummies = ["Province","type of property","kitchen","subtype of property",
                   "state of the building","garden","terrace","digit"]
    df =pd.get_dummies(data=df, columns=get_dummies)

    #normalize these columns
    columns_to_normalize = ["latitude","longitude","living area","livable area",
                        "garden area","total property area","total land area",
                        "number of facades","number of bedrooms","terrace area"]
    df[columns_to_normalize]=preprocessing.minmax_scale(df[columns_to_normalize])
 
    #replace True with 1, and False with 0, turn them into numerical data
    df.replace([True,False],[1,0],inplace=True)
    print("Dataframe has been cleaned.")
    return df

def remove_outliners(df,columns,n_std):
    """Function to remove outliners"""
    for col in columns:
        mean = df[col].mean()
        sd = df[col].std()
        df = df[(df[col] <= mean+(n_std*sd))]
        df = df[(df[col] >= mean-(n_std*sd))]
    return df

