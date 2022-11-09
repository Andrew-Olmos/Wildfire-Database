--Number of times each unit has responded to a fire in another state within the US

select  nwcg_units.UNITID, count(*) from fires
inner join nwcg_sources on fires.fpa_id = nwcg_sources.fpa_id
inner join nwcg_units on nwcg_sources.NWCG_UNIT_ID = nwcg_units.UNITID
inner join states s1 on s1.STATE_ID = fires.state
inner join states s2 on s2.STATE_ID = nwcg_units.state
inner join countries c1 on c1.COUNTRY_ID = s1.COUNTRY_ID
inner join countries c2 on c2.COUNTRY_ID = s2.COUNTRY_ID
where c1.COUNTRY_ID = c2.COUNTRY_ID and c1.COUNTRY_ID == 'US' and s1.state_id <> s2.state_id
group by nwcg_units.UNITID
order by count(*) desc