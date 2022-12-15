# web-scraping

# 1. Imported the following packages:
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# 2. Find two websites for the scraping and use the requests package to bring it into the python file
# I chose the website Guardian.com to pull information abouot books of the day. I then chose the YellowPages.com to bring information about car insurance agents 

# 3. Create a beautiful soup object

# For the car insurance site, I used the a tag and class="listing-name" to obtain all the names of the car insurance agents 

# I used the a tag and class_='phone' to obtain the phone numbers of the agents 

# After extracting all the information, I created two lists with the names and phone numbers 

# Created a new dictionary with the two lists

# Create a new dataframe

# Saved the dataframe to a csv file called 'car-insurance.csv'