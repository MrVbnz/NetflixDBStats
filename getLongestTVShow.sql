WITH
    SHOWS AS ( SELECT * FROM netflix_titles WHERE type == 'TV Show'),
    TIME AS (SELECT show_id, CAST(REPLACE(duration, ' Season', '') AS INTEGER) AS 'time'  FROM SHOWS),
    MAXTIME AS (SELECT * FROM TIME WHERE time == (SELECT MAX(time) FROM TIME))
SELECT * FROM SHOWS WHERE show_id == (SELECT show_id FROM MAXTIME)