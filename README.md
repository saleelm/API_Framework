# SDET Assignments - API Framework

This repository contains an API testing framework designed to efficiently test, validate, and ensure the functionality of APIs.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Running Tests](#running-tests)
- [Directory Structure](#directory-structure)
- [Reporting](#reporting)
- [Logs](#logs)
- [Test Data](#test-data)
- [Utils](#utils)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- Virtual environment (optional but recommended)

## Setup & Installation

  chmod +x setup_and_run_tests.sh
  ./setup_and_run_tests.sh

  **To run all testcases**
  1.  PYTHONPATH=`pwd` python3 -m pytest tests/

  **To run Specific testscases:**
  To run functional testcases:
  1.  PYTHONPATH=`pwd` python3 -m pytest -m functional tests/

  To run Datatype testcases:
  2. 1.  PYTHONPATH=`pwd` python3 -m pytest -m datatype tests/

  to run security testcases:
  1.  PYTHONPATH=`pwd` python3 -m pytest -m security tests/

  to run async testcases:
  1.  PYTHONPATH=`pwd` python3 -m pytest -m async tests/

  

## Directory Structure

- `tests/`: Contains all the test cases.
- `config/`: Configuration files and settings (if any).
- `testdata/`: Test data and fixtures.
- `utils/`: Utility functions and helpers.

## Reporting

After running tests, reports can be found in the `reports` directory.

## Logs

Logs generated during test execution can be found in the `logs` directory.

## Test Data

Test-related data can be found in the `testdata` directory.

## Utils

The `utils` directory contains utility functions and scripts that assist in test execution and data processing.

