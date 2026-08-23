import streamlit as st
import pandas as pd

# 1. App ka Title set kar rahe hain
st.title("🚀 Auto Data Analyzer & Dashboard")
st.write("Apni raw CSV file upload karo aur jadoo dekho!")

# 2. File Upload karne ka button bana rahe hain
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

# 3. Agar user ne file upload kar di hai, toh aage ka kaam shuru hoga
if uploaded_file is not None:
    
    # Data ko read kar rahe hain
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 1. Raw Data Preview")
    st.write("Yeh raha aapka original data:")
    st.dataframe(df.head()) # Shuru ki 5 rows dikhayega
    
    # 4. AUTO-CLEANING: Yahan hum missing (khaali) data ko hata rahe hain
    st.subheader("🧹 2. Auto-Cleaning Process")
    df_clean = df.dropna() 
    st.success(f"Cleaning Done! Original rows: {len(df)} | Clean rows: {len(df_clean)}")
    
    # 5. AUTO-ANALYSIS: Data ki summary nikal rahe hain (Average, Min, Max)
    st.subheader("📊 3. Data Summary")
    st.write(df_clean.describe()) # Yeh line apne aap maths calculate kar leti hai
    
    # 6. AUTO-DASHBOARD: Charts generate kar rahe hain
    st.subheader("📈 4. Auto-Generated Chart")
    
    # Sirf numbers wale columns dhoondh rahe hain taaki chart ban sake
    numeric_columns = df_clean.select_dtypes(include=['float64', 'int64']).columns
    
    if len(numeric_columns) > 0:
        # User ko option de rahe hain column select karne ka
        selected_col = st.selectbox("Chart ke liye column chunein:", numeric_columns)
        # Line chart bana rahe hain
        st.line_chart(df_clean[selected_col])
    else:
        st.warning("Chart banane ke liye data mein koi numbers nahi hain.")