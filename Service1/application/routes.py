from application import app
from flask import render_template, request
from flask_mysqldb import MySQL
import requests
import os


app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']

mysql=MySQL(app)

    
@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://Service4:5003/randomword')
    story = response.text      
    print(story) 
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO data_persistence(Story) VALUES (%s)", [story])
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', story = story, title = 'Home')
    