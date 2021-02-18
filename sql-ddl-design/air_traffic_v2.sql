-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic

CREATE TABLE tickets
(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    seat TEXT NOT NULL
);

CREATE TABLE departures
(
    id SERIAL PRIMARY KEY,
    departure_id INTEGER REFERENCES tickets,
    departure TIMESTAMP NOT NULL,
    arrival TIMESTAMP NOT NULL,
    airline TEXT NOT NULL
);

CREATE TABLE destinations
(
    id SERIAL PRIMARY KEY,
    dest_id INTEGER REFERENCES departures,
    from_city TEXT NOT NULL,
    from_country TEXT NOT NULL,
    to_city TEXT NOT NULL,
    to_country TEXT NOT NULL
);

INSERT INTO tickets
    (first_name, last_name, seat)
VALUES
    ('Jennifer', 'Finch', '33B'),
    ('Thadeus', 'Gathercoal', '8A'),
    ('Sonja', 'Pauley', '12F'), 
    ('Jennifer', 'Finch', '20A'),
    ('Waneta', 'Skeleton', '23D'),
    ('Thadeus', 'Gathercoal', '18C'),
    ('Berkie', 'Wycliff', '9E'),
    ('Alvin', 'Leathes', '1A'),
    ('Berkie', 'Wycliff', '32B'),
    ('Cory', 'Squibbes', '10D');

INSERT INTO departures
    (departure_id, departure, arrival, airline)
VALUES
    (1, '2018-04-08 09:00:00', '2018-04-08 12:00:00', 'United'),
    (2, '2018-12-19 12:45:00', '2018-12-19 16:15:00', 'British Airways'),
    (3, '2018-01-02 07:00:00', '2018-01-02 08:03:00', 'Delta'),
    (4, '2018-04-15 16:50:00', '2018-04-15 21:00:00', 'Delta'),
    (5, '2018-08-01 18:30:00', '2018-08-01 21:50:00', 'TUI Fly Belgium'),
    (6, '2018-10-31 01:15:00', '2018-10-31 12:55:00', 'Air China'),
    (7, '2019-02-06 06:00:00', '2019-02-06 07:47:00', 'United'),
    (8, '2018-12-22 14:42:00', '2018-12-22 15:56:00', 'American Airlines'),
    (9, '2019-02-06 16:28:00', '2019-02-06 19:18:00', 'American Airlines'),
    (10, '2019-01-20 19:30:00', '2019-01-20 22:45:00', 'Avianca Brasil');

INSERT INTO destinations
    (dest_id, from_city, from_country, to_city, to_country)
VALUES
    (1, 'Washington DC', 'United States', 'Seattle', 'United States'),
    (2, 'Tokyo', 'Japan', 'London', 'United Kingdom'),
    (3, 'Los Angeles', 'United States', 'Las Vegas', 'United States'),
    (4, 'Seattle', 'United States', 'Mexico City', 'Mexico'),
    (5, 'Paris', 'France', 'Casablanca', 'Morocco'),
    (6, 'Dubai', 'UAE', 'Beijing', 'China'),
    (7, 'New York', 'United States', 'Charlotte', 'United States'),
    (8, 'Cedar Rapids', 'United States', 'Chicago', 'United States'),
    (9, 'Charlotte', 'United States', 'New Orleans', 'United States'),
    (10, 'Sao Paolo', 'Brazil', 'Santiago', 'Chile');