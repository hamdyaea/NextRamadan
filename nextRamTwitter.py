#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import datetime
import requests
import os
from twython import Twython



def main():
    twitter = Twython(*(os.environ[key] for key in ("TWITTER_CONSUMER_KEY", "TWITTER_CONSUMER_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN_SECRET")))
    response = requests.get("https://www.nextramadan.info/static/ramadanlist.txt", timeout=15)
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

if __name__ == "__main__":
    raise SystemExit("Posting disabled: review the expired calendar and publishing workflow first.")
