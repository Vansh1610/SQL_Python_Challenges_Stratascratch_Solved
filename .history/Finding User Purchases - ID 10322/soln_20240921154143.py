SELECT distinct a1.user_id FROM amazon_transactions a1,amazon_transactions a2
where a1.user_id=a2.user_id and a1.id<>a2.id and abs(datediff(a1.created_at,a2.created_at))<=7