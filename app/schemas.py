from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    completed: bool = False
    
    class Config:
        from_attributes = True

class TaskResponse(TaskSchema):
    id: int