# Import your libraries
import pandas as pd


amazon_transactions=amazon_transactions.sort_values(by=['user_id','created_at'])[['user_id','created_at']]
amazon_transactions['created_at']=amazon_transactions.groupby('user_id').diff()
amazon_transactions=amazon_transactions[amazon_transactions['created_at'].dt.days<=7][['user_id']]

amazon_transactions=amazon_transactions['user_id'].unique()