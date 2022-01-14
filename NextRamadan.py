#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import datetime
import requests
from flask import Flask, render_template, request
import re


def main():
    with open("./static/ramadanlist.txt") as file:
        lines = file.readlines()

    date_list = []

    for i in lines:
        i = str(i)
        i = i.replace("\n", "")
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


main()
