# Import your libraries
import pandas as pd


sf_transactions['created_at']=sf_transactions['created_at'].dt.to_period('M')

sf_transactions=sf_transactions.groupby('created_at').sum().reset_index()[['created_at','value']]

sf_transactions=sf_transactions.sort_values(by='created_at')
sf_transactions['p_month']=sf_transactions['value'].shift(1)

sf_transactions['revenue_diff_pct']=round((sf_transactions['value']-sf_transactions['p_month'])*100/sf_transactions['p_month'],2)

sf_transactions=sf_transactions[['created_at','revenue_diff_pct']]

# Start writing code