from mysql.connector import errorcode
import mysql.connector
from databases import cursor

db_name = "acme"

tables = {}
tables['logs'] = (
    "CREATE TABLE logs ("
    " id INT(11) NOT NULL AUTO_INCREMENT,"
    " text VARCHAR(250) NOT NULL,"
    " user VARCHAR(250) NOT NULL,"
    " created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (id)"
    ") ENGINE=InnoDB"
)


def createDatabase():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    print("database {} created".format(db_name))

def create_tables():
    cursor.execute("use {}".format(db_name))

    for table_name in tables:
        table_desc = tables[table_name]
        try :
            print("creating table {}".format(table_name))
            cursor.execute(table_desc)
        except mysql.connector.Error as err:
            if(err.no == errorcode.ER_TABLE_EXISTS_ERROR):
                print("Already exists")
            else:
                print(err.msg)

createDatabase()
create_tables()
