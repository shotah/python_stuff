all: hooks lint install-dev

PHONY: lint
lint:
	pipenv run pre-commit run --all-files

PHONY: test
test:
	pipenv run pytest .

PHONY: install
install:
	pipenv install

PHONY: install-dev
install-dev:
	pipenv install --dev

PHONY: sync
sync:
	pipenv sync

PHONY: sync-dev
sync-dev:
	pipenv sync --dev

PHONY: hooks
hooks:
	pipenv run pre-commit install
