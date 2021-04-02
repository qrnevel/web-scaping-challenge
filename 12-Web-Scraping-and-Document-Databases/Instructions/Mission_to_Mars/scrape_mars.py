# Import Dependecies 
from bs4 import BeautifulSoup
from splinter import Browser
import os
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
import pprint

def scrape():
    # # NASA Mars News
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URLs of pages to be scraped
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url) #you are typing in the link
    myhtml = browser.html  #you are retrieving the html of that link

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(myhtml, 'html.parser')

    news_title = soup.find('div', class_="list_text")

    #Loop through returned results
    for news in news_title:
        list_date = soup.find('div', class_='list_date')
        latest_title = soup.find('div', class_ ='content_title')
        latest_parag = soup.find('div', class_ = 'article_teaser_body')

    print(list_date.text)
    print(latest_title.text)
    print(latest_parag.text)

    # # JPL Mars Space Images - Featured Image
    #Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Visit URL for the feartures image
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url) 
    myhtml_2 = browser.html  
    soup2 = BeautifulSoup(myhtml_2, 'html.parser')
    #pprint.pprint(soup2)

    #Retrieve URL for featured image
    feat_image = soup2.find('img', class_="headerimage fade-in")

    featured_image_url = "https://spaceimages-mars.com/" + feat_image['src']
    print(featured_image_url)


    # # Mars Facts
    #Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Setting URLs to variables
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url) 
    myhtml_4 = browser.html  
    soup4 = BeautifulSoup(myhtml_4, 'html.parser')

    facts_table = pd.read_html(facts_url)
    print(facts_table)

    mars_df = facts_table[0]
    mars_df.columns = ['Mars - Earth Comparison', 'Mars', 'Earth']
    mars_df.head(7)


    # # Mars Hemispheres
    #Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Setting URLs to variables
    hemis_url = "https://marshemispheres.com/"
    rowser.visit(hemis_url) 
    myhtml_3 = browser.html  
    soup3 = BeautifulSoup(myhtml_3, 'html.parser')
    #pprint.pprint(soup3)

    hemisphere_image_urls = []
    mars_hemis = soup3.find_all('div', class_="item")

    for mars in mars_hemis:
        #finding and printing each title per hemisphere
        hemis = mars.find('div', class_ = 'description')
        hemis_titles = hemis.h3.text
    
        #finding and printing each base url
        hemis_links = mars.a['href']
        hemis_urls = "https://marshemispheres.com/" + hemis_links
    
        #finding and printing ehnanved image url
        browser.visit(hemis_urls)
        soup_for_image = BeautifulSoup(browser.html, 'html.parser')
        hemis_image = soup_for_image.find('div', class_ = 'downloads')
        hemis_image_url = hemis_image.find('li').a['href']
    
        #creating dictionatries
        hemis_dictionary = {}
        hemis_dictionary["title"] = hemis_titles
        hemis_dictionary["image_url"] = hemis_image_url
    
        hemisphere_image_urls.append(hemis_dictionary)
    
        print("------------")
        print(hemis_titles)
        print("------------")
        print(hemis_urls + hemis_image_url) 
        print(hemisphere_image_urls)    

        return hemis_dictionary
        
        # Return mars_data dictionary 

        return mars_info
    finally:

        browser.quit()
