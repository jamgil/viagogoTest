# viagogo test
A Python CLI program that accepts a 2d coordinate and returns a list of the 5 nearest events, along with the cheapest ticket for each of those events.

## Setup
This project uses Python 3.6, which can either be installed from https://www.python.org/downloads/ or a package manager.

The Windows installer comes with a `py` wrapper that should be used instead of `python` when running the program.

This program only uses the standard Python libraries - no dependencies need to be installed.

## Running
Inside the root directory -

Run the program with the following command:
```
py -m viagogoTest
```

And run the unit test with the following command:
```
py -m unittest viagogoTest/test.py
```
Keeping in mind to use the Python 3 wrapper (`py`) if necessary based on your dev environment setup.

## Questions
#### Please detail any assumptions you have made
* I assumed that basic error handling would suffice for this demonstration. In a real world scenario, I would use much more extensive error handling and use of exceptions.

#### How might you change your program if you needed to support multiple events at the same location?
* I would switch from using the dict datatype to a list, which would be able to contain duplicate items.

#### How would you change your program if you were working with a much larger world size?
* I would split the full grid into smaller regions. This would allow me to iterate over the events in a particular region (and surrounding regions, if close to a border), which would result in a much lower number of events that would need to be compared.
* In a real world scenario, I would store the events in a spatial database, such as PostgreSQL + PostGIS. This would allow me to do much more efficient event lookups by location, and allows for easier scalability.