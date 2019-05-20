![image](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg "CalVer")
![image](https://travis-ci.org/devsetgo/python_common_functions.svg "Build Status")
![image](/app/coverage.svg "CalVer")

# Python Common Functions
A place to store reusable code snipts and functions to simplify my development.

**Contributions are welcome!**

### JSON and CSV file processing
A way to simplify working CSV and JSON files for my projects. Just pass a file name and the data for it to be stored. Pass the file name to retrieve the data.

Run pytest with coverage
    pytest --cov=com_lib tests/ --cov-report=html

Create coverage badge
    coverage-badge -o coverage.svg -f

### Notes:
- Requires Python 3.6 and higher


## Changelog
### 19.5.19
- Updates to Pytest to make them function better
- Adding test to cover create_sample_files
- Adding 'example.py' to show use
- Adding Type Hints to functions
- Adding coverage badge

### 19.5.12
- Adding File Processing (filepro)
- Adding Tests for fileproc
- Save and Open JSON
- Save and Open CSV (returns a dictionary/json object)
- using Loguru for logging
- Adding Travis-CI