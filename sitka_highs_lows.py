import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f: # файл открывается и сохряняется как f
    reader = csv.reader(f) # создали объект чтения данных для этого файла. модуль csv содержит функцию next(), котороая возвращает следующую строку файла
    header_row = next(reader) # next вызывается для получения 1й строки файла, содержащей заголовки

# Чтение максимальных/минимальных температур и дат
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha=0.5) # alpha - степень прозрачности вывода
ax.plot(dates, lows, c='blue', alpha=0.5) 
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # для закрашивания области между highs and lows

# Форматирование диаграммы.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate() # выводит метки дат на оси Х по диагонали
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()