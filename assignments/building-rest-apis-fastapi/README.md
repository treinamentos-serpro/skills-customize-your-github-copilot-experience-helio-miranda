# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST usando o framework FastAPI. Ao final, você terá uma API de tarefas com endpoints para consultar, criar, atualizar e excluir recursos, além de validação automática de dados.

## 📝 Tarefas

### 🛠️ Criar Endpoints de Leitura

#### Descrição
Complete os endpoints básicos da API para verificar seu funcionamento e listar as tarefas armazenadas em memória.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI usando o arquivo `main.py`.
- Disponibilizar `GET /health` retornando `{ "status": "ok" }`.
- Disponibilizar `GET /tasks` retornando a lista de tarefas.
- Permitir consultar uma tarefa específica por meio de `GET /tasks/{task_id}`.
- Retornar status HTTP `404` quando a tarefa solicitada não existir.

### 🛠️ Criar e Validar Tarefas

#### Descrição
Adicione um endpoint para criar novas tarefas e use um modelo Pydantic para validar os dados recebidos no corpo da requisição.

#### Requisitos
O programa concluído deve:

- Definir um modelo `TaskCreate` com título obrigatório e campo `completed` opcional.
- Disponibilizar `POST /tasks` para criar uma tarefa.
- Gerar um identificador único para cada nova tarefa.
- Retornar a tarefa criada com status HTTP `201`.
- Rejeitar requisições inválidas com a validação automática do FastAPI.

### 🛠️ Atualizar e Excluir Tarefas

#### Descrição
Complete o CRUD da API implementando a atualização parcial e a exclusão de tarefas existentes.

#### Requisitos
O programa concluído deve:

- Disponibilizar `PUT /tasks/{task_id}` para atualizar o título ou o status de uma tarefa.
- Disponibilizar `DELETE /tasks/{task_id}` para excluir uma tarefa.
- Retornar status HTTP `404` nas operações que receberem um identificador inexistente.
- Retornar a tarefa atualizada após uma alteração bem-sucedida.
- Retornar uma resposta adequada após uma exclusão bem-sucedida.

Para executar a API localmente, instale `fastapi` e `uvicorn` e use:

```bash
uvicorn main:app --reload
```

A documentação interativa estará disponível em `http://127.0.0.1:8000/docs`.
