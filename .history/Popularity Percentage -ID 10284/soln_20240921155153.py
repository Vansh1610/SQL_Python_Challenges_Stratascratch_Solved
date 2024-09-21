# Import your libraries
import pandas as pd

# Start writing code
df1=facebook_friends
df2=facebook_friends.rename(columns={'user1':'user2','user2':'user1'})

df=df1.append(df2)

df=df.groupby('user1').count().reset_index()[['user1','user2']]

df['user2']=df['user2']*100/df['user1'].nunique()

df=df.sort_values(by='user1')