install:
	@python3 setup.py install --user

build:
	@python3 setup.py sdist

upload:
	@twine upload dist/*

clean:
	@rm -rf dist/ && rm -rf *.egg-info
	@echo cleaned all local builds
