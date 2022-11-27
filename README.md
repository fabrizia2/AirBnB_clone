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

### models/base_model.py
 This file is the base class of all our models. 
 It contains common elements: -attributes: id, created_at and updated_at
                              +methods: save() and to_json()

### models/engine
 This directory will contain all storage classes (using the same prototype). For the moment you will have only one: *** file_storage.py ***
