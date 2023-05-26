from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# Создание подключения к базе данных
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("p71.sqlite")
if not db.open():
    print("Ошибка подключения к базе данных")
    exit(1)

# Обновление данных
updateQuery = QSqlQuery()
updateQuery.prepare("UPDATE contacts SET job = :job WHERE id = :id")
updateQuery.bindValue(":job", "Новая должность")
updateQuery.bindValue(":id", 1)
if not updateQuery.exec():
    print("Ошибка при обновлении данных:", updateQuery.lastError().text())
else:
    print("Данные успешно обновлены")

deleteQuery = QSqlQuery()
deleteQuery.prepare("DELETE FROM dds WHERE id = :id")
deleteQuery.bindValue(":sds", 5555)
if not deleteQuery.exec():
    print("Ошибка при удалении записи:", deleteQuery.lastError().text())
    # raise Exception("Ошибка при удалении записи")
else:
    print("Запись успешно удалена")

# Закрытие подключения к базе данных
db.close()
