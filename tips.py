import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import datetime as dt
import numpy as np
import yfinance as yf

st.title('Чаевые')

# Шаг 1. Загрузка CSV файла
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')


st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

# Создай столбец time_order. Заполни случайной датой от 2023-01-01 до 2023-01-31
start_date = dt.datetime(2023, 1, 1)
end_date = dt.datetime(2023, 1, 31)

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = np.random.randint(0, days_between_dates + 1)
    random_date = start_date + dt.timedelta(days=random_number_of_days)
    return random_date

tips['time_order'] = [generate_random_date(start_date, end_date) for _ in range(len(tips))]

# Построй график показывающий динамику чаевых во времени
st.sidebar.write('''### Динамика чаевых во времени''')

st.write('''### Динамика чаевых во времени''')

fig, ax = plt.subplots(figsize=(10,6))
scatter = ax.scatter(tips['tip'], tips['time_order'], c=tips['tip'], cmap='ocean', alpha=0.7)
plt.colorbar(scatter, label='Чаевые')
ax.set_xlabel('Чаевые')
ax.set_ylabel('Дата')
plt.grid()
st.pyplot(fig)

filename1 = 'scatter.png'
fig.savefig(filename1)

st.sidebar.download_button(label='Скачать график',
                   data=filename1,
                   file_name='scatter.png',
                   mime='image/png')

# total_bill hist
st.sidebar.write('''### Гистограмма "Total bill"''')
st.write('''### Гистограмма "Total bill"''')

plt.figure(figsize=(12, 6))
total_bill_hist = sns.displot(tips['total_bill'], kind='hist', alpha=0.6, color='b')
plt.xlabel('Сумма')
plt.ylabel('Частота')
plt.grid()
st.pyplot(total_bill_hist)

filename2 = 'total_bill_hist.png'
fig.savefig(filename2)

st.sidebar.download_button(label='Скачать график',
                   data=filename2,
                   file_name='total_bill_hist.png',
                   mime='image/png')

# Сделай аналогичный график используя многофункциональный метод displot
# Поиграйся с другими формами отображения меняя параметр параметр kind

st.write('''### Гистограмма "Total bill"('kde')''')
st.sidebar.write('''### Гистограмма "Total bill"('kde')''')
plt.figure(figsize=(10, 6))
total_bill_kde = sns.displot(tips['total_bill'], kind='kde', alpha=0.6, color='b')
plt.xlabel('Сумма')
plt.ylabel('Частота')
plt.grid()
st.pyplot(total_bill_kde)

filename3 = 'total_bill_kde.png'
fig.savefig(filename3)

st.sidebar.download_button(label='Скачать график',
                   data=filename3,
                   file_name='total_bill_kde.png',
                   mime='image/png')

#Нарисуйте scatterplot, показывающий связь между total_bill and tip¶
st.write('''### Зависимость счета от чаевых''')
st.sidebar.write('''### Зависимость счета от чаевых''')
fig, ax = plt.subplots(figsize=(10,6))
totalbil_vs_tip = ax.scatter(tips['tip'], tips['total_bill'],
                             c=tips['tip'], cmap='gist_earth', alpha=0.7)
ax.set_xlabel('Чаевые')
ax.set_ylabel('Счет')
plt.grid()
st.pyplot(fig)

filename4 = 'totalbil_vs_tip.png'
fig.savefig(filename4)

st.sidebar.download_button(label='Скачать график',
                   data=filename4,
                   file_name='totalbil_vs_tip.png',
                   mime='image/png')

#Сделай аналогичный график используя многофункциональный метод relplot
st.write('''### Зависимость счета от чаевых(replot)''')
st.sidebar.write('''### Зависимость счета от чаевых(replot)''')
plt.figure(figsize=(10, 15))
totalbil_vs_tip_rel = sns.relplot(data=tips, x='total_bill', y='tip',
                                  kind='scatter', hue='tip', palette='gist_earth',
                                  alpha=0.6)
plt.xlabel('Чаевые')
plt.ylabel('Счет')
plt.grid()
st.pyplot(totalbil_vs_tip_rel)

filename5 = 'totalbil_vs_tip_rel.png'
fig.savefig(filename5)

st.sidebar.download_button(label='Скачать график',
                   data=filename5,
                   file_name='totalbil_vs_tip_rel.png',
                   mime='image/png')

#Нарисуйте 1 график, связывающий total_bill, tip, и size
st.write('''### График зависимости между общим счетом, чаевыми и размером группы''')
st.sidebar.write('''### График зависимости между общим счетом, чаевыми и размером группы''')
fig, ax = plt.subplots(figsize=(10,6))
bill_tip_size = sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    size='size',
    hue='size',
    palette='rainbow_r',
    sizes=(20,100),
    alpha=0.6,
    ax=ax)
ax.set_xlabel('Общий счет')
ax.set_ylabel('Чаевые')
st.pyplot(fig)

filename6 = 'bill_tip_size.png'
fig.savefig(filename6)

st.sidebar.download_button(label='Скачать график',
                   data=filename6,
                   file_name='bill_tip_size.png',
                   mime='image/png')

#Покажите связь между днем недели и размером счета
st.write('''### Связь между днем недели и размером счета''')
st.sidebar.write('''### Связь между днем недели и размером счета''')
fig, ax = plt.subplots(figsize=(10,6))
tips_bill_bar = sns.barplot(data=tips, x='day', y='total_bill',
                       palette='flare', legend=False, hue='day')
