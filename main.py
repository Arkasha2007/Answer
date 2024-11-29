import sys
from ui import Ui_MainWindow
from random import randint
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn_create_circle">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>560</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>СОЗДАТЬ</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn_create_circle.clicked.connect(self.create)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(250, 255, 0))
        r = randint(0, 250)
        qp.drawEllipse(randint(0, 399 - r), randint(0, 561 - r), r, r)
        self.do_paint = False

    def create(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())