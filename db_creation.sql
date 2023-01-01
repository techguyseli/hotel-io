CREATE DATABASE hotelio;

USE  hotelio;

CREATE TABLE users (
    user_id int PRIMARY KEY IDENTITY(1,1),
    email VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    adress VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    role VARCHAR(15) NOT NULL
);

CREATE TABLE cities (
    city_id int PRIMARY KEY IDENTITY(1,1),
    city_name VARCHAR(25) NOT NULL UNIQUE   
);

CREATE TABLE hotels (
    hotel_id int PRIMARY KEY IDENTITY(1,1),
    hotel_name VARCHAR(25) NOT NULL UNIQUE,
    hotel_adress VARCHAR(30) NOT NULL UNIQUE,
    stars int NOT NULL,
    rib VARCHAR(50) NOT NULL,
    city_id int foreign key references cities(city_id) ON DELETE SET NULL,
    manager_id int foreign key references users(user_id) ON DELETE SET NULL
);

CREATE TABLE options (
    option_id int PRIMARY KEY IDENTITY(1,1),
    hotel_option VARCHAR(25) NOT NULL UNIQUE,
);

CREATE TABLE hotels_options (
    option_id int foreign key references options(option_id) ON DELETE CASCADE,
    hotel_id int foreign key references hotels(hotel_id) ON DELETE CASCADE,
    PRIMARY KEY (option_id, hotel_id)
);

CREATE TABLE rooms (
    room_id int PRIMARY KEY IDENTITY(1,1),
    hotel_id int foreign key references hotels(hotel_id) ON DELETE CASCADE,
    room_type VARCHAR(20) NOT NULL,
    price float NOT NULL,
    sheet_count int NOT NULL,
    extra_bed bit NOT NULL,
    rooms_count int NOT NULL,
    UNIQUE (hotel_id, room_type) 
);

CREATE TABLE comments (
    comment_id int PRIMARY KEY IDENTITY(1,1),
    comment_str VARCHAR(5000) NOT NULL,
    comment_date datetime NOT NULL,
    hotel_id int foreign key references hotels(hotel_id) ON DELETE CASCADE,
    user_id int foreign key references users(user_id) ON DELETE SET NULL
);

CREATE TABLE reservations (
    reservation_id int PRIMARY KEY IDENTITY(1,1),
    user_id int foreign key references Users(user_id) ON DELETE CASCADE,
    arrival_date Date NOT NULL,
    departure_date Date NOT NULL,
    reservation_status VARCHAR(20),
    CHECK (reservation_status = 'paid' or reservation_status ='not paid' or reservation_status = 'canceled') 
);

CREATE TABLE rooms_reservation (
    reservation_id int foreign key references reservations(reservation_id) ON DELETE CASCADE,
    room_id int foreign key references rooms(room_id) ON DELETE CASCADE,
    reserved_rooms_count int NOT NULL,
    PRIMARY KEY (reservation_id, room_id)
);

CREATE TABLE ml_training_data (
	hotel_id int PRIMARY KEY,
	comment_str VARCHAR(5000) NOT NULL,
	rating int NOT NULL,
	CHECK(rating = 1 or rating = 0 or rating = -1),
	constraint ml_training_fk foreign key(hotel_id) references hotels(hotel_id) 
);

CREATE TABLE ml_testing_data (
	hotel_id int PRIMARY KEY,
	comment_str VARCHAR(5000) NOT NULL,
	rating int NOT NULL,
	CHECK(rating = 1 or rating = 0 or rating = -1),
	constraint ml_testing_fk foreign key(hotel_id) references hotels(hotel_id) 
);
