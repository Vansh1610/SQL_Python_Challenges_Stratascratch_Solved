# Import your libraries
import pandas as pd

# Start writing code

car_launches=car_launches.groupby(['year','company_name']).count().reset_index().sort_values(by='year')[['company_name','product_name']]

def find_diff(x):

    return x.loc[x.index[1]]-x.loc[x.index[0]]

car_launches=car_launches.groupby('company_name').agg({'product_name':find_diff}).reset_index()