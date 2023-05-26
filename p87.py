from PyQt5.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("81.sqlite")
con.open()

query = QSqlQuery()
query.exec("SELECT name, job, email FROM contacts")
query.first()

name, job, email = range(3)

query.value(name)

query.next()
query.value(job)

query.last()
query.value(email)
