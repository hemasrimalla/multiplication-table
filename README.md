# Multiplication Table Generator

A beginner-friendly, interactive Python command-line application that generates clean, well-aligned multiplication tables for any given number and limit.

---

## Project Structure

```text
multiplication-table/
├── multiplication_table.py   # Main Python script
├── output.txt                # Sample execution output for 5, 7, and 12
└── README.md                 # Project documentation and interview Q&A
```

---

## Features

- **Robust Input Validation:**
  - Validates that the base number is a valid integer (handles positive, negative, and zero; re-prompts on invalid input).
  - Validates that the limit is a positive integer greater than `0`.
- **Clean Column Alignment:**
  - Dynamically aligns columns using Python format specifiers so numbers of varying digit lengths line up neatly.
- **Modular Design:**
  - Logic is encapsulated in modular functions (`print_table`, `get_integer_input`, `get_positive_integer_input`, `main`) with an `if __name__ == "__main__":` entry point guard.
- **Interactive Re-run Loop:**
  - Allows users to generate another table or exit gracefully (`y`/`n`).

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd multiplication-table
   ```
3. Run the script using Python:
   ```bash
   python multiplication_table.py
   ```
4. Follow the on-screen prompts to input a number, specify a limit, and decide whether to generate another table.

---

## Sample Output

Below is the output for three test numbers (**5**, **7**, and **12**) with a limit of **10**:

### 1. Table for 5 (Limit: 10)
```text
Multiplication Table of 5
-------------------------
5 x  1 =   5
5 x  2 =  10
5 x  3 =  15
5 x  4 =  20
5 x  5 =  25
5 x  6 =  30
5 x  7 =  35
5 x  8 =  40
5 x  9 =  45
5 x 10 =  50
```

### 2. Table for 7 (Limit: 10)
```text
Multiplication Table of 7
-------------------------
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
7 x  4 =  28
7 x  5 =  35
7 x  6 =  42
7 x  7 =  49
7 x  8 =  56
7 x  9 =  63
7 x 10 =  70
```

### 3. Table for 12 (Limit: 10)
```text
Multiplication Table of 12
--------------------------
12 x  1 =  12
12 x  2 =  24
12 x  3 =  36
12 x  4 =  48
12 x  5 =  60
12 x  6 =  72
12 x  7 =  84
12 x  8 =  96
12 x  9 = 108
12 x 10 = 120
```

---

## Concepts Used

### Interview Questions & Answers

#### 1. When would you use a `for` loop?
> A `for` loop is used for **definite iteration**—when you need to traverse over a known sequence or iterable (e.g., a `list`, `tuple`, `string`, `dict`, or `range()`), or when you know in advance how many times the loop should run.
> In contrast, a `while` loop is preferred for **indefinite iteration**, where the loop repeats until a specific boolean condition changes (such as waiting for valid user input).

#### 2. What does `range()` return?
> In Python 3, `range()` returns an **immutable sequence object** of type `range`. It is not a list; instead, it generates integers on demand using **lazy evaluation**. Because it calculates values as requested rather than creating the entire sequence in memory at once, it consumes a constant amount of memory ($O(1)$ space complexity), regardless of how large the range is.

#### 3. What is the difference between `range(5)` and `range(1, 5)`?
> - **`range(5)`:** Takes a single argument as the `stop` value. The `start` defaults to `0`, producing 5 numbers from `0` up to (but not including) `5`:
>   `0, 1, 2, 3, 4`
> - **`range(1, 5)`:** Takes two arguments: `start = 1` and `stop = 5`. It produces 4 numbers starting from `1` up to (but not including) `5`:
>   `1, 2, 3, 4`
