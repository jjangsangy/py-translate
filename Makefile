init:
	pip install -r requirements.txt

test:
	nosetests

.PHONY: clean

build:
	python setup.py build

dist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

install:
	pip2 install py-translate
	pip3 install py-translate

uninstall:
	pip3 uninstall py-translate
	pip2 uninstall py-translate

publish:
	python setup.py sdist upload -r pypi
	python setup.py bdist_wheel upload -r pypi

clean:
	rm -rf translate/*.pyc
	rm -rf __pycache__
	rm -rf translate/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
