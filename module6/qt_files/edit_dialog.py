import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog
from qt_files.edit_members_dialog import EditMembersDialog
from team import Team

Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_dialog.ui")


class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, league_from_main=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.new_team = []
        self._delete_team_list = []
        self._dia_teams_list = []
        self.add_team.clicked.connect(self.add_button_clicked)
        self.delete_team.clicked.connect(self.delete_button_clicked)
        self.edit_team.clicked.connect(self.edit_button_clicked)
        if league_from_main:
            for x in league_from_main.teams:
                self._dia_teams_list.append(x)
                self.update_ui()

    def update_league(self, league_from_main):
        if len(self.new_team) > 0:
            self.add_team_to_league(league_from_main)
        if len(self._delete_team_list) > 0:
            self.delete_team_from_league(league_from_main)
        self.update_ui()
        print(league_from_main.teams)

    def delete_team_from_league(self, league_from_main):
        for x in self._delete_team_list:
            league_from_main.delete_team(x)
        self.update_ui()

    def add_team_to_league(self, league_from_main):
        for x in self.new_team:
            league_from_main.add_team(x)
        self.update_ui()

    def delete_button_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Question, "Remove Team?", "Are you sure you want to delete Team?",
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            self._delete_team_list.append(self._dia_teams_list[self.list_teams.currentRow()])
            del self._dia_teams_list[self.list_teams.currentRow()]
            self.update_ui()
        else:
            print("Aborted")

    def warn(self, title, message):
        mb = QMessageBox(QMessageBox.Icon.Critical, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def edit_button_clicked(self):
        row = self.selected_row()
        print(row)
        if row == -1:
            return self.warn("Select league to edit", "You must select a league")
        team_from_main = self._dia_teams_list[row]
        dialog = EditMembersDialog(team_from_main)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            dialog.update_team(team_from_main)
        self.update_ui()

    def selected_row(self):
        selection = self.list_teams.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        for i, l in enumerate(self._dia_teams_list):
            if str(l) == selected_item.text():
                return i
        return -1

    def add_button_clicked(self):
        t = Team(self.team_oid_add.text(), self.team_name_add.text())
        self._dia_teams_list.append(t)
        self.update_ui()
        self.new_team.append(t)

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
