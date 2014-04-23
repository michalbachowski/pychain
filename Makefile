.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "doctest - run doctests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc
	rm -fr htmlcov/

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	python -B setup.py test

test-all:
	tox

coverage:
	python -B -mcoverage run --source pychain setup.py test
	python -B -mcoverage report -m

docs:
	rm -f docs/pychain.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pychain
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release: clean
	python -B setup.py sdist upload
	python -B setup.py bdist_wheel upload

dist: clean
	python -B setup.py sdist
	python -B setup.py bdist_wheel
	ls -l dist
