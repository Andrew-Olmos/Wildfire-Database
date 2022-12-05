--Displays which fire data came from a certain system
select fire_name, system_id
from fires, system_sources
where system_sources.FPA_ID = fires.FPA_ID