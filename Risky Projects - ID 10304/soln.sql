WITH p_salary AS (
    SELECT p.project_id, SUM(e.salary) AS total_budget
    FROM linkedin_emp_projects p
    INNER JOIN linkedin_employees e ON p.emp_id = e.id
    GROUP BY p.project_id
),
time_data AS (
    SELECT id, title, budget, DATEDIFF(end_date, start_date) AS project_time 
    FROM linkedin_projects
),
pro_rated_sal as (SELECT title,budget,ceil(total_budget*project_time/365) as pro_sal from time_data t
inner join p_salary p
on t.id=p.project_id)


select * from pro_rated_sal where pro_sal>budget