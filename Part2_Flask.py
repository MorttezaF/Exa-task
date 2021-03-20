from flask import Flask, request, jsonify
import sqlite3
import os
import Part1 as pone

app = Flask(__name__)
exa = pone.Exa_Task("bolt://localhost:7687", "neo4j", "1399")
ht,hf,ha=exa.read_data()
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This is a prototype API</p>"


@app.route('/api/hashtag/all/', methods=['GET'])
def api_all():
    
    return str(ha)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found</p>", 404

@app.route('/api/hashtag/countr/', methods=['GET'])
def api_filter():
    return str(ht)

@app.route('/api/hashtag/countf/', methods=['GET'])
def api_filter1():
    return str(hf)


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)