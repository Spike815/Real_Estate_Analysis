from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

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

    #split the data
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=seed, test_size=test_size)
    return X_train, X_test, y_train, y_test

def _show_result(model,X_train, X_test, y_train, y_test,title):
    """This function prints out the score and plot the result"""
    train_score = model.score(X_train,y_train)
    test_score = model.score(X_test,y_test)
    y_pred = model.predict(X_test)
    print(f"Train score is {train_score}")
    print(f"Test score is {test_score}")
    
    #plot result
    a = np.array([0,max(y_test)[0]])
    plt.scatter(y_test,y_pred)
    plt.plot(a,a,color="red")
    plt.xlabel("y_test")
    plt.ylabel("y_predict")
    plt.title(title)
    plt.show()


def linear_regression(X_train, X_test, y_train, y_test):
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    title = "Linear Regression"
    _show_result(reg,X_train, X_test, y_train, y_test,title)

def decision_tree_regression(X_train, X_test, y_train, y_test):
    reg = DecisionTreeRegressor(min_samples_leaf=10)
    reg.fit(X_train, y_train)
    title = "Decision Tree"
    _show_result(reg,X_train, X_test, y_train, y_test,title)

def random_forest_regression(X_train, X_test, y_train, y_test):
    reg =RandomForestRegressor(n_estimators=20)#using a reasonable n_estimators to speed up the process
    reg.fit(X_train, y_train)
    title = "Random Forest"
    _show_result(reg,X_train, X_test, y_train, y_test,title)

def XGBoost_regression(X_train, X_test, y_train, y_test):
    reg = XGBRegressor()
    reg.fit(X_train, y_train)
    title = "XGBoost"
    _show_result(reg,X_train, X_test, y_train, y_test,title)