# Web Scraping Challenge - Mission to Mars

This challenge requires that a web application be built for scraping data related to the Mission to Mars. The data and images will be displayed in a single HTML page.

### Project setup

There is a folder called Missions_to_Mars that includes the files for this project  
* The scraping is first done in a Jupyter Notebook, mission_to_mars.ipynb
* The flask app is app.py, which renders the html template and also performs the scrape function when running app.py
    * The app creates a connection to Mongo and stores the information collected from the scrape

### Scraping done in Jupyter Notebook and in scrape_mars.py

* The [Mars News Site](https://redplanetscience.com/) is scraped for the latest News Title and Paragraph Text and the results are assigned to variables
* The [Featured Space Image site](https://spaceimages-mars.com) is scraped for the Mars featured image and the image url is stored to a variable.
* The [Mars Facts webpage](https://galaxyfacts-mars.com) is scraped using Pandas to retrieve the table containing facts about the planet including Diameter, Mass, etc  
    * In Pandas the data is converted to a HTML table string
* The [Astrogeology site](https://marshemispheres.com/) is scraped for urls to high resolution images for each of Mar's hemispheres and titles used for the images on the site
    * Dictionaries for each hemisphere are appended to with the image url strings and the hemisphere titles, and the dictionaries are stored as a list "hemisphere_image_urls"

### Step 2 - MongoDB and Flask Application

MongoDB with Flask templating is used to create a new HTML page that displays all of the information that was scraped from the URLs above

* The code used to scrape the websites in Jupyter notebook is moved into a Python script called `scrape_mars.py` with a function called `scrape` that executes the scraping code to return a Python dictionary containing all scraped data

* A route called `/scrape` imports `scrape_mars.py` script and calls the `scrape` function
    * The info and image urls returned are stored in Mongo as a Python dictionary

* The home route `/` queries the Mongo database and passes the mars data into an HTML template to display the data

* The template HTML file called `index.html` takes the mars data dictionary and displays all of the data in the appropriate HTML elements
    * The Project Title and the scrape button are displayed as jumbotron, top center of the page
    * The other info and images collected are displayed beneath the Title and scrape button
    * Screenshots of final application are included on GitHub along with the Jupyter Notebook

* Screenshot of recent web scraping results
<img width="335" alt="image" src="https://user-images.githubusercontent.com/78495351/149627325-8a6d58e9-aeab-4c06-a06c-dacfa614179e.png">


