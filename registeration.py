from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QRadioButton, QComboBox)
from PyQt5.QtGui import QIcon, QFont
import sys
import json
import os
import re


class UserInfoApp(QWidget):
    file_path = 'users.json'
    regions = ["Toshkent shahri", "Andijon viloyati", "Namangan viloyati", "Farg'ona viloyati", "Sirdaryo viloyati", "Jizzax viloyati", "Samarqand viloyati", "Navoiy viloyati", "Buxoro viloyati", "Xorazm viloyati", "Qashqadaryo viloyati", "Surxondaryo viloyati", "Jizzax viloyati"]

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Foydalanuvchi Ma'lumotlari")
        self.setWindowIcon(QIcon("m.png"))
        self.setGeometry(1000, 300, 800, 500)
        self.setWindowOpacity(0.9)

        self.createWidgets()
        self.setStyleSheet("border: 4px solid black; border-radius: 3px")
        self.show()

    def createWidgets(self):
        font_bold = QFont()
        font_bold.setPixelSize(25)
        font_bold.setBold(True)

        font_regular = QFont()
        font_regular.setPixelSize(19)

        self.ism_yozish = QLineEdit(self)
        self.ism_yozish.setPlaceholderText('Ismingizni kiriting')
        self.ism_yozish.setStyleSheet("border: 3px solid #152e59; border-radius: 10")

        self.fam_yozish = QLineEdit(self)
        self.fam_yozish.setPlaceholderText('Familiyangizni kiriting')
        self.fam_yozish.setStyleSheet("border: 3px solid #152e59; border-radius: 10")

        self.age_kiritish = QLineEdit(self)
        self.age_kiritish.setPlaceholderText('Yoshingizni kiriting')
        self.age_kiritish.setStyleSheet("border: 3px solid #152e59; border-radius: 10")

        self.tel_raqam = QLineEdit(self)
        self.tel_raqam.setPlaceholderText("+998 ")
        self.tel_raqam.setStyleSheet("border: 3px solid #152e59; border-radius: 10")

        self.email_kiritish = QLineEdit(self)
        self.email_kiritish.setPlaceholderText('Emailingizni kiriting')
        self.email_kiritish.setStyleSheet("border: 3px solid #152e59; border-radius: 10")

        self.jins_erkak = QRadioButton("Erkak", self)
        self.jins_erkak.setFont(font_regular)
        self.jins_ayoll = QRadioButton("Ayol", self)
        self.jins_ayoll.setFont(font_regular)

        self.region_combo = QComboBox(self)
        self.region_combo.addItems(self.regions)
        self.region_combo.setFont(font_regular)

        self.saqlash_button = QPushButton("Saqlash", self)
        self.tozalash_button = QPushButton("Faylni tozalash", self)
        self.black_mode = QPushButton("Night mode", self)

        self.saqlash_button.clicked.connect(self.saqla)
        self.tozalash_button.clicked.connect(self.clear_file)
        self.black_mode.clicked.connect(self.toggle_mode)

        self.setupLayout(font_bold, font_regular)

    def setupLayout(self, font_bold, font_regular):
        self.ism_yozish.move(250, 40)
        self.ism_yozish.setFont(font_regular)
        self.ism_yozish.setFixedHeight(35)
        self.ism_yozish.setFixedWidth(530)

        self.fam_yozish.move(250, 110)
        self.fam_yozish.setFont(font_regular)
        self.fam_yozish.setFixedWidth(530)

        self.age_kiritish.move(250, 180)
        self.age_kiritish.setFont(font_regular)
        self.age_kiritish.setFixedWidth(530)

        self.tel_raqam.move(250, 250)
        self.tel_raqam.setFont(font_regular)
        self.tel_raqam.setFixedWidth(530)

        self.email_kiritish.move(250, 320)
        self.email_kiritish.setFont(font_regular)
        self.email_kiritish.setFixedWidth(530)

        self.jins_erkak.move(250, 390)
        self.jins_ayoll.move(350, 390)

        self.region_combo.move(250, 440)
        self.region_combo.setFixedWidth(530)

        self.saqlash_button.move(280, 490)
        self.tozalash_button.move(20, 490)
        self.black_mode.move(540, 490)

        self.saqlash_button.setFixedSize(250, 40)
        self.tozalash_button.setFixedSize(250, 40)
        self.black_mode.setFixedSize(250, 40)

        self.saqlash_button.setStyleSheet("background-color: #5F6AE1; border: 2px solid #0400E1; border-radius: 5px")
        self.tozalash_button.setStyleSheet("background-color: #5F6AE1; border: 2px solid #0400E1; border-radius: 5px")
        self.black_mode.setStyleSheet("background-color: #5F6AE1; border: 2px solid #0400E1; border-radius: 5px")

        self.saqlash_button.setFont(font_bold)
        self.tozalash_button.setFont(font_bold)
        self.black_mode.setFont(font_bold)

    def saqla(self):
        
        if not self.ism_yozish.text():
            self.ism_yozish.setPlaceholderText('Ismingizni kiriting!')
            return
        if not self.fam_yozish.text():
            self.fam_yozish.setPlaceholderText('Familiyangizni kiriting!')
            return
        if not self.age_kiritish.text().isdigit():
            self.age_kiritish.setPlaceholderText('Yoshingizni to‘g‘ri kiriting!')
            return
        if not self.tel_raqam.text()[1:].isdigit() or not self.tel_raqam.text().startswith("+998"):
            self.tel_raqam.setPlaceholderText('Telefon raqam faqat raqamlardan iborat bo‘lsin!')
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_kiritish.text()):
            self.email_kiritish.setPlaceholderText('Emailni to‘g‘ri kiriting!')
            return
        if not self.jins_erkak.isChecked() and not self.jins_ayoll.isChecked():
            QMessageBox.warning(self, "Warning", "Jinsingizni tanlang!")
            return

        user_info = {
            "Ism": self.ism_yozish.text(),
            "Familiya": self.fam_yozish.text(),
            "Yosh": self.age_kiritish.text(),
            "Tel Raqami": self.tel_raqam.text(),
            "Email": self.email_kiritish.text(),
            "Jins": "Erkak" if self.jins_erkak.isChecked() else "Ayol",
            "Viloyat": self.region_combo.currentText()
        }

        

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(user_info)

        with open(self.file_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        QMessageBox.information(self, "Success", "Ma'lumotlar muvaffaqiyatli saqlandi!")
        self.clear_fields()

    def clear_fields(self):
        self.ism_yozish.clear()
        self.fam_yozish.clear()
        self.age_kiritish.clear()
        self.tel_raqam.clear()
        self.email_kiritish.clear()
        self.jins_erkak.setChecked(False)
        self.jins_ayoll.setChecked(False)
        self.region_combo.setCurrentIndex(0)

    def clear_file(self):
        if os.path.exists(self.file_path):
            
            with open(self.file_path, 'w') as file:
                file.write('[]')
                

            QMessageBox.information(self, "Success", "Fayl tozalandi!")
        else:
            QMessageBox.warning(self, "Warning", "Fayl topilmadi!")

    def toggle_mode(self):
        if self.black_mode.text() == "Night mode":
            self.set_dark_mode()
        else:
            self.set_white_mode()

    def set_dark_mode(self):
        self.setStyleSheet("background-color: #0a1629; border: 2px solid #0400E1; border-radius: 5px")
        self.ism_yozish.setStyleSheet("color: white; border: 3px solid #0a1629")
        self.fam_yozish.setStyleSheet("color: white; border: 3px solid #0a1629")
        self.age_kiritish.setStyleSheet("color: white; border: 3px solid #0a1629")
        self.tel_raqam.setStyleSheet("color: white; border: 3px solid #0a1629")
        self.email_kiritish.setStyleSheet("color: white; border: 3px solid #0a1629")
        self.black_mode.setText("Light mode")

    def set_white_mode(self):
        self.setStyleSheet("background-color: white; border: 2px solid #0400E1; border-radius: 5px")
        self.ism_yozish.setStyleSheet("color: black; border: 3px solid #0a1629")
        self.fam_yozish.setStyleSheet("color: black; border: 3px solid #0a1629")
        self.age_kiritish.setStyleSheet("color: black; border: 3px solid #0a1629")
        self.tel_raqam.setStyleSheet("color: black; border: 3px solid #0a1629")
        self.email_kiritish.setStyleSheet("color: black; border: 3px solid #0a1629")
        self.black_mode.setText("Night mode")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserInfoApp()
    sys.exit(app.exec_())