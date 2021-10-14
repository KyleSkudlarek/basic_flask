all: clean test

clean:
	/bin/rm -rf ./__pycache__/
	/bin/rm -rf ./.pytest_cache

test: clean
	bash scripts/test.sh

.PHONY: all clean test