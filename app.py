
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson import json_util
import os

app = Flask(__name__)
 
client = MongoClient("mongodb+srv://safastars21:hime1212@cluster0.eueotfs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.comment
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    collection.insert_one({'name': name, 'email': email})
    return "Submitted successfully! <a href='/'>Go back</a>"

@app.route('/get_data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
