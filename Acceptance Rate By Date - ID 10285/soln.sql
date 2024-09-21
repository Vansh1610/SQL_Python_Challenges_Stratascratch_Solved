with total_requests as (select date,count(distinct user_id_sender) as tot from fb_friend_requests where action='sent' group by date ),

accepted_req as (select s.date, count(distinct r.user_id_receiver) as acc from fb_friend_requests s
inner join fb_friend_requests r
on s.user_id_sender=r.user_id_sender and s.user_id_receiver=r.user_id_receiver
where s.action='sent' and r.action='accepted'
group by s.date)


select t.date,acc/tot from total_requests t
inner join accepted_req a
on t.date=a.date