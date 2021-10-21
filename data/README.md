
# Player DB Microservice

Your assignment is to create a microservice which serves the contents of the `People.csv` through a
REST API. You are free to choose whatever programming language you are comfortable with, SDKs, web
frameworks, databases, and online resources to complete this exercise.

## Requirements:
* Provide a REST API to your service
* Package the application for distribution. Some examples of this:
  * Docker image (preferred)
  * Tomcat WAR
  * Static binary
  * others...

## REST API

The service should expose two REST endpoints:
* `GET /api/players` - returns the list of all players
* `GET /api/players/{playerID}` - returns a single player by it's ID

Given a player line of the CSV file:
```
playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID
aardsda01,1981,12,27,USA,CO,Denver,,,,,,,David,Aardsma,David Allan,215,75,R,R,2004-04-06,2015-08-23,aardd001,aardsda01
```

The json representation of a player should be the following, where each field name is equal to the CSV column name:
```json
{
    "playerID": "aardsda01",
    "birthYear": 1981,
    "birthMonth": 12,
    "birthDay": 27,
    "deathYear": null,
    "deathMonth": null,
    "deathDay": null,
    "nameFirst": "David",
    "nameLast": "Aardsma",
    "height": 75,
    ...
    ...
}
```

## Bonus Requirements:

The service should expose two additional REST API endpoint:
* `PUT /api/players/{playerID}/weight` - increments a player's weight by 1
* `PUT /api/players/{playerID}/height` - increments a player's height by 1

The request and response payloads of these endpoints can be an empty JSON dictionary: `{}`
