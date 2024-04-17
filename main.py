import sys

import pyqtgraph as pg

from PyQt6 import QtWidgets

from mainWindowApp import Ui_Form

from api import *

bar_flag = False
graph_flag = True


class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.btnGetCurrentWeather.clicked.connect(self.on_get_weather_press)

        self.btnGetWeatherDay.clicked.connect(self.build_graph)

        self.btnGetWeatherWeek.clicked.connect(self.on_get_weather_7day_press)

    def build_graph(self):
        if self.layoutDayGraph.count() > 0:
            self.layoutDayGraph.removeWidget(self.plll)
        town = self.lineEditTownDay.text()
        if len(town) == 0 or not (graph_flag or bar_flag):
            self.label_town_graph.setText("Произошла ошибка. Проверьте введеные данные.")
            return
        self.label_town_graph.setText(town)
        self.label_town_graph.setText(town)
        data = get_weather_5day(town)
        temperature = get_temp_5day(data)
        time = get_time_5day(data)
        xtime = [i for i in range(len(temperature))]
        xdict = dict(enumerate(time))
        self.plll = pg.plot(title="Погода")
        self.plll.plot(xtime, temperature)
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        self.plll.setAxisItems(axisItems={'bottom': stringaxis})
        self.layoutDayGraph.addWidget(self.plll)
        self.lineEditTownDay.setText("")

    def on_get_weather_press(self):
        town = self.lineEditTownCurrent.text()
        if len(town) == 0:
            self.label_current_weather.setText('Введите город')
        else:
            try:
                stats = get_weather(town)
                day_time = get_time(stats)
                wind = stats['wind']
                clouds = stats['weather'][0]['description']
                prime = stats['main']
                max_temp = prime['temp_max']
                min_temp = prime['temp_min']
                self.label_current_weather.setText(f"Город {stats['name']} \n \n"
                                       f"Дата: {day_time[0]} \n"         
                                       f"Текущее время: {day_time[1]} \n \n"                                                   
                                       f"Влажность: {prime['humidity']}% \n"
                                       f"Макс. темп: {round(max_temp, 2)}°C \n"
                                       f"Мин. темп: {round(min_temp, 2)}°C \n"
                                       f"Осадки: {clouds} \n"
                                       f"Облачность: {stats['clouds']['all']}% \n"
                                       f"Скорость ветра: {wind['speed']} м/с \n"
                                       f"Давление: {round(prime['pressure'] * 0.75, 1)} мм. рт. ст. \n"
                                       f"(изменения только по кнопке)")
                self.lineEditTownCurrent.setText('')
            except:
                self.label_current_weather.setText("Что-то пошло не так. Попробуйте еще раз")

    def on_get_weather_7day_press(self):
        town = self.lineEditTownWeek.text()
        if len(town) == 0:
            self.label_week.setText('Введите город')
        else:
            try:
                template = get_weather_7day(town)
                self.label_week.setText(template)
                self.lineEditTownWeek.setText('')
            except:
                self.label_week.setText("Что-то пошло не так. Попробуйте еще раз")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.show()
    app.exec()
