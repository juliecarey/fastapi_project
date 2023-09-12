#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:46:25 2023

@author: juliecarey
"""

from fastapi import FastAPI
import sqlite3

# connect to database
database = sqlite3.connect("name.db")

# create API
app = FastAPI()

# user most choose a name_id, such as "George"
@app.get("/{name_id}")
async def read_item(name_id):
    # select information from database based on name user chose
    cursor = database.cursor()
    cursor.execute('SELECT * FROM name_stats WHERE name=(?)', (name_id,))
    results = cursor.fetchall()[0][1:]
    return  {"Name" : results[0], "Average Age of Death": results[1], "Most Common Country": results[2], "Most Common Occupation": results[3]}

