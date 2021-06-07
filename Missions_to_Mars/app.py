from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

@app.route("/")
def home():
    
   

    # Return template and data
    return render_template("index.html")

@app.route("/scrape")
def scraper():

# listings = mongo.db.listings
# scraped_data = scrape_mars.scrape()    
# like listings_data = scrape_phone.scrape()
#     listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)