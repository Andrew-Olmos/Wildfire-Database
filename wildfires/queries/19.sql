--Fires and Units where both are from NY and the info came from a fed system

select FPA_ID, Fire_name, unitid, nwcg_units.name from fires
inner join nwcg_sources on fires.fpa_id = nwcg_sources.fpa_id
inner join nwcg_units on nwcg_sources.NWCG_UNIT_ID = nwcg_units.UNITID
inner join system_sources on fires.fpa_id = system_sources.fpa_id
inner join systems on system_sources.SYSTEM_ID = systems.SYSTEM_ID
inner join states s1 on s1.STATE_ID = fires.state
inner join states s2 on s2.STATE_ID = nwcg_units.state
where s1.state_id == 'NY' and s1.state_id == s2.state_id and systems.SYSTEM_TYPE = 'FED'