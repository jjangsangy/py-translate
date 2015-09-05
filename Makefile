SCRIPT := $(shell which translate)

VERSION = 3

PIP        := pip$(VERSION)
PYTHON     := python$(VERSION)
APP        := translate
TEST       := test
DOCKER_TAG := jjangsangy/python3:3.5.0b4


env: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv --python=$(PYTHON) env
	source env/bin/activate; $(PIP) install -r requirements.txt --upgrade
	touch env/bin/activate

.PHONY: clean wheel publish docker bash daemon

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


docker:
	docker build -t $(DOCKER_TAG) .
bash:
	docker run -i -t $(DOCKER_TAG) /bin/bash -l
daemon:
	docker run -d -P $(DOCKER_TAG)
