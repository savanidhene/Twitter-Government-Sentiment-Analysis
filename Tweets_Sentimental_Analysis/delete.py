
# from flask import Flask , render_template , session , request , redirect
# from werkzeug.utils import append_slash_redirect
# from get_tweet import scrape
from csv_to_db import *
# import os

def del_():
    connection = sqlite3.connect("table_name.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tweets")
    connection.commit()
    print("Deletion complete")

