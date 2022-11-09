--Sorts by fire size
select fire_name, fire_size, fire_year, state
from fires
group by fire_name
ORDER BY fire_size desc