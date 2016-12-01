# Message Board Web Application
### Data Representation and Querying Project 2016

This is my Third Year project for Data Representation and Querying

## Project Overview

This is a single page application that is designed to allow the user to input their name along with a message into a database using SQLite3. The database then returns the entered name along with their message back onto the web page in a table.

## Running The Application

This application was written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org), thus both must be installed in order to run it. Along with this [SQLlite3](https://docs.python.org/2/library/sqlite3.html) is used for the database and must also be installed.

Once these prerequisites are met, the application can be run locally by cloning this repository to a directory of your choice and accessing the directory in a command line:
```
$ cd C:\Users\[NAME]\[SAVED DIRECTORY]\dataRepProject2016
```
From there you must first create a folder in the app directory called 'data', then run the db.py file in order to initialise the database, followed by webapp.py to run the application
```
$ mkdir data
$ python db.py
$ python webapp.py
```
And finally, one running, you can access application on your browser at http://127.0.0.1:5000/

## Architecture

This application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/)framework and is using SQLite as a database. While Python 3 and Flask were required for the project, I chose to use SQLite due to its' easy integration with Python.

