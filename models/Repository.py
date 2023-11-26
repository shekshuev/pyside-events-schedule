# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

from models.event_model import EventModel


class Repository(QObject):
    def __init__(self, parent=None):
        self.__conn = QSqlDatabase.addDatabase("QSQLITE")
        self.__conn.setDatabaseName("database.sqlite")

    def connect(self):
        if not self.__conn.open():
            raise ConnectionError(self.__conn.lastError().databaseText())
        else:
            QSqlQuery(self.__conn).exec(
                """
                create table if not exists events (
                    id integer primary key autoincrement,
                    title text not null,
                    description text,
                    begin_date integer not null,
                    end_date integer,
                    event_type text not null
                )
                """
            )

    def get_all_events(self):
        model = QSqlTableModel()
        model.setTable("events")
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "Title")
        model.setHeaderData(2, Qt.Horizontal, "Description")
        model.setHeaderData(3, Qt.Horizontal, "Begin date")
        model.setHeaderData(4, Qt.Horizontal, "End date")
        model.setHeaderData(5, Qt.Horizontal, "Event type")
        model.select()
        return model
