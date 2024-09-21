# Import your libraries
import pandas as pd
df=google_gmail_emails

df=df.groupby('from_user').count().reset_index()[['from_user','to_user']]

df=df.sort_values(by=['to_user','from_user'],ascending=[False,True])

df['rank_cnt']=df['to_user'].rank(method='first',ascending=False)
df