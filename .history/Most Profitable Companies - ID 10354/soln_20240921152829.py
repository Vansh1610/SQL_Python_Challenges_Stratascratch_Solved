import pandas as pd

df=forbes_global_2010_2014
df=df.sort_values(by='profits',ascending=False)[['company','profits']]
df.head(3)