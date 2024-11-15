# AirBnB Clone

## Project Description
This project is an AirBnB clone, which includes building a command interpreter for managing a simplified version of an AirBnB website. It focuses on creating a shell-like program that can interact with data models, serialize/deserialize objects, and support interactive and non-interactive modes.

## Command Interpreter Description
The command interpreter allows the user to interact with the program via a shell. Users can perform operations like creating, listing, and updating objects such as users, places, and bookings. The interpreter supports both interactive and non-interactive modes.

## How to Start
To start the interpreter:
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/YisehakKEK/AirBnB_clone.git
    ```
2. Navigate to the project folder:
    ```bash
    cd AirBnB_clone
    ```
3. Set up a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```
4. Install required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

5. Run the interpreter in interactive mode:
    ```bash
    ./console.py
    ```

## How to Use
Once the interpreter is running, you can enter commands to interact with the program. Available commands include:
- **help**: Lists available commands.
- **quit**: Exits the interpreter.
- **create**: Creates an object (e.g., create a user).
- **show**: Displays information about an object (e.g., show a user).
- **all**: Lists all objects of a certain class (e.g., list all users).

### Examples
Here39s how to use the interpreter in interactive mode:

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
(hbnb) show User 123
(hbnb) all User
(hbnb) quit

