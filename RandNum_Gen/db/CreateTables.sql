CREATE DATABASE IF NOT EXISTS flask-db;

CREATE table IF NOT EXISTS flask-db.randnum(
    User_id Integer NOT NULL AUTO_INCREMENT PRIMARY KEY,  
    RandNum Integer (20) NOT NULL
); 

LOCK TABLES `randnum`WRITE; 
INSERT INTO `randnum`VALUES (1,'admin','admin');
UNLOCK TABLES; 