-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music

CREATE TABLE songs
(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    duration_in_seconds INTEGER NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    artist_id INTEGER REFERENCES songs,
    artists TEXT[] NOT NULL
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    album_id INTEGER REFERENCES artists,
    album TEXT NOT NULL
);

CREATE TABLE producers(
    id SERIAL PRIMARY KEY,
    producer_id INTEGER REFERENCES albums, 
    producers TEXT[] NOT NULL
);

INSERT INTO songs
    (title, duration_in_seconds, release_date)
VALUES
    ('MMMBop', 238, '04-15-1997'),
    ('Bohemian Rhapsody', 355, '10-31-1975'),
    ('One Sweet Day', 282, '11-14-1995'),
    ('Shallow', 216, '09-27-2018'),
    ('How You Remind Me', 223, '08-21-2001'),
    ('New York State of Mind', 276, '10-20-2009'),
    ('Dark Horse', 215, '12-17-2013'),
    ('Moves Like Jagger', 201, '06-21-2011'),
    ('Complicated', 244, '05-14-2002'),
    ('Say My Name', 240, '11-07-1999');

INSERT INTO artists 
    (artist_id, artists)
VALUES
    (1, '{"Hanson"}'),
    (2, '{"Queen"}'),
    (3, '{"Mariah Cary", "Boyz II Men"}'),
    (4, '{"Lady Gaga", "Bradley Cooper"}'),
    (5, '{"Nickelback"}'),
    (6, '{"Jay Z", "Alicia Keys"}'),
    (7, '{"Katy Perry", "Juicy J"}'),
    (8, '{"Maroon 5", "Christina Aguilera"}'),
    (9, '{"Avril Lavigne"}'),
    (10, '{"Destiny''s Child"}');

INSERT INTO albums
    (album_id, album)
VALUES
    (1, 'Middle of Nowhere'),
    (2, 'A Night at the Opera'),
    (3, 'Daydream'),
    (4, 'A Star Is Born'),
    (5, 'Silver Side Up'),
    (6, 'The Blueprint 3'),
    (7, 'Prism'),
    (8, 'Hands All Over'),
    (9, 'Let Go'),
    (10, 'The Writing''s on the Wall' );

INSERT INTO producers 
    (producer_id, producers)
VALUES
    (1, '{"Dust Brothers", "Stephen Lironi"}'),
    (2, '{"Roy Thomas Baker"}'),
    (3, '{"Walter Afanasieff"}'),
    (4, '{"Benjamin Rice"}'),
    (5, '{"Rick Parashar"}'),
    (6, '{"Al Shux"}'),
    (7, '{"Max Martin", "Cirkut"}'),
    (8, '{"Shellback", "Benny Blanco"}'),
    (9, '{"The Matrix"}'),
    (10, '{"Darkchild"}');


  