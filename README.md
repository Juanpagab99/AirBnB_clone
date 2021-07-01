<h1>AirBnB clone - The console 💻🐍🐚</h1> <br>

<div>

<p><b>"The only way to do great work is to love what you do."</b> <i>Steve Jobs</i></p>

<img src= "https://www.tabbykatz.com/hbnb.png" >

</div>

<h2>Table of contents📄</h2> <br>

- [x] Description
- [x] How to start the console
- [x] Command interpreter
- [x] Authors

<h2>Description 📑</h2> <br>

In this project, as the first step of the AirBnB clone, a console was made that will allow you to control, manage or administer your AirBnB objects. This is a segment that contains a fundamental concepts of higher level programming. The goal of the project is make a simple copy of the AirBnB website.

<h2>Command interpreter 📑</h2> <br>

It is like a shell only that it has its own specific characteristics, which are:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

All of the above, works with the following commands:

| Command   | Description                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------- |
| `create`  | Create a new instance of Class-name, saves it and print the id.                                                   |
| `show`    | Prints the string representation of an instance based on the class-name and id.                                   |
| `destroy` | Deletes an instance based on the class name and id.                                                               |
| `all`     | Prints all string representation of all instances based or not on the class name.                                 |
| `update`  | Updates an instance based on the class name and id by adding or updating attribute                                |
| `EOF`     | Clean method to logs out the terminal with CTRL-D or write EOF in the console.                                    |
| `quit`    | Quit command to exit the program                                                                                  |
| `help `   | this action is provided by default by cmd but you should keep it updated and documented as you work through tasks |

<h2>How to start the console 💻📑</h2> <br>

<h3>Instalation</h3> <br>

- Clone this repository with: `git clone https://github.com/Juanpagab99/AirBnB_clone.git`
- Access into de AirBnB directory: `cd AirBnB_clone`
- Run the console (Interactively method): `./console.py`
- Run the console (non-interecatively method): `echo "<command>" | ./console.py`

<h3>Implementation</h3> <br>

It should work in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
$
```

And it should work in non_interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

<h2>Author 👦🍫</h2> <br>
- Juan Pablo Gaviria Barrera | [Github] (https://github.com/Juanpagab99) | [Twiter](https://twitter.com/JuanPab27132211)
<div dir="rtl">28/06/2021</div>
