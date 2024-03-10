from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask import make_response
import requests
import json
import urllib
import math
import random
from json2html import *

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def getRandomRestaurant():
    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": ""
    }
    if request.method == 'GET':
        stateURI = 'https://restaurants-near-me-usa.p.rapidapi.com/restaurants/all-state'
        cityURI =  'https://restaurants-near-me-usa.p.rapidapi.com/restaurants/all-city'
        stateResponse = requests.get(stateURI, headers=headers)
        cityResponse = requests.get(cityURI, headers=headers)
        states = stateResponse.json()
        cities = cityResponse.json()
        data = {}
        stateList = []
        cityList = []
        for state in states:
            stateList.append(state.get('stateName'))
        stateList = ','.join(state for state in stateList)
        for city in cities:
            cityList.append(city.get('cityName'))
        cityList = ','.join(city for city in cityList)
        data['cities'] = cityList
        data['states'] = stateList
        return render_template('form.html', data=data) 
        #return render_template('form.html')
    if request.method == 'POST':
        baseUrl = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/"
        pageNum = 0
        def createURI(city, state, pageNum):
            queryString = f"{state}/city/{city}/{pageNum}"
            queryString = urllib.parse.quote(queryString)
            return f"{baseUrl}{queryString}"
        city = request.form['city']
        state = request.form['state']
        restaurantResponse = requests.get(createURI(city, state, pageNum), headers=headers)
        restaurantResponse = restaurantResponse.json()
        allRestaurants = restaurantResponse.get('restaurants')
        '''totalResults = restaurantResponse.get('matching_results')
        pagesNeeded = math.ceil((totalResults - 10)/10)
        if pagesNeeded >= 9:
            for i in range(1,10):
                pageNum = i
                additionalPage = requests.get(createURI(city, state, random.choice(range(1,pagesNeeded))), headers=headers)
                allRestaurants.extend(additionalPage.json().get('restaurants'))'''
        randomRestaurant = allRestaurants[random.choice(range(0,len(allRestaurants)))]
        secondrandomRestaurant = allRestaurants[random.choice(range(0,len(allRestaurants)))]
        resp = make_response(render_template('table.html', data=json2html.convert(json = randomRestaurant,table_attributes="class=\"table table-hover table-responsive\"")))
        cookie_str = json.dumps(secondrandomRestaurant, separators=(',', ':'))
        resp.set_cookie('restaurants', cookie_str, None, None, '/') 
        return resp
