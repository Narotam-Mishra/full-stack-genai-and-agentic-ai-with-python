# Gen AI Engineering with Python 

## Sec 6 - Functions in Python

## 39. Functions - Reducing Duplication and Splitting Complex Tasks (14:30)

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

## 40. Functions - 3 More Features (12:32)

## Python Functions – Simple Notes (Part 2)

This part explains **3 more benefits of functions**:

1. Hiding Implementation Details
2. Improving Readability (using `return`)
3. Improving Traceability

---

## 1. Hiding Implementation Details

### Concept

Sometimes functions contain **complex logic**.

Other developers **do not need to know how the function works internally**.
They only need to know **what the function does**.

This is called **hiding implementation details**.

Example tasks in a user registration system:

1. Get user input
2. Validate the input
3. Save data to database

Each task can be a separate function.

---

### Example

```python
def get_input():
    print("Getting user input")

def validate_input():
    print("Validating user information")

def save_to_db():
    print("Saving data to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")

register_user()
```

### Output

```
Getting user input
Validating user information
Saving data to database
User registration complete
```

---

### Why this is useful

Benefits:

* Clean structure
* Easy debugging
* Easy teamwork
* Hide complexity

Example structure:

```
register_user()
   ├ get_input()
   ├ validate_input()
   └ save_to_db()
```

Each function handles **one responsibility**.

This idea is called:

### Separation of Concerns

Meaning:
Break a large task into **smaller independent parts**.

---

## 2. Improving Readability

Functions make code **easier to read and understand**.

Example scenario:

A shop calculates the bill based on:

* number of cups
* price per cup

Instead of writing the formula everywhere, create a function.

---

## Using Return

Important concept:

### `print()` vs `return`

| print              | return                |
| ------------------ | --------------------- |
| Displays output    | Sends value back      |
| Cannot reuse value | Can store value       |
| Used for display   | Used for calculations |

---

### Example

```python
def calculate_bill(cups, price_per_cup):
    total = cups * price_per_cup
    return total
```

Calling the function:

```python
bill = calculate_bill(3, 15)
print(bill)
```

Output

```
45
```

---

### Directly Using Inside Print

```python
print("Order for table 2:", calculate_bill(2, 50))
```

Output

```
Order for table 2: 100
```

---

### Why `return` is powerful

With return we can:

* store results
* reuse results
* perform further calculations

Example

```python
bill = calculate_bill(4, 20)

tax = bill * 0.1

final_amount = bill + tax

print(final_amount)
```

---

## 3. Improving Traceability

### Concept

Traceability means:

You can **easily track where logic exists** and **fix it in one place**.

Example:

A shop adds **10% tax (VAT)** to every order.

Instead of writing tax calculation everywhere, create a function.

---

### Example

```python
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100
```

List of orders:

```python
orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print("Original:", price, "Final with VAT:", final_amount)
```

Output

```
Original: 100 Final with VAT: 110
Original: 150 Final with VAT: 165
Original: 200 Final with VAT: 220
```

---

### Why this is useful

If tax changes from **10% to 12%**

You update only one place:

```python
add_vat(price, 12)
```

Instead of changing tax calculation everywhere.

---

## Important Concepts Covered

## 1. Function Definition

Functions are defined using `def`.

```python
def greet():
    print("Hello")
```

---

## 2. Calling a Function

```python
greet()
```

---

## 3. Parameters

Variables inside function definition.

```python
def greet(name):
```

---

## 4. Arguments

Values passed when calling the function.

```python
greet("Aman")
```

---

## 5. Return Value

Returns result from function.

```python
def add(a, b):
    return a + b
```

---

## 6. Function Structure

```
Main Function
   ├ helper function
   ├ helper function
   └ helper function
```

This makes code **clean and modular**.

---

## Best Practices for Functions

### 1. Use meaningful names

Bad

```
f1()
x()
doStuff()
```

Good

```
calculate_bill()
register_user()
add_vat()
```

---

### 2. One function = one task

Bad

```
function does 5 things
```

Good

```
each function does 1 job
```

---

### 3. Keep functions small

Small functions are easier to:

* read
* debug
* reuse

---

## Quick Real-Life Example

ATM Machine

Functions could be:

```
check_balance()
withdraw_money()
deposit_money()
validate_pin()
```

Each function performs **one specific task**.

---

## Final Key Takeaways

Functions help to:

- Reduce code duplication
- Hide complex logic
- Improve readability
- Improve traceability
- Break big problems into small tasks
- Reuse code easily

---

## 41. Scope and Named Space in functions (12:04)

## Python Functions – Scopes (Simple Notes)

## What is Scope?

**Scope** means **where a variable can be accessed in the program**.

In simple words:

> Scope defines **the visibility and lifetime of a variable**.

Example idea:

* Some variables are usable **only inside a function**
* Some variables are usable **everywhere**

---

## Cafe Example 

Imagine a **chai cafe** called **Global Sip**.

* The **owner has a master notepad** (global data)
* Each **worker has their own notepad** (local data)

