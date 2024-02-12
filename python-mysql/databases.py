import mysql.connector

config = {
    "user" : "root",
    "password" : "admin",
    "host" : "localhost",
    "database" : "acme"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()