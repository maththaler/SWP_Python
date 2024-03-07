import sqlite3 as db

_fields = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def insert_dict(dict):
    for item in _fields:
        if not item in dict.keys():
            dict[item] = 0
        else:
            dict[item] = int(dict[item])

def init_db():
    connection = db.connect("Rock_Paper_Scissors_Spock_Lizard.db")

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Rock_Paper_Scissors_Spock_Lizard \
                (id INTEGER PRIMARY KEY AUTOINCREMENT, rock INTEGER, paper INTEGER, \
                scissors INTEGER, spock INTEGER, lizard INTEGER)")
    return cursor, connection

def insert_data(dict):
    cursor, connection = init_db()
    insert_dict(dict)
    print(dict)
    cursor.execute(f"INSERT INTO Rock_Paper_Scissors_Spock_Lizard \
                  (rock, paper, scissors, spock, lizard) VAlUES \
                  ({dict['Rock']}, {dict['Paper']}, {dict['Scissors']}, {dict['Spock']}, {dict['Lizard']})")
    connection.commit()
    connection.close()