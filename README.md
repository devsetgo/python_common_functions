![image](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg "CalVer")
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

CI/CD Pipeline:

[![codecov](https://codecov.io/gh/devsetgo/python_common_functions/branch/master/graph/badge.svg)](https://codecov.io/gh/devsetgo/python_common_functions)
[![Actions Status](https://github.com/devsetgo/python_common_functions/workflows/Run%20Tests/badge.svg)](https://github.com/devsetgo/python_common_functions/actions)


SonarCloud

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_python_common_functions&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=devsetgo_python_common_functions)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_python_common_functions&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=devsetgo_python_common_functions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_python_common_functions&metric=alert_status)](https://sonarcloud.io/dashboard?id=devsetgo_python_common_functions)



# Python Common Functions
A place to store reusable code snipts and functions to stop writting the functions new for every app.

**Contributions are welcome!**

### JSON, CSV, and Text file processing
A way to simplify working CSV, JSON, and Text files for my projects. Just pass a file name and the data for it to be stored. Pass the file name to retrieve the data.

.. From app directory

#### Run All
Run Tests, Coverage Badge and Pre-Commit at the same time
~~~
./scripts/tests.sh
~~~

Run each individually

#### Run Individually
~~~~
python3 -m pytest
~~~~

Create coverage badge
~~~~
    coverage-badge -o coverage.svg -f
~~~~

Pre-Commit & Hooks
~~~~
    - Follow install instructions: [Install](https://pre-commit.com/#install)
    - pre-commit install
    - pre-commit run -a
~~~~

### Notes:
- Requires Python 3.6 and higher

### TODO
- [x] Add exception tests to
    - [x] folder test
    - [x] file tests
    - [x] pass lib tests
- [x] Research logging locking (non-issue caused by permissions)
- [ ] Add testing around logging in functions

## Changelog

### 20.1.3
- regex pattern between two characters
- tests for patterns

### 19.12.19
- updating file functions and tests
- file functions have better exceptions
- test directories have a better layout to keep tests organized
- adding simple_functions for new capabilities

### 19.09.07
- Adding delete file function + tests
- Adding exception tests for file_functions.py
- Adding Password encyrption/verify + tests
- Changing exceptions to be more specific
- Adding check to ensure data is provided to functions correctly

### 19.8.31
- Adding text file save and open
- Adding tests for text file processing
- Adding Pre-Commit
- Adding Travis CI
- Some refactoring of test to run correctly in Travis CI
- Adding Travis CI badge
- Adding some exclusions against example functions
- Adding settings configuration via .env file
- adding configuraton for pytest, isort, black in setup.cfg

### 19.6.23
- Adding exception tests
- Code coverage increased to 91%
- Cleanup of file/folder functions removing returns for exceptions

### 19.6.22
- Adding folder function tests
  - TODO: Add exception mocking to tests
  - CodeCoverage at 83% due to missing exception tests
- Cleanup of folder functions and adding missing exception handling
- Adding additional example functions
- Additional Logging and a TODO to determine logging locking issue
- Edit of logging configuration

### 19.5.19
- Updates to Pytest to make them function better
- Adding test to cover create_sample_files
- Adding 'example.py' to show use
- Adding Type Hints to functions
- Adding coverage badge
- Adding get directory list function
- Adding tests for get directory list
- Code coverage at 87%
- Fix of travis-ci build

### 19.5.12
- Adding File Processing (filepro)
- Adding Tests for fileproc
- Save and Open JSON
- Save and Open CSV (returns a dictionary/json object)
- using Loguru for logging
- Adding Travis-CI