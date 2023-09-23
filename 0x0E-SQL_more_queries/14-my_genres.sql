-- script that uses thes of Dexter tvshow

SELECT tg.name AS name FROM tv_genres tg, tv_shows ts, tv_show_genres tsg
WHERE ts.title = 'Dexter' AND ts.id = tsg.show_id AND tsg.genre_id = tg.id
ORDER BY tg.name;
