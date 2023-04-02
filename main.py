import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import numpy as np
from joblib import load  #for loading saved model

#App header
st.header("Endometriosis Prediction App")
st.text_input("Enter your Name: ", key="name")

#creat the dataframe
data = pd.read_excel("CleanDataset0.xlsx")

# load model
best_model = load('rf.joblib')  #loading Fandom Forest Classifier model
#best_model = load('lr.joblib')  #loading Logistic Regression model
#best_model = load('svc.joblib')  #loading SVM Classification model

#list the dataframe by check
if st.checkbox('Show Training Dataframe'):
    data

#Get user input
feature1 = st.radio('Heavy / Extreme menstrual bleeding:', ('Yes', 'No'))
var1 = 1 if feature1 == 'Yes' else 0
feature2 = st.radio('Menstrual pain (Dysmenorrhea):', ('Yes', 'No'))
var2 = 1 if feature2 == 'Yes' else 0
feature3 = st.radio('Painful / Burning pain during sex (Dyspareunia) :', ('Yes', 'No'))
var3 = 1 if feature3 == 'Yes' else 0
feature4 = st.radio('Pelvic pain:', ('Yes', 'No'))
var4 = 1 if feature4 == 'Yes' else 0
feature5 = st.radio('Irregular / Missed periods:', ('Yes', 'No'))
var5 = 1 if feature5 == 'Yes' else 0
feature6 = st.radio('Cramping:', ('Yes', 'No'))
var6 = 1 if feature6 == 'Yes' else 0
feature7 = st.radio('Abdominal pain / pressure:', ('Yes', 'No'))
var7 = 1 if feature7 == 'Yes' else 0
feature8 = st.radio('Back pain:', ('Yes', 'No'))
var8 = 1 if feature8 == 'Yes' else 0
feature9 = st.radio('Painful bowel movements :', ('Yes', 'No'))
var9 = 1 if feature9 == 'Yes' else 0
feature10 = st.radio('Nausea:', ('Yes', 'No'))
var10 = 1 if feature10 == 'Yes' else 0
feature11 = st.radio('Menstrual clots:', ('Yes', 'No'))
var11 = 1 if feature11 == 'Yes' else 0
feature12 = st.radio('Infertility:', ('Yes', 'No'))
var12 = 1 if feature12 == 'Yes' else 0
feature13 = st.radio('Painful cramps during period:', ('Yes', 'No'))
var13 = 1 if feature13 == 'Yes' else 0
feature14 = st.radio('Pain / Chronic pain:', ('Yes', 'No'))
var14 = 1 if feature14 == 'Yes' else 0
feature15 = st.radio('Diarrhea :', ('Yes', 'No'))
var15 = 1 if feature15 == 'Yes' else 0
feature16 = st.radio('Long menstruation:', ('Yes', 'No'))
var16 = 1 if feature16 == 'Yes' else 0
feature17 = st.radio('Constipation / Chronic constipation:', ('Yes', 'No'))
var17 = 1 if feature17 == 'Yes' else 0
feature18 = st.radio('Vomiting / constant vomiting:', ('Yes', 'No'))
var18 = 1 if feature18 == 'Yes' else 0
feature19 = st.radio('Fatigue / Chronic fatigue:', ('Yes', 'No'))
var19 = 1 if feature19 == 'Yes' else 0
feature20 = st.radio('Painful ovulation:', ('Yes', 'No'))
var20 = 1 if feature20 == 'Yes' else 0
feature21 = st.radio('Stomach cramping:', ('Yes', 'No'))
var21 = 1 if feature21 == 'Yes' else 0
feature22 = st.radio('Migraines:', ('Yes', 'No'))
var22 = 1 if feature22 == 'Yes' else 0
feature23 = st.radio('Extreme / Severe pain:', ('Yes', 'No'))
var23 = 1 if feature23 == 'Yes' else 0
feature24 = st.radio('Leg pain:', ('Yes', 'No'))
var24 = 1 if feature24 == 'Yes' else 0
feature25 = st.radio('Irritable Bowel Syndrome (IBS) :', ('Yes', 'No'))
var25 = 1 if feature25 == 'Yes' else 0
feature26 = st.radio('Syncope (fainting, passing out):', ('Yes', 'No'))
var26 = 1 if feature26 == 'Yes' else 0
feature27 = st.radio('Mood swings:', ('Yes', 'No'))
var27 = 1 if feature27 == 'Yes' else 0
feature28 = st.radio('Depression:', ('Yes', 'No'))
var28 = 1 if feature28 == 'Yes' else 0
feature29 = st.radio('Bleeding:', ('Yes', 'No'))
var29 = 1 if feature29 == 'Yes' else 0
feature30 = st.radio('Lower back pain:', ('Yes', 'No'))
var30 = 1 if feature30 == 'Yes' else 0
feature31 = st.radio('Fertility Issues:', ('Yes', 'No'))
var31 = 1 if feature31 == 'Yes' else 0
feature32 = st.radio('Ovarian cysts:', ('Yes', 'No'))
var32 = 1 if feature32 == 'Yes' else 0
feature33 = st.radio('Painful urination:', ('Yes', 'No'))
var33 = 1 if feature33 == 'Yes' else 0
feature34 = st.radio('Headaches:', ('Yes', 'No'))
var34 = 1 if feature34 == 'Yes' else 0
feature35 = st.radio('Constant bleeding :', ('Yes', 'No'))
var35 = 1 if feature35 == 'Yes' else 0
feature36 = st.radio('Pain after Intercourse:', ('Yes', 'No'))
var36 = 1 if feature36 == 'Yes' else 0
feature37 = st.radio('Digestive / GI problems:', ('Yes', 'No'))
var37 = 1 if feature37 == 'Yes' else 0
feature38 = st.radio('IBS-like symptoms:', ('Yes', 'No'))
var38 = 1 if feature38 == 'Yes' else 0
feature39 = st.radio('Excessive bleeding:', ('Yes', 'No'))
var39 = 1 if feature39 == 'Yes' else 0
feature40 = st.radio('Anaemia / Iron deficiency:', ('Yes', 'No'))
var40 = 1 if feature40 == 'Yes' else 0
feature41 = st.radio('Hip pain:', ('Yes', 'No'))
var41 = 1 if feature41 == 'Yes' else 0
feature42 = st.radio('Vaginal Pain/Pressure:', ('Yes', 'No'))
var42 = 1 if feature42 == 'Yes' else 0
feature43 = st.radio('Sharp / Stabbing pain:', ('Yes', 'No'))
var43 = 1 if feature43 == 'Yes' else 0
feature44 = st.radio('Bowel pain:', ('Yes', 'No'))
var44 = 1 if feature44 == 'Yes' else 0
feature45 = st.radio('Anxiety:', ('Yes', 'No'))
var45 = 1 if feature45 == 'Yes' else 0
feature46 = st.radio('Cysts (unspecified):', ('Yes', 'No'))
var46 = 1 if feature46 == 'Yes' else 0
feature47 = st.radio('Dizziness:', ('Yes', 'No'))
var47 = 1 if feature47 == 'Yes' else 0
feature48 = st.radio('Malaise / Sickness:', ('Yes', 'No'))
var48 = 1 if feature48 == 'Yes' else 0
feature49 = st.radio('Abnormal uterine bleeding:', ('Yes', 'No'))
var49 = 1 if feature49 == 'Yes' else 0
feature50 = st.radio('Fever:', ('Yes', 'No'))
var50 = 1 if feature50 == 'Yes' else 0
feature51 = st.radio('Hormonal problems:', ('Yes', 'No'))
var51 = 1 if feature51 == 'Yes' else 0
feature52 = st.radio('Bloating:', ('Yes', 'No'))
var52 = 1 if feature52 == 'Yes' else 0
feature53 = st.radio('Feeling sick:', ('Yes', 'No'))
var53 = 1 if feature53 == 'Yes' else 0
feature54 = st.radio('Decreased energy / Exhaustion:', ('Yes', 'No'))
var54 = 1 if feature54 == 'Yes' else 0
feature55 = st.radio('Abdominal Cramps during Intercourse:', ('Yes', 'No'))
var55 = 1 if feature55 == 'Yes' else 0
feature56 = st.radio('Insomnia / Sleeplessness:', ('Yes', 'No'))
var56 = 1 if feature56 == 'Yes' else 0
feature57 = st.radio('Acne / pimples:', ('Yes', 'No'))
var57 = 1 if feature57 == 'Yes' else 0
feature58 = st.radio('Loss of appetite:', ('Yes', 'No'))
var58 = 1 if feature58 == 'Yes' else 0

#Make predictions
if st.button('Make Prediction'):
    inputs = np.expand_dims(
        [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30, var31, var32, var33, var34, var35, var36, var37, var38, var39, var40, var41, var42, var43, var44, var45, var46, var47, var48, var49, var50, var51, var52, var53, var54, var55, var56, var57, var58], 0)
    prediction = best_model.predict(inputs)
    #np.squeeze(prediction, -1)
    diagnosis = "Yes" if prediction == 1 else "No"
    print("final diagnosis: ", diagnosis)
    st.write(f"From our model prediction, the final diagnosis is: ",diagnosis)
    st.write(f"Thank you {st.session_state.name} testing our model! I hope you liked it.")