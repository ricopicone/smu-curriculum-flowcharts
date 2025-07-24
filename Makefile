.PHONY: pypi all

nothing: # Default to nothing

all: pypi

pypi:
	poetry lock
	poetry build
	poetry publish
