from src.data_cleaning import cleaning
from src.data_cleaning import remove_outliers
from src.model import train_test, linear_regression, decision_tree_regression, random_forest_regression, XGBoost_regression
import pandas as pd

# import and clean the data
raw_data = pd.read_csv(".\data\data_cleaned.csv", index_col=[0])
df = cleaning(raw_data)
outliners_to_remove = ["number of bedrooms", "livable area", "living area",
                       "total property area", "garden area", "total land area", "terrace area"]
df = remove_outliers(df, outliners_to_remove, 3)

# remove extreme prices (price > price.mean() + 4 * std)
df = remove_outliers(df, ["price"], 4)

# split the data and create X_train, X_test, y_train, y_test with normalized array
X_train, X_test, y_train, y_test = train_test(df, seed=21, test_size=0.2)

# Use Linear Regression
print("---Using Linear Regression---")
linear_regression(X_train, X_test, y_train, y_test)

# Use Decision Tree regressor
print("\n---Using Decision Tree---")
decision_tree_regression(X_train, X_test, y_train, y_test)

# Use Decision Tree regressor
print("\n---Using Random Forest---")
random_forest_regression(X_train, X_test, y_train, y_test)

# Use Decision Tree regressor
print("\n---Using RGBoost---")
XGBoost_regression(X_train, X_test, y_train, y_test)
