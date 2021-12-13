
from flask import Flask , render_template , session , request , redirect, url_for
from numpy import positive
from werkzeug.utils import append_slash_redirect
from get_tweet import scrape
from csv_to_db import *
import os
from delete import del_
from tweets_labelling import tsa
from tweets_model import analyze
from tweets_analysis import analysis

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    connection = sqlite3.connect("table_name.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tweets")
    rows = cursor.fetchall()
    percentage=analysis()
    positive = percentage[0]
    negative = percentage[1]
    return render_template("result.html",rows = rows,positive=positive,negative=negative)



@app.route('/search' , methods = ['POST','GET'])
def search():
    del_()
    if request.method == 'POST':
        words = request.form['words']
        date_since = request.form['date_since']
        numtweet = 200
        scrape(words,date_since,numtweet)
        #os.system('python csv_to_db.py')
        tsa()
        analyze()
        analysis()
        os.system('python csv_to_db.py')
        result()
        #return render_template('search.html')
        return redirect('/result')
    
    return render_template('search.html')
'''
def search():
    #del_()
    if ((request.method == 'POST') or (request.method == 'GET')):
        words = request.form.get('words')
        date_since = request.form.get('date_since')
        numtweet = 200
        scrape(words,date_since,numtweet)
        os.system('python csv_to_db.py')
        return render_template('search.html')
    else:
        print("error")
    return render_template('search.html')

'''
if __name__ == "__main__":
    app.run(debug=True, port=5001)




    '''if request.method == 'POST':
        del_()
        words = request.form['words']
        date_since = request.form['date_since']
        numtweet = 200
        scrape(words,date_since,numtweet)
        os.system('python csv_to_db.py')
        
        return render_template('search.html')
    return render_template('search.html')
'''
'''
    elif request.method == "GET":
        connection = sqlite3.connect("table_name.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tweets")
        rows = cursor.fetchall()
        return render_template("search.html",rows = rows)
    return render_template('result.html')
    '''

'''
@app.route('/result' , methods = ['GET', 'POST'])

def result():
    
    if request.method == 'POST':
        words = request.form['words']
        date_since = request.form['date_since']
        numtweet = 200
        scrape(words,date_since,numtweet)
        os.system('python csv_to_db.py')
        os.system('python tsa_positive.py')
        
        
    return render_template('result.html')
'''
