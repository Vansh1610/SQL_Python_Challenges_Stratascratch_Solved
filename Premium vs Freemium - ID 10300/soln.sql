with user_paying as (
select user_id,paying_customer
from ms_user_dimension u
inner join ms_acc_dimension a
on u.acc_id=a.acc_id),

download_paying as (
select date,d.user_id, d.downloads,p.paying_customer from user_paying p
inner join ms_download_facts d
on p.user_id=d.user_id)

select date,
sum(case when paying_customer='yes' then downloads else null end) as paying,
sum(case when paying_customer='no' then downloads else null end) as non_paying
from download_paying
group by date
having non_paying>paying
order by date asc