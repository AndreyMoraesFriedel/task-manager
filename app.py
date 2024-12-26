from flask import Flask
from routes.tasks import tasks_bp
from database.db_config import init_db

#Inicialização do Flask
app = Flask(__name__)

#Inicializar o banco de dados
init_db()

#Registrar rotas
app.register_blueprint(tasks_bp)

@app.route("/")
def home():
    return {"message": "API Task Manager funcionando!"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
