from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtCore import QEvent, Signal, QModelIndex, QRect
from models.event_type import EventType
from views.event_list_item import EventListItem

class EventListItemDelegate(QStyledItemDelegate):

    delete_clicked = Signal(QModelIndex)

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
        if event.type() == QEvent.MouseButtonRelease:
            click_global_pos = self.__button.mapToGlobal(event.pos())
            click_global_pos.setX(click_global_pos.x() - option.widget.spacing())
            click_global_pos.setY(click_global_pos.y() - option.widget.spacing())
            button_rect = self.__button.geometry()
            button_global_pos = self.__button.mapToGlobal(button_rect.topLeft())
            global_button_rect = QRect(button_global_pos, button_rect.size())
            if global_button_rect.contains(click_global_pos):
                self.delete_clicked.emit(index)
                return True
            else:
                return False
        else:
            return False
