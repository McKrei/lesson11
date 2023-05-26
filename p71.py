import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("p71.sqlite")

if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)


createTableQuery = QSqlQuery()
createTableQuery.exec(
    f"""
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    );
    """
)
print(con.tables())

name = "Linda"
job = "Technical Lead"
email = "linda@example.com"

query = QSqlQuery()
query.exec(
        f"""INSERT INTO contacts (name, job, email)
        VALUES ('{name}', '{job}', '{email}')"""
    )
