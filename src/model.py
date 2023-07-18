from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np

def train_test(df):
    """This function takes the dataframe as parameter. It converts the dataframe\
        to numpy array, selects the features, normalizes the array, and return the\
             training and testing data """
    columns_to_drop = ["id","type of property","subtype of property","locality","latitude","longitude","street","price","type of sale",
                   "state of the building","Gemeente","Province","Density","Area(per province)",
                   "Population( per province)","kitchen","price per sqr"]
    #convert the dataframe to numpy array
    X=df.drop(columns=columns_to_drop,axis=1).to_numpy()
    y=df.loc[:,"price"].to_numpy().reshape(-1,1)

    #Now normalize the data
    # X=preprocessing.normalize(X_raw)
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=21, train_size= 0.20)
    return X_train, X_test, y_train, y_test

