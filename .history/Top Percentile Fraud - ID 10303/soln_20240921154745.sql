select policy_num,state,claim_cost,fraud_score 
from (select *, NTILE(100) OVER(PARTITION BY state order by fraud_score desc) as percentile from fraud_score) as sub_q where percentile<=5