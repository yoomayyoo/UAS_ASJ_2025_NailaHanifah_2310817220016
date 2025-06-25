from flask_mysqldb import MySQL
from flask import current_app

mysql = MySQL()

def init_app(app):
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("MYSQL_DATABASE")
    mysql.init_app(app)
