-- Filters by specific cause of fires
select fire_name, stat_cause_descr, fire_year, state
from fires
where stat_cause_descr LIKE '%Lightning%'