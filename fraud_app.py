
import streamlit as st
st.title('Fraud Detection App')
st.subheader('Is this a Fraudulent transaction')
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


# Step1: Load the pickled model

model = open('sqw.pkl','rb') # read binary
clf = pickle.load(model)
model.close()

# Step2: Get input from front end user

# Create input fields for features
feature1 = st.number_input("V1", value=0.0)
feature2 = st.number_input("V2", value=0.0)
feature3 = st.number_input("V3", value=0.0)
feature4 = st.number_input("V4", value=0.0)
feature5 = st.number_input("V5", value=0.0)
feature6 = st.number_input("V6", value=0.0)
feature7 = st.number_input("V7", value=0.0)
feature8 = st.number_input("V8", value=0.0)
feature9 = st.number_input("V9", value=0.0)
feature10 = st.number_input("V10", value=0.0)
feature11 = st.number_input("V11", value=0.0)
feature12 = st.number_input("V12", value=0.0)
feature13 = st.number_input("V13", value=0.0)
feature14 = st.number_input("V14", value=0.0)
feature15 = st.number_input("V15", value=0.0)
feature16 = st.number_input("V16", value=0.0)
feature17 = st.number_input("V17", value=0.0)
feature18 = st.number_input("V18", value=0.0)
feature19 = st.number_input("V19", value=0.0)
feature20 = st.number_input("V20", value=0.0)
feature21 = st.number_input("V21", value=0.0)
feature22 = st.number_input("V22", value=0.0)
feature23 = st.number_input("V23", value=0.0)
feature24 = st.number_input("V24", value=0.0)
feature25 = st.number_input("V25", value=0.0)
feature26 = st.number_input("V26", value=0.0)
feature27 = st.number_input("V27", value=0.0)
feature28 = st.number_input("V28", value=0.0)
feature29 = st.number_input("V29", value=0.0)

# Step3: Collect the front end user input as model input data

data = {'V1':feature1, 
        'V2':feature2,
        'V3':feature3,
        'V4':feature4,
        'V5':feature5,
        'V6':feature6,
        'V7':feature7,
        'V8':feature8,
        'V9':feature9,
        'V10':feature10,
        'V11':feature11,
        'V12':feature12,
        'V13':feature13,
        'V14':feature14,
        'V15':feature15,
        'V16':feature16,
        'V17':feature17,
        'V18':feature18,
        'V19':feature19,
        'V20':feature20,
        'V21':feature21,
        'V22':feature22,
        'V23':feature23,
        'V24':feature24,
        'V25':feature25,
        'V26':feature26,
        'V27':feature27,
        'V28':feature28,
        'V29':feature29,
       }
input_data = pd.DataFrame([data])

# Step4: get the predictions and print the result

preds=clf.predict(input_data)[0]
if st.button('Predict'):
    if preds==1:
        st.error('Fraud')
    if preds<1:
        st.error('Legit')
