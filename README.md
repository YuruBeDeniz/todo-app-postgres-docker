 todo-app-postgres-docker

### run a file
python app/database.py

### create a virtual env
python3 -m venv venv

### activate a virtual env
source venv/bin/activate

### to start the app
uvicorn app.main:app --reload

### install a package inside your venv
pip install fastapi uvicorn motor pydantic python-dotenv certifi

### deactivate
deactivate

### To list your project dependencies
pip install -r requirements.txt
pip freeze > requirements.txt

### alembic
alembic revision --autogenerate -m "update-user-model"
alembic upgrade head


### test backend
http://localhost:8000/docs#/



## PostgreSQL

psql -h localhost -p 5432 -U postgres todo_app

## Docker
create Dockerfile
create compose.yaml
create infra.yaml

docker-compose build
docker-compose up -d
docker-compose logs

docker exec -it todo-postgres psql -U postgres -d todo_app



#### to mnually connect the existing PostgreSQL container
docker network create app-network
docker network connect app-network todo-postgres



### materials

https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb

https://medium.com/@ktechhub/effortlessly-manage-multiple-databases-in-fastapi-with-sqlalchemy-and-alembic-784b6d2cf644

https://blog.stackademic.com/error-and-exception-handling-in-fastapi-c0949bb42e1b

https://medium.com/@aashirshakya/fastapi-alembic-sqlalchemy-detecting-all-the-custom-apps-automatically-2936f47f62fa

https://jnikenoueba.medium.com/using-fastapi-with-sqlalchemy-5cd370473fe5