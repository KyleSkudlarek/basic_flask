import mysql.connector

cnx = mysql.connector.connect(user='kyle', password='KJSkud26',
                              host='127.0.0.1',
                              database='main',
                              port=3306,
                              autocommit=True)
cursor = cnx.cursor()


def create_table():
    # Create table
    query = """
    CREATE TABLE players(
       name VARCHAR(100) NOT NULL,
       score INT,
       PRIMARY KEY ( name )
    );
    """
    print(query)
    cursor.execute(query)
    cursor.close()


def load_table():
    # Insert into table
    query = """
    INSERT INTO players(name)
    VALUES ('Kyle');
    """
    print(query)
    cursor.execute(query)
    cursor.close()


if __name__ == "__main__":
    create_table()
    load_table()