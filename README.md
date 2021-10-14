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
```
curl --location --request GET '127.0.0.1:5000/'
```