from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

def train_test(df,seed,test_size):
    """This function takes the dataframe as parameter. It converts the dataframe\
        to numpy array, selects the features, normalizes the array, and return the\
             training and testing data """
    columns_to_drop = ["id","locality","street","price","type of sale"
                   ,"Density","Area(per province)",
                   "Population( per province)","price per sqr","open fire","postalCode","Gemeente"]
    #convert the dataframe to numpy array
    X=df.drop(columns=columns_to_drop,axis=1).to_numpy()
    y=df.loc[:,"price"].to_numpy().reshape(-1,1)

    #Now normalize the data
    # X=preprocessing.normalize(X_raw)
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=seed, test_size=test_size)
    return X_train, X_test, y_train, y_test

def _show_result(model,X_train, X_test, y_train, y_test):
    train_score = model.score(X_train,y_train)
    test_score = model.score(X_test,y_test)
    print(f"Train score is {train_score}")
    print(f"Test score is {test_score}")



def linear_regression(X_train, X_test, y_train, y_test):
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    _show_result(reg,X_train, X_test, y_train, y_test)

def decision_tree_regression(X_train, X_test, y_train, y_test):
    reg = DecisionTreeRegressor(min_samples_leaf=10)
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    _show_result(reg,X_train, X_test, y_train, y_test)

def XGBoost_regression(X_train, X_test, y_train, y_test):
    reg = XGBRegressor()
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    _show_result(reg,X_train, X_test, y_train, y_test)