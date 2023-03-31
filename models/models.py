from pydantic import BaseModel
from typing import List, Dict, Tuple, Union

# class Item(BaseModel):
#     item: str
#     status: str

# class Todo(BaseModel):
#     id: int
#     item: Item


class Todo(BaseModel):
    id: int
    item: str


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example":{
                "item":"Example"
            }
        }

# class TodoItems(BaseModel):
#     item: List[TodoItem]
    
#     class Config:
#         schema_extra = {
#             "example":{
#                 "todos":[
#                     {
#                         "item": "Example schema 1!"
#                     },
#                     {
#                         "item": "Example schema 2!"
#                     }
#                 ]
#             }
#         }