select id_guest,dense_rank() over(order by n_messages desc) as ranks,n_messages
from (

select id_guest,sum(n_messages) as n_messages from airbnb_contacts
group by id_guest

) as sub_q
order by n_messages desc