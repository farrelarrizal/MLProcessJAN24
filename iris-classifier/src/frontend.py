import streamlit as st
import time
import requests

# Header
st.image('../assets/header-iris.png')
st.title('Iris Classifier App')
st.markdown('Created By: Farrel Arrizal | Batch Period: JAN 24')
st.divider()

# content
st.subheader('Just type the value, and get the result :sunglasses:')

with st.form(key='iris_form'):
    sepal_length = st.number_input('Sepal Length', min_value=0.0, help='Numeric Sepal Length')
    sepal_width = st.number_input('Sepal Width', min_value=0.0, help='Numeric Sepal Width')
    petal_length = st.number_input('Petal Length', min_value=0.0, help='Numeric Petal Length')
    petal_width = st.number_input('Petal Width', min_value=0.0, help='Numeric Petal Width')
    
    submit_button = st.form_submit_button(label='Predict')
    
    if submit_button:
        # do something
        data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }
        
        with st.spinner('Predicting...'):
            # do something
            response = requests.post('http://localhost:8000/predict', json=data)
            result = response.json()
            
            
        # if success
        if result['status'] == 'OK':
            st.success(result['prediction'])
            st.balloons()
        else:
            st.error(result['message'])
            
        
        

