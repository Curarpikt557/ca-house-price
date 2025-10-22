import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

st.title('California Housing Data (1990) by Junru Liu')
df = pd.read_csv('housing.csv')
price_filter = st.slider('(Minimal Median House Price):', 0.0, 500001.0, 200000.0)

ocean_filter = st.sidebar.multiselect(
    'loaction type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)

option = ['low','medium','high']
level = st.sidebar.radio('Choose income level', option,)
if level =='low':
    df = df[df.median_income<=2.5]
elif level =='medium':
     df = df[(df.median_income<=4.5) & (df.median_income>2.5)]
elif level =='high':
     df = df[df.median_income>4.5]


df = df[df.median_house_value>= price_filter]

df = df[df.ocean_proximity.isin(ocean_filter)]


st.map(df)

st.subheader(' median house value')
fig, ax = plt.subplots(figsize=(20, 5))
df.median_house_value.hist(bins=30)
st.pyplot(fig)

