PIPENV_IGNORE_VIRTUALENVS=1

all: hooks install-dev lint test

PHONY: clean
clean:
	pipenv clean || echo "no environment found to clean"
	pipenv run python -c "import os; os.remove('Pipfile.lock')" || echo "no lock file to remove"

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
	pip install pre-commit
	pre-commit install
