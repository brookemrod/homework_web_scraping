#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports and dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time 


# In[2]:


#Site navigation
executable_path = {"executable_path"}
browser = Browser("chrome", headless=False)


# # NASA Mars News

# In[3]:


mars_data = {}
hemisphere_image_urls = []


# In[5]:


#Visit NASA Mars News site and scrape page into Soup
news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html
soup = bs(html, "html.parser")

#Get news title and paragraph text
article = soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text

mars_data["news_title"] = news_title
mars_data["news_p"] = news_p
mars_data


# # JPL Mars Space Images - Featured Image

# In[6]:


#Visit JPL Mars site and scrape page into Soup
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)
html = browser.html
soup = bs(html, "html.parser")

#Get image
image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)


# # Mars Weather

# In[7]:


#Twitter API Keys
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)
time.sleep(1)
html = browser.html

weather_soup = bs(html, 'html.parser')
weather = weather_soup.find('div', class_='js-tweet-text-container')

mars_weather = weather.p.text
mars_data["mars_weather"] = mars_weather
mars_data


# # Mars Facts

# In[8]:


#Visit Space Facts site and scrape page into Soup
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
mars_data = pd.read_html(facts_url)
mars_data = pd.DataFrame(mars_data[0])
mars_facts = mars_data.to_html(header = False, index = False)
print(mars_facts)


# # Mars Hemispheres

# In[9]:


hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = bs(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup = bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})


# In[ ]:




