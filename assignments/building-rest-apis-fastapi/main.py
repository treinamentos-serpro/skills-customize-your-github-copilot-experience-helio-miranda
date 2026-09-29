from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks = {
    1: Task(id=1, title="Learn FastAPI", completed=False),
    2: Task(id=2, title="Build a REST endpoint", completed=False),
}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    # TODO: Generate an id, store the new task, and return it.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    # TODO: Update an existing task and return the updated value.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete an existing task and return a confirmation response.
    pass
