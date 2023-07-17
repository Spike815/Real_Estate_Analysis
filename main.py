from src.data_cleaning import cleaning
from src.data_cleaning import remove_outliners
from src.model import train_test
from sklearn.linear_model import LinearRegression
import pandas as pd

# import and clean the data
raw_data= pd.read_csv(".\data\data_cleaned.csv",index_col=[0])
df = cleaning(raw_data)
df = remove_outliners(df,["number of bedrooms","total property area","livable area","garden area"],3)

#split the data and create X_train, X_test, y_train, y_test with normalized array
X_train, X_test, y_train, y_test=train_test(df)

#fit the data
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
score = reg.score(X_train,y_train)
print(score)
