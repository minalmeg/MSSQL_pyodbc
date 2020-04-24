/* Create a table called Animal List which has two fields - ID and ANIMAL*/

CREATE TABLE animal_list(

	ID INT NULL,
	ANIMAL NCHAR(10) NULL
);

GO

/*Insert values into the table animal_list*/

INSERT INTO animal_list(ID,ANIMAL) VALUES(1, 'Wolf')
INSERT INTO animal_list(ID,ANIMAL) VALUES(2, 'Cheetah')
INSERT INTO animal_list(ID,ANIMAL) VALUES(3, 'Rabbit')
INSERT INTO animal_list(ID,ANIMAL) VALUES(4, 'Tiger')
INSERT INTO animal_list(ID,ANIMAL) VALUES(5, 'Deer')

go 

/*select all values from the table animal_list*/

SELECT * FROM animal_list
