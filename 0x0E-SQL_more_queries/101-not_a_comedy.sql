-- Not comedy
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN
	(SELECT ts.id
	 FROM tv_genres tg
	 INNER JOIN tv_show_genres tsg
	 ON tg.id = tsg.genre_id
	 INNER JOIN tv_shows ts
	 ON ts.id = tsg.show_id
	 WHERE tg.name = "Comedy")
ORDER BY ts.title;
