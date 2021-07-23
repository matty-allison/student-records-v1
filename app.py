import sqlite3
from flask import Flask, render_template, request

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print("Table created succesfully")
    conn.close()

init_sqlite_db()

app = Flask(__name__)
@app.route('/enter-new/')
def enter_new_student():
    template_name = 'student.html'

    return render_template(template_name)

@app.route('/add-new-record/', methods=['POST'])
def add_new_record():
    msg = None
    if request.method == "POST":
        try:
            name = request.form['name']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("INSER INTO students(name, addr, city, pin) VALUES(?, ?, ?, ?)", (name, addr, city, pin))
                conn.commit()
                msg = "Record added successfully."
        except Exception as e:
            conn.rollback()
            msg = "Error occured during the insert operation" + e
        finally:
            conn.close()
            return render_template('result.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)
