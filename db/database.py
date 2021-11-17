import re
import mysql.connector
import mysql.connector.errors
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    passwd="",
    database="csapatsport"
)

cursor = db.cursor(buffered=True, dictionary=True)


def create_database():
    try:
        cursor.execute("CREATE DATABASE Csapatsport")
    except mysql.connector.errors.DatabaseError:
        print("Csapatsport db already exists")
    finally:
        db.commit()


def print_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name} ")
    for x in cursor:
        print(x)


def create_tables():
    print(f"Executing sql file: create_tables.sql")
    statement = ""
    with open(os.path.join("db/sql", "create_tables.sql"), "r") as file:
        for row in file:
            if re.search(r';$', row):
                statement += row
                cursor.execute(statement)
                statement = ""
            else:
                statement += row
    db.commit()

def triggers():
    statement = ""
    for row in open(os.path.join("db/sql", "triggers.sql")):
        if re.search(r'END;$', row):
            statement += row
            cursor.execute(statement)
            statement = ""
        else:
            statement += row

def drop_tables():
    print(f"Executing sql file: reset_tables.sql")
    for line in open(os.path.join("db/sql", "reset_tables.sql")):
        try:
            cursor.execute(line)
        except mysql.connector.errors.ProgrammingError:
            print("Tables doesen't exists")
    db.commit()

def fill_up_tables(sql_file_name):
    print(f"Executing sql file: {sql_file_name}")
    with open(os.path.join("db/sql", sql_file_name), "r", encoding="utf-8") as file:
        for line in file:
            cursor.execute(line)
    db.commit()
