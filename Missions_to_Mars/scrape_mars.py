import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Identify the website url to be visited for news, and scrape for first news title and paragraph
    browser.visit('https://redplanetscience.com/')
    news_title = browser.find_by_css('div.content_title').text
    news_p = browser.find_by_css('div.article_teaser_body').text 

    # Identify the website url to be visited for the featured image
    browser.visit('https://spaceimages-mars.com/')

    # Click the button "FULL IMAGE" that displays the image and save the image url to a variable
    browser.find_link_by_partial_text('FULL IMAGE').click()
    featured_image_url = browser.find_by_css('img.fancybox-image')['src']

    # Identify the website url to be visited for facts and use pd.read_html to grab the html
    mars_facts = pd.read_html('https://galaxyfacts-mars.com/')[0].to_html()

    # Identify the website url to be visited for the hemispheres and create a list for the four urls
    browser.visit('https://marshemispheres.com/')
    hemispheres_image_urls = []
    # Set up a for loop that will happen four times (one for each hemisphere link)
    for x in range(1, 5):

    # Click the links that display the image 
        browser.find_link_by_partial_text('Enhanced').click()
        hemisphere_name = browser.find_by_css('h2.title').text
        img_url = browser.find_by_css('img.thumb')['src']
        hemispheres_dict = {"title":hemisphere_name, 'img_url':img_url}
        hemispheres_image_urls.append(hemispheres_dict)
        browser.back()

    variables_dict = {
        'Latest Mars News':news_title,
        'Latest News Paragraph':news_p,
        'Featured Mars Image':featured_image_url,
        'Mars Facts':mars_facts,
        'Mars Hemispheres':hemispheres_image_urls
    }  
    # Quit the browser
    browser.quit()

    return variables_dict