import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import streamlit as st

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

st.title("PENAMBANGAN DATA")
st.write("By: Indyra Januar - 200411100022")
st.write("Grade: Penambangan Data C")
upload_data, preporcessing, modeling, implementation = st.tabs(["Upload Data", "Prepocessing", "Modeling", "Implementation"])


with upload_data:
    st.write("""# Upload File""")
    st.write("Dataset yang digunakan adalah Heart Attack Dataset yang diambil dari https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset")
    st.write("Heart Attack (Serangan Jantung) adalah kondisi medis darurat ketika darah yang menuju ke jantung terhambat.")
    uploaded_files = st.file_uploader("Upload file CSV", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write("Nama File Anda = ", uploaded_file.name)
        st.dataframe(df)


with preporcessing:
    st.write("""# Preprocessing""")

    "### There's no need for categorical encoding"
    x = df.iloc[:, 1:-1].values
    y = df.iloc[:, -1].values
    x,y

    "### Splitting the dataset into training and testing data"
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 0)
    st.write("Shape for training data", x_train.shape, y_train.shape)
    st.write("Shape for testing data", x_test.shape, y_test.shape)

    "### Feature Scaling"
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    x_train,x_test

with modeling:
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=4)
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    st.write("""# Modeling """)
    st.subheader("Berikut ini adalah pilihan untuk Modeling")
    st.write("Pilih Model yang Anda inginkan untuk Cek Akurasi")
    naive = st.checkbox('Naive Bayes')
    kn = st.checkbox('K-Nearest Neighbor')
    des = st.checkbox('SVM')
    mod = st.button("Modeling")

    # NB
    model = GaussianNB()
    model.fit(x_train, y_train)

    predicted = model.predict(x_test)

    akurasi_nb = round(accuracy_score(y_test, predicted)*100)

    #KNN
    model = KNeighborsClassifier(n_neighbors = 1)  
    model.fit(x_train, y_train)
    predicted = model.predict(x_test)
    
    st.write(confusion_matrix(y_test, predicted))
    akurasi_knn = round(accuracy_score(y_test, predicted.round())*100)

    #SVM
    model = SVC()
    model.fit(x_train, y_train)
    
    predicted = model.predict(x_test)
    akurasi_svm = round(accuracy_score(y_test, predicted)*100)

    if naive :
        if mod :
            st.write('Model Naive Bayes accuracy score: {0:0.2f}'. format(akurasi_nb))
    if kn :
        if mod:
            st.write("Model KNN accuracy score : {0:0.2f}" . format(akurasi_knn))
    if des :
        if mod :
            st.write("Model SVM score : {0:0.2f}" . format(akurasi_svm))