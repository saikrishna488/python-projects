from databases import db,cursor

def addLogs(text,user):
    sql = "insert into logs(text, user) values(%s,%s)"
    cursor.execute(sql,(text,user))
    db.commit()
    log_id = cursor.lastrowid
    print("Add log {}".format(log_id))

# addLogs("this is log 1", "brad")
# addLogs("this is log 2", "jeff")

def getLogs():
    sql = "select * from logs"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def getLog(user):
    sql = "select * from logs where user=%s"
    cursor.execute(sql,(user,))
    result = cursor.fetchall()
    for row in result:
        print(row)

def updateLog(id,text):
    sql = "update logs set text=%s where id=%s"
    cursor.execute(sql,(text,id))
    db.commit()
    print("Log updated")

def deleteLog(id):
    sql = "delete from logs where id=%s"
    cursor.execute(sql,(id,))
    db.commit()

deleteLog(2)
getLogs()