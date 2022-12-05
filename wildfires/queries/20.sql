--Number of times each reporter has covered a fire in California

select  reporters.REPORTING_UNIT_ID, count(*) from fires
inner join reporting_sources on fires.fpa_id = reporting_sources.fpa_id
inner join reporters on reporting_sources.REPORTING_UNIT_ID = reporters.REPORTING_UNIT_ID
inner join states s1 on s1.STATE_ID = fires.state
where s1.state_id = 'CA'
group by reporters.REPORTING_UNIT_ID
order by count(*) desc