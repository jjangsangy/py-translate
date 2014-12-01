init:
	pip3 install -r requirements.txt

test:
	nosetests -v

.PHONY: clean

build:
	python3 setup.py build

dist:
	python3 setup.py sdist

wheel:
	python3 setup.py bdist_wheel

publish:
	pandoc README.md --from=markdown --to=rst -o README.rst
	python3 setup.py sdist upload -r pypi
	python3 setup.py bdist_wheel upload -r pypi

clean:
	rm -rf translate/*.pyc
	rm -rf __pycache__
	rm -rf translate/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
