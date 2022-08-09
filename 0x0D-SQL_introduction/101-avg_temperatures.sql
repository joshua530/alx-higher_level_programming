-- imports dumped data into database and displays information
-- to download script, run
-- curl https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql -LO
-- run cat temperatures.sql | sudo mysql <database-name>
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`
    GROUP BY `city`
    ORDER BY `avg_temp` DESC;
