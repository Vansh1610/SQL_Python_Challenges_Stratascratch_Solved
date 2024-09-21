# Import your libraries
import pandas as pd

# Start writing code
df=fb_friend_requests

tot=df[df['action']=='sent'].groupby('date').nunique().reset_index()[['date','user_id_sender']]
df=df.merge(df,how='inner',on='user_id_sender')

df=df[(df['action_x']=='sent') & (df['action_y']=='accepted')]

acc=df.groupby('date_x').nunique().reset_index()[['date_x','user_id_receiver_y']]

df=acc.merge(tot,how='inner',left_on='date_x',right_on='date')
df['rate']=df['user_id_receiver_y']/df['user_id_sender']
df=df[['date','rate']]

df.head()