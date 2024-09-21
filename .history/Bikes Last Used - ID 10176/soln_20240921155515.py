# Import your libraries
import pandas as pd
df=dc_bikeshare_q1_2012

df=df.groupby('bike_number').max().reset_index()[['bike_number','end_time']]

df=df.sort_values(by='end_time',ascending=False)
# Start writing code