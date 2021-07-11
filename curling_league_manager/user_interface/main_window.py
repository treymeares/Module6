import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog

from source.emailer import Emailer
from source.league_database import LeagueDatabase
from source.league import League
from user_interface.edit_dialog import EditDialog

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._dia_leagues = []
        self.league_loaded = None
        self.add_league.clicked.connect(self.add_button_clicked)
        self.email_league.clicked.connect(self.email_button_clicked)
        self.edit_league.clicked.connect(self.edit_button_clicked)
        self.delete_league.clicked.connect(self.delete_button_clicked)
        self.action_open.triggered.connect(self.action_open_triggered)
        self.action_save.triggered.connect(self.action_save_triggered)

    def warn(self, title, message):
        mb = QMessageBox(QMessageBox.Icon.Critical, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def email_button_clicked(self):
        fe = Emailer.instance()
        fe.configure("treymeares@gmail.com")
        for x in self._dia_leagues:
            for y in x.teams:
                for z in y.members:
                    fe.send_plain_email(z.email, "Subject", "Body")

    def edit_button_clicked(self):
        row = self.selected_row()
        print(row)
        if row == -1:
            return self.warn("Select league to edit", "You must select a league")
        league_from_main = self._dia_leagues[row]
        dialog = EditDialog(league_from_main)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            dialog.update_league(league_from_main)
        self.update_ui()

    def action_open_triggered(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            dia_file_name = dialog.selectedFiles()

            if dia_file_name[0].endswith('.pickle'):
                league_loaded = LeagueDatabase.load(str(dia_file_name[0]))
                self._dia_leagues.clear()
                for x in league_loaded.leagues:
                    self._dia_leagues.append(x)
        self.update_ui()

    def action_save_triggered(self):
        file, check = QFileDialog.getSaveFileName(None, "Save File",
                                                  "", "Database File (*.pickle)")
        if check:
            pickler = LeagueDatabase.instance()
            pickler.save(file)
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

    def selected_row(self):
        selection = self.league_list.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        for i, l in enumerate(self._dia_leagues):
            if str(l) == selected_item.text():
                return i
        return -1

    def add_button_clicked(self):
        l = League(self.league_oid_add.text(), self.league_name_add.text())
        adder = LeagueDatabase.instance()
        adder.add_league(l)
        self._dia_leagues.append(l)
        self.update_ui()
        print(str(l))

    def update_ui(self):
        row = self.selected_row()
        self.league_list.clear()
        for x in self._dia_leagues:
            self.league_list.addItem(str(x))
            print(x)
        if row != -1 and len(self._dia_leagues) > row:
            self.league_list.setCurrentItem(self.league_list.item(row))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
