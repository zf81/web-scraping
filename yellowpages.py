#import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.yellowpages.com/best/new-york-ny/car-insurance')

#create BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#print pretty
print(soup.prettify())

# Get names of each car insurance agent
names = soup.find_all('a',class_='listing-name')
output_names = []
for i in names: #for x in y: 
    print(i.text)
    data = i.text
    output_names.append(data)

len(output_names)

# Get phone numbers of each agent
telephone = soup.find_all('a',class_='phone')
output_telephone = []
for i in telephone: 
    print(i.text)
    data = i.text
    output_telephone.append(data)

len(output_telephone)

#create lists
list1= output_names
list2= output_telephone

#create new dictionary with new lists
dictionary = {'names': list1, 'telephone': list2}

#create new dataframe
df = pd.DataFrame({'names':output_names,'telephone': output_telephone})

#save dataframe to csv file
df.to_csv('/Users/fizzahzaidi/downloads/car-insurance.csv')