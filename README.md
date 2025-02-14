# QA Engineer Homework

### Dependencies
Ensure Python 3.8 or later is installed and execute:
```sh
pip3 install black
```

## Task A: String sort 
The `sort.py` script sorts characters in a string based on the following order:
1. Numbers (treated as full numeric values, not individual digits)
2. Lowercase letters
3. Uppercase letters
4. Other characters (sorted by ASCII value)
5. Unicode characters sorted by Unicode Code Point

### Limitation
- The maximum input size is set to **10 000 000 characters** in order to keep reasonoble execution time (<2s). If the input exceeds this limit, the function will raise a `ValueError`.

### Usage
Run the script with a command-line argument:
```sh
python3 src/sort.py A11a4
```
Example Output:
```
411aA
```

### Running Tests
To test `sort.py`, run:
```sh
python3 -m unittest test/test_sort.py
```

---

## Task B: Archive files

### Description
The `archiver.py` script monitors the `tmp` directory for file changes. When the number of files reaches 10, it archives them into `files.tar.gz` and clears the folder.
Also this function contains helper which can create 10 files automatically. This helper can be triggered by sending `true` as first argument for scrip run.

### Usage
Run the script with an optional argument to control file creation:
```sh
python3 src/archiver.py [true|false]
```
- `true`: Automatically generates 10 files in the `tmp` directory.
- `false`: Only monitors existing files.

### Running Tests
To test `archiver.py`, use:
```sh
python3 -m unittest test/test_archiver.py
```