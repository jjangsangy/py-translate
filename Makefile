SCRIPT := $(shell which translate)

VERSION = 3

PIP = pip$(VERSION)
PYTHON = python$(VERSION)
APP = translate
TEST= test


env: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv --python=$(PYTHON) env
	source env/bin/activate; $(PIP) install -r requirements.txt --upgrade
	touch env/bin/activate

.PHONY: clean wheel publish

all:
	$(PYTHON) setup.py build

build: env
	source env/bin/activate; $(PYTHON) setup.py install

install:
	$(PIP) install -e .

test: build
	source env/bin/activate; $(PIP) install -r test_requirements.txt --upgrade; python setup.py $(TEST)

wheel:
	$(PYTHON) setup.py bdist_wheel

publish:
	$(PYTHON) setup.py build nosetests
	$(PYTHON) setup.py sdist upload -r pypi
	$(PYTHON) setup.py bdist_wheel upload -r pypi

clean:
	rm -rf $(APP)/*.pyc
	rm -rf __pycache__
	rm -rf $(APP)/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
	rm -rf env
	if [ -f "$(SCRIPT)" ]; then rm "$(SCRIPT)"; fi
