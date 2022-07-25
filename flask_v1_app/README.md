# Dvelopment Guide

## Get the App Running

Change into the flask app directory:

```
cd flask_v1_app
```

Initialize the python virtual environment. What the command below is saying:
initialize the virtual environment using python3, specifically python 3.7

```
/export/apps/python/3.7/bin/python3 -m venv venv
```

Then activate the environment:

```
. venv/bin/activate
```

Next install the dependencies for the python app (ensure your virtual environment is activated)

```
pip3 install -r requirements.txt
```

The requirements.txt force's pip3 to use specific older dependencies so that flask 1.1.2 works

To run the flask app:

```
export FLASK_APP=webapp export DB_USERNAME="flask_usr" export DB_PASSWORD="password" && flask run
```

## Debugging

To deactivate venv run the following command

```
deactivate venv
```

To remove all depenedencies from your current virtual env:

```
pip3 uninstall -y -r <(pip freeze)
```

After running this you should see the `venv/lib` folder shrink

## Additional Details

Fun fact: On linkedin computers, python binaries are stored at this location (/export/apps/python):

```
ls /export/apps/python
2.7  2.7.15 3.10   3.10.0 3.10.2 3.5  3.5.6  3.6  3.6.13 3.7  3.7.10 3.8   3.8.10 3.9  3.9.5
```

## Get the Database Running
