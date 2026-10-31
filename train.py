import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
import joblib
df=pd.read_csv("student-mat.csv",sep=";")
x=df[["studytime","failures","absences","G1","G2"]]
y=df["G3"]
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
joblib.dump(model,"model.pkl")
