# Gen AI Engineering with Python 

## Sec 6 - Functions in Python

## Functions - Reducing Duplication and Splitting Complex Tasks (14:30)

Here is a **simple summary of the tutorial** along with **clear explanations and examples** so the concept of Python functions becomes easy to understand.

---

## Python Functions – Simple Summary

## 1. What is a Function?

A **function** is a block of code that performs a specific task and can be **reused multiple times**.

Think of it like a **machine**:

Input → Machine (Function) → Output

Example in real life:

* Coffee machine
* You press a button → machine prepares coffee.

In programming:

* You call a function → it performs a task.

---

## Why Functions Are Important

Functions help to:

### 1. Reuse Code

Instead of writing the same code again and again, we write it **once inside a function**.

### 2. Improve Readability

Functions make code easier to read and understand.

### 3. Maintain Code Easily

If something changes, you only update it **in one place**.

### 4. Break Large Problems into Small Tasks

Complex tasks can be divided into **smaller manageable functions**.

---

## Basic Syntax of a Function

In Python we use the **`def` keyword**.

```python
def function_name():
    # code to execute
```

Example:

```python
def greet():
    print("Hello World")

greet()
```

Output:

```
Hello World
```

---

## Parameters vs Arguments

Important terms:

| Term      | Meaning                             |
| --------- | ----------------------------------- |
| Parameter | Variable inside function definition |
| Argument  | Value passed when calling function  |

Example:

```python
def greet(name):   # name = parameter
    print("Hello", name)

greet("Aman")      # Aman = argument
```

Output:

```
Hello Aman
```

---

## Example 1 – Reducing Code Duplication

### Problem

You manage a tea stall and need to print customer orders.

Without functions:

```python
print("Aman ordered masala chai")
print("Rahul ordered ginger chai")
print("Riya ordered tulsi chai")
```

If the message format changes, you must edit **every line**.

---

### Using Function

```python
def print_order(name, chai_type):
    print(name, "ordered", chai_type, "chai!")

print_order("Aman", "Masala")
print_order("Rahul", "Ginger")
print_order("Riya", "Tulsi")
```

Output:

```
Aman ordered Masala chai!
Rahul ordered Ginger chai!
Riya ordered Tulsi chai!
```

### Advantage

If you want to change the message:

```python
print(name, "just ordered", chai_type, "chai ☕")
```

You update it **only once**.

---

## Example 2 – Splitting a Complex Task

### Problem

You want to generate a monthly cafe sales report.

Instead of writing everything in one big block, we divide it into functions.

Steps:

1. Fetch sales data
2. Filter valid orders
3. Summarize data
4. Generate report

---

### Solution Using Functions

```python
def fetch_sales():
    print("Fetching sales data")

def filter_valid_orders():
    print("Filtering valid orders")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("Report is ready")

generate_report()
```

Output:

```
Fetching sales data
Filtering valid orders
Summarizing sales data
Report is ready
```

---

## Why This Approach Is Better

Without functions:

```
Very long messy code
Hard to read
Hard to debug
```

With functions:

```
Small readable blocks
Reusable code
Easy debugging
Easy teamwork
```

Example structure:

```
generate_report()
    ├ fetch_sales()
    ├ filter_valid_orders()
    └ summarize_data()
```

---

## Important Best Practice

### Use Good Function Names

Bad:

```
def f1()
def x()
```

Good:

```
def calculate_total()
def generate_report()
def print_order()
```

The function name should **describe what the function does**.

---

## Key Takeaways

* Functions help **reuse code**
* Defined using **`def`**
* **Parameters** receive data
* **Arguments** send data
* They make code:

  * readable
  * maintainable
  * modular

---