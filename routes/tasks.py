from flask import Blueprint, request, jsonify
from models.task_model import create_task, get_all_tasks, get_task_by_id, update_task, delete_task

tasks_bp = Blueprint("tasks", __name__)

#POST
@tasks_bp.route("/tasks", methods=["POST"])
def create():
    data = request.get_json()
    create_task(data["title"], data.get("description", ""), data["status"])
    return jsonify({"message": "Tarefa criada com sucesso!"}), 201

#GET(ALL)
@tasks_bp.route("/tasks", methods=["GET"])
def list_all():
    tasks = get_all_tasks()
    return jsonify(tasks), 200

#GETBY(ID)
@tasks_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get(task_id):
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({"message": "Tarefa não encontrada"}), 404

#PUT
@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update(task_id):
    data = request.get_json()
    update_task(task_id, data["title"], data.get("description", ""), data["status"])
    return jsonify({"message": "Tarefa atualizada com sucesso!"}), 200

#DELETE
@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete(task_id):
    delete_task(task_id)
    return jsonify({"message": "Tarefa excluída com sucesso!"}), 200
