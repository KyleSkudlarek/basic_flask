## How to Install

```
# Initialize the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the project specific depdencies
pip3 install -r requirements.txt
```

## How to Run
```
flask run
```


## How to Unit Test
```
make test
```

## How to Live Test

Get all players
```
curl --location --request GET '127.0.0.1:5000/api/players'
```

Get player by playerID
```
curl --location --request GET '127.0.0.1:5000/api/players/aardsda01'
```

Increment player height by playerID
```
curl --location --request PUT '127.0.0.1:5000/api/players/aardsda01/height' \
--data-raw ''
```

Increment player weight by playerID
```
curl --location --request PUT '127.0.0.1:5000/api/players/aardsda01/weight' \
--data-raw ''
```