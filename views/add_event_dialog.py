# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog

from views.ui_add_event_dialog import Ui_Dialog


class AddEventDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def get_dialog_data(self):
        return {
            "title": self.ui.title_line_edit.text(),
            "description": self.ui.description_text_edit.toPlainText()
        }

