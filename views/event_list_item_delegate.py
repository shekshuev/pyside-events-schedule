from PySide6.QtWidgets import QAbstractItemDelegate
from PySide6.QtCore import QEvent, Signal, QModelIndex, QRect
from models.event_type import EventType
from views.event_list_item import EventListItem

class EventListItemDelegate(QAbstractItemDelegate):

    delete_button_clicked = Signal(QModelIndex)

    def paint(self, painter, option, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        begin_date = record.value("begin_date")
        end_date = record.value("end_date")
        event_type = EventType[record.value("event_type")]
        item = EventListItem(title, description, begin_date, end_date, event_type, self.parent())
        self.__button = item.ui.delete_button
        item.setGeometry(option.rect)
        item.render(painter, option.rect.topLeft())

    def sizeHint(self, option, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        begin_date = record.value("begin_date")
        end_date = record.value("end_date")
        event_type = EventType[record.value("event_type")]
        item = EventListItem(title, description, begin_date, end_date, event_type, self.parent())
        return item.sizeHint()

    def editorEvent(self, event, model, option, index):
        self.delete_button_clicked.emit(index)
        if event.type() == QEvent.MouseButtonRelease:
            click_pos = event.pos()
            button_rect = self.__button.rect()
            button_rect.moveTopLeft(option.widget.mapToGlobal(self.__button.rect().topLeft()))
            print(click_pos, button_rect)
#            if self.__button_rect.contains(click_pos):

#                self.delete_button_clicked.emit(index)
#                return True
#            else:
#                return False
        else:
            return False
