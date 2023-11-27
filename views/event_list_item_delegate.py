from PySide6.QtWidgets import QAbstractItemDelegate
from models.event_type import EventType
from views.event_list_item import EventListItem

class EventListItemDelegate(QAbstractItemDelegate):
    def setEditorData(self, editor, index):
        pass

    def setModelData(self, editor, model, index):
        pass

    def createEditor(self, parent, option, index):
        pass

    def paint(self, painter, option, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        begin_date = record.value("begin_date")
        end_date = record.value("end_date")
        event_type = EventType[record.value("event_type")]
        item = EventListItem(title, description, begin_date, end_date, event_type, self.parent())
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

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
