# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget

from views.ui_event_list_item import Ui_Form
from models.event_type import EventType

from datetime import datetime


class EventListItem(QWidget):
    def __init__(self, title: str, description: str, begin_date: int, end_date: int, event_type: EventType, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.title_label.setText(title)
        self.ui.description_label.setText(description)
        self.ui.begin_date_label.setText(f"С {str(datetime.fromtimestamp(begin_date))}")
        self.ui.end_date_label.setText(f"по {str(datetime.fromtimestamp(end_date))}")
        self.ui.event_type_label.setText(event_type.value)
        self.ui.delete_button.clicked.connect(self.on_delete_button_clicked)

    def on_delete_button_clicked(self):
        print(123)

