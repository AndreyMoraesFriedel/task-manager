import sqlite3

DB_NAME = "task_manager.db"

def get_db_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()