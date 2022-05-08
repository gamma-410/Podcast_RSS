# podcast | app.py
# Copyright 2022・5・8 @gamma_410

from flask import Flask, render_template
import feedparser

rss_url = "https://anchor.fm/s/96134214/podcast/rss"
app = Flask(__name__)

feed = feedparser.parse(rss_url)

@app.route('/')
def index():
    return render_template('index.html', feed=feed.entries)

if __name__ == "__main__":
    app.run(debug=True)