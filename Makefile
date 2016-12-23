.PHONY: all

all: test lint

test:
	python -m unittest discover

lint:
	python -m flake8 && python -m pylint *.py
