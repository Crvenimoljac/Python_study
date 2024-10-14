/*Kreiranje tabele*/
CREATE TABLE users(
    id int primary key auto_increment,
    first_name varchar(150),
    last_name varchar(150),
    username varchar(150),
    email varchar(250),
    password varchar(255),
    rand_num int,
    broj decimal(3,2)
)
/*Unos u tabelu*/
INSERT INTO naziv_tabele(first_name, last_name, username,rand_num) 
VALUES("Laki", "CVET", "Moljac", 52)

/*citanje svih podataka iz tabele*/
SELECT * FROM naziv_tabele
/* citanje svih podataka iz tabele gde je uslov ispunjen */
SELECT * FROM naziv_tabele WHERE rand_num=48
/*prebrojavanje redova u tabeli*/
SELECT COUNT(*) FROM users WHERE rand_num=48

/*Kreiraj tabelu spisak kurseva*/