select user_id ,avg(time_spent_seconds) from (SELECT 
    user_id,
    date(timestamp) AS day,
    TIMESTAMPDIFF(SECOND, 
        MAX(CASE WHEN action = 'page_load' THEN timestamp END), 
        MIN(CASE WHEN action = 'page_exit' THEN timestamp END)
    ) AS time_spent_seconds
    
FROM 
    facebook_web_log
GROUP BY 
    user_id,
    DATE(timestamp)) as sub_q
    
where time_spent_seconds is not null
group by user_id