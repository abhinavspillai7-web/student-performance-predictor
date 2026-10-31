import joblib
import streamlit as st
import pandas as pd
model=joblib.load("model.pkl")
st.title("student performence predictor")
studytime=st.number_input("enter study time:",min_value=1,max_value=4,step=1)
failures=st.number_input("enter no of failed exams:",min_value=0,max_value=3,step=1)
absences=st.number_input("enter no of times absent:",min_value=0,max_value=75,step=1)
G1=st.number_input("enter exam 1 marks:",min_value=0,max_value=20,step=1)
G2=st.number_input("enter exam 2 marks:",min_value=0,max_value=20,step=1)
input_data=pd.DataFrame({"studytime":[studytime],"failures":[failures],"absences":[absences],"G1":[G1],"G2":[G2]})
if st.button("predict"):
    prediction=round(model.predict(input_data)[0],2)
    st.success(f"predicted score:{prediction}")