# Makefile extensions for linux.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

LD_LIBRARY_PATH ?= /opt/senzing/g2/lib
SENZING_TOOLS_DATABASE_URL ?= sqlite3://na:na@nowhere/tmp/sqlite/G2C.db
PATH := $(MAKEFILE_DIRECTORY)/bin:$(PATH)

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	@rm -fr $(DIST_DIRECTORY) || true
	@rm -f  $(MAKEFILE_DIRECTORY)/coverage.xml || true
	@rm -fr $(MAKEFILE_DIRECTORY)/docs/build || true
	@rm -fr $(MAKEFILE_DIRECTORY)/htmlcov || true
	@rm -fr $(TARGET_DIRECTORY) || true
	@find . | grep -E "(/__pycache__$$|\.pyc$$|\.pyo$$)" | xargs rm -rf


.PHONY: coverage-osarch-specific
coverage-osarch-specific:
	@pytest --cov=src --cov-report=xml  $(shell git ls-files '*.py'   )
	@coverage html
	@xdg-open $(MAKEFILE_DIRECTORY)/htmlcov/index.html


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	$(info "Hello World, from linux.")


.PHONY: setup-osarch-specific
setup-osarch-specific:
	$(info "No setup required.")


.PHONY: test-osarch-specific
test-osarch-specific:
	@echo "--- Unit tests -------------------------------------------------------"
	@pytest tests/ --verbose --capture=no --cov=src/senzing_abstract --cov-report xml:coverage.xml
#	@echo "--- Test examples ----------------------------------------------------"
#	@pytest examples/ --verbose --capture=no --cov=src/senzing_abstract
	@echo "--- Test examples using unittest -------------------------------------"
	@python3 -m unittest \
		examples/szconfig/*.py \
		examples/szconfigmanager/*.py \
		examples/szdiagnostic/*.py \
		examples/szengine/*.py \
		examples/szproduct/*.py		


.PHONY: test-examples
test-examples:
	@echo "--- Test examples using unittest -------------------------------------"
	@python3 -m unittest \
		examples/misc/add_truthset_datasources.py \
		examples/misc/add_truthset_data.py


.PHONY: sphinx-osarch-specific
sphinx-osarch-specific:
	@cd docs; rm -rf build; make html


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-linux
only-linux:
	$(info "Only linux has this Makefile target.")
