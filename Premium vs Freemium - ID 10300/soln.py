# Import your libraries
import pandas as pd
u_p=ms_user_dimension.merge(ms_acc_dimension,on='acc_id',how='inner')[['user_id','paying_customer']]

d_p=ms_download_facts.merge(u_p,on='user_id',how='inner')

def paying_sum(x):
    print(x[x=='no'])

d_p=d_p.groupby(['date','paying_customer'])['downloads'].sum().reset_index()
d_p_no=d_p[d_p['paying_customer']=='no'][['date','downloads']]
d_p_y=d_p[d_p['paying_customer']=='yes'][['date','downloads']]

d_p=d_p_y.merge(d_p_no,how='inner',on='date')

d_p=d_p[d_p['downloads_x']<d_p['downloads_y']]