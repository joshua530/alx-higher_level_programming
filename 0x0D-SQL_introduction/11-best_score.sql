-- lists records in an ordered manner based on a condition
SELECT `score`, `name` FROM `second_table`
    WHERE `score` >= 10
    ORDER BY `score` DESC;
