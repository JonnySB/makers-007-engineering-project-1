DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text NOT NULL UNIQUE,
    email text NOT NULL UNIQUE,
    hashed_password BYTEA NOT NULL
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

----------------

DROP TABLE IF EXISTS booking_requests CASCADE;
DROP SEQUENCE IF EXISTS booking_requests_id_seq;

CREATE SEQUENCE IF NOT EXISTS booking_requests_id_seq;
CREATE TABLE booking_requests (
    id SERIAL PRIMARY KEY,
    guest_id int,
    constraint fk_user foreign key(guest_id)
        references users(id)
        on delete cascade,  
    pending boolean,
    accepted boolean,
    booking_id int,
    constraint fk_booking foreign key(booking_id)
        references bookings(id)
        on delete cascade  
);

----------------

DROP TABLE IF EXISTS booking_requests CASCADE;
DROP SEQUENCE IF EXISTS booking_requests_id_seq;

CREATE SEQUENCE IF NOT EXISTS booking_requests_id_seq;
CREATE TABLE booking_requests (
    id SERIAL PRIMARY KEY,
    guest_id int,
    constraint fk_user foreign key(guest_id)
        references users(id)
        on delete cascade,  
    pending boolean,
    accepted boolean,
    booking_id int,
    constraint fk_booking foreign key(booking_id)
        references bookings(id)
        on delete cascade  
);

INSERT INTO users (username, email, hashed_password) VALUES ('user1', 'user1@user.com', '\x243262243132247869754d4f49332f43434a713167786d78505152567538782f5269726d4a32303450424d6a53766f7464744a4476436641616e3761');
INSERT INTO users (username, email, hashed_password) VALUES ('user2', 'user2@user.com', '\x243262243132247869754d4f49332f43434a713167786d78505152567538782f5269726d4a32303450424d6a53766f7464744a4476436641616e3761');
INSERT INTO users (username, email, hashed_password) VALUES ('user3', 'user3@user.com', '\x243262243132247869754d4f49332f43434a713167786d78505152567538782f5269726d4a32303450424d6a53766f7464744a4476436641616e3761');
INSERT INTO users (username, email, hashed_password) VALUES ('user4', 'user4@user.com', '\x243262243132247869754d4f49332f43434a713167786d78505152567538782f5269726d4a32303450424d6a53766f7464744a4476436641616e3761');
INSERT INTO users (username, email, hashed_password) VALUES ('user5', 'user5@user.com', '\x243262243132247869754d4f49332f43434a713167786d78505152567538782f5269726d4a32303450424d6a53766f7464744a4476436641616e3761');

INSERT INTO spaces (name, description, price, user_id) VALUES ('Enchanted Retreat', 'Discover the magic of this hidden gem. A cozy haven surrounded by nature, perfect for a peaceful escape.', 130, 1);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Urban Oasis Loft', 'Experience city living at its finest. Our modern loft offers stunning views and all the amenities you need for a stylish stay.', 130, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Sunset Serenity Cottage', 'Unwind in our charming cottage with breathtaking sunset views. A tranquil setting for a memorable getaway.', 130, 3);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Luxury Skyline Penthouse', 'Indulge in luxury high above the city. Our penthouse boasts panoramic skyline views and top-notch amenities.', 130, 4);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Seaside Bliss Villa', 'Escape to paradise in our seaside villa. Relax to the sound of waves and enjoy the ultimate beachfront experience.', 130, 1);

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

INSERT INTO booking_requests (guest_id, pending, accepted, booking_id) VALUES (1, 'TRUE', 'FALSE', 1);
INSERT INTO booking_requests (guest_id, pending, accepted, booking_id) VALUES (1, 'TRUE', 'FALSE', 1);
INSERT INTO booking_requests (guest_id, pending, accepted, booking_id) VALUES (1, 'TRUE', 'FALSE', 1);
