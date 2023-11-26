# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from datetime import datetime


class Repository(QObject):
    def __init__(self, parent=None):
        self.__conn = QSqlDatabase.addDatabase("QSQLITE")
        self.__conn.setDatabaseName("database.sqlite")
        self.__model = QSqlTableModel()

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
            self.__model.setTable("events")
            self.__model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
            self.__model.setHeaderData(0, Qt.Horizontal, "ID")
            self.__model.setHeaderData(1, Qt.Horizontal, "Title")
            self.__model.setHeaderData(2, Qt.Horizontal, "Description")
            self.__model.setHeaderData(3, Qt.Horizontal, "Begin date")
            self.__model.setHeaderData(4, Qt.Horizontal, "End date")
            self.__model.setHeaderData(5, Qt.Horizontal, "Event type")

    def get_all_events(self):
        self.__model.select()
        return self.__model

    def add_event(self, title, description, begin_date = int(datetime.now().timestamp()), end_date = None, event_type = ''):
        query = QSqlQuery(self.__conn)
        query.prepare(
            """
            insert into events (title, description, begin_date, end_date, event_type)
            values (?, ?, ?, ?, ?)
            """)
        query.addBindValue(title)
        query.addBindValue(description)
        query.addBindValue(begin_date)
        query.addBindValue(end_date)
        query.addBindValue(event_type)
        if query.exec():
            self.__model.select()
