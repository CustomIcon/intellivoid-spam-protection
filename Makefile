
install:
	python3 setup.py install

build:
	python3 setup.py sdist

upload:
	twine upload dist/*