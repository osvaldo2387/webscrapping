from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pandas
import requests

def init_browser():

    executable_path={"executable_path":"chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

mars_info={}

def scrape_mars_news():
    try:
        browser=init_browser()

        url='https://mars.nasa.gov/news/'
        browser.visit(url)

        html=browser.html

        soup=BeautifulSoup(html, 'html.parser')

        news_title=soup.find("li", class_="slide").find("div",class_="content_title").text 
        news_p=soup.find("li", class_="slide").find("div",class_="article_teaser_body").text

        mars_info['news_title']=news_title
        mars_info['news_paragraph']=news_p
        return mars_info
    finally:
        browser.quit()

def scrape_mars_image():
    try:

        browser=init_browser()

        image_url_featured= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)

        html_image=browser.html

        soup=BeautifulSoup(html_image, 'html.parser')

        featured_image_url=soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        main_url= 'https://www.jpl.nasa.gov'

        featured_image_url=main_url+featured_image_url

        featured_image_url

        mars_info['featured_image_url']=featured_image_url
        return mars_info

    finally: 
        browser.quit()
    
def scrape_mars_weather():
    try:

        browser=init_browser()

        tweet_url='https://twitter.com/marswxreport?lang=en'
        browser.visit(tweet_url)

        html_weather=browser.html

        first_tweet_soup=BeautifulSoup(html_weather, 'html.parser')

        tweets=first_tweet_soup('ol',class_='stream-items')

        mars_weather=tweets.find('p', class_="tweet-text").text

        mars_info['weather']=mars_weather
        return mars_info
    finally:
        browser.quit()

def scrape_mars_facts():

    mars_facts_url='https://space-facts.com/mars/'

    tables=pd.read_html(mars-facts_url)

    mars_facts_df=tables[1]

    mars_facts_df.columns=['Description','Value']

    mars_facts_df.set_index('Description',inplace=True)

    data=mars_facts_df.to_html()

    mars_info['mars_facts']=data
    return mars_info

def scrape_mars_hemispheres():

    try:

        browser=init_browser()

        hemispheres_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        hemisphere_image_urls=[]

        links=browser.find_by_css("a.product-item h3")
        for item in range(len(links)):
            hemisphere={}

            browser.find_by_css("a.product-item h3")[item].click()
            
            sample_element=browser.find_link_by_text("Sample").first
            hemisphere["img_url"] = sample_element["href"]

            hemisphere["title"] = browser.find_by_css("h2.title").text

            hemisphere_image_urls.append(hemisphere)

            browser.back()

        mars_info['hemispheres']=hemisphere_image_urls

        return mars_info
    finally:
        browser.quit()














    












