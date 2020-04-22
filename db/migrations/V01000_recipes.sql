CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    origin VARCHAR(100)
);

CREATE TYPE UOM AS ENUM (
    'cup',
    'tsp',
    'tbsp',
    'oz',
    'lb',
    'g',
    'kg',
    'count',
    'pinch',
    'qt',
    'pt'
);

CREATE TABLE ingredient (
    id BIGSERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipe(id),
    name VARCHAR(100),
    quantity DECIMAL,
    units UOM
);

CREATE TABLE step (
    id BIGSERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipe(id),
    step_no INTEGER NOT NULL,
    description VARCHAR(500)
);

CREATE TABLE note (
    id BIGSERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipe(id),
    note_no INTEGER NOT NULL,
    description VARCHAR(500)
);

INSERT INTO recipe (title, origin) VALUES ('Aloo Palak', 'India');
INSERT INTO ingredient (recipe_id, name, quantity, units) VALUES (1, 'Potatoes', 2, 'count');
INSERT INTO ingredient (recipe_id, name, quantity, units) VALUES (1, 'Spinach', 9, 'oz');
INSERT INTO step (recipe_id, step_no, description) VALUES (1, 1, 'Put oil and cumin seeds into a fry and heat to a sizzle.');
INSERT INTO step (recipe_id, step_no, description) VALUES (1, 2, 'Add red chili, hing and something else...');



-- Make a view to extract all the unique ingredients
