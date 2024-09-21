# Import your libraries
import pandas as pd

# Starwriting code

df=hotel_reviews

df=df[df['hotel_name']=='Hotel Arena']

df=df.groupby(['reviewer_score','hotel_name']).count().reset_index()[['reviewer_score','hotel_name','total_number_of_reviews']]