# holbertonschool-AirBnB_clone
## Table of Contents
- [Author Details](https://github.com/seba17962/holbertonschool-AirBnB_clone/blob/main/AUTHORS)
- [Requirements](#requirements)
- [Project Description](#project-description)
- [Commmand Interpreter Description and Execution](#commmand-interpreter-description-and-execution)
- [How to Use it with Examples](#how-to-use-it-with-examples)

##  Requirements:
*   Allowed editors: vi, vim, emacs
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly #!/usr/bin/python3
*   A README.md file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.*)
*   All your files must be executable
*   The length of your files will be tested using wc
*   All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
*   All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
*   All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Project Description:
This project is a clone of the AirBnB page made by students for learning purposes.
Looking to learn:
*   How to create a Python package
*   How to create a command interpreter in Python using the cmd module
*   What is Unit testing and how to implement it in a large project
*   How to serialize and deserialize a Class
*   How to write and read a JSON file
*   How to manage datetime
*   What is a UUID
*   What is *args and how to use it
*   What is **kwargs and how to use it
*   How to handle named arguments in a function

## Commmand Interpreter Description And Execution:

The command interpreter is used to create and manage instances of each program method (BaseModel, User, etc...)

how to use?:
```
$ git clone https://github.com/seba17962/holbertonschool-AirBnB_clone.git
$ cd holberton-AirBnB_clone
~/holberton-AirBnB_clone$ ./console
```

Start the command interpreter as shown below:
```
~/holberton-AirBnB_clone$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb)quit
$
```
But also it can be started like this in non-interactive mode: (like the Shell project in C):
```
~/holberton-AirBnB_clone$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$cat test_help
help
$
~/holberton-AirBnB_clone$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

## How to Use it with Examples:
```
~/holberton-AirBnB_clone$ ./console.py
(hbnb)all MyModel
** class doesn't exist **
(hbnb)show
** class name missing **
(hbnb)show BaseModel
** instance id missing **
(hbnb)show BaseModel 12121212-1212-1212-1212-121212121212
** no instance found **
(hbnb)create
** class name missing **
(hbnb)create BaseModel
2a937e57-2b41-45de-a019-fe7c7b83f245
(hbnb)all
[BaseModel] (2a937e57-2b41-45de-a019-fe7c7b83f245) {'id': '2a937e57-2b41-45de-a019-fe7c7b83f245', 'created_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475379), 'updated_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475422)}
(hbnb)all BaseModel
[BaseModel] (2a937e57-2b41-45de-a019-fe7c7b83f245) {'id': '2a937e57-2b41-45de-a019-fe7c7b83f245', 'created_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475379), 'updated_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475422)}
(hbnb)show BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245
[BaseModel] (2a937e57-2b41-45de-a019-fe7c7b83f245) {'id': '2a937e57-2b41-45de-a019-fe7c7b83f245', 'created_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475379), 'updated_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475422)}
(hbnb)destroy
** class name missing **
(hbnb)destroy BaseModel
** instance id missing **
(hbnb)update BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245 first_name = "Betty"
(hbnb)update BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245 last_name = "Holberton"
(hbnb)update BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245 last_name "Holberton"
(hbnb)update BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245 first_name "Betty"
(hbnb)show BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245
[BaseModel] (2a937e57-2b41-45de-a019-fe7c7b83f245) {'id': '2a937e57-2b41-45de-a019-fe7c7b83f245', 'created_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475379), 'updated_at': datetime.datetime(2023, 10, 29, 15, 38, 16, 949963), 'first_name': 'Betty', 'last_name': 'Holberton'}
(hbnb)create BaseModel
b166eeec-d0e6-4e00-90d9-6c3d1541d956
(hbnb)all
[BaseModel] (2a937e57-2b41-45de-a019-fe7c7b83f245) {'id': '2a937e57-2b41-45de-a019-fe7c7b83f245', 'created_at': datetime.datetime(2023, 10, 29, 15, 34, 57, 475379), 'updated_at': datetime.datetime(2023, 10, 29, 15, 38, 16, 949963), 'first_name': 'Betty', 'last_name': 'Holberton'}
[BaseModel] (b166eeec-d0e6-4e00-90d9-6c3d1541d956) {'id': 'b166eeec-d0e6-4e00-90d9-6c3d1541d956', 'created_at': datetime.datetime(2023, 10, 29, 15, 39, 7, 907787), 'updated_at': datetime.datetime(2023, 10, 29, 15, 39, 7, 907812)}
(hbnb)destroy BaseModel 2a937e57-2b41-45de-a019-fe7c7b83f245
(hbnb)destroy BaseModel b166eeec-d0e6-4e00-90d9-6c3d1541d956
(hbnb)quit
```
