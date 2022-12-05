--Would be a query to show which agency's and departments work with each other
select fire_name, department, agency, WildLandRole, fire_year
from NWCG_units, fires
WHERE  
department = 'AK' AND
agency = 'C&L' AND