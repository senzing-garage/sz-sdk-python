# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-abstract/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                               |    Stmts |     Miss |   Cover |   Missing |
|--------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_abstract/\_\_init\_\_.py              |        9 |        0 |    100% |           |
| src/senzing\_abstract/observer\_abstract.py        |        5 |        5 |      0% |     13-33 |
| src/senzing\_abstract/szconfig\_abstract.py        |       27 |        0 |    100% |           |
| src/senzing\_abstract/szconfigmanager\_abstract.py |       25 |        0 |    100% |           |
| src/senzing\_abstract/szdiagnostic\_abstract.py    |       23 |        0 |    100% |           |
| src/senzing\_abstract/szengine\_abstract.py        |      117 |       20 |     83% |1077, 1095, 1106, 1117, 1136, 1160, 1185, 1213, 1237, 1250, 1267, 1274, 1286, 1300, 1312, 1325, 1340, 1355, 1370, 1393 |
| src/senzing\_abstract/szengineflags.py             |       80 |        4 |     95% |     32-35 |
| src/senzing\_abstract/szerror.py                   |       63 |       26 |     59% |600-601, 610-622, 631, 640-648, 660-666, 682-697 |
| src/senzing\_abstract/szhasher\_abstract.py        |       21 |        0 |    100% |           |
| src/senzing\_abstract/szhelpers.py                 |       94 |       94 |      0% |     9-298 |
| src/senzing\_abstract/szproduct\_abstract.py       |       22 |        2 |     91% |  151, 164 |
|                                          **TOTAL** |  **486** |  **151** | **69%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-abstract/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-abstract/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-abstract/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-abstract/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fsenzing-garage%2Fsz-sdk-python-abstract%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-abstract/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.