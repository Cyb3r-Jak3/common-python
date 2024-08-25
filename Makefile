.PHONY: clean clean-build clean-pyc test check-dist lint format docs

clean: clean-build clean-pyc

full-test: lint test

ifeq ($(OS),Windows_NT)
    RM = del //Q //F
    RRM = rmdir //Q //S
else
    RM = rm -f
    RRM = rm -f -r
endif

clean-build:
	$(RMM) -r build
	$(RMM) -r dist
	$(RMM) -r *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec $(RM) {} +
	find . -name '*.pyo' -exec $(RM) {} +
	find . -name '*~' -exec $(RM) {} +

build:
	poetry build

check-dist:
	pip install wheel twine --quiet
	poetry build
	twine check --strict dist/*

lint:
	poetry run ruff format --check --line-length 100 --target-version py310 cyberjake
	poetry run pylint cyberjake
	poetry run flake8 --max-line-length 100 --statistics --show-source --count cyberjake
	poetry run bandit -r cyberjake

test:
	poetry run pytest --cov cyberjake tests/ -vv

format:
	poetry run ruff format --line-length 100 --target-version py310 cyberjake

docs:
	poetry run sphinx-apidoc -f -o docs/ cyberjake
	$(MAKE) -C docs clean
	$(MAKE) -C docs html