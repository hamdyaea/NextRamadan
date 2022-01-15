#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import datetime
import requests
from flask import Flask, render_template, request
import re

app = Flask(__name__,)

@app.route('/static/.well-known/acme-challenge/BK5uUSfFLM5O6NSg3k_kl2Ko78F201Bm2bjkuNad7q0')
def letsencrypt_check(challenge):
    challenge_response = {
        "BK5uUSfFLM5O6NSg3k_kl2Ko78F201Bm2bjkuNad7q0":"BK5uUSfFLM5O6NSg3k_kl2Ko78F201Bm2bjkuNad7q0.dQSy-msKhnnIcLMYOa1UAj4I5sxJOMnaD4fKecX1Heg",
        "BK5uUSfFLM5O6NSg3k_kl2Ko78F201Bm2bjkuNad7q0":"BK5uUSfFLM5O6NSg3k_kl2Ko78F201Bm2bjkuNad7q0.dQSy-msKhnnIcLMYOa1UAj4I5sxJOMnaD4fKecX1Heg"
    }
    return Response(challenge_response[challenge], mimetype='text/plain')


@app.route("/")
def main():
    response = requests.get("https://nextramadan.herokuapp.com/static/ramadanlist.txt")
    data = response.text
    date_list_raw =  data.splitlines()

    date_list = []    
    
    for i in date_list_raw:
        i = str(i)
        i = datetime.datetime.strptime(i, "%Y-%m-%d").date()
        date_list.append(i)

    now = datetime.date.today()

    date_list_notneg = []

    # Remove negatives dates
    for i in date_list:
        value = i - now
        value = str(value)
        if value[0] != "-":
            date_list_notneg.append(i)

    differences = [abs(now - each_date) for each_date in date_list_notneg]

    minimum = min(differences)

    closest_date = date_list_notneg[differences.index(minimum)]

    # Find the number of days between nom and the next ramadan
    minimum = str(minimum)

    numdays = minimum[:-9]
    #closest_date and numdays are the needed variables
    #return str(numdays)+str("     ")+str(closest_date)
    return render_template("index.html", numdays=numdays,closest_date=closest_date)
