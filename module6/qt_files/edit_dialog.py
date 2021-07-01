import sys

from PyQt5 import QtWidgets, uic

from qt_files.main_window import QtBaseWindow, Ui_MainWindow

Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_dialog.ui")

class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())
