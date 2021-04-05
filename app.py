#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
import requests
from dotenv import dotenv_values
import json

app = Flask(__name__)

token = dotenv_values(".env")["TOKEN"]
BASE_URL = "https://superheroapi.com/api/"+token

dataFetched = [{"results":""}]

@app.route('/')
def index():
    return render_template('index.html', len=len(dataFetched), dataFetched=dataFetched)

@app.route('/search', methods=['POST'])
def getData():
    super_hero = request.form['name']
    print(super_hero)
    if (len(super_hero)<1):
        super_hero_dropdown = request.form['names']
        response = requests.get(BASE_URL+"/search/" + super_hero_dropdown)
    else:
        response = requests.get(BASE_URL+"/search/" + super_hero)
    # print(response)
    data = response.json()
    temp = []
    temp.append(data)
    # print(data)
    globals()['dataFetched'] = temp[0]["results"];
    return data

@app.route('/names')
def getNames():
    with open("names.json") as names:
        data = names.read()
    return data


if __name__ == "__main__":
    app.run(debug=False)
