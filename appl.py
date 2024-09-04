import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import numpy as np


st.title('Данные о котировках компании Apple')

# Получить данные по тикеру (история)
apple = yf.Ticker('AAPL')
apple_data = apple.history(period='1d', start='2010-5-31', end='2020-5-31')

# Для наглядности
st.write(apple_data.head(5))

# Графики открытия/закрытия акций
st.write("""
### Графики открытия и закрытия акций

""")
plt.subplot(1,2,1)
plt.figure(figsize=(12, 6))
plt.title('График закрытия акций')
plt.plot(apple_data['Close'], color='r')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')
plt.grid()
st.pyplot(plt)

plt.subplot(1,2,2)
plt.figure(figsize=(12, 6))
plt.title('График открытия акций')
plt.plot(apple_data['Close'], color='b')
plt.xlabel('Дата')
plt.ylabel('Цена открытия')
plt.grid()
st.pyplot(plt)



# Еще одна статистика
st.write("""
### Статистика по котировкам

""")
st.write(apple_data.describe(include=np.number))
