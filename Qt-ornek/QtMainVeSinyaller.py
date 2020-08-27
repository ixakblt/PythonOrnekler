"""
/*
------------------------------------
ixakblt - ibrahim AKBULUT
------------------------------------
Web Site :ixakblt
------------------------------------
All Sites : @ixakblt
------------------------------------
*/
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def pencere():
    app = QApplication(sys.argv)
    ekran = QWidget()
    ekran.setMaximumSize(QSize(300,250)) #Pencerenin max boyutu
    ekran.setMinimumSize(QSize(200,150)) #Pencerenin min boyutu
    h_box =QHBoxLayout() # Hbox oluşturduk düzen korunması için
    button1 = QPushButton("yaz") # Button oluşturduk ve üserine yaz ibaresi ekledik
    h_box.addWidget(button1)  # Buttonumuzu Hbox ' a ekledik
    ekran.setLayout(h_box) #Pencere Layout'umuzu Hbox olarka belirledik
    button1.clicked.connect(ekranabas) #Button1 e tıklandığında yapılacak işlemi söyledik () koymayacaz burası önemli
    ekran.setWindowTitle("Test bu kardess") # Pencere başlığı belirledik
    ekran.show()
    sys.exit(app.exec())
def ekranabas():
    print("tikladin knk") #ekrananas metodu yazdık butona tıklandığında çalışacak fonksiyonumuz bu


pencere()#pencere fonksiyonumuzu çağırdık
