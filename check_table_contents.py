#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3

# Check the contents of the table stored in the SQLite database

# Connect to the SQLite database
conn = sqlite3.connect('pokemon_data.db')

# Query the contents of the table
query = "SELECT * FROM pokemon_table"
df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Print the DataFrame
print(df)


# In[ ]:




