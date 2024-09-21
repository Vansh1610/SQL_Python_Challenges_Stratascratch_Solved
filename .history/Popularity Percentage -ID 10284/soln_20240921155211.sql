SELECT user,
       SUM(friends) / 
       (SELECT COUNT(DISTINCT user)
        FROM (
            SELECT user1 AS user FROM facebook_friends
            UNION 
            SELECT user2 AS user FROM facebook_friends
        ) AS users_union) * 100 AS popularity_percent
FROM (
    SELECT user1 AS user, COUNT(DISTINCT user2) AS friends
    FROM facebook_friends
    GROUP BY user1
    UNION
    SELECT user2 AS user, COUNT(DISTINCT user1) AS friends
    FROM facebook_friends
    GROUP BY user2
) AS sub_q
GROUP BY user;