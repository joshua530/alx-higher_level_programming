-- lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California (but the id can be different)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command

SELECT id, name
    FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = 'California')
    GROUP BY id
    ORDER BY id ASC;

-- a by the way :)
-- SELECT `c`.`name`, `c`.`id`
--     FROM `cities` `c`, `states` `s`
--     WHERE `s`.`name` = 'California' and `c`.`state_id` = `s`.`id`
--     GROUP BY `c`.`id`
--     ORDER BY `c`.`id`;
