import requests

import calendar

from geopy.geocoders import Nominatim

import statistics as st

from datetime import datetime

API_KEY = 'bd5e378503939ddaee76f12ad7a97608'

geo_locator = Nominatim(user_agent='climate-app-qt')


def get_weather(town):
    # Замените YOUR_API_KEY на ваш API ключ OpenWeatherMap
    CITY_NAME = town

    # Формируем URL для запроса
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&lang=ru&units=metric'

    # Отправляем GET запрос и получаем данные о погоде
    response = requests.get(url)
    data = response.json()

    # Извлекаем данные о погоде
    # Выводим данные о погоде
    return data


def get_time(data):
    import pytz
    from datetime import datetime
    from timezonefinder import TimezoneFinder

    # data = {'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 804, 'main': 'Clouds',
    #                                                              'description': 'пасмурно', 'icon': '04d'}],
    #      'base': 'stations', 'main': {'temp': 269.32, 'feels_like': 264.18, 'temp_min': 268.79, 'temp_max': 269.9,
    #                                   'pressure': 1036, 'humidity':
    #                                       95, 'sea_level': 1036, 'grnd_level': 1016}, 'visibility': 10000,
    #      'wind': {'speed': 3.98, 'deg': 241, 'gust': 10.72}, 'clouds': {'all': 99}
    #     , 'dt': 1706519011,
    #      'sys': {'type': 2, 'id': 47754, 'country': 'RU', 'sunrise': 1706506213, 'sunset': 1706536477},
    #      'timezone': 10800, 'id': 524901,
    #      'name': 'Москва', 'cod': 200}

    obj = TimezoneFinder()
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    obj = obj.timezone_at(lng=longitude, lat=latitude)
    tz = pytz.timezone(obj)
    datetime_town = datetime.now(tz)
    current_day = str(datetime_town.today()).split()[0]
    current_time = datetime_town.strftime("%H:%M:%S")
    return [current_day, current_time]


def get_air_pollution_data(town):
    location = geo_locator.geocode(town)
    lat = location.raw['lat']
    lon = location.raw['lon']
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()['list'][0]['components']
    template = '\n\n SO2 \t NO2 \t PM10 \t PM2.5 \t O₃ \t CO \n\n'.expandtabs(10)
    template += f'{data["so2"]} \t {data["no2"]} \t {data["pm10"]} \t {data["pm2_5"]} \t {data["o3"]} \t {data["co"]} \n\n'.expandtabs(
        10)

    if data["so2"] <= 20:
        template += f'Идеальное соотношение SO2\n\n'
    elif 20 < data["so2"] < 80:
        template += f'Малое превышение SO2 на {round(data["so2"] - 20, 2)} мкг/м3 \n\n'
    elif 80 <= data["so2"] < 250:
        template += f'Превышение SO2 на {round(data["so2"] - 20, 2)} мкг/м3 \n\n'
    elif 250 <= data["so2"] < 350:
        template += f'Значительное превышение SO2 на {round(data["so2"] - 20, 2)} мкг/м3 \n\n'
    else:
        template += f'Опасное количество SO2\n\n'

    if data["no2"] <= 40:
        template += f'Идеальное соотношение NO2\n\n'
    elif 40 < data["no2"] < 70:
        template += f'Малое превышение NO2 на {round(data["no2"] - 40, 2)} мкг/м3 \n\n'
    elif 70 <= data["no2"] < 150:
        template += f'Превышение NO2 на {round(data["no2"] - 40, 2)} мкг/м3 \n\n'
    elif 150 <= data["no2"] < 200:
        template += f'Значительное превышение NO2 на {round(data["no2"] - 40, 2)} мкг/м3 \n\n'
    else:
        template += f'Опасное количество NO2!\n\n'

    if data["pm10"] <= 20:
        template += f'Идеальное соотношение PM10\n\n'
    elif 20 < data["pm10"] < 50:
        template += f'Малое превышение PM10 на {round(data["pm10"] - 20, 2)} мкг/м3 \n\n'
    elif 50 <= data["pm10"] < 100:
        template += f'Превышение PM10 на {round(data["pm10"] - 20, 2)} мкг/м3 \n\n'
    elif 100 <= data["pm10"] < 200:
        template += f'Значительное превышение PM10 на {round(data["pm10"] - 20, 2)} мкг/м3 \n\n'
    else:
        template += f'Опасное количество PM10!\n\n'

    if data["pm2_5"] <= 10:
        template += f'Идеальное соотношение PM2.5\n\n'
    elif 10 < data["pm2_5"] < 25:
        template += f'Малое превышение PM2.5 на {round(data["pm2_5"] - 10, 2)} мкг/м3 \n\n'
    elif 25 <= data["pm2_5"] < 50:
        template += f'Превышение PM2.5 на {round(data["pm2_5"] - 10, 2)} мкг/м3 \n\n'
    elif 50 <= data["pm2_5"] < 75:
        template += f'Значительное превышение PM2.5 на {round(data["pm2_5"] - 10, 2)} мкг/м3 \n\n'
    else:
        template += f'Опасное количество PM2.5!\n\n'

    if data["o3"] <= 60:
        template += f'Идеальное соотношение O3\n\n'
    elif 60 < data["o3"] < 100:
        template += f'Малое превышение O₃ на {round(data["o3"] - 60, 2)} мкг/м3 \n\n'
    elif 100 <= data["o3"] < 140:
        template += f'Превышение O₃ на {round(data["o3"] - 60, 2)} мкг/м3 \n\n'
    elif 140 <= data["o3"] < 180:
        template += f'Значительное превышение O₃ на {round(data["o3"] - 60, 2)} мкг/м3 \n\n'
    else:
        template += f'Опасное количество O₃!\n\n'

    if data["co"] <= 4400:
        template += f'Идеальное соотношение CO\n\n'
    elif 4400 < data["co"] < 9400:
        template += f'Малое превышение CO на {round(data["co"] - 4400, 2)} мкг/м3 \n\n'
    elif 9400 <= data["co"] < 12400:
        template += f'Превышение CO на {round(data["co"] - 4400, 2)} мкг/м3 \n\n'
    elif 12400 <= data["co"] < 15400:
        template += f'Значительное превышение CO на {round(data["co"] - 4400, 2)} мкг/м3 \n\n'
    else:
        template += f'Опасное количество CO!\n'

    return template


