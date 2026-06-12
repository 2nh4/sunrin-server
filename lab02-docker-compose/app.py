from flask import Flask, request, render_template_string
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "sunrin123!"),
        database=os.environ.get("DB_NAME", "sunrin")
    )

FORM_HTML = '''
    <h2>Docker Compose 실습</h2>
    <form method="post">
        User: <input type="text" name="user"><br>
        <input type="submit" value="등록">
    </form>
'''

@app.route("/")
def index():
    if request.mehotd == 'POST':
        uid = request.form['userid']

        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
            conn.commit()
            cursor.close()
            conn.close()

            return f"{uid}님, 안녕하세요!"
        except Exception as e:
            return f"오류 발생 {e}"

    return render_template_string(FORM_HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
