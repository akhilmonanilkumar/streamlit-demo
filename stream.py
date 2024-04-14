import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import time

col_names=['column 1', 'column 2', 'column 3']

data = pd.DataFrame(np.random.randint(30, size=(30,3)), columns=col_names)


'Line Graph:'

st.line_chart(data)

'Bar Graph:'

st.bar_chart(data)

'Pie Chart Using Matplotlib:'

animals = ['cat', 'cow','dog']

heights=[30,150,80]

fig, ax = plt.subplots()

ax.pie(heights, labels=animals)

st.pyplot(fig)


rows = np.random.randn(1,1)

'Growing Line Chart :'

chart = st.line_chart(rows)

for i in range(1,100):
    new_rows = rows[0] + np.random.randn(1,1)
    chart.add_rows(new_rows)
    rows = new_rows
    time.sleep(2)


    values = np.random.randn(10)

    # 'MatplotLibs Line Chart :'


    # fig, ax = plt.subplots()
    # ax.plot(values)
    # st.pyplot(fig)


