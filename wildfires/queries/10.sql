-- Filters by specific cause of fires
select Distinct(stat_cause_descr)
from fires
group by stat_cause_descr