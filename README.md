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
alembic revision --autogenerate -m "update-task-model"

alembic upgrade head

rm -rf alembic/versions/*


### test backend
http://localhost:8000/docs#/



## PostgreSQL

psql -h localhost -p 5432 -U postgres todo_app

## Docker
create Dockerfile
create compose.yaml
create infra.yaml

docker run -d --name mycontainer -p 8000:80 myimage

docker-compose down
docker-compose up -d

to remove volumes:
docker-compose down -v
 

docker-compose build
docker-compose up -d
docker-compose logs

docker exec -it postgres_container psql -U postgres -d todo_app

##### Stop and Remove Existing Containers: 
docker-compose -f compose.yaml down

##### Rebuild the Backend Image:
docker-compose build backend

##### Start the Updated Containers: 
docker-compose up


#### to manually connect the existing PostgreSQL container
docker network create app-network
docker network connect app-network todo-postgres



### materials

https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb

https://medium.com/@ktechhub/effortlessly-manage-multiple-databases-in-fastapi-with-sqlalchemy-and-alembic-784b6d2cf644

https://blog.stackademic.com/error-and-exception-handling-in-fastapi-c0949bb42e1b

https://medium.com/@aashirshakya/fastapi-alembic-sqlalchemy-detecting-all-the-custom-apps-automatically-2936f47f62fa

https://jnikenoueba.medium.com/using-fastapi-with-sqlalchemy-5cd370473fe5


To verify:

Start your PostgreSQL container:
bash
Copy code
docker run -d --name postgres_test postgres:15
Open a shell inside the container:
bash
Copy code
docker exec -it postgres_test bash
Navigate to the data directory:
bash
Copy code
cd /var/lib/postgresql/data
ls

docker logs postgres_container
