-- lists records that have non empty name
SELECT `score`, `name` FROM `second_table`
    WHERE `name` IS NOT NULL AND `name` != ''
    ORDER BY `score` DESC;
