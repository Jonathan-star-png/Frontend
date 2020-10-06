from flask import Flask
from flask import request
from flask import render_template
from urllib.request import urlopen
from flask import url_for
from flask import redirect
import requests
import json
import pygal
#import urllib2
import simplejson as json
app= Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('books.html')

@app.route('/hello')
def hello():
    with urlopen('http://localhost:8081/getAllBooks') as r:
        text = r.read()
        listaa=json.loads(text)
    return render_template('books.html', list=json.loads(text))

@app.route('/addNewBook', methods=["GET", "POST"])
def addNewBook():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        price = request.form['Price']
        next = request.args.get('next', None)
        payload={'titleBook':title,'descriptionBook':description,'priceBook':price}
        #urllib.urlopen()
        print(json.dumps(payload))
    return render_template('addNewBook.html')
@app.route('/test', methods=["GET", "POST"])
def test():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        price = request.form['Price']
        pri=int(price)
        next = request.args.get('next', None)
        payload={'title':title,'description':description,'price':pri}
        #req = urlopen('http://localhost:8081/createBook')
        #req.add_header('Content-Type', 'application/json')
        #response = urlopen(req, json.dumps(payload))
        url = 'http://localhost:8081/createBook'
        #payload = {'some': 'data'}
        headers = {'content-type': 'application/json'}
        print(payload)
        print(json.dumps(payload))
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(response)
    return render_template("addNewBook.html")

@app.route('/pygalexample/')
def pygalexample():
    with urlopen('http://localhost:8081/getAllBooks') as r:
        texto = r.read()
    lista=json.loads(texto)
    #print (lista)
    #a=lista[0]
    #print(a)
    #b=a['Price']
    #print(b)
    prices=[]
    for recorrido in lista:
        print(recorrido['Price'])

        prices.append(recorrido['Price'])

    graph = pygal.Bar()
    graph.title = 'Book Prices'
    graph.add('Books', prices)
    graph_data=graph.render_data_uri()
    print(prices)    
    return render_template("graphing.html",graph_data=graph_data)
    #return render_template("graphing.html")

    
    
if __name__=='__main__':
   app.run(debug=True, port =8000)