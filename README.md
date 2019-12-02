# Shopping Basket CLI
This program is used to calculate a user's spend in a shop based on a list of products. 

It will not consider any list items which are not matches to the products we support.

A user who wants to know what products are available can run the command `python main.py --check-shelves` to see a list
of products available to put in their shopping list


> This CLI is not guaranteed to work on windows as the author has not explicitly tested on this platform. This should
not cause any users a problem, as the recommended way to use this application and develop for it is by using Docker


## Installation methods

* Docker (Recommended)
* Python 3.7+ (Not Supported)


## Setup with docker
Some users wont want to install virtual python environments etc, so there's a way to use & develop this program with docker

Pre pull the base container, to speed up the next step `docker pull python:3.7.4-alpine`. (otherwise it can look like the next command is hanging)

Run an interactive container to run the program, and tests etc.

`docker run --rm -it -v $PWD:/app $(docker build -q .) /bin/sh`

Then use this interactive shell to execute the program:

`python main.py Apples Soup Soup Bread Apples Milk` for example

#### To run the tests
Run the tests (and gather coverage data) with `coverage run -m unittest`

You view the coverage report with `coverage report -m`


## If not using docker (NOT SUPPORTED)

* Install a python 3.7+ virtual environment 
* Activate the virtual environment
* Install dev dependencies (for running tests and coverage) `pip install -r requirements.txt`
* To run the tests and coverage `coverage run -m unittest` and then `coverage report -m`

To run the CLI use

`python main.py <my list of items seperated by spaces>`

## Developing
To add a new product, go to the `./goods` folder this contains the definitions of the shop items, create a new one of these (see an existing one for format)

You can create some % off discounts by creating an object in the `./store/current_offers.py file`, (see `Apples` example)

If you need to add any more exotic offers (Like the soups + bread) you will need to implement a custom offer in the ./offers folder

Tests are found in the `./test` folder

# Future work
* Handle inputs that are comma and/or space delimited.
* More default discounts "types" like BOGOF
* Decide if / what to show a user if the product they have requested is not available (misspelling/not in out products?)
* Improve CI (see initial CI in .github/workflows/pythonapp.yml)
* Create a Python Package from this code, so a user can install this with pip
* Break some of the maths bits (percentage discount for example) out into their own package, so more extensive testing can be done on those sections and we can encourage code-reuse in the future
* Discuss with Product Owner/Business as to how and where we apply rounding of prices, at the moment its setup to maximise profit
* The products could be refactored out of code and into config (or external provider) by changing from using Python types to work out what's in the basket to looking at names (if we created objects from a base product class instead of creating child classes)
* Decide if we should validate if a developer creates a discount that is more than 100% or less then (or equal to) 0%
