from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    variables_dict = {}

    # Identify the website url to be visited
    browser.visit('https://redplanetscience.com/')

    # Scrape the webpage for the text for the first news item title, <div class='content_title'>
    news_title = browser.find_by_css('div.content_title').text

    # Scrape the webpage for the text for the first news item paragraph <div class='article_teaser_body'>
    news_p = browser.find_by_css('div.article_teaser_body').text 

    # Identify the website url to be visited
    browser.visit('https://spaceimages-mars.com/')

    # Click the button "FULL IMAGE" that displays the image 
    browser.find_link_by_partial_text('FULL IMAGE').click()

    # Find then save the image to a variable (img class='fancybox-image' and src identifies the jpg)
    featured_image_url = browser.find_by_css('img.fancybox-image')['src']

    # Identify the website url to be visited and use pd.read_html to see the html
    mars_facts = pd.read_html('https://galaxyfacts-mars.com/')[0].to_html()

    # Identify the website url to be visited
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


    # Quit the browser
    browser.quit()

    return variables_dict