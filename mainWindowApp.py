# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(993, 732)
        Form.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0.921, y1:0.0965, x2:0.023, y2:1, stop:0 rgba(158, 165, 176, 255), stop:1 rgba(0, 147, 255, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(511, 377))
        self.tabWidget.setStyleSheet("color: white")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(parent=self.tab)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_6.addWidget(self.frame)
        self.frame_13 = QtWidgets.QFrame(parent=self.tab)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_13.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditTownCurrent = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEditTownCurrent.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEditTownCurrent.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditTownCurrent.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.lineEditTownCurrent.setObjectName("lineEditTownCurrent")
        self.horizontalLayout.addWidget(self.lineEditTownCurrent)
        spacerItem = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnGetCurrentWeather = QtWidgets.QPushButton(parent=self.frame_13)
        self.btnGetCurrentWeather.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btnGetCurrentWeather.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGetCurrentWeather.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.btnGetCurrentWeather.setObjectName("btnGetCurrentWeather")
        self.horizontalLayout.addWidget(self.btnGetCurrentWeather)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.frame_4 = QtWidgets.QFrame(parent=self.tab)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_current_weather = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.label_current_weather.setFont(font)
        self.label_current_weather.setStyleSheet("color: black")
        self.label_current_weather.setText("")
        self.label_current_weather.setObjectName("label_current_weather")
        self.verticalLayout_18.addWidget(self.label_current_weather)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(parent=self.tab_2)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_14 = QtWidgets.QFrame(parent=self.tab_2)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_14.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditTownDay = QtWidgets.QLineEdit(parent=self.frame_14)
        self.lineEditTownDay.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEditTownDay.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditTownDay.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.lineEditTownDay.setObjectName("lineEditTownDay")
        self.horizontalLayout_2.addWidget(self.lineEditTownDay)
        spacerItem1 = QtWidgets.QSpacerItem(217, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnGetWeatherDay = QtWidgets.QPushButton(parent=self.frame_14)
        self.btnGetWeatherDay.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btnGetWeatherDay.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGetWeatherDay.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.btnGetWeatherDay.setObjectName("btnGetWeatherDay")
        self.horizontalLayout_2.addWidget(self.btnGetWeatherDay)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_3 = QtWidgets.QFrame(parent=self.tab_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_town_day = QtWidgets.QLabel(parent=self.frame_3)
        self.label_town_day.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_town_day.setFont(font)
        self.label_town_day.setStyleSheet("background-color:none")
        self.label_town_day.setObjectName("label_town_day")
        self.verticalLayout_9.addWidget(self.label_town_day, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 931, 515))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_day = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label_day.setFont(font)
        self.label_day.setStyleSheet("color: black")
        self.label_day.setText("")
        self.label_day.setObjectName("label_day")
        self.verticalLayout_2.addWidget(self.label_day)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_5 = QtWidgets.QFrame(parent=self.tab_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_11.addWidget(self.frame_5)
        self.frame_15 = QtWidgets.QFrame(parent=self.tab_3)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_15.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditTownWeek = QtWidgets.QLineEdit(parent=self.frame_15)
        self.lineEditTownWeek.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEditTownWeek.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditTownWeek.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.lineEditTownWeek.setObjectName("lineEditTownWeek")
        self.horizontalLayout_3.addWidget(self.lineEditTownWeek)
        spacerItem2 = QtWidgets.QSpacerItem(217, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnGetWeatherWeek = QtWidgets.QPushButton(parent=self.frame_15)
        self.btnGetWeatherWeek.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btnGetWeatherWeek.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGetWeatherWeek.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.btnGetWeatherWeek.setObjectName("btnGetWeatherWeek")
        self.horizontalLayout_3.addWidget(self.btnGetWeatherWeek)
        self.verticalLayout_11.addWidget(self.frame_15)
        self.frame_6 = QtWidgets.QFrame(parent=self.tab_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_week = QtWidgets.QLabel(parent=self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.label_week.setFont(font)
        self.label_week.setStyleSheet("color: black")
        self.label_week.setText("")
        self.label_week.setObjectName("label_week")
        self.verticalLayout_10.addWidget(self.label_week)
        self.layoutWeekGraph = QtWidgets.QVBoxLayout()
        self.layoutWeekGraph.setObjectName("layoutWeekGraph")
        self.verticalLayout_10.addLayout(self.layoutWeekGraph)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_7 = QtWidgets.QFrame(parent=self.tab_4)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_17.addWidget(self.frame_7)
        self.frame_16 = QtWidgets.QFrame(parent=self.tab_4)
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_16.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditTownWeekHourly = QtWidgets.QLineEdit(parent=self.frame_16)
        self.lineEditTownWeekHourly.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEditTownWeekHourly.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditTownWeekHourly.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.lineEditTownWeekHourly.setObjectName("lineEditTownWeekHourly")
        self.horizontalLayout_4.addWidget(self.lineEditTownWeekHourly)
        spacerItem3 = QtWidgets.QSpacerItem(217, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btnGetWeatherWeekHourly = QtWidgets.QPushButton(parent=self.frame_16)
        self.btnGetWeatherWeekHourly.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btnGetWeatherWeekHourly.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGetWeatherWeekHourly.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.btnGetWeatherWeekHourly.setObjectName("btnGetWeatherWeekHourly")
        self.horizontalLayout_4.addWidget(self.btnGetWeatherWeekHourly)
        self.verticalLayout_17.addWidget(self.frame_16)
        self.frame_12 = QtWidgets.QFrame(parent=self.tab_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.frame_12)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 931, 541))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_longhourly = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        self.label_longhourly.setFont(font)
        self.label_longhourly.setStyleSheet("color: black")
        self.label_longhourly.setText("")
        self.label_longhourly.setObjectName("label_longhourly")
        self.verticalLayout_21.addWidget(self.label_longhourly)
        self.layoutGraph = QtWidgets.QVBoxLayout()
        self.layoutGraph.setObjectName("layoutGraph")
        self.verticalLayout_21.addLayout(self.layoutGraph)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_19.addWidget(self.scrollArea_2)
        self.verticalLayout_17.addWidget(self.frame_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_8 = QtWidgets.QFrame(parent=self.tab_5)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_14.addWidget(self.frame_8)
        self.frame_17 = QtWidgets.QFrame(parent=self.tab_5)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_17.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEditTownAirPollution = QtWidgets.QLineEdit(parent=self.frame_17)
        self.lineEditTownAirPollution.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEditTownAirPollution.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditTownAirPollution.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.lineEditTownAirPollution.setObjectName("lineEditTownAirPollution")
        self.horizontalLayout_5.addWidget(self.lineEditTownAirPollution)
        spacerItem4 = QtWidgets.QSpacerItem(217, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.btnGetWeatherAirPollution = QtWidgets.QPushButton(parent=self.frame_17)
        self.btnGetWeatherAirPollution.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btnGetWeatherAirPollution.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGetWeatherAirPollution.setStyleSheet("background-color:rgba(192, 192, 192);\n"
"color: black")
        self.btnGetWeatherAirPollution.setObjectName("btnGetWeatherAirPollution")
        self.horizontalLayout_5.addWidget(self.btnGetWeatherAirPollution)
        self.verticalLayout_14.addWidget(self.frame_17)
        self.frame_9 = QtWidgets.QFrame(parent=self.tab_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_8.setStyleSheet("Background-color: none")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_air_pollution = QtWidgets.QLabel(parent=self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_air_pollution.setFont(font)
        self.label_air_pollution.setStyleSheet("background-color: none")
        self.label_air_pollution.setText("")
        self.label_air_pollution.setObjectName("label_air_pollution")
        self.verticalLayout_8.addWidget(self.label_air_pollution, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_14.addWidget(self.frame_9)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_10 = QtWidgets.QFrame(parent=self.tab_6)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_10.setStyleSheet("background-color:rgba(192, 192, 192)")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_15.addWidget(self.label_6, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_16.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(parent=self.tab_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_20.addWidget(self.label_7)
        self.verticalLayout_16.addWidget(self.frame_11)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Текущая погода"))
        self.lineEditTownCurrent.setPlaceholderText(_translate("Form", "Местоположение"))
        self.btnGetCurrentWeather.setText(_translate("Form", "Получить прогноз"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Текущая"))
        self.label_2.setText(_translate("Form", "Прогноз на день (ежечасно)"))
        self.lineEditTownDay.setPlaceholderText(_translate("Form", "Местоположение"))
        self.btnGetWeatherDay.setText(_translate("Form", "Получить прогноз"))
        self.label_town_day.setText(_translate("Form", "День"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "День"))
        self.label_3.setText(_translate("Form", "Прогноз на неделю (ежедневно)"))
        self.lineEditTownWeek.setPlaceholderText(_translate("Form", "Местоположение"))
        self.btnGetWeatherWeek.setText(_translate("Form", "Получить прогноз"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Неделя"))
        self.label_4.setText(_translate("Form", "Прогноз на 5 дней (по 3 часа)"))
        self.lineEditTownWeekHourly.setPlaceholderText(_translate("Form", "Местоположение"))
        self.btnGetWeatherWeekHourly.setText(_translate("Form", "Получить прогноз"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Долгосрочно"))
        self.label_5.setText(_translate("Form", "Интересная дополнительная информация"))
        self.lineEditTownAirPollution.setPlaceholderText(_translate("Form", "Местоположение"))
        self.btnGetWeatherAirPollution.setText(_translate("Form", "Получить данные"))
        self.label_8.setText(_translate("Form", "Атмосферное загрязнение (микрограмм на кубометр)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Доп."))
        self.label_6.setText(_translate("Form", "Узнать исторические данные"))
        self.label_7.setText(_translate("Form", "В разработке"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Истор. Данные"))
