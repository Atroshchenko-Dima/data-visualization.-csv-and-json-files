import json
from plotly import offline # для вывода карты
from plotly.graph_objs import Scattergeo, Layout 

filename = 'datajson/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # преобразует формат в данные с которыми может работать python (словарь)

readable_file = 'datajson/readable_eq_data.json' # файл для записи тех же данных в более удобочитаемый формат
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) # json.dump - получает объект данных json и обьект файла и записывает данные в этот файл, indent=4 - приказывает форматировать данные с отступами

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] # индекс 0 - долгота
    lat = eq_dict['geometry']['coordinates'][1] # широта
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
# Нанесение данных на карту
data = [{
    'type': 'scattergeo', 
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags, # какой диапозон цветов должен использоваться
        'colorscale': 'Viridis', # диапазон от темно-синего до светло-желтого цвета
        'reversescale': True, # чтоб темно-синий для самых разрушительных землятрясений использовался, а желтый для слабых
        'colorbar': {'title': 'Magnitude'}, # цветная полоса выводящаяся сбоку, чтоб понимать что значат цвета
    },
}]
my_layout = Layout(title='Global Earthquakes') # заголовок диаграммы

fig = {'data': data, 'layout': my_layout} # словарь содержащий данные и макет
offline.plot(fig, filename='global_earthquakes.html')