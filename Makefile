.SUFFIXES: .ui .py
rwildcard = $(wildcard $1$2)$(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))
UI_FILES = $(call rwildcard,weave/gui/uis/,*.ui)
PY_FILES = $(UI_FILES:.ui=.py)

PREFIX = /usr/local

all: uis

.ui.py:
	pyuic5 $< -o $@

uis: $(PY_FILES)

.PHONY: test
test:
	python3 -m pytest

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '.cache' -type d | xargs rm -fr
	rm -fr deb_dist dist npc.egg-info

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

.PHONY: deb
deb:
	python3 setup.py --command-packages=stdeb.command bdist_deb
