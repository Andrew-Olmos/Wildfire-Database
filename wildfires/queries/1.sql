--Sort fire name alphabetically ASC, displays name, year, and state
select FIRE_NAME, Fire_Year, STATE
from Fires
GROUP BY FIRE_NAME
order by FIRE_NAME ASC