CREATE DATABASE vision;
USE vision;
CREATE TABLE ponto_interesse(
id INT(6) AUTO_INCREMENT,
lat DECIMAL(10, 6) NOT NULL,
lng DECIMAL(11, 6) NOT NULL,
ponto_interesse varchar(50),
PRIMARY KEY (id));