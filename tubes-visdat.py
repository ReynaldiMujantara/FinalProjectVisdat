import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import mpld3

# Import Dataset
df = pd.read_csv("covid_vaccine_statewise.csv")
# slicing index 0 - 20
slicing = df.iloc[0:20]
# menampilkan dataframe
st.dataframe(slicing)

# membuat plot chart
fig, ax = plt.subplots()
# memasukan data pertama
ax.plot(slicing["Updated On"], slicing["Total Individuals Vaccinated"])
# memasukan data kedua
ax.plot(slicing["Updated On"], slicing["Male(Individuals Vaccinated)"])
# memasukan data ketiga
ax.plot(slicing["Updated On"], slicing["Female(Individuals Vaccinated)"])

# convert chart menjadi html
fig_html = mpld3.fig_to_html(fig)
# menampilkan chart menjadi html
components.html(fig_html, height=600)

# membuat scatter plot
fig2, ax2 = plt.subplots()
# memasukan data
ax2.scatter(slicing["Updated On"], slicing["Total Individuals Vaccinated"],)

# convert chart menjadi html
fig_html = mpld3.fig_to_html(fig2)
# menampilkan chart menjadi html
components.html(fig_html, height=600)

# membuat boxplot
fig3, ax3 = plt.subplots()
# memasukan data yang akan ditampilkan pada boxplot dalam 1 array
arrBoxplot = [slicing["Total Individuals Vaccinated"], slicing["Male(Individuals Vaccinated)"], slicing["Female(Individuals Vaccinated)"]]
# memasukan data ke dalam boxplot
ax3.boxplot(arrBoxplot, labels=["Total Individuals Vaccinated", "Male(Individuals Vaccinated)","Female(Individuals Vaccinated)"])

# convert chart menjadi html
fig_html = mpld3.fig_to_html(fig3)
# menampilkan chart menjadi html
components.html(fig_html, height=600)