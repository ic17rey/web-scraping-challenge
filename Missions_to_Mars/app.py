from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars.py


app = flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

@app.route("/")
def index():
    print("")
    #listings = mongo.db.listings.find_one()
    #listings_data = scrape_mars.py.scrape()

if __name__ == "__main__":
    app.run(debug=True)