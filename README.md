# Ulo - Ulo an
(still on development, contain bugs)
#INSTALLATION
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
Make sure you also installed virtual environment or venv
```bash
# install virtual environment
♥_ python3.6 -m venv venv
#activate 
♥_ . venv/bin/activate
# pip wheel install
♥_ pip install wheel
# install requirements
♥_ pip install requirements.txt
```
Database
Create database in postgresql
you can use cli or app like pg-admin
CLI examples
```bash
♥_ sudo -u postgres psql
♥_ CREATE DATABASE dbname;
```
this will result like
```
postgres=# CREATE DATABASE testdb;
postgres-# 
```
```bash
#connect to db
♥_ \connect db_name
# show tables
♥_ \dt
```
apply database name to database configuration in ```app/config/database.yml```
```bash
♥_ . venv/bin/activate
♥_ python migrate.py db init
♥_ python migrate.py db migrate
♥_ python migrate.py db upgrade
```

### Run GRPC Server
```bash
python server.py
python test_grpc_server.py
```

### Run Endpoint http-json
use api client like Postman
```bash
python run.py
```