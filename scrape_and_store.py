#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3


url = 'https://pokemondb.net/pokedex/all?fbclid=IwZXh0bgNhZW0CMTAAAR2T9ZAhkwwV03h5xcWuMRC64vEtJQAgOVUx0WRY_D6O8z3c1MF-bQhuT3E_aem_61HhQO2QUVzk1JU5DpOyUA'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table in the HTML
    table = soup.find('table')

    # Extract the table headers
    headers = [header.text.strip() for header in table.find_all('th')]

    # Extract the rows
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)

     # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('pokemon_data.db')

    # Save DataFrame to SQLite database
    df.to_sql('pokemon_table', conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()

    print("Data saved to sqlite database 'pokemon_data.db' in the table 'pokemon_table'")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


# In[ ]:




