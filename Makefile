SHELL   := /bin/bash
PROJECT := py-translate
VERSION := 2
PYTHON  := $(shell which python$(VERSION))
OSNAME  := $(shell uname -s)
ARCH    := $(shell uname -m)

PIP        := pip$(VERSION)
APP        := py-translate
TEST       := test
DOCKER_TAG := jjangsangy/python3:3.5.0b4

INSTALL := Miniconda$(subst 2,,$(VERSION))-latest-$(subst Darwin,MacOSX,$(OSNAME))-$(ARCH).sh
URL     := http://repo.continuum.io/miniconda/${INSTALL}
CONDA   := miniconda/bin/conda
IPYTHON := miniconda/bin/ipython
CACHE   := cache

BIN     := node_modules/.bin
NPM     := $(BIN)/npm
BOWER   := $(BIN)/bower
NVM     := https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh
NVM_DIR := $(PWD)/nvm
LOAD    := ./$(CACHE)/$(INSTALL)

.PHONY: all
all: install

.PHONY: miniconda
miniconda: $(CONDA)
	$(CONDA) update conda

$(CONDA):
	@echo $(LAOD)
	@echo "installing Miniconda"
	@if  [ -x $(which curl) ]; then \
	  curl -O $(URL) -o $(LOAD); \
	elif [ -x $(which wget) ]; then \
	  wget $(URL) -o $(LOAD); \
	fi
	@if  [ -r miniconda ]; then rm -rf miniconda; fi
	@bash $(INSTALL) -b -p miniconda
	$(CONDA) create -n venv python=$(VERSION)*

.PHONY: help
help:
	@echo " Usage: \`make <target>'"
	@echo " ======================="
	@echo "  npm        install npm and nodejs"
	@echo "  bower      install bower and javascript"
	@echo "  serve      serve ipython notebook on port 8000"
	@echo "  clean      remove build files"
	@echo "  miniconda  boostrap anacondas python"
	@echo
	@echo

.PHONY: ipython
ipython: $(CONDA)
	@echo "Installing IPython"

$(IPYTHON):
	@echo "Installing Required Packages"
	$(CONDA) install -y anaconda

npm: $(NVM_DIR)/nvm.sh
	@echo "Installing NodeJS Packages"
	@test -d $(BIN) || mkdir -p $(BIN)
	npm install .

$(NVM_DIR)/nvm.sh:
	@echo "Installing NVM"
	@git clone https://github.com/creationix/nvm.git
	source nvm/nvm.sh && nvm install stable && nvm use stable && npm install .

.PHONY: bower
bower: npm
	@echo "Installing Javascript Packages"
	@$(NPM) install --loglevel silent .

bower.json: bower
	$(bower) init
	@$(BOWER) install

.PHONY: install
install: miniconda npm bower
	@echo "Installing Packages"

.PHONY: serve
serve: install
	$(IPYTHON)/ipython nbconvert --serve Qadium.ipynb

.PHONY: clean
clean:
	rm -rf node_modules
	rm -rf venv
	rm -rf .DS_Store
	rm -rf miniconda
	rm -rf nvm

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv --python=$(PYTHON) venv
	source venv/bin/activate; \
	 $(PIP) install --upgrade pip setuptools wheel; \
	 $(PIP) install -r requirements.txt --upgrade
	touch venv/bin/activate

.PHONY: clean wheel publish docker bash daemon

all:
	$(PYTHON) setup.py build

build: venv
	source env/bin/activate; \
	 $(PYTHON) setup.py install

install:
	$(PIP) install -e .

test: build
	source venv/bin/activate; \
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


docker:
	docker build -t $(DOCKER_TAG) .
bash:
	docker run -i -t $(DOCKER_TAG) /bin/bash -l
daemon:
	docker run -d -P $(DOCKER_TAG)
