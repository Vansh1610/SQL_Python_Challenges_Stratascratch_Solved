SELECT *,rank() over(order by total_emails desc,from_user) from (SELECT from_user,count(*) as total_emails FROM google_gmail_emails
group by from_user) as sub_q