CREATE DATABASE hotelio;

USE  hotelio;

CREATE TABLE Users (
    idUser int PRIMARY KEY IDENTITY(1,1),
    email VARCHAR(20) NOT NULL UNIQUE,
    mdp VARCHAR(200) NOT NULL,
    nom VARCHAR(15) NOT NULL,
    prenom VARCHAR(30) NOT NULL,
    adresse VARCHAR(50) NOT NULL,
    numTel VARCHAR(15) NOT NULL UNIQUE,
    userRole VARCHAR(15) NOT NULL
);

CREATE TABLE Villes (
    idVille int PRIMARY KEY IDENTITY(1,1),
    nomVille VARCHAR(25) NOT NULL UNIQUE   
);

CREATE TABLE Hotels (
    idHotel int PRIMARY KEY IDENTITY(1,1),
    nom VARCHAR(25) NOT NULL UNIQUE,
    nbrEtoiles int NOT NULL,
    rib VARCHAR(50) NOT NULL,
    idVille int foreign key references Villes(idVille) ON DELETE SET NULL
);

CREATE TABLE Options (
    idOption int PRIMARY KEY IDENTITY(1,1),
    HotelOption VARCHAR(25) NOT NULL UNIQUE,
);

CREATE TABLE HotelOptions (
    idOption int foreign key references Options(idOption) ON DELETE CASCADE,
    idHotel int foreign key references Hotels(idHotel) ON DELETE CASCADE,
    PRIMARY KEY (idOption, idHotel)
);

CREATE TABLE Chambres (
    idChambre int PRIMARY KEY IDENTITY(1,1),
    idHotel int foreign key references Hotels(idHotel) ON DELETE CASCADE,
    typeChambre VARCHAR(20) NOT NULL,
    prix float NOT NULL,
    nbrCouchages int NOT NULL,
    litDePlus bool NOT NULL,
    nbrChambres int NOT NULL,
    UNIQUE (idHotel, typeChambre) 
);

CREATE TABLE Commentaires (
    idCommentaire int PRIMARY KEY IDENTITY(1,1),
    Commentaire VARCHAR(500) NOT NULL,
    idHotel int foreign key references Hotels(idHotel) ON DELETE CASCADE,
    idUser int foreign key references Users(idUser) ON DELETE SET NULL
);

CREATE TABLE Reservations (
    idReservation int PRIMARY KEY IDENTITY(1,1),
    idUser int foreign key references Users(idUser) ON DELETE CASCADE,
    dateArrivee Date NOT NULL,
    dateDepart Date NOT NULL,
    resevationStatut VARCHAR(20),
    CHECK (resevationStatut = 'Payee' or resevationStatut ='Non payee' or resevationStatut = 'Annulee') 
);

CREATE TABLE ChambresReservee (
    idReservation int foreign key references Reservations(idReservation) ON DELETE CASCADE,
    idChambre int foreign key references Chambres(idChambre) ON DELETE CASCADE,
    nbrChambreReservee int NOT NULL,
    PRIMARY KEY (idReservation, idChambre)
);

CREATE TABLE Training (
	hotel_id int PRIMARY KEY,
	comment VARCHAR(500) NOT NULL,
	rating int NOT NULL,
	CHECK(rating = 1 or rating = 0 or rating = -1)
);

CREATE TABLE Test (
	hotel_id int PRIMARY KEY,
	comment VARCHAR(500) NOT NULL,
	rating int NOT NULL,
	CHECK(rating = 1 or rating = 0 or rating = -1)
);