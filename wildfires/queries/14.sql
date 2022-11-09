--Displays how many agencies have been responded to fires
select count(DISTINCT(agency)), name, UnitType
from NWCG_Units
group by agency