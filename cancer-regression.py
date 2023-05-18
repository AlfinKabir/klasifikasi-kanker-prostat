import pickle
import streamlit as st

# membaca model
cancer_model = pickle.load(open('cancer_model_regression.sav', 'rb'))

#judul web
st.title('Prediksi Kanker Prostat')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    radius = st.number_input('input nilai Radius karakteristik visual kanker')
    texture = st.number_input('input nilai Tekstur karakteristik visual kanker')
    perimeter = st.number_input('input nilai Keliling karakteristik visual kanker')

with col2 :
    area = st.number_input('input nilai Luas karakteristik visual kanker')
    smoothness = st.number_input('input nilai Kelembutan karakteristik visual kanker')
    compactness = st.number_input('input nilai Kepadatan karakteristik visual kanker')

cancer_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Kanker'):
    cancer_prediction = cancer_model.predict([[radius, texture, perimeter, area, smoothness, compactness]])

    if cancer_prediction[0] == 1:
        cancer_diagnosis = 'Pasien Terkena Kanker Prostat Ganas'
    else:
        cancer_diagnosis = 'Pasien Terkena Kanker Prostat Jinak'
    st.success(cancer_diagnosis)
