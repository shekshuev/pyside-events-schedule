from PySide6.QtWidgets import QAbstractItemDelegate
from PySide6.QtCore import Qt

from views.event_list_item import EventListItem

class EventListItemDelegate(QAbstractItemDelegate):
    def setEditorData(self, editor, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        editor.set_title(title)
        editor.set_description(description)

    def setModelData(self, editor, model, index):
        title = editor.get_title()
        description = editor.get_description()
        model.setData(index, (title, description), Qt.EditRole)

    def createEditor(self, parent, option, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        item = EventListItem(title, description, self.parent())
        item.setGeometry(option.rect)
        return item

    def paint(self, painter, option, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        item = EventListItem(title, description, self.parent())
        item.setGeometry(option.rect)
        item.render(painter, option.rect.topLeft())

    def sizeHint(self, option, index):
        record = index.model().record(index.row())
        title = record.value("title")
        description = record.value("description")
        item = EventListItem(title, description, self.parent())
        return item.sizeHint()

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
