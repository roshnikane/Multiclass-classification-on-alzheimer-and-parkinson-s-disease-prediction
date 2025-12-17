# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 09:40:50 2024

@author: rutuja kane
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu 
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score



st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")



#heart
heart_disease_model = pickle.load(open("C:/Users/rutuja kane/OneDrive/Desktop/multipal diseases prediction/saved model/heart_disease_model.sav",'rb'))

diabetes_model = pickle.load(open("C:/Users/rutuja kane/OneDrive/Desktop/multipal diseases prediction/saved model/diabetes_model.sav", 'rb'))

parkinsons_model = pickle.load(open("C:/Users/rutuja kane/OneDrive/Desktop/multipal diseases prediction/saved model/parkinsons_model.sav", 'rb'))

alzymner_disease_model = pickle.load(open("C:/Users/rutuja kane/OneDrive/Desktop/multipal diseases prediction/saved model/alzheimers_data.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'alzheimers prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'square'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
#alzyemer
if selected == 'alzheimers prediction':
    
    # Page title
    st.title('alzheimers preddiction using ML')
    
    # Getting the input data from the user
    # Columns for input fields
    col1, col2, col3 = st.columns(3)
    
   # with col1:
     #  PatientID = st.text_input('PatientID')
    
    with col1:
        Age = st.text_input('Age')
    
    with col2:
        Gender = st.text_input('Gender')
    
    with col3:
        Ethnicity = st.text_input('Ethnicity')
    
    with col1:
        EducationLevel = st.text_input('EducationLevel')
    
    with col2:
        BMI = st.text_input('BMI') 
    
    with col3:
        Smoking = st.text_input('Smoking')
    
    with col1:
        AlcoholConsumption = st.text_input('AlcoholConsumption')
        
    with col2:
        PhysicalActivity = st.text_input('PhysicalActivity')
      
    with col3:
        DietQuality = st.text_input('DietQuality')
      
    with col1:
        SleepQuality = st.text_input('SleepQuality')     
          
    with col2:
        FamilyHistoryAlzheimers = st.text_input('FamilyHistoryAlzheimers')
     
    with col3:
        CardiovascularDisease = st.text_input('CardiovascularDisease')
     
    with col1:
        Diabetes = st.text_input('Diabetes')
    
    with col2:
        Depression = st.text_input('Depression')
     
    with col3:
        HeadInjury = st.text_input('HeadInjury')
     
    with col1:
        Hypertension = st.text_input('Hypertension')
         
    with col2:
        SystolicBP = st.text_input('SystolicBP')
      
    with col3:
        DiastolicBP = st.text_input('DiastolicBP')
      
    with col1:
        CholesterolTotal = st.text_input('CholesterolTotal')
          
    with col2:
        CholesterolLDL = st.text_input('CholesterolLDL')
       
    with col3:
        CholesterolHDL = st.text_input('CholesterolHDL')
       
    with col1:
        CholesterolTriglycerides = st.text_input('CholesterolTriglyceridest')
       
    with col2:
        MMSE = st.text_input('MMSE')
       
    with col3:
        FunctionalAssessment = st.text_input('FunctionalAssessment')
         
    with col1:
        MemoryComplaints = st.text_input('MemoryComplaints')
        
    with col2:
        BehavioralProblems = st.text_input('BehavioralProblems')
        
    with col3:
        ADL = st.text_input('ADL') 
        
    with col1:
        Confusion = st.text_input('Confusion')    
     
    with col2:
        Disorientation = st.text_input('Disorientation')
         
    with col3:
        PersonalityChanges = st.text_input('PersonalityChanges')
        
    with col1:
        DifficultyCompletingTasks = st.text_input('DifficultyCompletingTasks')    
     
    with col2:
        Forgetfulness = st.text_input('Forgetfulness')
         
   # with col3:
     #  Diagnosis = st.text_input('Diagnosis')
    
    # Code for prediction
    alzheimers_diagnosis = ''
    
    # Creating a button for prediction
    if st.button('alzheimers Test Result'):
        try:
            user_input = [
                 Age, Gender,Ethnicity , EducationLevel, BMI, Smoking, AlcoholConsumption, PhysicalActivity, DietQuality,
                SleepQuality, FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury, Hypertension, SystolicBP, DiastolicBP, CholesterolTotal,
                CholesterolLDL, CholesterolHDL , CholesterolTriglycerides, MMSE, FunctionalAssessment, MemoryComplaints, BehavioralProblems,ADL, Confusion,Disorientation, PersonalityChanges,DifficultyCompletingTasks,
                Forgetfulness
            ]
            

            user_input = [float(i) for i in user_input]

            # Make prediction using the Alzheimer’s model
            alzheimer_prediction = alzymner_disease_model.predict([user_input])

            # Display the prediction result
            st.write(f'Alzheimer’s Prediction: {alzheimer_prediction}')

        except Exception as e:
            st.error(f"An error occurred: {e}")
            
