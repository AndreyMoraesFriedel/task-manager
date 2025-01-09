# **Task Manager API**

Um sistema básico para gerenciamento de tarefas com operações **CRUD** (Create, Read, Update, Delete). Ideal para aprendizado de conceitos como desenvolvimento de APIs, uso de banco de dados e containerização.

## **Funcionalidades**

- Criar tarefas com título, descrição e status.
- Listar todas as tarefas.
- Atualizar informações de uma tarefa existente.
- Excluir tarefas.

## **Tecnologias**

- **Backend**: Python com Flask.
- **Banco de Dados**: SQLite.
- **Containerização**: Docker.
- **CI/CD**: Automação de build e deploy com GitHub Actions.

## **Instruções Básicas**

### **1. Configurar Ambiente**
Criar e ativar o ambiente virtual:

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate      # Linux/Mac
```

### **1.1 Instalar dependências:**
```bash
pip install -r requirements.txt
```

### **2. Executar**
Iniciar o servidor localmente:
```bash
python app.py
```

### **3. Docker**
Construir a imagem:
```bash
docker build -t task-manager-api .
```

Rodar o contêiner:
```bash
docker run -d -p 5000:5000 task-manager-api
```
