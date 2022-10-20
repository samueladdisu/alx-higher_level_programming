-- nuber of shows by genre
SELECT s.name AS genre, COUNT(g.show_id) AS number_of_shows
FROM tv_genres AS s
INNER JOIN tv_show_genres AS g
ON s.id = g.genre_id
GROUP BY g.genre_id
ORDER BY number_of_shows DESC;
