import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog

from team import Team

Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_dialog.ui")


class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._dia_teams_list = []
        self.add_team.clicked.connect(self.add_button_clicked)
        self.delete_team.clicked.connect(self.delete_button_clicked)
        self.edit_team.clicked.connect(self.edit_button_clicked)
        if league:
            for x in league.teams:
                self._dia_teams_list.append(x)
                self.update_ui()

    def delete_button_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Question, "Remove Team?", "Are you sure you want to delete Team?",
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            del self._dia_teams_list[self.teams_list.currentRow()]
            self.update_ui()
        else:
            print("Aborted")

    def edit_button_clicked(self):
        row = self.teams_list.currentRow()
        team = self._dia_teams_list[row]
        dialogue = EditMembersDialog(team)
        if dialogue.exec() == QDialog.DialogCode.Accepted:
            pass
        else:
            pass

    def add_button_clicked(self):
        t = Team(self.team_oid_add.text(), self.team_name_add.text())
        self._dia_teams_list.append(t)
        self.update_ui()
        print(str(t))

    def delete_button_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Question, "Remove League?", "Are you sure you want to delete League",
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            del self._dia_teams_list[self.list_teams.currentRow()]
            self.update_ui()
        else:
            print("Aborted")

    def update_ui(self):
        self.list_teams.clear()
        for x in self._dia_teams_list:
            self.list_teams.addItem(str(x))
            print(x)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())
