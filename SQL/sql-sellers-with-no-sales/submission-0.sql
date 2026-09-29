-- Write your query below
select seller.seller_name 
from seller left join orders on seller.seller_id = orders.seller_id
AND orders.sale_date >= '2020-01-01' and  orders.sale_date < '2021-01-01'
where orders.seller_id is NULL
order by seller.seller_name asc;