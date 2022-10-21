-- not my genres
SELECT name FROM tv_genres
WHERE name NOT IN
(SELECT g.name FROM
tv_genres AS g
INNER JOIN tv_show_genres AS tg
ON g.id = tg.genre_id
INNER JOIN tv_shows AS s
ON s.id = tg.show_id
WHERE s.title = "Dexter")
ORDER BY name;
