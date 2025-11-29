from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("database.db")
    conn.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, completed INTEGER)")
    conn.close()

init_db()

# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todos", methods=["GET"])
def get_todos():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, completed FROM todos")
    todos = cursor.fetchall()
    conn.close()

    results = [{"id": row[0], "task": row[1], "completed": bool(row[2])} for row in todos]
    return jsonify(results)

@app.route("/add", methods=["POST"])
def add_todo():
    data = request.json
    task = data["task"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task, completed) VALUES (?, ?)", (task, 0))
    conn.commit()
    conn.close()

    return jsonify({"message": "Todo added!"})

@app.route("/delete/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Todo deleted!"})

@app.route("/toggle/<int:todo_id>", methods=["PUT"])
def toggle(todo_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT completed FROM todos WHERE id=?", (todo_id,))
    row = cursor.fetchone()

    new_status = 0 if row[0] == 1 else 1
    cursor.execute("UPDATE todos SET completed=? WHERE id=?", (new_status, todo_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Status updated!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
