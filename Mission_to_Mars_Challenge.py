#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

#mars = {}

#visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
#Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find('div', class_='content_title')

#only get the the text not html
#use the parent element to find the first 'a 'tag and it as "news_title"
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
#mars["news_title"] = news_title


#use the parent element to find the paragraph text (article teaser body is find by going on the webpage, clicking the dev tools and hovering over article summary(teaser))
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p
#mars["news_p"] = news_p


# ### Featured Images

#Visit URL 
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

#Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


#Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url
#mars["featured_image"] =  img_url

#scraping entire table with pandas
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df
#mars["facts"] = df.to_html()


df.to_html()

#browser.quit()
# D1: Scrape High-Resolution Mars' Hemisphere Images and Titles
# Hemispheres

# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

link = browser.find_by_css("a.product-item h3")
print(link)
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range (4):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    element = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = element['href']
    hemisphere["title"] = browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemisphere)
    browser.back()

hemisphere_image_urls
#mars["hemisphere"] = hemisphere_image_urls

# 5. Quit the browser
browser.quit()





