import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1q2w3e4r5t",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="library")

    cursor = connection.cursor()

    query = """ CREATE TABLE IF NOT EXISTS book (
                    id INT PRIMARY KEY,
                    author varchar(255), 
                    title varchar(255) 
                );
                CREATE TABLE IF NOT EXISTS reader (
                    id INT PRIMARY KEY,
                    first_name varchar(255), 
                    last_name varchar(255) 
                );
                
                INSERT INTO book
                    (id, author, title)
                VALUES 
                    (1, 'Chinua Achebe', 'hings Fall Apart'),
                    (2, 'Hans Christian Andersen', 'Fairy tales'),
                    (3,'Dante Alighieri','The Divine Comedy'),
                    (4,'Unknown','Sumer and Akkadian Empire'),
                    (5,'Unknown','Achaemenid Empire'),
                    (6,'Unknown','One Thousand and One Nights'),
                    (7,'Unknown','Old Norse'),
                    (8,'Jane Austen','Pride and Prejudice'),
                    (9,'Honoré de Balzac','Le Père Goriot'),
                    (10,'Samuel Beckett','Molloy, Malone Dies, The Unnamable, the trilogy'),
                    (11,'Giovanni Boccaccio','The Decameron');
                 
                INSERT INTO reader
                    (id, first_name, last_name)
                VALUES 
                    (1, 'Ivan', 'Ivanov'),   
                    (2, 'Alexandr', 'Petrov'),   
                    (3, 'Artyom', 'Tihonov'),   
                    (4, 'Mikhail', 'Sidorov'),   
                    (5, 'Anatoliy', 'Lukin'),   
                    (6, 'Olga', 'Goncharova'),   
                    (7, 'Irina', 'Gordeeva');   
                    
            """
    cursor.execute(query)
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
