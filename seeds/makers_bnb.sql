DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text NOT NULL UNIQUE,
    email text NOT NULL UNIQUE,
    hashed_password text NOT NULL
);

----------------

DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price float,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

----------------

DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date date,
    available boolean,
    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade  
);

INSERT INTO users (username, email, hashed_password) VALUES ('user1', 'user1@user.com', 'Password');
INSERT INTO users (username, email, hashed_password) VALUES ('user2', 'user2@user.com', 'Password');
INSERT INTO users (username, email, hashed_password) VALUES ('user3', 'user3@user.com', 'Password');
INSERT INTO users (username, email, hashed_password) VALUES ('user4', 'user4@user.com', 'Password');
INSERT INTO users (username, email, hashed_password) VALUES ('user5', 'user5@user.com', 'Password');

INSERT INTO spaces (name, description, price, user_id) VALUES ('Space1', 'Example description 1', 130, 1);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Space2', 'Example description 2', 130, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Space3', 'Example description 3', 130, 3);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Space4', 'Example description 4', 130, 4);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Space5', 'Example description 5', 130, 1);

INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-10', 'TRUE', 1);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-11', 'FALSE', 1);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-12', 'FALSE', 1);

INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-10', 'FALSE', 2);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-11', 'FALSE', 2);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-12', 'TRUE', 2);

INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-10', 'TRUE', 3);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-11', 'TRUE', 3);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-12', 'TRUE', 3);

INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-10', 'TRUE', 4);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-11', 'TRUE', 4);
INSERT INTO bookings (date, available, space_id) VALUES ('2024-05-12', 'TRUE', 4);
