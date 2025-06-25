from flask import Blueprint, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

app = Blueprint('routes', __name__)
mysql = MySQL()

@app.before_app_first_request
def init_db():
    app.root_path.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.root_path.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.root_path.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.root_path.config['MYSQL_DB'] = os.getenv("MYSQL_DATABASE")
    mysql.init_app(app.root_path)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM catatan")
    data = cur.fetchall()
    return render_template("index.html", catatan=data)

@app.route('/tambah', methods=['POST'])
def tambah():
    keterangan = request.form['keterangan']
    jumlah = request.form['jumlah']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO catatan(keterangan, jumlah) VALUES (%s, %s)", (keterangan, jumlah))
    mysql.connection.commit()
    return redirect('/')

@app.route('/hapus/<int:id>')
def hapus(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM catatan WHERE id = %s", (id,))
    mysql.connection.commit()
    return redirect('/')
