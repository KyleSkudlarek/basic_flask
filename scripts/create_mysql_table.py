import mysql.connector

cnx = mysql.connector.connect(user='kyle', password='KJSkud26',
                              host='127.0.0.1',
                              database='main',
                              port=3306,
                              autocommit=True)
cursor = cnx.cursor()



# playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID
def create_table():
    # Create table
    query = """
    CREATE TABLE players(
       playerID VARCHAR(100) NOT NULL,
       birthYear INT,
       birthMonth INT,
       birthDay INT,
       birthCountry VARCHAR(100),
       birthState VARCHAR(100),
       birthCity VARCHAR(100),
       deathYear INT,
       deathMonth INT,
       deathDay INT,
       deathCountry VARCHAR(100),
       deathState VARCHAR(100),
       deathCity VARCHAR(100),
       nameFirst VARCHAR(100),
       nameLast VARCHAR(100),
       nameGiven VARCHAR(100),
       weight INT,
       height INT,
       bats VARCHAR(100),
       throws VARCHAR(100),
       debut VARCHAR(100),
       finalGame VARCHAR(100),
       retroID VARCHAR(100),
       bbrefID VARCHAR(100),     
       PRIMARY KEY ( playerID )
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
    # load_table()