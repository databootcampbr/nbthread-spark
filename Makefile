.PHONY: install clean release

ROOT_PATH=$(shell pwd)

install:
	@pip install --process-dependency-links -e .

clean:
	-@rm -rf $(ROOT_PATH)/*.egg-info
	-@rm -rf $(ROOT_PATH)/dist
	-@rm -rf $(ROOT_PATH)/build

release: clean
	@python setup.py register sdist upload -r pypi
