-- Sub query
SELECT id, name FROM cities WHERE state_id in
(SELECT id FROM states WHERE name = "california") ORDER BY id;
