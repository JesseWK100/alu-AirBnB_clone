**alu-AirBnB\_clone**

---

## Project Description

**alu-AirBnB\_clone** is a simple console-based clone of the AirBnB web application. The project allows users to manage objects like Users, Places, Cities, States, and Reviews entirely from the command line, using a custom-built command interpreter. It demonstrates object-oriented Python, file storage (JSON serialization), and a mini shell interface.

## Command Interpreter

The command interpreter (`console.py`) accepts commands to create, show, update, and destroy instances of your classes.

### How to Start

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-organization>/alu-AirBnB_clone.git
   cd alu-AirBnB_clone
   ```

2. (Optional) Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Run the console:

   ```bash
   python3 console.py
   ```

### How to Use

In the `(hbnb)` prompt, you can use the following commands:

* `create <ClassName>`: Creates a new instance of `ClassName` and prints its id.
* `show <ClassName> <id>`: Prints the string representation of an instance based on class name and id.
* `destroy <ClassName> <id>`: Deletes an instance based on the class name and id.
* `all [<ClassName>]`: Prints all string representations of all instances, or all instances of `ClassName` if provided.
* `update <ClassName> <id> <attribute_name> "<attribute_value>"`: Updates an instance by adding or updating an attribute.
* `count <ClassName>`: Retrieves the number of instances of `ClassName`.
* `quit` or `EOF`: Exits the console.

### Examples

```bash
$ python3 console.py
(hbnb) create User
8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc
(hbnb) show User 8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc
[User] (8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc) {"id": "8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc", "created_at": "2025-05-14T12:00:00.000000", "updated_at": "2025-05-14T12:00:00.000000"}
(hbnb) all User
[[User] (8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc) { ... }]
(hbnb) update User 8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc name "Alice"
(hbnb) show User 8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc
[User] (8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc) {"id": "8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc", "created_at": "2025-05-14T12:00:00.000000", "updated_at": "2025-05-14T12:05:00.000000", "name": "Alice"}
(hbnb) destroy User 8f1e54a2-3d2b-4f6a-9d5e-51c0c1e7fabc
(hbnb) all User
[]
(hbnb) quit
```

---

## Repository & Collaboration

* **GitHub repo**: `alu-AirBnB_clone`
* **Branching**: Use feature branches (e.g., `feature-console`, `feature-storage`) for new work.
* **Pull Requests**: Open a PR when a feature is ready. Include description of changes, testing steps, and assign reviewers.
* **Code Style**: Follow PEP8. Use `flake8` or similar to lint your code before pushing.

---

## AUTHORS

An `AUTHORS` file is provided at the root of this repository, listing all contributors.

Please see [AUTHORS](AUTHORS) for the full list of names and contact information.

