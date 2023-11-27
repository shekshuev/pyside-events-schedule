# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PySide6.QtCore import Slot, QModelIndex
from models.repository import Repository
from views.event_list_item_delegate import EventListItemDelegate
from views.add_event_dialog import AddEventDialog


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.repository = Repository()
        try:
            self.repository.connect()
        except ConnectionError as e:
            QMessageBox.critical(
                    None,
                    "App Name - Error!",
                    f"Database Error: {e}"
                )
            sys.exit(1)
        model = self.repository.get_all_events()
        delegate = EventListItemDelegate(self.ui.events_list_view)
        delegate.delete_clicked.connect(self.on_delete_event_button_clicked)
        self.ui.events_list_view.setItemDelegate(delegate)
        self.ui.events_list_view.setModel(model)

    @Slot(QModelIndex)
    def on_delete_event_button_clicked(self, index):
        self.repository.delete_event(index)

    @Slot()
    def on_add_new_event_button_clicked(self):
        dialog = AddEventDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_dialog_data()
            self.repository.add_event(data["title"], data["description"], data["begin_date"], data["end_date"], data["event_type"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
