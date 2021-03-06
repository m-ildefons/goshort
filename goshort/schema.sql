DROP TABLE IF EXISTS home;
DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	ident TEXT UNIQUE NOT NULL,
	long_uri TEXT NOT NULL
);

CREATE TABLE home (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	display_name TEXT UNIQUE NOT NULL,
	uri_id INTEGER NOT NULL,
	FOREIGN KEY (uri_id) REFERENCES urls (id)
);
