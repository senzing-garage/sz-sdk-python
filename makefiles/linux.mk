# Makefile extensions for linux.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

SENZING_TOOLS_DATABASE_URL ?= sqlite3://na:na@/tmp/sqlite/G2C.db

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	@rm -rf $(TARGET_DIRECTORY) || true
	@rm -rf $(DIST_DIRECTORY) || true
	@rm -rf $(MAKEFILE_DIRECTORY)/__pycache__ || true
	@rm $(MAKEFILE_DIRECTORY)/coverage.xml || true


.PHONY: dependencies-osarch-specific
dependencies-osarch-specific:


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	@echo "Hello World, from linux."


.PHONY: setup-osarch-specific
setup-osarch-specific:


.PHONY: test-osarch-specific
test-osarch-specific:


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-linux
only-linux:
	@echo "Only linux has this Makefile target."
