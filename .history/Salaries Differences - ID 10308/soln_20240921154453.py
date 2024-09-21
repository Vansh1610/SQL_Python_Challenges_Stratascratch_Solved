# Import your libraries
import pandas as pd
df=db_employee

df=df[df['department_id'].isin([1,4])]

df=df.groupby('department_id').agg({'salary':'max'})

df=df.diff().iloc[[1]]