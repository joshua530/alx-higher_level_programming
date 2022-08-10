-- link to script: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT ts.title, tsg.genre_id
    FROM tv_shows ts
        INNER JOIN tv_show_genres tsg
        ON ts.id = tsg.show_id
    ORDER BY 
        ts.title ASC,
        tsg.genre_id ASC;
