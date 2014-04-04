init:
	pip install -r requirements.txt

test:
	py.test

.PHONY: clean

build:
	python setup.py build

dist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

install:
	python setup.py install

clean:
	rm -rf translate/*.pyc
	rm -rf __pycache__
	rm -rf translate/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
