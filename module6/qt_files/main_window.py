import sys

from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.add_league.clicked.connect(self.add_button_clicked)

    def add_button_clicked(self):
        self.league_list.addItem(self.league_name_add.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
