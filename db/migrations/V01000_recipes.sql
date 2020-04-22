CREATE TABLE map (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description VARCHAR(500),
    created TIMESTAMP NOT NULL,
    last_update TIMESTAMP NOT NULL
);

CREATE TYPE SHAPE AS ENUM (
    'circle',
    'square',
    'triangle',
    'character'
);

CREATE TABLE coordinates (
    id BIGSERIAL PRIMARY KEY,
    map_id INTEGER REFERENCES map(id),
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    description VARCHAR(500),
    symbol CHAR,
    shape SHAPE,
    red INTEGER,
    green INTEGER,
    blue INTEGER
);

INSERT INTO map (title, description, created, last_update)
    VALUES ('test map', 'map to test with', current_timestamp, current_timestamp);
INSERT INTO map (title, description, created, last_update)
    VALUES ('test map 2', 'another map to test with', current_timestamp, current_timestamp);
INSERT INTO coordinates (map_id, x, y, description)
    VALUES (1, 100, 100, 'test coordinates');
INSERT INTO coordinates (map_id, x, y, description)
    VALUES (1, -100, 200, 'test coordinates');
INSERT INTO coordinates (map_id, x, y, description)
    VALUES (2, 300, -200, 'test coordinates');
INSERT INTO coordinates (map_id, x, y, description)
    VALUES (2, -175, 900, 'test coordinates');
-- Make a view to extract all the unique ingredients
