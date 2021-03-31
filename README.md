![hbnb Logo](https://i.imgur.com/sxvbWgO.png "hbnb Logo")

# AirBnB Clone

The goal of this project is to deploy on our server a simple copy of the AirBnB website.

We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

Our application will be composed by:
* A command interpreter to manipulate data without a visual interface, like in a Shell
* A website that shows the final: static and dynamic
* A database or files that store data
* An API that provides a communication interface between the front-end and our data

---

## 🖥 The command interpreter
### Execution
The command interpreter can be launched in interactive or non-interactive mode as follows:
* Interactive Mode: `$ ./console.py`
* Non-interactive Mode: `$ echo <command> | ./console.py`

### Usage
The command interpreter currently handles:
* `all [class_name]` - prints all string representation of all instances (or of the specified *class_name*)
  *  Can also be used as `<class_name>.all()`
* `create <class_name>` - creates a new instance of BaseModel, saves it and prints the id
* `<class_name>.count()` - prints the number of instances of a class
* `destroy <class_name> <id>` - deletes an instance
  *  Can also be used as `<class_name>.destroy(<id>)`
* `quit` OR `⌃ + D` (EOF) - exits the program
* `show <class_name> <id>` - prints the string representation of an instance
  *  Can also be used as `<class_name>.show(<id>)`
* `update <class_name> <id> <attribute_name> <attribute_value>` - updates an instance by adding or updating attribute
  *  Can also be used as `<class_name>.update(<id>, <attribute_name>, <attribute_value>)`
     OR `<class_name>.update(<id>, <dictionary_representation>)`
     
### Example of use
```
[vagrant@ubuntu AirBnB_clone ]$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
d115b993-d908-4e26-8fab-959a52d49019
(hbnb) User.update("d115b993-d908-4e26-8fab-959a52d49019", {"first_name": "John", "last_name": "Doe", "Age": 42})
(hbnb) show User "d115b993-d908-4e26-8fab-959a52d49019"
[User] (d115b993-d908-4e26-8fab-959a52d49019) {'created_at': datetime.datetime(2021, 2, 17, 15, 28, 17, 826093), 'last_name': 'Doe', 'Age': 42, 'first_name': 'John', 'id': 'd115b993-d908-4e26-8fab-959a52d49019', 'updated_at': datetime.datetime(2021, 2, 17, 15, 29, 22, 539231)}
(hbnb) create Place
ed8d930d-33a2-4eba-9133-beb2ab8e633d
(hbnb) all
["[User] (d115b993-d908-4e26-8fab-959a52d49019) {'created_at': datetime.datetime(2021, 2, 17, 15, 28, 17, 826093), 'last_name': 'Doe', 'Age': 42, 'first_name': 'John', 'id': 'd115b993-d908-4e26-8fab-959a52d49019', 'updated_at': datetime.datetime(2021, 2, 17, 15, 29, 22, 539231)}", "[User] (dc1b70d8-282e-42dc-a25e-0e4893000705) {'created_at': datetime.datetime(2021, 2, 17, 15, 22, 36, 332889), 'id': 'dc1b70d8-282e-42dc-a25e-0e4893000705', 'updated_at': datetime.datetime(2021, 2, 17, 15, 22, 36, 332908)}", "[Place] (ed8d930d-33a2-4eba-9133-beb2ab8e633d) {'created_at': datetime.datetime(2021, 2, 17, 15, 30, 14, 168508), 'id': 'ed8d930d-33a2-4eba-9133-beb2ab8e633d', 'updated_at': datetime.datetime(2021, 2, 17, 15, 30, 14, 168520)}"]
(hbnb) quit
[vagrant@ubuntu AirBnB_clone ]$
```

---

## 🐞 Bugs
No known bugs at this time.

## 🧑‍💻 Authors
Work forked from [this repository](https://github.com/justinmajetich/AirBnB_clone.git) wrote by:
- [Ezra Nobrega](https://github.com/eNobreg)
- [Justin Majetich](https://github.com/justinmajetich)

Improved by:
- [Med Salah Bourouba](https://github.com/Brandixitor)
