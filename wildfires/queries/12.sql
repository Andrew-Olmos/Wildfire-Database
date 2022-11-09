--Shows which reporting unit reported to a specific fire, there will be variations of this
select fire_name,reporting_unit_name fire_year
from fires, reporters
where reporting_unit_id = NWCG_reporting_unit_id
ORDER BY fire_year DESC