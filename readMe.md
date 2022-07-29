# devtools library

Work in progress...

A little bit of software development, a little bit of DevOps, a little relational data, and a little bit of learning...

| Pipeline | Status
|--|--
| Continuous Integration | [![CI_Pipeline](https://github.com/iDataEngineer/pyDevLib/actions/workflows/CI_Pipeline.yml/badge.svg)](https://github.com/iDataEngineer/pyDevLib/actions/workflows/CI_Pipeline.yml)
| Continuous Deployment | [![Build_Pipeline](https://github.com/iDataEngineer/pyDevLib/actions/workflows/Build_pipeline.yml/badge.svg)](https://github.com/iDataEngineer/pyDevLib/actions/workflows/Build_pipeline.yml)

---

## Python Modules

In the src folder in the repo:

|**Script**|**Function**
|--|--
|[db_create.py](src\db_create.py) | Create new table in DB.
| [db_execute.py](src\db_execute.py) | Run a query on a DB given the query string and the access credentials etc.
|  |  

The list will be updated as the project proceeds.

---

## Environmnet Set-up

To create the repo and set up the virtual environment.

In the command line :

````bash
# Make the repo
mkdir pyDB && cd pyDB

# Create virtual env
python -m venv pyDB_env

# Activate venv (windows) 
cd pyDB_env/scripts
activate.bat

# Update pip & install dependencies
python -m pip install update pip 
python -m pip install...

# Create requriements file
python -m pip freeze > requirements.txt

# Make app & tests dir
mkdir src && mkdir tests
````

Now we have an active environment for developing our app.

In windows it you may get a permission error when setting up - run as admin will resolve this e.g. open VS Code as admin and use the terminal there.

