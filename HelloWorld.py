from flask import Flask
from flask import request
from flask import render_template
from urllib.request import urlopen
from flask import url_for
from flask import redirect
import json
import pygal
import simplejson as json
app= Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('books.html')

@app.route('/hello')
def hello():
    with urlopen('http://localhost:8081/getAllBooks') as r:
        text = r.read()
    return render_template('books.html', list=json.loads(text))

@app.route('/addNewBook', methods=["GET", "POST"])
def addNewBook():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        price = request.form['Price']
        next = request.args.get('next', None)
        payload={'titleBook':title,'descriptionBook':description,'priceBook':price}
        print(json.dumps(payload))
    return render_template('addNewBook.html')

#@app.route('/pygalexample/')
#def pygalexample():
#        graph = pygal.Bar()
#        graph.title = 'Browser usage evolution (in %)'
#        graph.x_labels = map(str, range(2002, 2013))
#        graph.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
#        graph.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
#        graph.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
#        graph.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
#        graph_data=graph.render_data_uri()
#        return render_template("graphing.html",graph_data=graph_data)


    
    
if __name__=='__main__':
   app.run(debug=True, port =8000)