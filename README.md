This contains a collection of exercises that are part of the testing lectures for ENPM611. The examples illustrate how to write unit tests in Python. It also provides a setup to evaluate a set of test cases for completeness in terms of the equivalence partition and boundary value analysis methods.

# Repository Contents

The following can be found in this repository:

* `app`: contains functions to be tested as well as some utility functions
* `test`: specifies test cases that execute the functions in the `app` directory
* `inputs`: contains a sample spreadsheet with test inputs

# Setup

The setup is similar to other repositories we have worked with. It assumes that you have Python 3.x installed. You should also have VisualStudio Code installed to run unit tests. To install the necessary dependencies
* Create a virtual environment
* Activate that virtual environment
* Install dependencies as they are specified in the `requirements.txt` file.

The commands below describe how to perform these actions for Unix and Windows.

## Setup on Unix/MacOS

Open a bash window and navigate to a place where you want to store the repository source code. Then execute the following commands:

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Setup on Windows

To avoid permission issues, open a command line window in Administrator mode. Then, navigate to a directory of your choice and execute the following commands:

```bash
python -m venv .env
.env/Scripts/activate
pip install -r requirements.txt
```

# Test

In class, we discussed how to specify and run unit tests in Python. For more information about running tests in VSCode, see:

https://code.visualstudio.com/docs/python/testing