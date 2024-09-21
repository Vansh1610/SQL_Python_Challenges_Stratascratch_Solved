# Import your libraries
import pandas as pd

# Start writing code

df=fraud_score

df['rank_score']=df.groupby('state')[['fraud_score']].rank(pct=True)

df=df[df['rank_score']>0.95][['policy_num','state','claim_cost','fraud_score']]