clean:
	rm -rf build/
	rm -rf dist/
	rm -rf docs/.venv docs/build docs/changelog.md
	rm -rf f-cli.egg-info/
	rm -rf tmp/

build: clean
	poetry build
