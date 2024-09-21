# Import your libraries
import pandas as pd



df=worker
df['rank_sal']=df['salary'].rank(method='dense',ascending=False)
df=df[df['rank_sal']==1][['worker_id']]

df2=title

df=df.merge(df2,left_on='worker_id',right_on='worker_ref_id',how='inner')[['worker_title']]
df.head()