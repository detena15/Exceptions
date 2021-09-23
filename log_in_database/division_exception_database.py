"""
Error handling. The def is a division.
The code analise some exceptions and save the data in a data base.
"""
import traceback
from datetime import datetime
import sqlite3

database = "error.db"


def connect_database():
    con = sqlite3.connect(database)
    return con


def check_if_table_exists():
    con = connect_database()
    con.execute("""
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'Exceptions'
    );
    """)


def create_table():
    try:
        con = connect_database()
        con.execute("""
        CREATE TABLE if not exists "Exceptions" (
            "timestamp"	TEXT,
            "traceback"	TEXT
        );
        """)

        con.commit()
        con.close()
    except:
        insert_row(time=datetime.today(), exception=traceback.format_exc())


def insert_row(time, exception):
    con = connect_database()
    con.execute("""
        INSERT INTO "Exceptions" ("timestamp", "traceback") 
        VALUES (?, ?)
        """, [time, exception])

    con.commit()
    con.close()


def division(x, y):
    try:
        z = x/y
        return z
    except ZeroDivisionError:
        # Store the information in the data base
        insert_row(time=datetime.today(), exception=traceback.format_exc())
    except TypeError:
        # Store the information in the data base
        insert_row(time=datetime.today(), exception=traceback.format_exc())
    except:
        # Store the information in the data base
        insert_row(time=datetime.today(), exception=traceback.format_exc())


while True:
    try:
        divisor = float(input("Divisor: "))
        break
    except ValueError:
        print("Debes introducir un número!")

while True:
    try:
        dividendo = float(input("Dividendo: "))
        break
    except ValueError:
        print("Debes introducir un número!")


resultado = division(x=divisor, y=dividendo)

if type(resultado) == float:
    print("El resultado es: ", resultado)
else:
    print("Hubo un error! Revisar la base de datos!")


create_table()

