import json

filename = 'datajson/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # преобразует формат в данные с которыми может работать python (словарь)

readable_file = 'datajson/readable_eq_data.json' # файл для записи тех же данных в более удобочитаемый формат
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) # json.dump - получает объект данных json и обьект файла и записывает данные в этот файл, indent=4 - приказывает форматировать данные с отступами

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] # индекс 0 - долгота
    lat = eq_dict['geometry']['coordinates'][1] # широта
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

