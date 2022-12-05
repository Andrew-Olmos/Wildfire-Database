-- This query allow users to input spceific coordinates if they know a spceific location they wish to query to
select fire_name, fire_year, state
from fires
where 
latitude = '40.27868' AND
longitude = '-92.60136'