ax.set_xlabel('День недели')
ax.set_ylabel('Сумма счета')
st.pyplot(fig)

filename7 = 'tips_bill_bar.png'
fig.savefig(filename7)

st.sidebar.download_button(label='Скачать график',
                   data=filename7,
                   file_name='tips_bill_bar.png',
                   mime='image/png')

#Нарисуйте scatter plot с днем недели по оси Y, чаевыми по оси X, и цветом по полу¶
st.write('''
         ### График зависимости между общим счетом и днем недели по полу
        ''')

st.sidebar.write('''
         ### График зависимости между общим счетом и днем недели по полу
        ''')

tips['color'] = tips['sex'].map({'Male' : 'blue', 'Female' : 'red'})

fig, ax = plt.subplots(figsize=(10,6))
color_bill_day = sns.scatterplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex',
    palette={'Male' : 'blue', 'Female' : 'red'},
    sizes=(20,200),
    alpha=0.6
)
ax.set_xlabel('День недели')
ax.set_ylabel('Общий счет')
st.pyplot(fig)

filename8 = 'color_bill_day.png'
fig.savefig(filename8)

st.sidebar.download_button(label='Скачать график',
                   data=filename8,
                   file_name='color_bill_day.png',
                   mime='image/png')

#Нарисуйте box plot c суммой всех счетов за
#каждый день, разбивая по time (Dinner/Lunch)¶
st.write('''
         ### Счета за каждый день по времени
        ''')
st.sidebar.write('''
         ### Счета за каждый день по времени
        ''')

fig, ax = plt.subplots(figsize=(10,6))
time_bill_box = sns.boxplot(data=tips, x='time_order', y='total_bill', hue='time')
ax.set_xlabel('Дата')
ax.set_ylabel('Сумма счета')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

filename9 = 'time_bill_box.png'
fig.savefig(filename9)

st.sidebar.download_button(label='Скачать график',
                   data=filename9,
                   file_name='time_bill_box.png',
                   mime='image/png')

# Нарисуйте 2 гистограммы чаевых на обед и ланч.
# Расположите их рядом по горизонтали.
dinner_lunch = st.sidebar.write('''### Сумма чаевых за обед и ланч
                 ''')
dinner = tips[tips['time'] == 'Dinner']
lunch = tips[tips['time'] == 'Lunch']

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].hist(dinner['tip'], color='salmon')
ax[0].set_title('Чаевые на обед')
ax[0].set_xlabel('Сумма чаевых')
ax[0].set_ylabel('Частота')

ax[1].hist(lunch['tip'], color='skyblue')
ax[1].set_title('Чаевые на ланч')
ax[1].set_xlabel('Сумма чаевых')
ax[1].set_ylabel('Частота')

plt.tight_layout()

st.pyplot(fig)

filename10 = 'dinner_lunch.png'
fig.savefig(filename10)

st.sidebar.download_button(label='Скачать график',
                   data=filename10,
                   file_name='dinner_lunch.png',
                   mime='image/png')

#Нарисуйте 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых,
# дополнительно разбив по курящим/некурящим. Расположите их по горизонтали.¶
scatter_tip_bill = st.sidebar.write('''### Связь размера счета и чаевых между мужчинами и женщинами с учетом пристрастия к курению''')
male = tips[tips['sex'] == 'Male']
female = tips[tips['sex'] == 'Female']

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

sns.scatterplot(data=male,
                x='tip',
                y='total_bill',
                hue='smoker',
                alpha=0.7,
                ax=ax[0],
                palette={'Yes': 'salmon', 'No': 'skyblue'})
ax[0].set_xlabel('Чаевые')
ax[0].set_ylabel('Общий счет')
ax[0].set_title('Мужчины: связь счета и чаевых')

sns.scatterplot(data=female,
                x='tip',
                y='total_bill',
                hue='smoker',
                alpha=0.7,
                ax=ax[1],
                palette={'Yes': 'salmon', 'No': 'skyblue'})
ax[1].set_xlabel('Чаевые')
ax[1].set_ylabel('Общий счет')
ax[1].set_title('Женщины: связь счета и чаевых')

plt.tight_layout()

st.pyplot(fig)

filename11 = 'scatter_tip_bill.png'
fig.savefig(filename11)

st.sidebar.download_button(label='Скачать график',
                   data=filename11,
                   file_name='scatter_tip_bill.png',
                   mime='image/png')

# Построй тепловую карту зависимостей численных переменных
st.write('''
         ### Тепловая карта корреляций численных переменных
        ''')
st.sidebar.write('''
         ### Тепловая карта корреляций численных переменных
        ''')
corr_method = tips[['total_bill', 'tip', 'size']].corr()
fig, ax = plt.subplots(figsize=(10,6))
corr_heat = sns.heatmap(corr_method, annot=True, fmt=".2f",
            vmin=-1, vmax=1, center=0, square=True, linewidths=0.5)

st.pyplot(fig)

filename12 = 'corr_heat.png'
fig.savefig(filename12)

st.sidebar.download_button(label='Скачать график',
                   data=filename12,
                   file_name='corr_heat.png',
                   mime='image/png')


# ПЕРВОЕ ЗАДАНИЕ


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