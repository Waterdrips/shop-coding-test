# To run the application
## Required programs

* Docker (Recommended)
* Python 3.7+ (If not using Docker)


## Setup with docker
Some users wont want to install virtual python environments etc, so there's a way to use & develop this program with docker

Run an interactive container to run the program, and tests etc.

`docker run --rm -it -v $PWD:/app $(docker build -q .) /bin/sh`

Then use this interactive shell to execute the program:

`python main.py Apples Soup Soup Bread Apples Milk` for example

#### To run the tests
Run the tests (and gather coverage data) with `coverage run -m unittest`

You view the coverage report with `coverage report --omit="*/test*"`


## If not using docker

* Install a python 3.7+ virtual environment (not covered by this doc)
* Activate the virtual environment
* Install dev dependencies (for running tests and coverage) `pip install -r requirements.txt`
* To run the tests and coverage `coverage run -m unittest` and then `coverage report --omit="*/test*"`

To run the command use

`python main.py [my list of items!]`

and you should see the output.

## Developing
To add a new product, go to the folder called `goods` this contains the definitions of the shop items, create a new one of these (see an existing one for format)

# Future work
* Handle inputs that are comma and/or space delimited.
* More default discounts "types" like BOGOF