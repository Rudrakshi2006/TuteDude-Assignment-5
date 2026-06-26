## ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python



## Objective
This assignment demonstrates the use of Python dictionaries and list slicing operations. It covers searching for data in a dictionary, handling missing keys, extracting list elements using slicing, and reversing lists.

---

# Task 1: Create a Dictionary of Student Marks

## Description
This program creates a dictionary where student names are stored as keys and their corresponding marks are stored as values. The user is prompted to enter a student's name. If the name exists in the dictionary, the program displays the student's marks; otherwise, it displays an appropriate message.

## Features
- Creates a dictionary of student names and marks.
- Accepts user input.
- Searches for a student in the dictionary.
- Displays the student's marks if found.
- Displays **"Student not found."** if the student does not exist.

## Sample Output

### Student Found

```
Enter the student's name: Alice
Alice's marks: 85
```

### Student Not Found

```
Enter the student's name: John
Student not found.
```

---

# Task 2: Demonstrate List Slicing

## Description
This program creates a list of numbers from 1 to 10, extracts the first five elements using list slicing, reverses the extracted list, and displays both the extracted and reversed lists.

## Features
- Creates a list using `range()`.
- Extracts the first five elements using slicing.
- Reverses the extracted list using slicing.
- Displays the original list, extracted list, and reversed list.

## Sample Output

```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```

---

# Concepts Used

- Python Dictionary
- Dictionary Lookup
- Conditional Statements (`if-else`)
- User Input (`input()`)
- Lists
- List Slicing (`[:]`)
- Reverse Slicing (`[::-1]`)
- `range()` Function
- `print()` Function

---

# Requirements

- Python 3.x

---

# How to Run

1. Save the programs as:
   - `task1.py`
   - `task2.py`
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the desired program:

```bash
python task1.py
```

or

```bash
python task2.py
```

---

# Files Included

```
├── task1.py          # Dictionary of Student Marks
├── task2.py          # List Slicing Demonstration
└── README.md         # Project Documentation
```

---
