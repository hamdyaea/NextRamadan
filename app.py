#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import datetime
import requests
from flask import Flask, render_template, request
import re

app = Flask(__name__,)


@app.route("/")
def main():
    response = requests.get("https://nextramadan.info/static/ramadanlist.txt")
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
    return render_template("index.html", numdays=numdays,closest_date=closest_date,now=now)

if __name__ == "__main__":
    app.run(debug=True)
