# AirBnB Console Project
![The logo](https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg)
 This is the start of all the AirBnb clone work. Where we make a console to interact with the system,

##Project's Concepts
+Unittest - and please work all together on tests cases
-Python packages concept page
-Serialization/Deserialization
-*args, **kwargs
+datetime
-More coming soon!

## Base Class Containing all the attributes and methods to be inherited from
 Contains a base class that forms the basis for all models, attributes and methods to be added in the
 project.

## Files and Directories
### Models
 This directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

### Tests
 This directory will contain all unit tests.

### Console.py
 This file is the entry point of our command interpreter.

##How the Console works
"`
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
"`

### models/base_model.py
 This file is the base class of all our models. 
 It contains common elements: -attributes: id, created_at and updated_at
                              +methods: save() and to_json()

### models/engine
 This directory will contain all storage classes (using the same prototype). For the moment you will have only one: ***file_storage.py***

## Description of the command interpreter
| Command   | Description |
| ----------| ------------|
| quit	 | Quits the console|
|Ctrl+D	|Quits the console|
|help or help <command>	|Displays all commands or Displays instructions for a specific command|
| create <class>	| Creates an object of type , saves it to a JSON file, and prints the objects ID|
| show <class> <ID>	| Shows string representation of an object|
| destroy <class> <ID>	| Deletes an objects
| all or all <class>	| Prints all string representations of all objects or Prints all string representations of all objects of a specific class|
|update <class> <id> <attribute name> "<attribute value>"	|Updates an object with a certain attribute (new or existing)|
|<class>.all()	|Same as all <class>|
|<class>.count()	|Retrieves the number of objects of a certain class|
|<class>.show(<ID>)	|Same as show <class> <ID>|
|<class>.destroy(<ID>)	|Same as destroy <class> <ID>|
|<class>.update(<ID>, <attribute name>, <attribute value>	|Same as update <class> <ID> <attribute name> <attribute value>|
|<class>.update(<ID>, <dictionary representation>)	|Update objects based on a dictionary representation of attribute names and values|
