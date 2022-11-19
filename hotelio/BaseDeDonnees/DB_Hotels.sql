CREATE TABLE Users (
    idUser int PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(20) NOT NULL UNIQUE,
    mdp VARCHAR(200) NOT NULL,
    nom VARCHAR(15) NOT NULL,
    prenom VARCHAR(30) NOT NULL,
    adresse VARCHAR(50) NOT NULL,
    numTel VARCHAR(15) NOT NULL UNIQUE,
    userRole VARCHAR(15) NOT NULL
);

CREATE TABLE Villes (
    idVille int PRIMARY KEY AUTO_INCREMENT,
    nomVille VARCHAR(25) NOT NULL UNIQUE   
);

CREATE TABLE Hotels (
    idHotel int PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(25) NOT NULL UNIQUE,
    nbrEtoiles int NOT NULL,
    rib VARCHAR(50) NOT NULL,
    idVille int foreign key references Villes(idVille) ON DELETE SET NULL
);

CREATE TABLE Options (
    idOption int PRIMARY KEY AUTO_INCREMENT,
    HotelOption VARCHAR(25) NOT NULL UNIQUE,
);

CREATE TABLE HotelOptions (
    idOption int foreign key references Options(idOption) ON DELETE CASCADE,
    idHotel int foreign key references Hotels(idHotel) ON DELETE CASCADE,
    PRIMARY KEY (idOption, idHotel)
);

CREATE TABLE Chambres (
    idChambre int PRIMARY KEY AUTO_INCREMENT,
    idHotel int foreign key references Hotels(idHotel) ON DELETE CASCADE,
    typeChambre VARCHAR(20) NOT NULL,
    prix float NOT NULL,
    nbrCouchages int NOT NULL,
    litDePlus boolean NOT NULL,
    nbrChambres int NOT NULL,
    UNIQUE (idHotel, typeChambre) 
);

CREATE TABLE Commentaires (
    idCommentaire int PRIMARY KEY AUTO_INCREMENT,
    Commentaire VARCHAR(500) NOT NULL,
    idHotel int foreign key references Hotels(idHotel) ON DELETE CASCADE,
    idUser int foreign key references Users(idUser) ON DELETE SET NULL
);

CREATE TABLE Reservations (
    idReservation int PRIMARY KEY AUTO_INCREMENT,
    idUser int foreign key references Users(idUser) ON DELETE CASCADE,
    dateArrivee Date NOT NULL,
    dateDepart Date NOT NULL,
    resevationStatut VARCHAR(20),
    CHECK (resevationStatut = 'Payee' or resevationStatut ='Non payee' or resevationStatut = 'Annulee') 
);

CREATE TABLE ChambresReservee (
    idReservation int foreign key references Reservations(idReservation) ON DELETE SET NULL,
    idChambre int foreign key references Chambres(idChambre) ON DELETE CASCADE,
    nbrChambreReservee int NOT NULL,
    PRIMARY KEY (idReservation, idChambre)
);