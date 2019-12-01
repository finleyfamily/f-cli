clean:
	rm -rf build/
	rm -rf dist/
	rm -rf f-cli.egg-info/
	rm -rf tmp/

sync:
	PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev

build: clean
	python setup.py sdist bdist_wheel
