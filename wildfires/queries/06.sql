-- Shows all fires reported by certain Reporting unit
SELECT fire_name, reporting_unit_id, reporting_unit_name
from fires, reporters
where 
    reporting_unit_id = ' '