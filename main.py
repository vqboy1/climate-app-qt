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

        self.btn_get_weather.clicked.connect(self.on_get_weather_press)

        self.btn_get_weather.clicked.connect(self.on_get_weather_1day_press)

        self.btn_get_weather.clicked.connect(self.on_get_weather_7day_press)

        self.btn_get_weather.clicked.connect(self.on_get_air_pollution_press)

        self.btn_get_weather.clicked.connect(self.on_get_weather_5day_press)

        self.btn_get_weather.clicked.connect(self.town_name)

        self.btnGetWeatherAirPollution.clicked.connect(self.on_get_air_pollution_press)

    def town_name(self):
        town = self.lineEditTown.text()
        self.label_town.setText(f'Город: {town}')

    def on_get_weather_5day_press(self):
        if self.checkBox5day.isChecked():
            town = self.lineEditTown.text()
            if len(town) == 0:
                self.label_longhourly.setText('Введите город')
            else:
                try:
                    template = get_label_weather_5day(town)
                    self.label_longhourly.setText(template)
                except KeyError:
                    self.label_longhourly.setText("Что-то пошло не так. Попробуйте еще раз")
        else:
            self.label_longhourly.setText("")

    # def build_graph(self):
    #     if self.layoutGraph.count() > 0:
    #         self.layoutGraph.removeWidget(self.plll)
    #     town = self.lineEditTownDay.text()
    #     if len(town) == 0 or not (graph_flag or bar_flag):
    #         return
    #     data = get_weather_5day(town)
    #     temperature = get_temp_5day(data)
    #     time = get_time_5day(data)
    #     xtime = [i for i in range(len(temperature))]
    #     xdict = dict(enumerate(time))
    #     self.plll = pg.plot(title="Погода")
    #     self.plll.plot(xtime, temperature)
    #     stringaxis = pg.AxisItem(orientation='bottom')
    #     stringaxis.setTicks([xdict.items()])
    #     self.plll.setAxisItems(axisItems={'bottom': stringaxis})
    #     self.layoutGraph.addWidget(self.plll)
    #     self.lineEditTownDay.setText("")

    def on_get_air_pollution_press(self):
        town = self.lineEditTownAirPollution.text()
        if len(town) == 0:
            self.label_air_pollution.setText('Введите город')
        else:
            try:
                template = get_air_pollution_data(town)
                self.label_air_pollution.setText(template)
                self.label_8.setText(f'Атмосферное загрязнение (микрограмм на кубометр) - {town}')

            except KeyError:
                self.label_week.setText("Что-то пошло не так. Попробуйте еще раз")

    def on_get_weather_press(self):
        if self.checkBoxCurrent.isChecked():
            town = self.lineEditTown.text()
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

                    self.label_current_weather.setText(f"Дата: {day_time[0]} \n"
                                                       f"Текущее время: {day_time[1]} \n \n"
                                                       f"Влажность: {prime['humidity']}% \n"
                                                       f"Макс. темп: {round(max_temp, 2)}°C \n"
                                                       f"Мин. темп: {round(min_temp, 2)}°C \n"
                                                       f"Осадки: {clouds} \n"
                                                       f"Облачность: {stats['clouds']['all']}% \n"
                                                       f"Скорость ветра: {wind['speed']} м/с \n"
                                                       f"Направление ветра: {degToCompass(wind['deg'])} \n"
                                                       f"Давление: {round(prime['pressure'] * 0.75, 1)} мм. рт. ст. \n"
                                                       f"(изменения только по кнопке)")
                except KeyError:
                    self.label_current_weather.setText("Что-то пошло не так. Попробуйте еще раз")
        else:
            self.label_current_weather.setText("")

    def on_get_weather_1day_press(self):
        if self.checkBoxDay.isChecked():
            town = self.lineEditTown.text()
            if len(town) == 0:
                self.label_week.setText('Введите город')
            else:
                try:
                    template = get_weather_1day(town)
                    self.label_day.setText(template)
                except KeyError:
                    self.label_day.setText("Что-то пошло не так. Попробуйте еще раз")
        else:
            self.label_day.setText("")

    def on_get_weather_7day_press(self):
        if self.checkBoxWeek.isChecked():
            town = self.lineEditTown.text()
            if len(town) == 0:
                self.label_week.setText('Введите город')
            else:
                try:
                    template = get_weather_7day(town)
                    self.label_week.setText(template)
                except KeyError:
                    self.label_week.setText("Что-то пошло не так. Попробуйте еще раз")
        else:
            self.label_week.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.show()
    app.exec()
