# Makefile extensions for darwin.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

SENZING_DIR ?= /opt/senzing/g2
SENZING_TOOLS_SENZING_DIRECTORY ?= $(SENZING_DIR)

LD_LIBRARY_PATH := $(SENZING_TOOLS_SENZING_DIRECTORY)/lib:$(SENZING_TOOLS_SENZING_DIRECTORY)/lib/macos
DYLD_LIBRARY_PATH := $(LD_LIBRARY_PATH)

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
	@echo "Hello World, from darwin."


.PHONY: setup-osarch-specific
setup-osarch-specific:


.PHONY: test-osarch-specific
test-osarch-specific:


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-darwin
only-darwin:
	@echo "Only darwin has this Makefile target."
