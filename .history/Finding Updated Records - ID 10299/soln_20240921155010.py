# Import your libraries
import pandas as pd

df=ms_employee_salary
# Start writing code

df=df.groupby(['id','first_name','last_name','department_id']).max().reset_index()