CREATE TABLE IF NOT EXISTS 'netflix_actors' (
  'actor_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
  'name' varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS 'netflix_shows_to_actors' (
    actor_id INTEGER NOT NULL,
    show_id INTEGER NOT NULL,
    FOREIGN KEY (actor_id) REFERENCES netflix_actors(actor_id),
    FOREIGN KEY (show_id) REFERENCES netflix_titles(show_id)
);