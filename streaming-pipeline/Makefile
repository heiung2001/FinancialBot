# Export env variables from .env file if it exists.
ifneq (,$(wildcard .env))
include .env
export
endif


### INSTALL ###
install:
	@echo "Installing streaming pipeline..."

	poetry env use $(shell which python3.10) && \
	PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring poetry install

install_dev: install
	PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring poetry install --with dev

uninstall:
	@echo "Uninstall streaming pipeline..."

	poetry env remove ${env}


### RUN ###
search:
	poetry run python -m tools.search ${PARAMS}