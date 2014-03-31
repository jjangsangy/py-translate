init:
	pip install -r requirements.txt

test:
	py.test

.PHONY: clean

build:
	python setup.py build

clean:
	rm -rf translate/*.pyc
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
