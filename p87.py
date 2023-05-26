from PyQt5.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("81.sqlite")
con.open()

query = QSqlQuery()
query.exec("SELECT * FROM contacts")
query.first()

id, name, job, email = range(4)

while query.next():
    print(query.value(name))
    print(query.value(job))
    print(query.value(email))
    print("-----")