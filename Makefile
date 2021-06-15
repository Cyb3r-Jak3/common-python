.PHONY: clean clean-build clean-pyc test check-dist lint

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
	python setup.py sdist bdist_wheel

check-dist:
	pip install wheel twine --quiet
	python setup.py egg_info
	python setup.py sdist bdist_wheel
	twine check --strict dist/*

lint:
	black --line-length 100 --check cyberjake
	pylint cyberjake
	flake8 --max-line-length 100 --statistics --show-source --count cyberjake
	bandit -r cyberjake

test:
	py.test --cov cyberjake tests/ -vv

reformat:
	black --line-length 100 ./cyberjake