import requests

import calendar

from geopy.geocoders import Nominatim


def get_weather(town):


    # Замените YOUR_API_KEY на ваш API ключ OpenWeatherMap
    API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
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
    geo_locator = Nominatim(user_agent='climate-app-qt')
    location = geo_locator.geocode(town)
    lat = location.raw['lat']
    lon = location.raw['lon']
    API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
    CITY_NAME = town
    pass


def get_weather_7day(town):
    from datetime import datetime

    geo_locator = Nominatim(user_agent='climate-app-qt')
    location = geo_locator.geocode(town)
    lat = location.raw['lat']
    lon = location.raw['lon']

    API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
    CITY_NAME = town
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_KEY}" \
          f"&exclude=minutely,current,hourly,alerts&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    offset = data['timezone_offset']
    dates = []
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    template = 'День недели    Мин. темп.   Макс. темп.   Осадки \n\n'

    for i in range(7):
        ts = data['daily'][i]['dt'] + offset
        dates.append(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split()[0])

    for i in range(7):
        date = [int(i) for i in dates[i].split('-')]
        data_daily = data['daily']
        year, month, day = date[0], date[1], date[2]
        min_temp = str(int(data_daily[i]['temp']['min'])) + ' C°'
        max_temp = str(int(data_daily[i]['temp']['max'])) + ' C°'
        description = data_daily[i]['weather'][0]['description']
        day_number = days[calendar.weekday(year, month, day)]
        seps = {"Понедельник": ' ' * 10, "Вторник": ' ' * 19,
                "Среда": ' ' * 22, "Четверг": ' ' * 19, "Пятница": ' ' * 19, "Суббота": ' ' * 19,
                "Воскресенье": ' ' * 10}
        template += day_number + seps[day_number] + min_temp + ' ' * (5 - len(min_temp) + 7) * 2 + max_temp + ' ' * (
                    5 - len(max_temp) + 7) + description + '\n'

    return template


def get_weather_5day(town):

    API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
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

