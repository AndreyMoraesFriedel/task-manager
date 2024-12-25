from database.db_config import get_db_connection

def create_task(title, description, status):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
    """, (title, description, status))

    connection.commit()
    connection.close()

def get_all_tasks():
    connection = get_db_connection()
    cursor = connection.cursor()

    tasks = cursor.execute("SELECT * FROM tasks").fetchall()
    connection.close()

    return [dict(task) for task in tasks]

def get_task_by_id(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    task = cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    connection.close()

    return dict(task) if task else None

def update_task(task_id, title, description, status):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?, status = ?
        WHERE id = ?
    """, (title, description, status, task_id))

    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()
