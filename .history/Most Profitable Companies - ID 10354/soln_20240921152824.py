import pandas as pd

# Start writing code
df=forbes_global_2010_2014

df=df.sort_values(by='profits',ascending=False)[['company','profits']]

df.head(3)