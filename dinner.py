#--------------------------------------------------------------------
# dinner selector using recipes from based.cooking
# 
# (C) 2023 camooz
# released under GNU Public License (GPL)
#--------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd

allRecipes = {
    'Title': [],
    'Tags': [],
    'URL': []
}

# function for request
def get():
    r = requests.get("https://based.cooking", timeout=5)
    if r.status_code == 200:
        r.encoding = "UTF-8"
        html = r.text
        return html
    else:
        print(f'Could not fetch website, error code {r.status_code}') 

# function to print the dinner
def output():
    print(f'''
    I declare that your dinner shall be:
    {fortune[0,0]}!

    You can check out the recipe here: {fortune[0,2]}
    ''')

soup = BeautifulSoup(get(), "html.parser")

# iterate over data and append to dict
recipes = soup.find(id="artlist")
for recipe in recipes.find_all('li'): 
    title = recipe.get_text() # gets recipe's title
    tags = recipe.get('data-tags').strip('[]').split() # gets recipe's tags
    for link in recipe.find_all('a'):
        url = link.get('href') # gets recipe's url
        allRecipes['Title'].append(title)
        allRecipes['Tags'].append(tags)
        allRecipes['URL'].append(url)

# structure data using pandas
df = pd.DataFrame(allRecipes)

fortune = df.sample().to_numpy()

output()