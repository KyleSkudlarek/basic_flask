#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -z "$VIRTUAL_ENV" ]; then
  echo "Please enable a python 3 virtual env"
  exit 1
fi

echo "Using virtualenv located in : $VIRTUAL_ENV"

echo -e "\n| --------------------- Running unit tests ------------------------ |"

cd src
python -m pytest

echo -e "| -------------------- Unit tests completed ------------------------ |\n"
