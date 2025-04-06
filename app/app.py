from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='rootpass',
        database='mydb'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM greetings;")
    result = cursor.fetchone()
    return result[0] if result else "No greeting found"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
