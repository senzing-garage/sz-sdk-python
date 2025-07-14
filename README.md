# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                  |    Stmts |     Miss |   Cover |   Missing |
|-------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing/\_\_init\_\_.py           |       10 |        0 |    100% |           |
| src/senzing/constants.py              |       13 |        0 |    100% |           |
| src/senzing/szabstractfactory.py      |       23 |        0 |    100% |           |
| src/senzing/szconfig.py               |       17 |        0 |    100% |           |
| src/senzing/szconfigmanager.py        |       28 |        0 |    100% |           |
| src/senzing/szdiagnostic.py           |       17 |        0 |    100% |           |
| src/senzing/szengine.py               |       73 |        0 |    100% |           |
| src/senzing/szengineflags.py          |       86 |        1 |     99% |        31 |
| src/senzing/szerror.py                |       22 |        0 |    100% |           |
| src/senzing/szhelpers.py              |       24 |        0 |    100% |           |
| src/senzing/szproduct.py              |       13 |        0 |    100% |           |
| src/senzing\_mock/\_\_init\_\_.py     |        2 |        0 |    100% |           |
| src/senzing\_mock/senzing\_mock.py    |      123 |        0 |    100% |           |
| src/senzing\_truthset/\_\_init\_\_.py |        5 |        5 |      0% |       1-6 |
| src/senzing\_truthset/customers.py    |        2 |        2 |      0% |       3-5 |
| src/senzing\_truthset/datasources.py  |        2 |        2 |      0% |       3-5 |
| src/senzing\_truthset/references.py   |        2 |        2 |      0% |       3-5 |
| src/senzing\_truthset/watchlist.py    |        2 |        2 |      0% |       3-5 |
|                             **TOTAL** |  **464** |   **14** | **97%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/senzing-garage/sz-sdk-python/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/senzing-garage/sz-sdk-python/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fsenzing-garage%2Fsz-sdk-python%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.