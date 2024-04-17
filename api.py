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


def get_weather_1day(town):
    location = geo_locator.geocode(town)
    lat = location.raw['lat']
    lon = location.raw['lon']
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_KEY}" \
          f"&exclude=minutely,current,daily,alerts&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    offset = data['timezone_offset']
    times = []
    dates = []
    lst_temp = []
    lst_temp_f = []
    template = f'{town}\n\nВремя \t Температура \t Ощущается как \t Осадки \n\n'.expandtabs(12)

    for i in range(1, 25):
        data_h = data['hourly'][i]
        temp, temp_f, desc = round(data_h['temp'], 1), round(data_h['feels_like'], 1), data_h['weather'][0]['description']
        lst_temp.append(temp)
        lst_temp_f.append(temp_f)
        ts = data['hourly'][i]['dt'] + offset
        hour = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split()[1][:5]
        template += f'{hour} \t {str(temp)}         \t {str(temp_f)}          \t {desc}\n\n'.expandtabs(12)

    mid_temp = int(st.mean(lst_temp))
    mid_temp_f = int(st.mean(lst_temp_f))
    diff_temp = str(round(max(lst_temp) - min(lst_temp), 1))
    diff_temp_f = str(round(max(lst_temp_f) - min(lst_temp_f), 1))

    template += f'\nСр арифм. \t {str(mid_temp)} C° \t \t {str(diff_temp)} C° \n\n'.expandtabs(12)
    template += f'Размах   \t {str(mid_temp_f)} C° \t \t {str(diff_temp_f)} C°'.expandtabs(12)


    return template


print(get_weather_1day('london'))


def get_weather_7day(town):

    geo_locator = Nominatim(user_agent='climate-app-qt')
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
    template = town + '\n\n' + 'День недели \t Мин. темп. \t Макс. темп. \t  Осадки \n\n'.expandtabs(12)
    lst_min = []
    lst_max = []

    for i in range(7):
        ts = data['daily'][i]['dt'] + offset
        dates.append(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split()[0])

    for i in range(7):
        date = [int(i) for i in dates[i].split('-')]
        data_daily = data['daily']
        year, month, day = date[0], date[1], date[2]

        min_temp = round(data_daily[i]['temp']['min'], 1)
        lst_min.append(min_temp)

        max_temp = round(data_daily[i]['temp']['max'], 1)
        lst_max.append(max_temp)

        min_temp = str(min_temp) + ' C°'
        max_temp = str(max_temp) + ' C°'

        description = data_daily[i]['weather'][0]['description']
        day_number = days[calendar.weekday(year, month, day)]
        template += f'{day_number}       \t {min_temp} \t \t {max_temp}  \t \t  {description}\n\n'.expandtabs(12)

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
