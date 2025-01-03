# Makefile extensions for linux.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

PATH := $(MAKEFILE_DIRECTORY)/bin:$(PATH)

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	@rm -f  $(MAKEFILE_DIRECTORY)/.coverage || true
	@rm -f  $(MAKEFILE_DIRECTORY)/coverage.xml || true
	@rm -fr $(DIST_DIRECTORY) || true
	@rm -fr $(MAKEFILE_DIRECTORY)/.mypy_cache || true
	@rm -fr $(MAKEFILE_DIRECTORY)/.pytest_cache || true
	@rm -fr $(MAKEFILE_DIRECTORY)/dist || true
	@rm -fr $(MAKEFILE_DIRECTORY)/docs/build || true
	@rm -fr $(MAKEFILE_DIRECTORY)/htmlcov || true
	@rm -fr $(TARGET_DIRECTORY) || true
	@find . | grep -E "(/__pycache__$$|\.pyc$$|\.pyo$$)" | xargs rm -rf


.PHONY: coverage-osarch-specific
coverage-osarch-specific:
	@$(activate-venv); pytest --cov=src --cov-report=xml  $(shell git ls-files '*.py'  ':!:examples/*')
	@$(activate-venv); coverage html
	@xdg-open $(MAKEFILE_DIRECTORY)/htmlcov/index.html


.PHONY: dependencies-for-development-osarch-specific
dependencies-for-development-osarch-specific:


.PHONY: documentation-osarch-specific
documentation-osarch-specific:
	@$(activate-venv); cd docs; rm -rf build; make html
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	$(info Hello World, from linux.)


.PHONY: package-osarch-specific
package-osarch-specific:
	@$(activate-venv); python3 -m build


.PHONY: setup-osarch-specific
setup-osarch-specific:
	$(info No setup required.)


.PHONY: test-osarch-specific-2
test-osarch-specific-2:
	$(info --- Unit tests -------------------------------------------------------)
	@pytest tests/ --verbose --capture=no --cov=src/senzing --cov-report xml:coverage.xml
#	$(info --- Test examples ----------------------------------------------------)
#	@pytest examples/ --verbose --capture=no --cov=src/senzing
	$(info --- Test examples using unittest -------------------------------------)
	@python3 -m unittest \
		examples/szconfig/*.py \
		examples/szconfigmanager/*.py \
		examples/szdiagnostic/*.py \
		examples/szengine/*.py \
		examples/szproduct/*.py


.PHONY: test-examples-2
test-examples-2:
	$(info --- Test examples using unittest -------------------------------------)
	@python3 -m unittest \
		examples/misc/add_truthset_datasources.py \
		examples/misc/add_truthset_data.py


.PHONY: venv-osarch-specific
venv-osarch-specific:
	@python3 -m venv .venv

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-linux
only-linux:
	$(info Only linux has this Makefile target.)
