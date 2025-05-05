# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], [markdownlint],
and this project adheres to [Semantic Versioning].

## [Unreleased]

## [0.2.11] - 2025-05-05

### Changed in 0.2.11

- Fixed incorrect flag defaults in szengine.py
- Fixed incorrect flag defaults in szengine.py in doc strings
- Spelling corrections

## [0.2.10] - 2025-04-30

### Changed in 0.2.10

- Added SZ_WHY_SEARCH_DEFAULT_FLAGS to szengineflags.py
- Changed default why_search() flag to SZ_WHY_SEARCH_DEFAULT_FLAGS

## [0.2.9] - 2025-04-24

### Changed in 0.2.9

- Update szerror.py

## [0.2.8] - 2025-04-21

### Changed in 0.2.8

- Simplify and clean up examples

## [0.2.7] - 2025-04-18

### Changed in 0.2.7

- Case on example variables

### Removed in 0.2.7

- Documentation on early adaptor methods
- Empty example files for early adaptor methods

## [0.2.6] - 2025-04-16

### Added in 0.2.6

- `SzEngine.why_search`

## [0.2.5] - 2025-03-11

### Changed in 0.2.5

- Restructured `SzConfigManager` and `SzConfig`

## [0.2.4] - 2025-02-14

### Changed in 0.2.4

- Updated documentation

## [0.2.3] - 2025-02-10

### Fixed in 0.2.3

- Added SzDatabaseTransientError & SzSdkError to \_\_init\_\_.py for importing

## [0.2.2] - 2025-01-28

### Added in 0.2.2

- Simpler class methods for szengineflags to build upon in a future release
- documentation-requirements.txt

### Changed in 0.2.2

- Switched Git workflows and make files to pytest
- Modified Sphinx documentation to pull examples from core and gRPC repositories
- General documentation updates

### Removed in 0.2.2

- Class methods for szengineflags, only required one moved to sz-python-tools helpers
- Examples, now referenced in core and gRPC when building docs

### Fixed in 0.2.2

- Fixed error from building Sphinx doc for html_static_path = ["_static"]

## [0.2.1] - 2025-01-09

### Changed in 0.2.1

- Added `typing-extensions` dependency for Python versions < 3.11

## [0.2.0] - 2024-12-04

### Changed in 0.2.0

- Changed repository from `sz-sdk-python-abstract` to `sz-sdk-python`

## [0.1.12] - 2024-11-27

### Removed in 0.1.12

- Removed kwargs from all method definitions

### Fixed in 0.1.12

- Typo and spelling errors

### Added in 0.1.12

- Additional docstring documentation where missing

## [0.1.11] - 2024-11-26

### Changed in 0.1.11

- In SzAbstractFactory, changed `create_sz_*` to `create_*`

## [0.1.10] - 2024-11-01

### Changed in 0.1.10

- Synchronized ezengineflags with latest V4 stage build

## [0.1.9] - 2024-10-31

### Changed in 0.1.9

- Modified signatures for process_redo_record to include default flag

## [0.1.8] - 2024-10-29

### Changed in 0.1.8

- Modified signatures for preprocess_record to include default flag
- Removed exception_map and moved into szerror.py

## [0.1.7] - 2024-10-28

### Changed in 0.1.7

- Modified signatures for find_network_by_entity_id and find_network_by_record_id

## [0.1.6] - 2024-10-28

### Removed in 0.1.6

- `SzAbstractFactory.destroy()`

## [0.1.5] - 2024-10-25

### Added in 0.1.5

- `SzAbstractFactory.destroy()`
- `SzAbstractFactory.reinitialize()`

### Deleted in 0.1.5

- `SzEngine.reinitialize()`
- `SzDiagnostic.reinitialize()`

## [0.1.4] - 2024-10-04

### Added in 0.1.4

- `sz_enzine.preprocess_record()`
- Engine flags:
  - `SZ_ENTITY_INCLUDE_RECORD_FEATURE_DETAILS`
  - `SZ_ENTITY_INCLUDE_RECORD_FEATURE_STATS`
  - `SZ_ENTITY_INCLUDE_RECORD_FEATURES`

### Deleted in 0.1.4

- Engine flags:
  - `SZ_ENTITY_INCLUDE_FEATURE_ELEMENTS`
  - `SZ_ENTITY_INCLUDE_RECORD_FEATURE_IDS`

## [0.1.3] - 2024-09-25

### Added in 0.1.3

- Added `help()` method

## [0.1.2] - 2024-09-24

### Changed in 0.1.2

- Added `abstract_factory`

## [0.1.1] - 2024-07-30

### Changed in 0.1.1

- Update to current sz-sdk-python
- Update to current template-python

## [0.1.0] - 2024-05-06

### Changed in 0.1.0

- Migrated from "g2" to "sz"

## [0.0.4] - 2023-12-21

### Changed in 0.0.4

- Add `help()`

## [0.0.3] - 2023-12-18

### Changed in 0.0.3

- Add truthset

## [0.0.2] - 2023-12-15

### Changed in 0.0.2

- Improving GitHub actions

## [0.0.1] - 2023-12-15

### Added to 0.0.1

- Initial work

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[markdownlint]: https://dlaa.me/markdownlint/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
