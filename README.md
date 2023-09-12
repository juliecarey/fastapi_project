# fastapi_project
Used fastapi in python to create an API that tells you most frequent occupation and country and average age of death for any given name in the kaggle dataset found here: https://www.kaggle.com/code/sumon9300/age-dataset/input .

name_age.py - transforms data and loads into a sql database

name.db - the database output from name_age.py

name_ape_api.py - here is where fastapi is created and pulls data from name.db
