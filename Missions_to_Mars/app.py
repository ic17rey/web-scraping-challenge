from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()
    
    # Return template and data
    return render_template("index.html", mars=destination_data ) 
    

@app.route("/scrape")
def scraper():
   
    variables_dict = scrape_mars.scrape()    
    mongo.db.collection.update({}, variables_dict, upsert=True)
    
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)