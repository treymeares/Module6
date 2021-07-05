import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog


from team_member import TeamMember

Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_members_dialog.ui")


class EditMembersDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, team_from_main=None, parent=None):
        super().__init__(parent)
        self._dia_members_list = []
        self._new_member_list = []
        self.delete_member_list = []
        self.setupUi(self)
        self.delete_member.clicked.connect(self.delete_button_clicked)
        self.add_update.clicked.connect(self.add_button_clicked)
        if team_from_main:
            for x in team_from_main.members:
                self._dia_members_list.append(x)
                self.update_ui()

    def update_team(self, team_from_main):
        if len(self._new_member_list) > 0:
            self.add_team_to_league(team_from_main)
        if len(self.delete_member_list) > 0:
            self.delete_member_from_team(team_from_main)
        self.update_ui()
        print(self._dia_members_list)

    def add_member_to_team(self, team_from_main):
        for x in self._new_member_list:
            team_from_main.add_member(x)
        self.update_ui()

    def delete_member_from_team(self, league_from_main):
        for x in self.delete_member_list:
            league_from_main.remove_member(x)
        self.update_ui()

    def delete_button_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Question, "Remove Team?", "Are you sure you want to delete Team?",
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.delete_member_list.append(self._dia_members_list[self.team_members_widget.currentRow()])
            del self._dia_members_list[self.team_members_widget.currentRow()]
            self.update_ui()
        else:
            print("Aborted")

    def add_button_clicked(self):
        m = TeamMember(self.member_oid.text(), self.member_name.text(), self.member_email.text())
        self._dia_members_list.append(m)
        self.update_ui()
        self._new_member_list.append(m)

    def update_ui(self):
        self.team_members_widget.clear()
        for x in self._dia_members_list:
            self.team_members_widget.addItem(str(x))
            print(x)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditMembersDialog()
    window.show()
    sys.exit(app.exec_())