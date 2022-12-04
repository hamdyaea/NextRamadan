#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import datetime
import requests
from RamKeys import *
from twython import Twython

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

def main():
    response = requests.get("https://www.nextramadan.info/static/ramadanlist.txt")
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
    msg =  "The next Ramadan is in "+str(numdays)+str(" days the ")+str(closest_date)
    message = str(msg) + str("\n#Ramadan #Islam  #nextramadan.info")
    photo = open("/var/www/NextRamadan/static/assets/images/ramadan.jpg", "rb")
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids=[response["media_id"]])

main()
