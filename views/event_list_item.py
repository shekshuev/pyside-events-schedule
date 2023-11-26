# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget

from views.ui_event_list_item import Ui_Form


class EventListItem(QWidget):
    def __init__(self, title='', description='', parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.set_title(title)
        self.set_description(description)

    def get_title(self):
        return self.ui.title_label.text()

    def get_description(self):
        return self.ui.description_label.text()

    def set_title(self, title):
        self.ui.title_label.setText(title)

    def set_description(self, description):
        self.ui.description_label.setText(description)
