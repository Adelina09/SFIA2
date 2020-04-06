import urllib3

from flask import Flask
from flask_mysqldb import MySQL
import os

app=Flask(__name__)

mysql=MySQL(app)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']


def test_service1():                                                        
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://localhost:5000/')
    assert 200  == r.status

def test_service2():                                                    
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://localhost:5001/')
    assert 404  == r.status

def test_service3():                                                        
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://localhost:5002/')
    assert 404  == r.status

def test_service4():                                                         
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://localhost:5003/')
    assert 404  == r.status


def test_select():                                               #select test
    with app.app_context():
        cur= mysql.connection.cursor()
        num_of_records=cur.execute('SELECT * FROM data_persistence')     
        mysql.connection.commit()
        cur.close()
        assert num_of_records == num_of_records                             

def test_insert():                                              #insert test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM data_persistence')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('INSERT INTO data_persistence (Story) VALUES ("test")')  #inserts at an autoincrement ID the value 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM data_persistence')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1] != new_num_records[len(new_num_records)-1]


    
def test_delete():                                              #delete test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM data_persistence')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('DELETE FROM data_persistence WHERE ID= %s', [int(num_of_records[len(num_of_records)-1][0])])  #delete all entries in the table that have the name 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM data_persistence')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1][0] != new_num_records[len(new_num_records)-1][0]
