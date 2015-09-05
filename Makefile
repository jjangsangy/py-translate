SCRIPT  := $(shell which translate)

VERSION := 3

PIP     := pip$(VERSION)
PYTHON  := python$(VERSION)
APP     := translate
TEST    := test

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv --python=$(PYTHON) venv
	source venv/bin/activate; \
	 $(PIP) install --upgrade pip setuptools wheel; \
	 $(PIP) install -r requirements.txt --upgrade
	touch venv/bin/activate

.PHONY: clean wheel publish

all:
	$(PYTHON) setup.py build

build: venv
	source env/bin/activate; \
	 $(PYTHON) setup.py install

install:
	$(PIP) install -e .

test: build
	source env/bin/activate; \
	 $(PIP) install -r test_requirements.txt --upgrade; \
	 $(PYTHON) setup.py $(TEST)

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
	rm -rf venv
	if [ -f "$(SCRIPT)" ]; then rm "$(SCRIPT)"; fi