If a worker writes an order in their notebook, it **does not change the owner's notebook**.

Same idea in programming:

* Variables inside functions **do not affect variables outside**

---

## Name Resolution (Important Concept)

When Python sees a variable, it decides **where to find it**.

This process is called:

**Name Resolution**

Python searches variables in this order:

### LEGB Rule

| Level | Meaning   |
| ----- | --------- |
| L     | Local     |
| E     | Enclosing |
| G     | Global    |
| B     | Built-in  |

Python checks variables in this order.

---

## 1. Local Scope

Local scope means:

> Variables declared **inside a function**.

They **only exist inside that function**.

---

## Example

```python
def serve_chai():
    chai_type = "Masala Chai"   # local variable
    print("Inside function:", chai_type)

serve_chai()
```

Output

```
Inside function: Masala Chai
```

---

### Accessing Outside (Error)

```python
def serve_chai():
    chai_type = "Masala Chai"

serve_chai()

print(chai_type)
```

Output

```
NameError: chai_type is not defined
```

Because **local variables cannot be accessed outside the function**.

---

## 2. Global Scope

Global scope means:

> Variables defined **outside any function**.

They can be accessed **throughout the program**.

---

## Example

```python
chai_type = "Lemon Chai"

def serve_chai():
    print("Inside function:", chai_type)

serve_chai()

print("Outside function:", chai_type)
```

Output

```
Inside function: Lemon Chai
Outside function: Lemon Chai
```

Because **global variables are accessible everywhere**.

---

## Local vs Global Example

```python
chai_type = "Lemon Chai"

def serve_chai():
    chai_type = "Masala Chai"
    print("Inside:", chai_type)

serve_chai()

print("Outside:", chai_type)
```

Output

```
Inside: Masala Chai
Outside: Lemon Chai
```

Explanation:

* Inside function → local variable used
* Outside → global variable used

---

## 3. Enclosing Scope (Nested Functions)

Enclosing scope occurs when:

> A function is defined **inside another function**.

The inner function can access variables from the **outer function**.

---

## Example

```python
def chai_counter():

    chai_order = "Lemon Chai"

    def inner_function():
        print("Inner:", chai_order)

    inner_function()
    print("Outer:", chai_order)

chai_counter()
```

Output

```
Inner: Lemon Chai
Outer: Lemon Chai
```

Explanation:

* `chai_order` belongs to outer function
* Inner function can still access it

---

## Nested Scope Example with Different Values

```python
def chai_counter():

    chai_order = "Lemon Chai"

    def inner_function():
        chai_order = "Ginger Chai"
        print("Inner:", chai_order)

    inner_function()

    print("Outer:", chai_order)

chai_counter()
```

Output

```
Inner: Ginger Chai
Outer: Lemon Chai
```

Explanation:

* Inner function creates its **own local variable**
* Outer variable remains unchanged

---

## 4. Built-in Scope

Built-in scope contains **Python's predefined functions**.

Examples:

* `print()`
* `len()`
* `range()`
* `type()`

These functions are always available.

---

## Example

```python
numbers = [1, 2, 3, 4]

print(len(numbers))
```

Output

```
4
```

Here `len()` comes from **built-in scope**.

---

## Combined Example (LEGB)

```python
chai_order = "Tulsi Chai"   # Global

def cafe():

    chai_order = "Lemon Chai"   # Enclosing

    def kitchen():
        chai_order = "Ginger Chai"  # Local
        print("Kitchen:", chai_order)

    kitchen()

    print("Cafe:", chai_order)

cafe()

print("Global:", chai_order)
```

Output

```
Kitchen: Ginger Chai
Cafe: Lemon Chai
Global: Tulsi Chai
```

Explanation:

* Local → Ginger
* Enclosing → Lemon
* Global → Tulsi

---

## Important Pointers

### 1. Variables inside functions are local

```python
def test():
    x = 10
```

`x` only exists inside `test()`.

---

### 2. Global variables exist outside functions

```python
x = 10
```

Accessible anywhere.

---

### 3. Nested functions create enclosing scope

```python
def outer():
    def inner():
        pass
```

Inner can access outer variables.

---

### 4. Python follows LEGB order

Python searches variables in this order:

```
Local
↓
Enclosing
↓
Global
↓
Built-in
```

---

## Simple Visual Diagram

```
Global Scope
│
├── Function A
│     └── Local Variables
│
├── Function B
│     └── Local Variables
│
└── Built-in Functions
```

Each function acts like **its own house**.

Variables inside a house **stay inside the house**.

---

## Key Takeaways

- Scope controls **where variables can be accessed**
- Python uses **LEGB rule** for variable lookup
- Local variables exist **inside functions**
- Global variables exist **outside functions**
- Nested functions create **enclosing scope**
- Built-in functions always exist

---

## 42. Non local vs Global scopes (09:08)

summaries this python tutorial transcript in simple words, make note of all important pointers and also explain each important concepts with basic code examples