
import pandas as pd


# Start writing code


facebook_web_log['timestamp']=pd.to_datetime(facebook_web_log['timestamp'],errors='coerce')
facebook_web_log['date']=facebook_web_log['timestamp'].dt.date


l_df=facebook_web_log[facebook_web_log['action']=='page_load'][['user_id','timestamp','date']]


e_df=facebook_web_log[facebook_web_log['action']=='page_exit'][['user_id','timestamp','date']]


facebook_web_log=l_df.merge(e_df,on=['user_id','date'])


facebook_web_log=facebook_web_log.groupby(['user_id','date']).agg({'timestamp_x':'max','timestamp_y':'min'}).reset_index()



facebook_web_log['duration']=(facebook_web_log['timestamp_y']-facebook_web_log['timestamp_x']).dt.total_seconds()


facebook_web_log=facebook_web_log.groupby('user_id').mean().reset_index()[['user_id','duration']]



facebook_web_log.head()