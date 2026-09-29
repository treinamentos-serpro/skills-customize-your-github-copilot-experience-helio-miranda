# 📘 Atividade: Persisting FastAPI Data with SQLite

## 🎯 Objetivo

Aprenda a persistir os dados de uma API FastAPI usando SQLite. Ao final, você terá uma API de tarefas cujo conteúdo continua disponível mesmo depois que o servidor for reiniciado.

## 📝 Tarefas

### 🛠️ Configurar o Banco de Dados SQLite

#### Descrição
Substitua o armazenamento em memória da API anterior por um banco de dados SQLite local e crie a tabela de tarefas quando a aplicação iniciar.

#### Requisitos
O programa concluído deve:

- Criar ou abrir um arquivo `tasks.db` usando o módulo `sqlite3`.
- Criar a tabela `tasks` automaticamente quando ela ainda não existir.
- Armazenar as colunas `id`, `title` e `completed`.
- Usar consultas parametrizadas para interagir com o banco de dados.
- Manter os dados disponíveis após reiniciar o servidor.

### 🛠️ Persistir as Operações CRUD

#### Descrição
Atualize os endpoints da API para ler e modificar as tarefas no SQLite em vez de usar o dicionário em memória.

#### Requisitos
O programa concluído deve:

- Fazer `GET /tasks` buscando os registros no banco de dados.
- Fazer `GET /tasks/{task_id}` buscando uma tarefa pelo identificador.
- Fazer `POST /tasks` inserindo uma nova tarefa e retornando o registro criado.
- Fazer `PUT /tasks/{task_id}` atualizando uma tarefa existente.
- Fazer `DELETE /tasks/{task_id}` removendo uma tarefa existente.

### 🛠️ Tratar Erros e Validar a Persistência

#### Descrição
Complete a API com respostas HTTP adequadas e verifique que os dados continuam corretos depois de diferentes operações e reinicializações.

#### Requisitos
O programa concluído deve:

- Retornar `404` quando uma tarefa não existir.
- Retornar `201` ao criar uma tarefa com sucesso.
- Validar o corpo das requisições usando modelos Pydantic.
- Fechar as conexões SQLite depois de cada operação.
- Demonstrar que uma tarefa criada permanece disponível após reiniciar o servidor.

Para executar a API localmente, instale `fastapi` e `uvicorn` e use:

```bash
uvicorn main:app --reload
```

A documentação interativa estará disponível em `http://127.0.0.1:8000/docs`.
