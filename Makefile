SCRIPT := $(shell which translate)

VERSION = 3

PIP = pip$(VERSION)
PYTHON = python$(VERSION)

NOSE_FLAGS = -v
NOSE = nosetests $(NOSE_FLAGS)

.PHONY: clean wheel publish test

all:
	$(PYTHON) setup.py build

install:
	$(PIP) install -e .

test:
	$(NOSE)

wheel:
	$(PYTHON) setup.py bdist_wheel

publish:
	pandoc README.md --from=markdown --to=rst -o README.rst
	$(PYTHON) setup.py build nosetests
	$(PYTHON) setup.py sdist upload -r pypi
	$(PYTHON) setup.py bdist_wheel upload -r pypi

clean:
	rm -rf translate/*.pyc
	rm -rf __pycache__
	rm -rf translate/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
	if [ -f "$(SCRIPT)" ]; then rm "$(SCRIPT)"; fi
