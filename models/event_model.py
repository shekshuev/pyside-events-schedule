from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt

class EventModel(QAbstractListModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.data[index.row()]
        elif role == Qt.EditRole:
            return self.data[index.row()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.data[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
