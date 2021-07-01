import os
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from league_database import LeagueDatabase
from league import League

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")

class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._dia_leagues = []
        self.add_league.clicked.connect(self.add_button_clicked)
        self.delete_league.clicked.connect(self.delete_button_clicked)
        self.action_open.triggered.connect(self.action_open_triggered)

    def edit_button_clicked(self):
        row = self.

    def action_open_triggered(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            dia_file_name = dialog.selectedFiles()

            if dia_file_name[0].endswith('.pickle'):
                league_loaded = LeagueDatabase.load(str(dia_file_name[0]))
                print(league_loaded)
                for x in league_loaded.leagues:
                    self._dia_leagues.append(x)
                    self.update_ui()

    def delete_button_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Question, "Remove League?", "Are you sure you want to delete League",
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            del self._dia_leagues[self.league_list.currentRow()]
            self.update_ui()
        else:
            print("Aborted")

    def add_button_clicked(self):
        l = League(self.league_name_add.text(), self.league_oid_add)
        self._dia_leagues.append(l)
        self.update_ui()
        self.league_list.addItem(self.league_name_add.text())

    def update_ui(self):
        self.league_list.clear()
        for x in self._dia_leagues:
            self.league_list.addItem(str(x))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