def get_weather_1day(town):
    location = geo_locator.geocode(town)
    lat = location.raw['lat']
    lon = location.raw['lon']
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_KEY}" \
          f"&exclude=minutely,current,daily,alerts&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()
    celc = ' C°'
    offset = data['timezone_offset']
    lst_temp = []
    lst_temp_f = []
    template = f'Время \t Температура \t Ощущается \t Влажность \t Ветер \t Осадки\n\n'.expandtabs(16)

    for i in range(1, 25):
        data_h = data['hourly'][i]
        temp = float(round(data_h['temp'], 1))
        temp_f = float(round(data_h['feels_like'], 1))
        desc = data_h['weather'][0]['description']
        humidity = data_h['humidity']
        wind = str(data_h['wind_speed']) + ' м/с'
        lst_temp.append(temp)
        lst_temp_f.append(temp_f)
        ts = data['hourly'][i]['dt'] + offset
        hour = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split()[1][:5]
        template += f'{hour} \t {str(temp) + celc} \t {str(temp_f) + celc} \t {str(humidity) + "%"} \t {wind} \t {desc}\n\n'.expandtabs(16)

    mid_temp = int(st.mean(lst_temp))
    mid_temp_f = int(st.mean(lst_temp_f))
    diff_temp = str(round(max(lst_temp) - min(lst_temp), 1))
    diff_temp_f = str(round(max(lst_temp_f) - min(lst_temp_f), 1))

    template += f'\nСр арифм. \t {str(mid_temp)} C° \t \t {str(diff_temp)} C° \n\n'.expandtabs(12)
    template += f'Размах   \t {str(mid_temp_f)} C° \t \t {str(diff_temp_f)} C°'.expandtabs(12)

    return template


def get_weather_7day(town):
    location = geo_locator.geocode(town)
    lat = location.raw['lat']
    lon = location.raw['lon']

    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_KEY}" \
          f"&exclude=minutely,current,hourly,alerts&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    offset = data['timezone_offset']
    dates = []
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    template = 'День недели \t Мин. темп. \t Макс. темп. \t Влажность \t\t Ветер \t\t  Осадки \n\n'.expandtabs(12)
    lst_min = []
    lst_max = []

    for i in range(7):
        ts = data['daily'][i]['dt'] + offset
        dates.append(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split()[0])

    for i in range(7):
        date = [int(i) for i in dates[i].split('-')]
        data_daily = data['daily']
        year, month, day = date[0], date[1], date[2]

        humidity = data_daily[i]['humidity']
        wind = str(data_daily[i]['wind_speed']) + ' м/с'

        min_temp = round(data_daily[i]['temp']['min'], 1)
        lst_min.append(min_temp)

        max_temp = round(data_daily[i]['temp']['max'], 1)
        lst_max.append(max_temp)

        min_temp = str(min_temp) + ' C°'
        max_temp = str(max_temp) + ' C°'

        description = data_daily[i]['weather'][0]['description']
        day_number = days[calendar.weekday(year, month, day)]
        template += f'{day_number}       \t {min_temp} \t \t {max_temp}  \t \t {str(humidity) + "%"} \t \t {wind} \t \t  {description}\n\n'.expandtabs(12)

    template += '\n' * 2
    mid_min_temp = int(st.mean(lst_min))
    mid_max_temp = int(st.mean(lst_max))
    diff_min = str(round(max(lst_min) - min(lst_min), 1))
    diff_max = str(round(max(lst_max) - min(lst_max), 1))

    template += f'Среднее арифм. \t {str(mid_min_temp)} C° \t \t {str(mid_max_temp)} C° \n\n'.expandtabs(12)
    template += f'Размах         \t {str(diff_min)} C° \t \t {str(diff_max)} C°'.expandtabs(12)

    return template


def get_weather_5day(town):
    CITY_NAME = town

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={API_KEY}'

    response = requests.get(url)
    data = response.json()

    return data


def get_label_weather_5day(town):
    CITY_NAME = town

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={API_KEY}&lang=ru&units=metric'

    response = requests.get(url)
    data = response.json()['list']
    template = 'Дата и время \t Температура \t Ощущается как \t Влажность \t\t Ветер \t\tОсадки \n\n'.expandtabs(12)
    for i in range(len(data)):
        time = data[i]["dt_txt"][5:-3]
        temp = str(data[i]["main"]["temp"])
        temp_f = str(data[i]["main"]["feels_like"])
        desc = str(data[i]["weather"][0]["description"])
        humidity = str(data[i]['main']["humidity"]) + '%'
        wind = str(data[i]["wind"]["speed"]) + ' м/с'
        template += (
            f'{time} \t {temp + " C°"} \t\t {temp_f + " C°"} \t \t {humidity} \t \t {wind} \t\t{desc}\n\n').expandtabs(12)

    return template


def get_time_5day(data):
    date = []

    for i in range(len(data["list"])):
        date.append(f'{data["list"][i]["dt_txt"][5:-6]}ч \n'.replace(' ', '\n'))

    return date


def get_temp_5day(data):
    temp = []

    for i in range(len(data["list"])):
        temp.append(round(data["list"][i]["main"]["temp"] - 273, 1))

    return temp
