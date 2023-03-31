from typing import List, Dict, Tuple, Union
from fastapi import APIRouter, Path, HTTPException, status
from models.models import Todo, TodoItem

todo_router = APIRouter()

todo_list = []

@todo_router.get("/todo")
async def retrieve_todo() -> Dict:
    if len(todo_list):
        return {
            "todos": todo_list
        }
    
    return {
        "todos": []
    }

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> Dict:
    todo_list.append(todo)
    return {
        "message":"Todo added sucessfully"
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(
    ..., title="The ID of the todo to retrieve."
    )) -> Dict:

    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo":todo
            }
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist."
        )
    
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(
    ..., title="The ID of the todo to be updated."
    )) -> Dict:

    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully"
            }
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist."
        )
    
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> Dict:

    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully"
            }
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist."
        )
    
@todo_router.delete("/todo/")
async def delete_single_todo() -> Dict:
    todo_list.clear()
    return {
                "message": "Todo deleted successfully"
            }