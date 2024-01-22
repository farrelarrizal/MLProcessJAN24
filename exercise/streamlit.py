import streamlit as st
import time
import pandas as pd

st.title("Hello World")


with st.form(key='user_input'):
    nama = st.text_input('Masukkan Nama', help='Nama harus diisi')
    umur = st.number_input('Masukkan Umur', min_value=0, help='Umurmu harus diatas 0')
    submit = st.form_submit_button(label='Submit')
    
    if submit:
        with st.spinner('Loading...'):
            time.sleep(2)
        st.balloons()
        st.write('Nama: ', nama)
        st.write('Umur: ', umur)
        
    