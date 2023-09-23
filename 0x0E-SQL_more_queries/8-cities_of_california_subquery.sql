-- lists all states in caloforniase hbtn_0d_usa

SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California';
