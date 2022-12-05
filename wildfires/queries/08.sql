-- Sorts by cause of fire
select fire_name, stat_cause_descr, fire_year, state
from fires
group by fire_name
order by stat_cause_descr