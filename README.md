# AirBnB Project

![slogan_hbnb_console-style](https://user-images.githubusercontent.com/28455356/86294724-c1ebf900-bbba-11ea-927d-c51e2260a73d.png)

The **AirBnB Clone project** starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website. You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

We won’t build this application all at once, but step by step. This is the **first phase** of the project, called **The Console**, where we'll build:
* **A command interpreter** to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

## The Console (Concept)
In this phase we must:

* Create our data model
* Manage (create, update, destroy, etc) objects via a console / command interpreter
* Store and persist objects to a file (`JSON` file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and `RestAPI` you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine represented in the image below, specifically where it's highlighted with the yellow lines:

![console_phase_hbnb](https://user-images.githubusercontent.com/28455356/86276872-5181af80-bb9b-11ea-8633-b5b92e152f9e.png)


## Requirements

### Python Scripts
* All files will be interpreted/compiled on `Ubuntu 14.04 LTS` using `python3` (version 3.4.3)
* The code should use the `PEP 8` style (version 1.7 or more)
* All files must be executable
* All modules, classes and functions should have a documentation (`docstring`)

### Python Unit Tests
* All test files should be inside a folder `tests/`
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* All test files should be python files (extension: `.py`)
* All test files and folders should start by `test_`prefix
* All tests should be executed by using this command: `python3 -m unittest discover tests` in the commands terminal, located inside of the project directory. Looks like this:


```bash
user@ubuntu:~/AirBnB_clone$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
user@ubuntu:~/AirBnB_clone$
```


* You can also execute file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py` in the commands terminal, located inside of the project directory (change the name of the test file do you want to execute)


## Files and Directories

|File                           |Description                  |
|-------------------------------|-----------------------------|
|`console.py`                   |Is the entry point of our command interpreter|
|`tests/`                        |Directory will contain all unit tests|
|`models/`                       |Directory will contain all classes used for the entire project |
|`models/base_model.py`         |Is the base class of all our models|
|`models/engine`                |Directory will contain all storage classes (using the same prototype)|
|`models/engine/file_storage.py`|Is the file that contain all storage classes|

Tree of the project

```bash
AirBnB_clone/
│
├── models/
│   ├── engine/
│   │   ├── __init__.py
│   │   └── file_storage.py
│   │
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
│
└── tests/
│   └── test_models/
│       ├── test_engine/
│       │   ├── __init__.py
│       │   └── test_file_storage.py
│       │
│       ├── __init__.py
│       ├── test_amenity.py
│       ├── test_user.py
│       ├── test_city.py
│       ├── test_place.py
│       ├── test_review.py
│       ├── test_base_models.py
│       └── test_state.py
│
└── console.py
```

## The Console (Command Interpreter)

### Download:
Clone the repository with the command line interface:

`git clone https://github.com/melandres8/AirBnB_clone.git`

### Execution:

It should work like this in interactive mode:

![execute_hbnb-console_interactive](https://user-images.githubusercontent.com/28455356/86287683-353b3e00-bbae-11ea-9946-287d3b3721cb.png)

Also in non-interactive mode:

![execute_hbnb-console_non-interactive](https://user-images.githubusercontent.com/28455356/86287722-4b48fe80-bbae-11ea-9293-50de957cec98.png)


### Commands:

|Command                                                         |Fuction                  |
|----------------------------------------------------------------|-----------------------------|
|`help`                                                          |Show the available commands|
|`help <command>`                                                |Show how `<command>` works|
|`create <class_name>`                                           |Creates a new instance of a class (`<class_name>`)|
|`show <class_name> <id>`                                        |Prints the string representation of an instance|
|`all`                                                           |Prints all string representation of all instances|
|`all <class_name>`                                              |Prints all string representation of all instances of a specific class (`<class_name>`)|
|`update <class_name> <id> <attribute name> "<attribute value>"`  |Updates an instance of a class by adding or updating an attribute|
|`destroy <class_name> <id>`                                     |Deletes an instance|
|`quit`                                                          |to exit the program|
|`EOF (Ctrl+D)`                                                  |to exit the program|

An empty line + ENTER shouldn’t execute anything

### Examples:

* **Help**

`help` command use:

![hbnb_help_command](https://user-images.githubusercontent.com/28455356/86296102-a33b3180-bbbd-11ea-8f23-bdf403dc3da9.png)

* **Create**

`create` command use:

![hbnb_create_command](https://user-images.githubusercontent.com/28455356/86296627-df22c680-bbbe-11ea-9e1a-fed3797c5b8c.png)

* **Show**

`show` command use:

![hbnb_show_command](https://user-images.githubusercontent.com/28455356/86297067-fdd58d00-bbbf-11ea-8258-698ad7b9ed9d.png)


## Resources
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)


## Authors

Melkin Mosquera - [GitHub](https://github.com/melandres8) | [Twitter](https://twitter.com/melandres8)

Nathaly Sotomayor Ampudia - [GitHub](https://github.com/nathsotomayor) | [Twitter](https://twitter.com/nathsotomayor)


...


`Made with 💛 in Holberton School Colombia (Cali) - Cohort 11`
