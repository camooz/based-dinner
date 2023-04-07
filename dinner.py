#--------------------------------------------------------------------
# dinner selector using recipes from based.cooking
# 
# (C) 2023 camooz
# released under GNU Public License (GPL)
#--------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd

# function for request
def get():
    r = requests.get("https://based.cooking", timeout=5)
    if r.status_code == 200:
        r.encoding = "UTF-8"
        html = r.text
        return html
    else:
        print(f'Could not fetch website, error code {r.status_code}') 

allReceitas = {
    'Title': [],
    'Tags': [],
    'URL': []
}

soup = BeautifulSoup(get(), "html.parser")

# iterate over data and append to dict
receitas = soup.find(id="artlist")
for receita in receitas.find_all('li'): 
    titulo = receita.get_text() # Pega o título da receita
    tags = receita.get('data-tags').strip('[]').split() # Pega as tags da receita
    for link in receita.find_all('a'):
        url = link.get('href') # Pega o link da receita
        allReceitas['Title'].append(titulo)
        allReceitas['Tags'].append(tags)
        allReceitas['URL'].append(url)

# structure data using pandas
df = pd.DataFrame(allReceitas)

fortune = df.sample().to_numpy()

print(f'''
I declare that your dinner shall be:
{fortune[0,0]}!

You can check out the recipe here: {fortune[0,2]}
''')