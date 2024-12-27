**_Install Dependencies_**
````
pip install -r requirements.txt
````

## Start server
```
flask run --host=0.0.0.0 --port=5050
```

**_Create venv_**

````
# on Windows
**Install virtualenv
    pip install virtualenv
**Create venv
    python -m venv venv
**Activate venv
    source venv/Scripts/activate
**Deactivate venv
    deactivate
# on Mac or linux
     python3 -m venv ./venv
#Activate venv
    .venv/bin/activate

````

## Start development server
```
flask run
flask run --debug
flask run --debug --host=0.0.0.0 --port=5050
```
```
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```
