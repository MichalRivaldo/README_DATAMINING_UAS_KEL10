import streamlit as st


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)


with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )

    st.title("Customer Churn")

    st.info("""
Data Mining Project

Framework:
CRISP-DM

Metode:
XGBoost + K-Means
""")



st.title(
    "Customer Churn Prediction & Customer Segmentation"
)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Accuracy",
        "86.95%"
    )

with col2:
    st.metric(
        "ROC-AUC",
        "87.78%"
    )

with col3:
    st.metric(
        "Cluster",
        "3"
    )

st.divider()


st.subheader("Deskripsi Proyek")

st.markdown("""
Aplikasi ini dikembangkan untuk membantu menganalisis perilaku pelanggan bank melalui dua pendekatan Data Mining:

- **Prediksi Customer Churn** menggunakan algoritma **XGBoost**
- **Segmentasi Pelanggan** menggunakan algoritma **K-Means Clustering**

Tujuan utama proyek ini adalah mengidentifikasi pelanggan yang berpotensi berhenti menggunakan layanan bank (churn) serta mengelompokkan pelanggan berdasarkan karakteristiknya sehingga dapat membantu pengambilan keputusan bisnis.
""")

st.divider()


st.subheader("Hasil Terbaik")

st.markdown("""
### Model Klasifikasi Terbaik
**XGBoost Tuned**

- Accuracy : **86.95%**
- ROC-AUC : **87.78%**

### Model Clustering
**K-Means**

- Jumlah Cluster : **3**
- Segmentasi pelanggan berhasil dibagi menjadi:
    - Nasabah Aktif Multi-Produk
    - Nasabah Bernilai Tinggi Tidak Aktif
    - Nasabah Bernilai Tinggi Aktif
""")

st.divider()

st.subheader("Dataset")

st.write("""
Dataset yang digunakan adalah **Bank Customer Churn Dataset** yang berisi informasi pelanggan bank seperti:

- Credit Score
- Geography
- Gender
- Age
- Balance
- Number of Products
- Satisfaction Score
- Point Earned
- Status Churn (Exited)

Total data yang digunakan sekitar **10.000 data pelanggan**.
""")

st.divider()

st.subheader("Anggota Kelompok")

st.markdown("""
### 1. Michal Rivaldo Fresca Kurniawan
NIM: **24051214167**

### 2. Moh Viki Nur Arifin
NIM: **24051214171**
""")

st.divider()


st.success(
    "Framework yang digunakan dalam proyek ini adalah CRISP-DM (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, dan Deployment)."
)