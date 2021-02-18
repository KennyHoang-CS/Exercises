-- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

\c outer_space

CREATE TABLE galaxys(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE planets
(
    id SERIAL PRIMARY KEY,
    planet_id INTEGER REFERENCES galaxys,
    name TEXT NOT NULL
);

CREATE TABLE orbits(
    id SERIAL PRIMARY KEY,
    orbit_id INTEGER REFERENCES planets,
    orbital_period_in_years FLOAT NOT NULL,
    orbits_around TEXT NOT NULL
);

CREATE TABLE moons(
    id SERIAL PRIMARY KEY,
    moon_id INTEGER REFERENCES planets,
    moons TEXT[]
);

INSERT INTO galaxys (name)
VALUES
    ('Milky Way'),
    ('Proxima Centauri');

INSERT INTO planets (planet_id, name)
VALUES
    (1, 'Earth'),
    (1, 'Mars'),
    (1, 'Venus'),
    (1, 'Neptune'),
    (2, 'Proxima Centauri b'),
    (1, 'Gliese 876 b');

INSERT INTO orbits (orbit_id, orbital_period_in_years, orbits_around)
VALUES
    (1, 1.00, 'The Sun'),
    (1, 1.88, 'The Sun'),
    (1, 0.62, 'The Sun'),
    (1, 164.8, 'The Sun'),
    (2, 0.03, 'Proxima Centauri'),
    (1, 0.23, 'Gliese 876');

INSERT INTO moons (moon_id, moons)
VALUES
    (1, '{"The Moon"}'),
    (1, '{"Phobos", "Deimos"}'),
    (1, '{}'),
    (1, '{"Naiad", "Thalassa", "Despina", "Galatea", "Larissa", "S/2004 N 1", "Proteus", "Triton", "Nereid", "Halimede", "Sao", "Laomedeia", "Psamathe", "Neso"}'),
    (2, '{}'),
    (1, '{}');
