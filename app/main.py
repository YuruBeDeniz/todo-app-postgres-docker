from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import task_routers
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

@app.get("/test-connection")
async def test_connection():
    engine = create_async_engine(DATABASE_URL, echo=True)
    try:
        async with engine.begin() as conn:
            result = await conn.execute("SELECT 1")  # Explicitly execute the query
            data = result.fetchone()  # Fetch the result
        return {"status": "Connection successful!", "data": data}
    except Exception as e:
        return {"status": "Connection failed!", "error": str(e)}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"],  # ['*'] to allow all standard methods
    allow_headers=["*"],  # ['*'] to allow all headers
)


# app.include_router(todo_routers.router, prefix="/api/todos", tags=["Todos"])
app.include_router(task_routers.router, prefix="/api/tasks", tags=["Tasks"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
