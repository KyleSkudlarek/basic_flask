import mysql.connector

cnx = mysql.connector.connect(user='kyle', password='KJSkud26',
                              host='127.0.0.1',
                              database='main',
                              port=3306,
                              autocommit=True)
cursor = cnx.cursor()



def load_table():


    # Open file
    with open('../data/People.csv', encoding='utf-8-sig') as file:
        i=0
        for line in file:
            if i==0:
                i+=1
                continue
            else:
                line = line.split(sep=",")

                #playerId, birthYear, birthMonth, birthDay, birthCountry, birthState, birthCity, deathYear, deathMonth, deathDay, deathCountry, deathState, deathCity, nameFirst, nameLast, nameGiven, weight, height, bats, throws, debut, finalGame, retroID, bbrefID

                playerID = line[0]
                birthYear = line[1]
                birthMonth = line[2]
                birthDay = line[3]
                birthCountry = line[4]
                birthState = line[5]
                birthCity = line[6]
                deathYear = line[7]
                deathMonth = line[8]
                deathDay = line[9]
                deathCountry = line[10]
                deathState = line[11]
                deathCity = line[12]
                nameFirst = line[13]
                nameLast = line[14]
                nameGiven = line[15]
                weight = line[16]
                height = line[17]
                bats = line[18]
                throws = line[19]
                debut = line[20]
                finalGame = line[21]
                retroID = line[22]
                bbrefID = line[23]


                # Insert into table
                query = f"""
                INSERT INTO players(playerId, birthYear, birthMonth, birthDay, birthCountry, birthState, birthCity, deathYear, deathMonth, deathDay, deathCountry, deathState, deathCity, nameFirst, nameLast, nameGiven, weight, height, bats, throws, debut, finalGame, retroID, bbrefID)
                VALUES ('{playerID}', '{birthYear}', '{birthMonth}', '{birthDay}','{birthCountry}','{birthState}','{birthCity}','{deathYear}','{deathMonth}','{deathDay}','{deathCountry}','{deathState}','{deathCity}','{nameFirst}','{nameLast}','{nameGiven}','{weight}','{height}','{bats}','{throws}','{debut}','{finalGame}','{retroID}','{bbrefID}');
                """
                print(query)
                cursor.execute(query)


if __name__ == "__main__":
    load_table()