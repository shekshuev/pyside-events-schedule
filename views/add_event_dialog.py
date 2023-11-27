# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog

from views.ui_add_event_dialog import Ui_Dialog
from models.event_type import EventType


class AddEventDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.__event_type_list = [EventType.CLASS, EventType.SPORTS, EventType.OTHER]
        self.ui.event_type_combo_box.addItems(map(lambda e: e.value, self.__event_type_list))

    def get_dialog_data(self):
        return {
            "title": self.ui.title_line_edit.text(),
            "description": self.ui.description_text_edit.toPlainText(),
            "begin_date": int(self.ui.begin_date_time_edit.dateTime().toMSecsSinceEpoch() / 1000),
            "end_date": int(self.ui.end_date_time_edit.dateTime().toMSecsSinceEpoch() / 1000),
            "event_type": self.__event_type_list[self.ui.event_type_combo_box.currentIndex()].name
        }

