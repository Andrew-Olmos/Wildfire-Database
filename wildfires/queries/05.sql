-- Shows fires by certain fire class
Select FIRE_NAME, Fire_size_class, Fire_Year, STATE
From Fires
WHERE FIRE_SIZE_CLASS = 'A'