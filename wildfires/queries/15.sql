--Insert Discovery date
Insert into Fires(discovery_date)
Values(1)

-- In the DB, discovery date is days from current time since fire was first discovered
-- Users who set a discovery date can start a day count timer that keeps track of
--days since user has seen fire