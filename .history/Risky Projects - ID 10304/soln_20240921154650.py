
import pandas as pd
import math

linkedin_projects['time']=((linkedin_projects['end_date']-linkedin_projects['start_date']).dt.days)/365


linkedin_emp_projects=linkedin_emp_projects.merge(linkedin_employees,left_on='emp_id',right_on='id')[['project_id','salary']]

linkedin_emp_projects=linkedin_emp_projects.groupby('project_id').sum().reset_index()


linkedin_projects=linkedin_projects.merge(linkedin_emp_projects,left_on='id',right_on='project_id')[['title','budget','time','salary']]

linkedin_projects['prorated_expense']=(linkedin_projects['salary']*linkedin_projects['time']).apply(lambda x:math.ceil(x))

linkedin_projects=linkedin_projects[linkedin_projects['prorated_expense']>linkedin_projects['budget']][['title','budget','prorated_expense']]