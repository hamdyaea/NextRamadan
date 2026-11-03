#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Countdown based on a maintained local calendar; never invent missing dates."""
from datetime import date
from pathlib import Path
from flask import Flask, render_template


def next_ramadan(text, today):
    dates = [date.fromisoformat(line.strip()) for line in text.splitlines() if line.strip()]
    upcoming = [value for value in dates if value >= today]
    if not upcoming:
        raise ValueError("Calendar has no upcoming Ramadan date; update the calendar.")
    closest = min(upcoming)
    return closest, (closest - today).days


def create_app(calendar_path=None):
    app = Flask(__name__)
    app.config["CALENDAR_PATH"] = Path(calendar_path) if calendar_path else Path(__file__).resolve().parent / "static/ramadanlist.txt"

    @app.get("/")
    def index():
        today = date.today()
        try:
            closest, days = next_ramadan(app.config["CALENDAR_PATH"].read_text(), today)
        except (OSError, ValueError):
            return "Calendar update required. Ramadan dates depend on local moon sighting.", 503
        return render_template("index.html", numdays=days, closest_date=closest, now=today)

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
