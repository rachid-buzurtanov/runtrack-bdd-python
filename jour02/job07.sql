CREATE DATABASE IF NOT EXISTS lethalcompany;
USE lethalcompany;

CREATE TABLE IF NOT EXISTS service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL(10, 2) NOT NULL,
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service(id)
);

START TRANSACTION;

INSERT INTO service (nom) VALUES ('Web'), ('Dev App'), ('Fullstack');

INSERT INTO employe (nom, prenom, salaire, id_service) VALUES 
    ('Azer', 'Qwer', 3400.00, (SELECT id FROM service WHERE nom = 'Web')),
    ('Zer', 'Wer', 2700.00, (SELECT id FROM service WHERE nom = 'Dev App')),
    ('Er', 'God', 3120.00, (SELECT id FROM service WHERE nom = 'Fullstack'));

COMMIT;
