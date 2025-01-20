import yaml
import psycopg2
from psycopg2 import Error

def open_yaml():
    with open('logbook.yaml') as logbook:
        data_logbook = yaml.load(logbook, Loader=yaml.FullLoader)
    return data_logbook

def search_in_library(data_input, id_book):
   filtered_books = list(filter(lambda x: x['book_id'] == id_book, data_input))
   sorted_book = sorted(filtered_books, key=lambda x: x['taken_at'])
   last = sorted_book[len(sorted_book) - 1]
   if last:
      return last
   else:
      return 0

def get_book_from_library(book_id):
    data_logbook = open_yaml()
    search_logbook = search_in_library(data_logbook, book_id)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1q2w3e4r5t",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="library")

        cursor = connection.cursor()

        cursor.execute("SELECT author, title from book WHERE id = %s", [book_id])
        author, title = cursor.fetchone()

        cursor.execute("SELECT first_name, last_name from reader WHERE id = %s", [search_logbook["reader_id"]])
        first_name, last_name = cursor.fetchone()

        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

    if search_logbook["returned_at"] != None:
        in_library = True
    else:
        in_library = False

    result = {
        "book_id": book_id,
        "book_name": title,
        "last_reader_id": search_logbook["reader_id"],
        "last_reader_full_name": first_name + " " + last_name,
        "in_library": in_library
    }
    return result