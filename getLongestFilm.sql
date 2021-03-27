WITH
    FILMS AS ( SELECT * FROM netflix_titles WHERE type == 'Movie'),
    TIME AS (SELECT show_id, CAST(REPLACE(duration, ' min', '') AS INTEGER) AS 'time'  FROM FILMS),
    MAXTIME AS (SELECT * FROM TIME WHERE time == (SELECT MAX(time) FROM TIME))
SELECT * FROM FILMS WHERE show_id == (SELECT show_id FROM MAXTIME)