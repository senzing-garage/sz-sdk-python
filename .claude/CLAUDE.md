# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `sz-sdk-python`, the Senzing Python SDK containing abstract base classes from which concrete implementations (Core and gRPC) are derived. The package is published to PyPI as `senzing`.

## Development Commands

### Setup and Dependencies

```bash
# Create virtual environment and install all development dependencies
make dependencies-for-development

# Install package dependencies only
make dependencies
```

### Linting

```bash
# Run all linters (pylint, mypy, bandit, black, flake8, isort)
make lint

# Run individual linters
make pylint
make mypy
make black
make flake8
make isort
make bandit
```

### Testing

```bash
# Run full test suite (requires Senzing C library installed)
make clean setup test

# Run unit tests only
pytest tests/ --verbose --capture=no

# Run a single test file
pytest tests/szengine_test.py --verbose

# Run a specific test
pytest tests/szengine_test.py::test_add_record --verbose

# Run tests with coverage
make coverage
```

### Build and Package

```bash
make package          # Build wheel file
make publish-test     # Publish to Test PyPI
```

### Documentation

```bash
make documentation    # Build and view Sphinx docs
```

## Architecture

### Package Structure

- `src/senzing/` - Main package with abstract base classes defining the SDK interface
- `src/senzing_mock/` - Mock implementations for testing
- `src/senzing_truthset/` - Sample test data (customers, references, watchlist)

### Core Abstract Classes

The SDK defines abstract base classes that implementations must fulfill:

- **SzAbstractFactory** - Factory pattern for creating SDK objects. Concrete implementations:
  - `SzAbstractFactoryCore` (in sz-sdk-python-core)
  - `SzAbstractFactoryGrpc` (in sz-sdk-python-grpc)

- **SzEngine** - Main entity resolution engine with methods like:
  - `add_record()`, `delete_record()` - Record management
  - `get_entity_by_*()` - Entity retrieval
  - `find_path_by_*()`, `find_network_by_*()` - Relationship discovery
  - `why_*()` - Explain entity resolution decisions
  - `search_by_attributes()` - Search functionality

- **SzConfig** - Configuration management
- **SzConfigManager** - Configuration versioning and registry
- **SzDiagnostic** - System diagnostics
- **SzProduct** - License and version info

### Error Hierarchy

`src/senzing/szerror.py` contains the exception hierarchy (auto-generated):
- `SzError` - Base exception
- `SzBadInputError` - User input errors (SzNotFoundError, SzUnknownDataSourceError)
- `SzRetryableError` - Transient errors that can be retried
- `SzUnrecoverableError` - Fatal errors (SzDatabaseError, SzLicenseError)

### Engine Flags

`SzEngineFlags` in `szengineflags.py` controls what information is returned from SDK methods.

## Code Style

- Line length: 120 characters (black, flake8)
- Type hints: Required (`mypy --strict`)
- Import sorting: isort with black profile
- Security: bandit for security checks (B101 skipped for assert usage)

## Testing Approach

Tests use pytest with mock implementations from `senzing_mock`. The mock classes implement all abstract methods with minimal return values, allowing interface verification without requiring the actual Senzing engine.

- Tests in `tests/` verify the abstract interface.
- Tests in `examples/` serve as both documentation and integration tests.

## Prerequisites

The Senzing C library must be installed at `/opt/senzing/er/lib` for running tests against actual implementations.
