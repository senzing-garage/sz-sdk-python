# Makefile extensions for windows.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

SENZING_TOOLS_DATABASE_URL ?= sqlite3://na:na@nowhere/C:\Temp\sqlite\G2C.db

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	del /F /S /Q $(DIST_DIRECTORY)
	del /F /S /Q $(MAKEFILE_DIRECTORY)/__pycache__
	del /F /S /Q $(MAKEFILE_DIRECTORY)/coverage.xml
	del /F /S /Q $(MAKEFILE_DIRECTORY)/docs/build
	del /F /S /Q $(MAKEFILE_DIRECTORY)/htmlcov
	del /F /S /Q $(TARGET_DIRECTORY)


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	$(info "Hello World, from windows.")


.PHONY: setup-osarch-specific
setup-osarch-specific:
	$(info "No setup required.")


.PHONY: sphinx-osarch-specific
sphinx-osarch-specific:
	# @cd docs; rm -rf build; make html


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@explorer file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-windows
only-windows:
	$(info "Only windows has this Makefile target.")
