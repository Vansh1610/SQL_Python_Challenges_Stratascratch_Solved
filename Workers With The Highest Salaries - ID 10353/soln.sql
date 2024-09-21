select worker_title from (select *,rank() over(order by salary desc) rank_emp from worker) as sub_q
inner join title
on sub_q.worker_id=title.worker_ref_id
where sub_q.rank_emp=1