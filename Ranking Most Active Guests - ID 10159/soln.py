# Import your libraries
import pandas as pd

df=airbnb_contacts

df=df.groupby('id_guest').sum().reset_index()[['id_guest','n_messages']]

df['ranks']=df['n_messages'].rank(method='dense',ascending=False)

df=df.sort_values(by='n_messages',ascending=False)

# Start writing code