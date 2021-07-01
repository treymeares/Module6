import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.add_league.clicked.connect(self.add_button_clicked)
        self.delete_league.clicked.connect(self.delete_button_clicked)
        self.action_open.triggered.connect(self.action_open_triggered)

    def action_open_triggered(self):
        mb = QMessageBox(QMessageBox.Icon.Critical, "Ouch", "Can't open files", QMessageBox.StandardButton.Ok)
        mb.exec()

    def delete_button_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Question, "Are you sure?", "Are you sure you want to delete League",
                             QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialog.exec()

    def add_button_clicked(self):
        self.league_list.addItem(self.league_name_add.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
