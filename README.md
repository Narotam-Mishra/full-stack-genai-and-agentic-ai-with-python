# [Gen AI Engineering with Python](https://chatgpt.com/share/69bbb1b8-b64c-8004-a981-3a6ccd5ff19b) 

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

## Python Scopes – `nonlocal` and `global`

In the previous lesson, we learned about **Python scope (LEGB rule)**:

| Scope     | Meaning                           |
| --------- | --------------------------------- |
| Local     | Inside current function           |
| Enclosing | Outer function (nested functions) |
| Global    | Top level of script               |
| Built-in  | Python’s built-in functions       |

Now we learn how to **modify variables from outer scopes** using:

* `nonlocal`
* `global`

---

## 1. Problem Without `nonlocal`

Suppose we have a **function inside another function**.

Example:

```python
def update_order():

    chai_type = "Elaichi"

    def kitchen():
        chai_type = "Kesar"

    kitchen()

    print("After kitchen update:", chai_type)

update_order()
```

### Output

```
After kitchen update: Elaichi
```

### Why?

Because:

* `chai_type = "Kesar"` creates a **new local variable**
* It does **not modify the outer variable**

---

## 2. Using `nonlocal`

`nonlocal` allows the **inner function to modify variables from the outer function**.

### Example

```python
def update_order():

    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"

    kitchen()

    print("After kitchen update:", chai_type)

update_order()
```

### Output

```
After kitchen update: Kesar
```

### Explanation

`nonlocal chai_type` tells Python:

> Use the variable from the **outer function**, not create a new one.

---

## Important Pointer About `nonlocal`

`nonlocal` works **only with enclosing functions**.

It **cannot access global variables directly**.

Example:

```python
chai_type = "Masala"

def kitchen():
    nonlocal chai_type
```

This will cause an error.

Because **nonlocal searches only the enclosing function**, not global.

---

## 3. Global Keyword

`global` allows functions to **modify global variables**.

Global variables exist **outside all functions**.

---

## Example

```python
chai_type = "Plain Chai"

def kitchen():
    global chai_type
    chai_type = "Irani Chai"

kitchen()

print("Final chai:", chai_type)
```

### Output

```
Final chai: Irani Chai
```

### Explanation

`global chai_type` tells Python:

> Use the **global variable**, not create a new local variable.

---

## Example Without `global`

```python
chai_type = "Plain Chai"

def kitchen():
    chai_type = "Irani Chai"

kitchen()

print(chai_type)
```

### Output

```
Plain Chai
```

Why?

Because a **new local variable** is created inside the function.

---

## Difference Between `nonlocal` and `global`

| Keyword  | Access Level               |
| -------- | -------------------------- |
| nonlocal | Outer (enclosing) function |
| global   | Entire program             |

---

### Example Structure

```
Global Scope
   |
   |-- outer_function
          |
          |-- inner_function
```

* `nonlocal` → accesses `outer_function`
* `global` → accesses **global scope**

---

## Example Showing All Scopes

```python
chai_type = "Tulsi"

def cafe():

    chai_type = "Lemon"

    def kitchen():
        nonlocal chai_type
        chai_type = "Ginger"

    kitchen()

    print("Cafe:", chai_type)

cafe()

print("Global:", chai_type)
```

### Output

```
Cafe: Ginger
Global: Tulsi
```

Explanation:

* `nonlocal` updated the **outer function variable**
* Global variable remained unchanged

---

## Why Using `global` Can Be Dangerous

Imagine many developers working on the same project.

Example:

```python
global_config = True
```

Multiple functions might change it.

Example:

```python
def functionA():
    global global_config
    global_config = "Ginger"
```

Another function expects it to be boolean:

```python
def functionB():
    if global_config:
        print("Working")
```

Now the program **breaks** because:

```
global_config = "Ginger"
```

So behavior becomes unpredictable.

---

## Best Practice

Avoid using `global` unless absolutely necessary.

Better approach:

Use **function parameters and return values**.

---

### Good Design Example

```python
def update_order(chai_type):
    chai_type = "Kesar"
    return chai_type

chai = "Elaichi"

chai = update_order(chai)

print(chai)
```

Output

```
Kesar
```

This approach is:

* safer
* easier to debug
* better for teamwork

---

## Key Points to Remember

### `nonlocal`

* Used inside **nested functions**
* Modifies **outer function variable**

### `global`

* Used to modify **global variables**
* Accessible from anywhere

### Important Warning

`global` can break large programs because:

* Many functions may modify the same variable

---

## Quick Visual Diagram

```
Global Scope
   |
   |-- Function A
   |       |
   |       |-- Inner Function
   |
   |-- Function B
```

Access rules:

```
Inner Function
   ↓
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
```

---

## Final Takeaways

✔ Python variables follow **LEGB scope rule**
✔ `nonlocal` modifies **outer function variables**
✔ `global` modifies **global variables**
✔ Avoid excessive use of `global`
✔ Prefer **function parameters and return values**

---

## 42. Handling Arguments in function (15:01)

## 1. Functions and Parameters in Python

A **function** is a block of code that performs a task.

### Basic Syntax

```python
def function_name(parameter):
    pass
```

Example:

```python
def prepare_chai(order):
    print("Preparing", order)
```

Here:

* `order` → **parameter** (placeholder)
* Actual value passed → **argument**

Calling the function:

```python
chai = "Ginger Chai"

prepare_chai(chai)
```

Output:

```
Preparing Ginger Chai
```

---

## 2. Parameters vs Arguments

| Term      | Meaning                                   |
| --------- | ----------------------------------------- |
| Parameter | Variable used in function definition      |
| Argument  | Actual value passed when calling function |

Example:

```python
def greet(name):   # name = parameter
    print("Hello", name)

greet("Rahul")     # "Rahul" = argument
```

---

## 3. Immutable vs Mutable Values (Very Important)

This concept affects **whether original data changes or not when passed to functions**.

## Immutable Data Types

Cannot be changed.

Examples:

* string
* integer
* float
* tuple

Example:

```python
chai = "Ginger Chai"

def prepare(order):
    order = "Masala Chai"

prepare(chai)

print(chai)
```

Output:

```
Ginger Chai
```

✔ Original value **does not change**.

---

## Mutable Data Types

Can be changed.

Examples:

* list
* dictionary
* set

Example:

```python
chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)

print(chai)
```

Output:

```
[1, 42, 3]
```

✔ Original list **changed**.

**Reason:** Lists are mutable.

---

## 4. Positional Arguments

Arguments passed **based on position**.

Example:

```python
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")
```

Here:

| Value      | Goes into |
| ---------- | --------- |
| Darjeeling | tea       |
| Yes        | milk      |
| Low        | sugar     |

Output:

```
Darjeeling Yes Low
```

---

## 5. Keyword Arguments

Arguments passed **using parameter names**.

Order does **not matter**.

Example:

```python
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai(
    sugar="Medium",
    tea="Green",
    milk="No"
)
```

Output:

```
Green No Medium
```

✔ Safer
✔ Clearer

---

## 6. *args (Variable Positional Arguments)

`*args` allows a function to accept **any number of positional arguments**.

Example:

```python
def special_chai(*ingredients):
    print(ingredients)

special_chai("Cinnamon", "Cardamom", "Ginger")
```

Output:

```
('Cinnamon', 'Cardamom', 'Ginger')
```

Important:

* `*args` stores values in a **tuple**

---

## 7. **kwargs (Keyword Arguments)

`**kwargs` accepts **any number of named arguments**.

Example:

```python
def special_chai(**extras):
    print(extras)

special_chai(sweetener="Honey", foam="Yes")
```

Output:

```
{'sweetener': 'Honey', 'foam': 'Yes'}
```

Important:

* `**kwargs` stores values in a **dictionary**

---

## 8. Using *args and **kwargs Together

Example:

```python
def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai(
    "Cinnamon",
    "Cardamom",
    sweetener="Honey",
    foam="Yes"
)
```

Output:

```
Ingredients: ('Cinnamon', 'Cardamom')
Extras: {'sweetener': 'Honey', 'foam': 'Yes'}
```

Explanation:

| Type     | Example                | Stored As  |
| -------- | ---------------------- | ---------- |
| *args    | "Cinnamon", "Cardamom" | tuple      |
| **kwargs | sweetener="Honey"      | dictionary |

---

## 9. Default Parameter Values

You can give **default values to parameters**.

Example:

```python
def make_chai(sugar="Medium"):
    print("Sugar level:", sugar)

make_chai()
make_chai("Low")
```

Output:

```
Sugar level: Medium
Sugar level: Low
```

---

## 10. Dangerous Default Mutable Values (Important Python Trap)

Using **mutable values like lists as default parameters can cause bugs**.

Example:

```python
def chai_orders(order=[]):
    order.append("Masala Chai")
    print(order)

chai_orders()
chai_orders()
```

Output:

```
['Masala Chai']
['Masala Chai', 'Masala Chai']
```

Problem:

The list **keeps growing every time the function runs**.

This happens because **Python creates the default list only once**.

---

## 11. Safe Way to Handle Default Lists

Use `None` instead.

Example:

```python
def chai_orders(order=None):

    if order is None:
        order = []

    order.append("Masala Chai")

    print(order)
```

Now calling multiple times:

```python
chai_orders()
chai_orders()
```

Output:

```
['Masala Chai']
['Masala Chai']
```

✔ No unexpected behavior.

---

## 12. Important Python Best Practices

### 1. Know Mutable vs Immutable

| Immutable | Mutable    |
| --------- | ---------- |
| string    | list       |
| int       | dictionary |
| float     | set        |
| tuple     |            |

---

### 2. Use Keyword Arguments for Clarity

Bad:

```python
make_chai("Green", "Yes", "Low")
```

Better:

```python
make_chai(
    tea="Green",
    milk="Yes",
    sugar="Low"
)
```

---

### 3. Avoid Mutable Default Parameters

Bad:

```python
def func(data=[]):
```

Good:

```python
def func(data=None):
```

---

## 13. Quick Visual Summary

```
Function

def func(parameter):
       ↑
   parameter

func(argument)
       ↑
   argument
```

---

## 14. Key Concepts from the Tutorial

- Function parameters accept many types of values
- Immutable values don't change original data
- Mutable values can change original data
- Positional arguments depend on order
- Keyword arguments use parameter names
- `*args` collects unlimited positional arguments (tuple)
- `**kwargs` collects unlimited keyword arguments (dictionary)
- Avoid mutable default values like `[]`
- Use `None` instead

---

## 42. Handle Multiple Return (10:43)

## What is `return` in Python?

The **`return` keyword** is used inside a function to **send a value back to the place where the function was called**.

Think of it like a **tea seller giving chai to the customer** ☕

* Function prepares something
* `return` gives the result back

---

## Basic Function Without Return

Example:

```python
def make_chai():
    print("Here is your Masala Chai")

make_chai()
```

Output:

```
Here is your Masala Chai
```

Here the function **prints** the result but **does not return anything**.

---

## Function With Return

Example:

```python
def make_chai():
    return "Here is your Masala Chai"

print(make_chai())
```

Output:

```
Here is your Masala Chai
```

Explanation:

* Function returns a value
* `print()` displays it

---

## Storing Returned Value in a Variable

Instead of printing directly, you can store the result.

Example:

```python
def make_chai():
    return "Masala Chai"

chai = make_chai()

print(chai)
```

Output:

```
Masala Chai
```

This is **more readable and flexible**.

---

## Important Rule: Functions Stop After `return`

When Python executes `return`, the function **immediately stops**.

Example:

```python
def test():
    print("Start")
    return "Done"
    print("This will never run")

print(test())
```

Output:

```
Start
Done
```

The last print statement **never executes**.

---

## Case 1: Function Returns Nothing (Returns `None`)

If a function **does not return anything**, Python automatically returns **`None`**.

Example:

```python
def chai_maker():
    pass

result = chai_maker()

print(result)
```

Output:

```
None
```

Explanation:

* Python automatically returns **None**
* This is called **implicit return**

---

## Case 2: Returning One Value

Example:

```python
def sold_cups():
    return 120

total = sold_cups()

print(total)
```

Output:

```
120
```

The function returns **one value**.

---

## Case 3: Early Return (Short Circuit)

You can **exit a function early using return**.

Example:

```python
def chai_status(cups_left):

    if cups_left == 0:
        return "Sorry, chai is over"

    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))
```

Output:

```
Sorry, chai is over
Chai is ready
```

Explanation:

If condition is true → function returns immediately.

---

## Case 4: Returning Multiple Values

Python allows functions to **return multiple values**.

Example:

```python
def chai_report():
    return 120, 20
```

Receiving values:

```python
sold, remaining = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)
```

Output:

```
Sold: 120
Remaining: 20
```

Python actually returns a **tuple internally**.

---

## Returning Three Values

Example:

```python
def chai_report():
    return 120, 10, 20
```

Receiving values:

```python
sold, unpaid, remaining = chai_report()

print(sold, unpaid, remaining)
```

Output:

```
120 10 20
```

---

## Ignoring Unwanted Returned Values

Sometimes you don't need all values.

Use `_` (underscore).

Example:

```python
def chai_report():
    return 120, 10, 20

sold, _, remaining = chai_report()

print(sold)
print(remaining)
```

Output:

```
120
20
```

Explanation:

`_` means:

> I know a value exists but I don't need it.

---

## What Can a Function Return?

A function can return **any Python object**:

| Type       | Example                   |
| ---------- | ------------------------- |
| Integer    | `return 10`               |
| String     | `return "chai"`           |
| Boolean    | `return True`             |
| List       | `return [1,2,3]`          |
| Dictionary | `return {"tea":"masala"}` |
| Tuple      | `return 1,2`              |

Example:

```python
def data():
    return [1,2,3]

print(data())
```

---

## Print vs Return (Very Important Difference)

| Print               | Return                |
| ------------------- | --------------------- |
| Displays output     | Sends value back      |
| Cannot reuse result | Can store and reuse   |
| Used for debugging  | Used in real programs |

Example:

Bad practice:

```python
def add(a,b):
    print(a+b)
```

Better:

```python
def add(a,b):
    return a+b
```

---

## Real Programming Example

Example:

```python
def calculate_total(price, tax):

    total = price + tax

    return total

bill = calculate_total(100, 10)

print("Total Bill:", bill)
```

Output:

```
Total Bill: 110
```

---

## Important Points to Remember

### 1️⃣ `return` sends a value back from a function.

### 2️⃣ If no value is returned → Python returns `None`.

### 3️⃣ Code after `return` **never runs**.

### 4️⃣ A function can return **multiple values**.

### 5️⃣ `_` can be used to **ignore unused return values**.

### 6️⃣ `return` is preferred over `print` in real programs.

---

## Quick Visual Summary

```
Function Call
      ↓
Function Executes
      ↓
return value
      ↓
Value goes back to caller
```

Example:

```
result = add(5,3)
           ↓
        return 8
           ↓
result = 8
```

---

## 43. Lambdas, Pure vs Impure functions (12:24)

## Types of Functions in Python (Simple Notes)

Functions are the **core building blocks** of large Python programs.
Even though a function is just a block of code, developers often categorize them based on **how they behave**.

Important types discussed:

1. **Pure Functions**
2. **Impure Functions**
3. **Recursive Functions**
4. **Lambda (Anonymous) Functions**

---

## 1. Pure Function

### Definition

A **pure function**:

* Uses **only its input parameters**
* **Does not modify external/global variables**
* Always gives the **same output for the same input**

These functions are **predictable and safe**, so they are recommended.

### Example

```python
def pure_chai(cups):
    return cups * 10
```

Usage:

```python
print(pure_chai(2))  
```

Output

```
20
```

### Why this is pure

* It **only uses the parameter `cups`**
* It **does not change any global variable**

### Key Points

✔ Works only with given inputs
✔ No side effects
✔ Recommended in real projects

---

## 2. Impure Function

### Definition

An **impure function**:

* Modifies **global variables**
* Depends on **external state**

This makes code **harder to debug and maintain**.

### Example

```python
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups
```

Usage

```python
impure_chai(3)
print(total_chai)
```

Output

```
3
```

### Why this is impure

The function **changes the global variable** `total_chai`.

### Problems with impure functions

❌ Hard to track changes
❌ Unexpected side effects
❌ Not recommended for clean code

### Key Idea

Avoid modifying **global variables inside functions**.

---

## 3. Recursive Function

### Definition

A **recursive function** is a function that **calls itself**.

But it must always have a **base condition** to stop the recursion.

Otherwise it will run **forever (infinite recursion)**.

---

### Example

```python
def pour_chai(n):
    if n == 0:
        print("All cups poured")
        return

    print("Remaining cups:", n)
    pour_chai(n - 1)
```

Usage

```python
pour_chai(3)
```

Output

```
Remaining cups: 3
Remaining cups: 2
Remaining cups: 1
All cups poured
```

---

### How recursion works

If we call

```
pour_chai(3)
```

Execution flow:

```
pour_chai(3)
   ↓
pour_chai(2)
   ↓
pour_chai(1)
   ↓
pour_chai(0)
```

At `n == 0`, the function stops.

---

### Key Parts of Recursion

1️⃣ **Base Case**
Condition that stops recursion

```python
if n == 0:
    return
```

2️⃣ **Recursive Call**

```python
pour_chai(n - 1)
```

---

### Where recursion is used

* Tree problems
* Graph traversal
* Factorial
* Fibonacci
* Backtracking problems

---

## 4. Lambda Functions (Anonymous Functions)

### Definition

A **lambda function** is a **small function without a name**.

Also called **anonymous functions**.

They are usually used **once (use and throw)**.

---

### Syntax

```
lambda arguments : expression
```

---

### Example

Normal function

```python
def square(x):
    return x * x
```

Lambda version

```python
square = lambda x: x * x

print(square(5))
```

Output

```
25
```

---

## Lambda Example with Filter

Suppose we have tea types:

```python
chai_types = ["light chai", "kadak chai", "ginger tea", "kadak chai"]
```

We want only **kadak chai**.

---

### Using lambda with filter

```python
strong_chai = list(
    filter(
        lambda chai: chai == "kadak chai",
        chai_types
    )
)

print(strong_chai)
```

Output

```
['kadak chai', 'kadak chai']
```

---

### How it works

`filter()` syntax

```
filter(function, iterable)
```

So here:

```
function → lambda chai: chai == "kadak chai"
iterable → chai_types
```

The filter:

1. Checks each element
2. Keeps elements where condition = **True**

---

### Example 2 (Exclude kadak chai)

```python
normal_chai = list(
    filter(
        lambda chai: chai != "kadak chai",
        chai_types
    )
)

print(normal_chai)
```

Output

```
['light chai', 'ginger tea']
```

---

## Important Points to Remember

### Pure Function

✔ Uses only input
✔ No global variables
✔ No side effects

---

### Impure Function

❌ Modifies global variables
❌ Not recommended

---

### Recursive Function

✔ Function calls itself
✔ Must have a **base condition**

Structure

```
if base_case:
    return

recursive_call()
```

---

### Lambda Function

✔ Anonymous function
✔ One-line function
✔ Mostly used with:

* `map()`
* `filter()`
* `sorted()`

Syntax

```
lambda parameters : expression
```

Example

```
lambda x: x * 2
```

---

## Quick Comparison

| Function Type      | Key Idea                 |
| ------------------ | ------------------------ |
| Pure Function      | No external state        |
| Impure Function    | Modifies global state    |
| Recursive Function | Calls itself             |
| Lambda Function    | Small anonymous function |

---

✅ **Interview Tip**

Many companies prefer **pure functions** because they make:

* debugging easier
* testing easier
* code predictable

---

## 44. Documenting your Functions and Built-in Functions (09:24)

- [Built-in Functions](https://docs.python.org/3/library/functions.html)

## Python Built-in Functions & Docstrings (Notes)

Python already provides many **built-in functions**, so we don't always need to write everything ourselves.

Examples of built-in functions:

* `print()`
* `len()`
* `type()`
* `min()`
* `max()`
* `filter()`
* `zip()`
* `sum()`
* `help()`

These functions are **always available in Python** without importing anything.

---

## 1. Built-in Functions

### Definition

**Built-in functions** are functions that are **already provided by Python**.

You can use them directly.

### Example

```python
numbers = [5, 2, 8, 1]

print(len(numbers))   # length
print(max(numbers))   # maximum value
print(min(numbers))   # minimum value
```

Output

```
4
8
1
```

### Common Built-in Functions

| Function   | Purpose            |
| ---------- | ------------------ |
| `len()`    | Length of object   |
| `type()`   | Type of variable   |
| `max()`    | Largest value      |
| `min()`    | Smallest value     |
| `sum()`    | Sum of numbers     |
| `filter()` | Filter elements    |
| `zip()`    | Combine iterables  |
| `help()`   | Show documentation |

---

## 2. Default Parameters in Functions

You can define **default values for parameters**.

If the user doesn't provide a value, Python uses the default.

### Example

```python
def chai_flavor(flavor="masala"):
    return flavor
```

Usage

```python
print(chai_flavor())
print(chai_flavor("ginger"))
```

Output

```
masala
ginger
```

### Key Idea

If no argument is passed → default value is used.

---

## 3. Docstrings (Function Documentation)

### Definition

A **docstring** is a string written at the **top of a function** that explains what the function does.

Docstrings use **triple quotes**.

```
""" documentation """
```

---

### Example

```python
def chai_flavor(flavor="masala"):
    """
    Returns the flavor of chai
    """
    return flavor
```

---

### Accessing Docstring

You can access the docstring using:

```
function.__doc__
```

Example:

```python
print(chai_flavor.__doc__)
```

Output

```
Returns the flavor of chai
```

---

### Important Rule

Docstring **must be the first line inside the function**.

❌ Wrong

```python
def test():
    x = 5
    """This will not work"""
```

✔ Correct

```python
def test():
    """This works"""
    x = 5
```

---

## 4. Dunder Methods

### Definition

**Dunder** means **Double UnderScore**.

Example format:

```
__something__
```

Examples:

* `__doc__`
* `__name__`
* `__init__`
* `__str__`

They are **special built-in attributes in Python**.

---

### Example 1 — `__doc__`

```python
def chai_flavor():
    """Returns chai flavor"""
    return "masala"

print(chai_flavor.__doc__)
```

Output

```
Returns chai flavor
```

---

### Example 2 — `__name__`

```python
def chai_flavor():
    return "masala"

print(chai_flavor.__name__)
```

Output

```
chai_flavor
```

### Why it is useful

Helpful for:

* debugging
* logging
* introspection

---

## 5. help() Function

### Definition

`help()` shows **documentation for any function, object, or module**.

### Example

```python
help(len)
```

Output shows:

* description
* parameters
* usage

You can also do:

```python
help(print)
help(list)
help(str)
```

Exit help mode by pressing **q**.

---

## 6. Writing Good Function Documentation

In large projects, many developers use your function.
So it's good practice to **write documentation inside the function**.

---

### Example: Properly Documented Function

```python
def generate_bill(chai=0, samosa=0):
    """
    Calculate total bill for chai and samosa.

    Parameters:
    chai : number of chai cups (10 rupees each)
    samosa : number of samosas (15 rupees each)

    Returns:
    total amount and a thank you message
    """

    total = chai * 10 + samosa * 15

    return total, "Thank you for visiting!"
```

Usage

```python
bill = generate_bill(2, 3)

print(bill)
```

Output

```
(65, 'Thank you for visiting!')
```

---

## 7. Why Documentation is Important

Good documentation helps:

✔ Other developers understand your code
✔ Easy debugging
✔ Code becomes maintainable
✔ Professional coding practice

Large companies **require docstrings in production code**.

---

## Key Takeaways (Important)

### Python Built-ins

* Python provides many built-in functions.
* No need to define them yourself.

Examples:

```
len(), max(), min(), sum(), filter(), zip(), type()
```

---

### Default Parameters

```
def func(param="default"):
```

Used when no argument is passed.

---

### Docstrings

Used for **function documentation**.

```
"""
Function explanation
"""
```

Access using:

```
function.__doc__
```

---

### Dunder Attributes

Double underscore methods.

Examples:

```
__doc__
__name__
```

---

### help() Function

Used to view **documentation of functions**.

```
help(function_name)
```

---

## Simple Visual Summary

```
Python Built-ins
        │
        ├── Built-in Functions
        │     len(), max(), min()
        │
        ├── Default Parameters
        │     def func(x=10)
        │
        ├── Docstrings
        │     """function description"""
        │
        ├── Dunder Methods
        │     __doc__, __name__
        │
        └── help()
              help(len)
```

---

## 44. Python Imports, Modules and Init File (14:41)

## Python Imports (Complete Notes)

In Python, **imports allow us to use code written in other files or libraries**.

Instead of rewriting the same functions again and again, we **reuse them by importing**.

Example scenario:

You have a file:

```
masala_chai.py
```

It contains chai-making functions.

Another file:

```
new_branch.py
```

Instead of rewriting the same code, you **import it**.

---

## 1. Basic Import

### Concept

Import the **entire module (file)**.

### Syntax

```python
import module_name
```

### Example

File: `masala_chai.py`

```python
def brew():
    return "Masala chai is ready"
```

File: `new_branch.py`

```python
import masala_chai

print(masala_chai.brew())
```

Output

```
Masala chai is ready
```

### How it works

* Python imports the **whole file**
* You access functions using **dot notation**

```
module.function()
```

---

## 2. Import Specific Functions (Named Import)

Sometimes we don't want the whole module.

We only import **specific functions**.

### Syntax

```python
from module_name import function_name
```

### Example

```python
from masala_chai import brew

print(brew())
```

Output

```
Masala chai is ready
```

### Advantage

You don't need to write:

```
module.function()
```

Just call the function directly.

---

## 3. Import Multiple Functions

You can import **multiple functions** from a module.

### Example

```python
from masala_chai import brew, prepare
```

Then use them directly:

```python
brew()
prepare()
```

---

## 4. Import with Alias (Rename Function)

Sometimes you want to **rename the imported function**.

### Syntax

```python
from module import function as new_name
```

### Example

```python
from masala_chai import brew as start_brewing

print(start_brewing())
```

Output

```
Masala chai is ready
```

### Why use alias?

* Avoid name conflicts
* Shorter names
* More readable code

---

## 5. Import Built-in Libraries

Python also has **standard libraries**.

Example: `datetime`

### Example

```python
from datetime import datetime

print(datetime.now())
```

---

Another popular library:

```
requests
```

Used for making API calls.

Example

```python
import requests
```

---

## 6. Import from Folder (Package Import)

Sometimes Python files are inside **folders**.

Example project structure:

```
chai_business/
│
├── main.py
│
├── recipes/
│     └── flavors.py
│
└── utils/
      └── discounts.py
```

---

### flavors.py

```python
def elaichi_chai():
    return "Elaichi chai is ready"

def ginger_chai():
    return "Ginger chai is ready"
```

---

### Import in main.py

```python
from recipes import flavors

print(flavors.ginger_chai())
```

Output

```
Ginger chai is ready
```

---

## 7. Import Specific Function from Folder

Instead of importing the whole module:

```python
from recipes.flavors import ginger_chai

print(ginger_chai())
```

---

## 8. Relative Imports

Relative imports are used when modules are **inside the same package**.

Example syntax:

```
.
```

means **current directory**

```
..
```

means **parent directory**

Example:

```python
from .flavors import ginger_chai
```

or

```python
from ..utils import discounts
```

Relative imports are **commonly used in large frameworks** like:

* Django
* FastAPI

---

## 9. Avoid Using `*` Import

Bad practice:

```python
from masala_chai import *
```

### Why avoid this?

Problems:

* Hard to know what was imported
* Can cause name conflicts
* Makes debugging difficult

Always prefer:

```
from module import specific_function
```

---

## 10. `__init__.py` File

You may see a file like:

```
__init__.py
```

Inside folders.

Example:

```
recipes/
    __init__.py
    flavors.py
```

### Purpose

Historically, it **converted a folder into a Python package**.

Example:

```
recipes → becomes Python package
```

---

### Important Update

Since **Python 3.3**, this file is **not required anymore**.

Python automatically treats folders as packages.

However:

* Many projects **still include it**
* Frameworks still expect it sometimes

So you will still see it in many repositories.

---

## 11. Common Import Patterns

### Import whole module

```python
import math

print(math.sqrt(16))
```

---

### Import specific function

```python
from math import sqrt

print(sqrt(16))
```

---

### Import with alias

```python
import numpy as np
```

---

### Import multiple functions

```python
from math import sqrt, pow
```

---

## Quick Visual Summary

```
Python Imports
      │
      ├── import module
      │       import math
      │
      ├── from module import function
      │       from math import sqrt
      │
      ├── alias import
      │       import numpy as np
      │
      ├── package import
      │       from recipes.flavors import ginger_chai
      │
      ├── relative import
      │       from .flavors import ginger_chai
      │
      └── avoid
              from module import *
```

---

## Important Points to Remember

✔ Imports help **reuse code**
✔ Python files are called **modules**
✔ Folders containing modules are **packages**
✔ Avoid `import *`
✔ Use **specific imports** for clean code
✔ `__init__.py` is optional in Python 3.3+

---

## Sec 7 - Comprehensions in Python

## 45. What are Comprehensions in python (06:39)

## Python Comprehensions (Notes)

## 1. What are Comprehensions?

**Comprehensions** are a **short and concise way to create collections** (like lists, sets, dictionaries, or generators) in **one line of code**.

Instead of writing multiple lines using loops, we can write **cleaner and shorter code**.

### Basic Idea

Normal loop:

```python
numbers = [1, 2, 3, 4]

squares = []
for n in numbers:
    squares.append(n * n)

print(squares)
```

Output

```
[1, 4, 9, 16]
```

Using **comprehension**

```python
numbers = [1, 2, 3, 4]

squares = [n * n for n in numbers]

print(squares)
```

Output

```
[1, 4, 9, 16]
```

Same result, but **shorter and cleaner code**.

---

## 2. Why Use Comprehensions?

Even though loops can do the same work, comprehensions are used because they:

### ✔ Make code shorter

### ✔ Make code cleaner

### ✔ Often run faster

### ✔ Use less memory in some cases

However:

* They may feel **confusing at first**
* But once you practice them, they become **very powerful**

---

## 3. Where Comprehensions Are Used in Real Life

Comprehensions are commonly used in **production Python code**.

### 1. Filtering Items

Selecting only certain items from a collection.

Example: Get only even numbers.

Loop version:

```python
numbers = [1,2,3,4,5,6]

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)
```

Comprehension version:

```python
numbers = [1,2,3,4,5,6]

evens = [n for n in numbers if n % 2 == 0]

print(evens)
```

Output

```
[2, 4, 6]
```

---

### 2. Transforming Data

Changing or modifying values.

Example: Convert prices from INR to USD.

```python
prices_inr = [100, 200, 300]

prices_usd = [price / 93 for price in prices_inr]

print(prices_usd)
```

Output

```
[1.20, 2.40, 3.61]
```

---

### 3. Creating a New Collection

Creating a new data structure from another.

Example:

```python
tea_names = ["masala", "ginger", "green"]

upper_case = [tea.upper() for tea in tea_names]

print(upper_case)
```

Output

```
['MASALA', 'GINGER', 'GREEN']
```

---

### 4. Flattening Nested Structures

Flattening nested lists.

Example:

```python
nested = [[1,2], [3,4], [5,6]]

flat = [num for sublist in nested for num in sublist]

print(flat)
```

Output

```
[1,2,3,4,5,6]
```

---

## 4. General Syntax of Comprehension

Basic format:

```python
[expression for item in iterable]
```

Example:

```python
[n * 2 for n in range(5)]
```

Output

```
[0,2,4,6,8]
```

---

### With condition

```python
[expression for item in iterable if condition]
```

Example:

```python
[n for n in range(10) if n > 5]
```

Output

```
[6,7,8,9]
```

---

## 5. Types of Comprehensions

Python has **four types of comprehensions**.

---

## 1. List Comprehension

Creates a **list**.

Example:

```python
numbers = [1,2,3,4]

squares = [n*n for n in numbers]

print(squares)
```

Output

```
[1,4,9,16]
```

---

## 2. Set Comprehension

Creates a **set**.

Example:

```python
numbers = [1,2,2,3,4]

unique_squares = {n*n for n in numbers}

print(unique_squares)
```

Output

```
{1,4,9,16}
```

Duplicates are removed automatically.

---

## 3. Dictionary Comprehension

Creates a **dictionary**.

Example:

```python
numbers = [1,2,3]

square_dict = {n: n*n for n in numbers}

print(square_dict)
```

Output

```
{1:1, 2:4, 3:9}
```

---

## 4. Generator Comprehension

Creates a **generator object** instead of a list.

Example:

```python
numbers = (n*n for n in range(5))

print(numbers)
```

Output

```
<generator object ...>
```

To see values:

```python
for n in numbers:
    print(n)
```

Output

```
0
1
4
9
16
```

Generators are **memory efficient** because values are created **one at a time**.

---

## 6. Key Advantages of Comprehensions

### Cleaner Code

Example:

```python
[n*n for n in numbers]
```

Instead of:

```python
for n in numbers:
    squares.append(n*n)
```

---

### Faster Execution

Sometimes faster than loops because Python optimizes them internally.

---

### Functional Programming Style

They encourage writing **compact logic**.

---

## Important Points to Remember

### 1️⃣ Comprehensions replace loops for simple tasks.

### 2️⃣ They make code **shorter and cleaner**.

### 3️⃣ They are widely used in **production Python code**.

### 4️⃣ Beginners often find them confusing at first.

### 5️⃣ Practice is required to master them.

---

## Simple Mental Model

Think of comprehension like **English sentence logic**.

Example:

```python
[n for n in numbers if n > 5]
```

Meaning:

```
Take n
for each n in numbers
if n is greater than 5
```

---

## Quick Visual Summary

```
Comprehensions
      │
      ├── List Comprehension
      │      [x for x in iterable]
      │
      ├── Set Comprehension
      │      {x for x in iterable}
      │
      ├── Dictionary Comprehension
      │      {k:v for k,v in iterable}
      │
      └── Generator Comprehension
             (x for x in iterable)
```

---

## 46. List Comprehensions in python (08:33)

## Python List Comprehension (Notes)

## 1. What is List Comprehension?

**List comprehension** is a **short and clean way to create lists in Python** using a **single line of code**.

Instead of writing a **for loop with multiple lines**, we can do the same thing in **one line**.

It is commonly used in **real-world Python projects**.

---

## 2. Basic Syntax of List Comprehension

General structure:

```python
[expression for item in iterable if condition]
```

### Meaning of each part

| Part       | Meaning                                  |
| ---------- | ---------------------------------------- |
| expression | What you want to add to the new list     |
| item       | Each element from the iterable           |
| iterable   | A collection (list, tuple, string, etc.) |
| condition  | Optional filter                          |

---

## 3. Example Without Comprehension (Using Loop)

Suppose we want to collect **iced teas** from a menu.

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger tea"
]

iced_teas = []

for tea in menu:
    if "iced" in tea:
        iced_teas.append(tea)

print(iced_teas)
```

Output

```
['iced lemon tea', 'iced peach tea']
```

---

## 4. Same Example Using List Comprehension

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger tea"
]

iced_teas = [tea for tea in menu if "iced" in tea]

print(iced_teas)
```

Output

```
['iced lemon tea', 'iced peach tea']
```

This is **shorter and cleaner**.

---

## 5. Understanding the Syntax Step-by-Step

Example:

```python
iced_teas = [tea for tea in menu if "iced" in tea]
```

Breakdown:

### Expression

```
tea
```

This is the value that will be added to the new list.

---

### Loop

```
for tea in menu
```

This loops through every item in the list.

---

### Condition

```
if "iced" in tea
```

Only items containing `"iced"` are selected.

---

## 6. Important Concept: Variable Names Must Match

Example:

❌ Incorrect code

```python
iced_teas = [tea for my_tea in menu if "iced" in tea]
```

Error occurs because `tea` was not defined.

---

✔ Correct code

```python
iced_teas = [my_tea for my_tea in menu if "iced" in my_tea]
```

The **variable name must match everywhere**.

---

## 7. Using Other Conditions

You can filter using **any condition**.

Example: Select teas whose name length is greater than 12.

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger tea"
]

result = [tea for tea in menu if len(tea) > 12]

print(result)
```

Output

```
['iced lemon tea', 'iced peach tea']
```

---

## 8. Comprehension Without Condition

Condition is optional.

Example:

Convert all tea names to uppercase.

```python
menu = ["masala chai", "green tea", "ginger tea"]

upper_menu = [tea.upper() for tea in menu]

print(upper_menu)
```

Output

```
['MASALA CHAI', 'GREEN TEA', 'GINGER TEA']
```

---

## 9. Real Use Cases

List comprehensions are commonly used for:

### 1. Filtering data

Example:

```python
numbers = [1,2,3,4,5,6]

evens = [n for n in numbers if n % 2 == 0]

print(evens)
```

Output

```
[2,4,6]
```

---

### 2. Transforming data

Example:

```python
numbers = [1,2,3,4]

squares = [n*n for n in numbers]

print(squares)
```

Output

```
[1,4,9,16]
```

---

### 3. Creating new lists

Example:

```python
names = ["ram", "shyam", "rahul"]

capital_names = [name.capitalize() for name in names]

print(capital_names)
```

Output

```
['Ram', 'Shyam', 'Rahul']
```

---

## 10. Key Advantages

### Cleaner Code

Less lines compared to loops.

---

### Easier Data Transformation

Very useful when working with **lists and data processing**.

---

### More Pythonic

Python developers prefer this style.

---

## Important Points to Remember

✔ List comprehension uses **square brackets**
✔ Syntax follows **expression → loop → condition**
✔ Condition is **optional**
✔ Works with any **iterable** (list, tuple, string, etc.)
✔ Variable names must be **consistent**

---

## Quick Visual Summary

```
List Comprehension Structure

[expression for item in iterable if condition]
        │        │        │
        │        │        └── filter items
        │        └────────── loop through data
        └────────────────── value added to list
```

---

## 47. Set Comprehensions in python (12:00)

## Python Set Comprehension (Notes)

## 1. What is Set Comprehension?

**Set comprehension** is a **short way to create sets in Python using one line of code**.

It works **almost exactly like list comprehension**, but it creates a **set instead of a list**.

### Key difference

| Comprehension Type | Brackets Used | Result |
| ------------------ | ------------- | ------ |
| List Comprehension | `[]`          | List   |
| Set Comprehension  | `{}`          | Set    |

---

## 2. Syntax of Set Comprehension

General syntax:

```python
{expression for item in iterable if condition}
```

### Explanation

| Part       | Meaning                                    |
| ---------- | ------------------------------------------ |
| expression | value added to set                         |
| item       | variable representing each element         |
| iterable   | collection (list, tuple, dictionary, etc.) |
| condition  | optional filter                            |

---

## 3. Basic Example – Finding Unique Items

Sets automatically **remove duplicate values**.

Example list with duplicates:

```python
favorite_chai = [
    "masala chai",
    "green tea",
    "masala chai",
    "lemon tea",
    "green tea",
    "lichi chai"
]
```

### Using Set Comprehension

```python
unique_chai = {chai for chai in favorite_chai}

print(unique_chai)
```

Output (duplicates removed)

```python
{'masala chai', 'green tea', 'lemon tea', 'lichi chai'}
```

### Why it works

Sets **only store unique values**, so duplicates disappear automatically.

---

## 4. Using Conditions in Set Comprehension

You can add filters.

Example: Only keep chai names longer than 8 characters.

```python
unique_chai = {chai for chai in favorite_chai if len(chai) > 8}

print(unique_chai)
```

Example output

```python
{'masala chai', 'green tea', 'lemon tea'}
```

---

## 5. Important Concept – Expression

In comprehension syntax:

```python
{expression for item in iterable}
```

The **expression determines what gets added to the result**.

Example:

```python
numbers = [1,2,3,4]

squares = {n*n for n in numbers}

print(squares)
```

Output

```python
{1,4,9,16}
```

The expression is:

```python
n*n
```

---

## 6. Complex Example (Nested Iteration)

Sometimes the iterable contains **nested data structures**.

Example dictionary with chai recipes.

```python
recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}
```

Goal: **Find all unique spices used in recipes.**

---

### Step-by-step logic

1. Loop through recipe values
2. Loop through ingredients inside each recipe
3. Collect unique spices

---

### Set Comprehension Solution

```python
unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}

print(unique_spices)
```

Output

```python
{'ginger', 'cardamom', 'clove', 'black pepper', 'milk'}
```

---

## 7. Understanding Nested Loops in Comprehension

This comprehension:

```python
{spice for ingredients in recipes.values() for spice in ingredients}
```

Equivalent loop version:

```python
unique_spices = set()

for ingredients in recipes.values():
    for spice in ingredients:
        unique_spices.add(spice)

print(unique_spices)
```

Both produce the same result.

---

## 8. Key Learning from Complex Example

Important rule:

> The **final value produced by the loop** is written in the **expression part**.

Example:

```python
{spice for ingredients in recipes.values() for spice in ingredients}
```

The final value is **spice**, so that becomes the expression.

---

## 9. Strategy to Write Comprehensions Easily

A useful trick:

### Step 1 — Write loops first

```python
for ingredients in recipes.values():
    for spice in ingredients:
```

### Step 2 — Convert into comprehension

```python
{spice for ingredients in recipes.values() for spice in ingredients}
```

This makes complex comprehensions easier to write.

---

## 10. Advantages of Set Comprehension

### Removes duplicates automatically

Sets guarantee **unique values**.

---

### Shorter code

Instead of multiple loops.

---

### Cleaner data processing

Useful for **filtering and extracting unique values**.

---

## Important Points to Remember

✔ Set comprehension uses **curly braces `{}`**
✔ Syntax is **same as list comprehension**
✔ Sets automatically remove **duplicates**
✔ Expression determines **what gets stored**
✔ Nested loops can be written in comprehensions
✔ Complex comprehensions can replace multiple loops

---

## Quick Visual Summary

```
Set Comprehension Structure

{expression for item in iterable if condition}
      │         │          │
      │         │          └─ filter
      │         └─ loop
      └─ value stored in set
```

Example:

```python
{n for n in numbers if n % 2 == 0}
```

Result → set of even numbers.

---

## 48. Dictionary Comprehensions in python (05:37)

## Python Dictionary Comprehension (Notes)

## 1. What is Dictionary Comprehension?

**Dictionary comprehension** is a **short way to create a dictionary using a single line of code**.

Just like **list and set comprehensions**, it helps write **cleaner and shorter Python code**.

---

## 2. Basic Syntax

General syntax:

```python
{key_expression: value_expression for item in iterable}
```

Optional condition:

```python
{key_expression: value_expression for item in iterable if condition}
```

### Explanation

| Part             | Meaning                    |
| ---------------- | -------------------------- |
| key_expression   | Key of the dictionary      |
| value_expression | Value of the dictionary    |
| item             | Each element from iterable |
| iterable         | Collection to loop through |
| condition        | Optional filter            |

---

## 3. Key Idea of Dictionary Comprehension

Dictionary comprehension **must return a key-value pair**.

Example:

```python
{key: value for item in iterable}
```

If you only return a **single value**, Python will treat it as a **set comprehension**.

So dictionary comprehension always uses:

```python
key: value
```

---

## 4. Example – Converting Tea Prices from INR to USD

Suppose we have a dictionary of tea prices in **Indian Rupees (INR)**.

```python
tea_prices_inr = {
    "masala chai": 40,
    "green tea": 50,
    "lemon tea": 200
}
```

Goal: Convert prices into **USD**.

Assume:

```
1 USD ≈ 80 INR
```

---

## 5. Dictionary Comprehension Solution

```python
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}

print(tea_prices_usd)
```

Output

```python
{
 'masala chai': 0.5,
 'green tea': 0.625,
 'lemon tea': 2.5
}
```

---

## 6. Understanding the Code

### Step 1 – Loop through dictionary

```python
for tea, price in tea_prices_inr.items()
```

`.items()` returns both:

* key
* value

Example output of `.items()`:

```
("masala chai", 40)
("green tea", 50)
("lemon tea", 200)
```

---

### Step 2 – Expression

```python
tea: price / 80
```

This creates the new dictionary entry.

Example result:

```
"masala chai": 0.5
```

---

## 7. Same Code Using Normal Loop

Dictionary comprehension replaces this longer code:

```python
tea_prices_usd = {}

for tea, price in tea_prices_inr.items():
    tea_prices_usd[tea] = price / 80

print(tea_prices_usd)
```

Comprehension version is **shorter and cleaner**.

---

## 8. Using Conditions in Dictionary Comprehension

Example: Only convert teas that cost more than 50 INR.

```python
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
    if price > 50
}

print(tea_prices_usd)
```

Output

```python
{'lemon tea': 2.5}
```

---

## 9. Another Example – Modify Values

Example: Add tax to prices.

```python
tea_prices = {
    "masala chai": 40,
    "green tea": 50,
    "lemon tea": 200
}

new_prices = {tea: price * 1.1 for tea, price in tea_prices.items()}

print(new_prices)
```

Output

```
{
 'masala chai': 44.0,
 'green tea': 55.0,
 'lemon tea': 220.0
}
```

---

## 10. Transform Keys Example

Example: Convert keys to uppercase.

```python
tea_prices = {
    "masala chai": 40,
    "green tea": 50
}

upper_keys = {tea.upper(): price for tea, price in tea_prices.items()}

print(upper_keys)
```

Output

```
{'MASALA CHAI': 40, 'GREEN TEA': 50}
```

---

## 11. Important Dictionary Methods

### `.items()`

Returns **both key and value**.

```python
dict.items()
```

Example:

```python
for key, value in dictionary.items():
```

---

### `.keys()`

Returns only keys.

```python
dictionary.keys()
```

---

### `.values()`

Returns only values.

```python
dictionary.values()
```

---

## 12. Key Advantages of Dictionary Comprehension

### Cleaner Code

Less code compared to loops.

---

### Easy Data Transformation

Very useful when **processing APIs or datasets**.

---

### Faster to Write

Python developers prefer this style.

---

## Important Points to Remember

✔ Dictionary comprehension uses **curly braces `{}`**
✔ Expression must contain **key:value pair**
✔ `.items()` is commonly used to loop through dictionaries
✔ Conditions can be added
✔ Helps transform keys or values easily

---

## Quick Visual Summary

```
Dictionary Comprehension

{key: value for key, value in iterable if condition}
       │        │          │
       │        │          └ filter
       │        └ loop
       └ new dictionary entry
```

Example:

```python
{tea: price/80 for tea, price in tea_prices.items()}
```

---

## 49. Generator Comprehensions for Memory Optimizations (07:07)

## 1. What is Generator Comprehension?

A **generator comprehension** is a way to create values **one at a time instead of storing everything in memory at once**.

It is mainly used to **save memory**.

Instead of building a **full list**, Python **generates values only when needed**.

This is useful when working with **large datasets (millions of items)**.

---

## 2. Why Generators are Important

Normal Python programs often run on machines with lots of RAM (64GB, 128GB etc.), so many programmers ignore memory efficiency.

But a **good software engineer writes memory-efficient programs**.

Generators help because:

* They **do not store the whole list in memory**
* They **produce values one by one**
* They are useful when dealing with **large data streams**

---

## 3. Syntax of Generator Comprehension

Generator comprehension looks almost the same as **list comprehension**.

The only difference:

* **List comprehension → uses `[]`**
* **Generator comprehension → uses `()`**

### List Comprehension

```python
[x for x in range(5)]
```

### Generator Comprehension

```python
(x for x in range(5))
```

---

## 4. Difference Between List and Generator

## List Comprehension

Creates the **entire list in memory immediately**.

Example:

```python
numbers = [x for x in range(5)]
print(numbers)
```

Output

```
[0, 1, 2, 3, 4]
```

Memory behavior:

```
All values stored in memory at once
```

---

## Generator Comprehension

Creates a **generator object** and produces values **one by one**.

Example:

```python
numbers = (x for x in range(5))
print(numbers)
```

Output

```
<generator object ...>
```

This means Python **has not generated the values yet**.

---

## 5. Generators Work Like a Stream

Generators behave like a **stream of data**.

Instead of giving everything together:

```
[1,2,3,4,5]
```

They give values **one at a time when requested**.

```
1 → 2 → 3 → 4 → 5
```

This makes them **memory efficient**.

---

## 6. Consuming a Generator

Since generators produce values gradually, they must be **consumed** using loops or functions like:

* `sum()`
* `list()`
* `for loop`

Example:

```python
numbers = (x for x in range(5))

for num in numbers:
    print(num)
```

Output

```
0
1
2
3
4
```

---

## 7. Example From the Tutorial (Daily Sales)

Suppose we have daily sales values.

```python
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
```

We want to **calculate total sales where value > 5**.

---

## 8. Using List Comprehension (Memory Heavy)

```python
sales = [sale for sale in daily_sales if sale > 5]

total = sum(sales)

print(total)
```

Steps:

1. Create full list
2. Store it in memory
3. Then sum it

---

## 9. Using Generator Comprehension (Memory Efficient)

```python
total = sum(sale for sale in daily_sales if sale > 5)

print(total)
```

What happens here:

1. Values are generated **one by one**
2. `sum()` consumes them immediately
3. No full list stored in memory

This is **more memory efficient**.

---

## 10. Example to See the Difference

### List comprehension

```python
nums = [x*x for x in range(10)]
print(nums)
```

Output

```
[0,1,4,9,16,25,36,49,64,81]
```

---

### Generator comprehension

```python
nums = (x*x for x in range(10))
print(nums)
```

Output

```
<generator object ...>
```

---

## 11. Converting Generator to List

If needed, you can convert a generator to a list.

```python
nums = (x*x for x in range(5))

print(list(nums))
```

Output

```
[0,1,4,9,16]
```

---

## 12. Important Functions That Work Well With Generators

Generators are commonly used with built-in functions:

### sum()

```python
total = sum(x for x in range(10))
```

---

### max()

```python
maximum = max(x for x in range(10))
```

---

### min()

```python
minimum = min(x for x in range(10))
```

---

## 13. Key Points to Remember

1. **Generators save memory**
2. They **produce values one at a time**
3. Used when working with **large datasets**
4. Syntax uses **parentheses `()`**
5. List comprehension uses **square brackets `[]`**
6. Generators return a **generator object**
7. They must be **consumed** using loops or functions
8. Often used with functions like **sum(), max(), min()**

---

## 14. Quick Comparison Table

| Feature      | List Comprehension | Generator        |
| ------------ | ------------------ | ---------------- |
| Syntax       | `[ ]`              | `( )`            |
| Memory usage | High               | Low              |
| Execution    | Immediate          | Lazy (on demand) |
| Output       | List               | Generator object |

---

✅ **Simple Summary**

* **List comprehension** builds the whole list in memory.
* **Generator comprehension** generates values **one at a time**.
* Generators are **more memory efficient**.
* Best used when handling **large data streams**.

---

## Sec 8 - Generators and Decorators in python

## 53. Generators with Yield and Next methods (10:34)

## 1. What Are Generators in Python?

A **generator** is a special type of function that **produces values one at a time instead of returning everything at once**.

Normal functions return the result **immediately**, but generators **pause and resume execution**.

Generators mainly help to:

* **Save memory**
* **Generate values only when needed**
* Work with **large data efficiently**

---

## 2. Key Concepts of Generators

The tutorial highlights **three important ideas**:

### 1️⃣ Memory Efficient

Generators **do not store all values in memory**.

They produce values **one by one**.

---

### 2️⃣ Results Not Immediate

Generators **do not compute everything instantly**.

They produce values **only when requested**.

---

### 3️⃣ Lazy Evaluation

This means **calculation happens only when required**.

Example:

Instead of creating:

```
[1,2,3,4,5]
```

The generator produces:

```
1 → 2 → 3 → 4 → 5
```

only when needed.

---

## 3. Important Keyword: `yield`

Generators use the keyword:

```
yield
```

instead of:

```
return
```

### Difference

| return            | yield                      |
| ----------------- | -------------------------- |
| Ends the function | Pauses the function        |
| Returns one value | Produces values one by one |
| Function stops    | Function resumes later     |

---

## 4. Basic Generator Example

### Generator Function

```python
def serve_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Elaichi Chai"
```

This function does **not return all values together**.

It generates them **one by one**.

---

## 5. Using a Generator With a Loop

The easiest way to use generators is with a **for loop**.

```python
def serve_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)
```

Output:

```
Masala Chai
Ginger Chai
Elaichi Chai
```

---

## 6. What Happens Internally?

When we write:

```python
stall = serve_chai()
```

Python **does NOT run the function immediately**.

Instead it creates a **generator object**.

Example:

```python
print(stall)
```

Output:

```
<generator object serve_chai at ...>
```

This means:

```
stall only holds a reference to the generator
```

---

## 7. Getting Values Using `next()`

Generators can also be controlled manually using **next()**.

Example:

```python
def get_chai():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai()

print(next(chai))
print(next(chai))
print(next(chai))
```

Output:

```
Cup 1
Cup 2
Cup 3
```

---

## 8. How `yield` Works Internally

When `next()` is called:

1️⃣ Generator starts executing
2️⃣ Runs until it finds `yield`
3️⃣ Returns the value
4️⃣ Pauses execution

Next time `next()` runs, it **continues from the same point**.

Example flow:

```
yield "Cup 1" → pause
yield "Cup 2" → pause
yield "Cup 3" → pause
```

---

## 9. StopIteration Error

If we call `next()` more times than available values:

```python
print(next(chai))
```

Python gives:

```
StopIteration
```

because the generator **has no more values to produce**.

---

## 10. Normal Function vs Generator

### Normal Function

```python
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]
```

Usage:

```python
chai = get_chai_list()
print(chai)
```

Output:

```
['Cup 1', 'Cup 2', 'Cup 3']
```

Everything is **stored in memory at once**.

---

### Generator Function

```python
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
```

Usage:

```python
chai = get_chai_gen()

for cup in chai:
    print(cup)
```

Values are **generated one at a time**.

---

## 11. Why Generators Are Useful

Generators are useful when:

### Large datasets

Example:

```
millions of records
```

Generators prevent **memory overload**.

---

### Streaming data

Example:

* reading large files
* processing logs
* API streaming

---

### Backend frameworks

Generators are used a lot in:

* **FastAPI**
* database connections
* streaming responses

---

## 12. Important Points to Remember

1️⃣ Generators are **special functions**
2️⃣ They use **yield instead of return**
3️⃣ `yield` **pauses the function**
4️⃣ Execution resumes when **next() is called**
5️⃣ Generators **produce one value at a time**
6️⃣ They are **memory efficient**
7️⃣ If values finish → **StopIteration error**
8️⃣ Often used with **for loops**

---

## 13. Quick Visual Difference

### Normal Function

```
Function runs completely
↓
Returns full result
↓
Memory used for entire data
```

---

### Generator

```
Function starts
↓
yield value
↓
pause
↓
resume when next() called
```

---

✅ **Simple Summary**

Generators are functions that:

* generate **values one at a time**
* use the **yield keyword**
* **pause and resume execution**
* help **save memory**
* are useful for **large data processing**

---

## 54. Infinite Generators in python (04:44)

## 1. What is an Infinite Generator?

An **infinite generator** is a generator that can produce **unlimited values**.

It does **not stop automatically** and keeps generating values forever unless we control it.

These generators usually use:

```python
while True:
```

Because of this, they **never stop unless we manually stop them**.

---

## 2. Why Infinite Generators Are Used

Infinite generators are useful in situations like:

### 1️⃣ Real-time systems

Example:

* live data streams
* stock market updates
* sensor data

### 2️⃣ Logging systems

Example:

* continuously reading logs

### 3️⃣ AI / Machine Learning pipelines

Example:

* streaming data to models

### 4️⃣ Event streams

Example:

* user activity tracking

---

## 3. Important Warning

Infinite generators should be used **carefully**.

If not controlled properly they can:

* run forever
* consume CPU
* create unwanted loops

But since generators **produce values one at a time**, they are still **memory efficient**.

---

## 4. Basic Infinite Generator Example

Example generator:

```python
def infinite_chai():
    count = 1
    
    while True:
        yield f"Refill {count}"
        count += 1
```

Explanation:

* `while True` → infinite loop
* `yield` → generates values one at a time
* `count` → tracks number of refills

---

## 5. Using the Infinite Generator

Create a generator object:

```python
refill = infinite_chai()
```

To get values:

```python
print(next(refill))
print(next(refill))
print(next(refill))
```

Output:

```
Refill 1
Refill 2
Refill 3
```

The generator **never ends**.

---

## 6. Controlling Infinite Generators

Because they are infinite, we must **limit them using loops**.

Example:

```python
refill = infinite_chai()

for _ in range(3):
    print(next(refill))
```

Output

```
Refill 1
Refill 2
Refill 3
```

Here `_` means **we don't care about the loop variable**.

It is just used to repeat the loop.

---

## 7. Why `_` Is Used

Sometimes we don't need the loop variable.

Instead of writing:

```python
for i in range(3):
```

We write:

```python
for _ in range(3):
```

This tells Python:

```text
This variable is intentionally unused
```

---

## 8. Multiple Generator Instances

One powerful feature of generators is that **each generator keeps its own state**.

Example:

```python
user1 = infinite_chai()
user2 = infinite_chai()
```

Now both users have **separate refill counters**.

---

## 9. Example with Two Users

```python
def infinite_chai():
    count = 1
    while True:
        yield f"Refill {count}"
        count += 1


user1 = infinite_chai()
user2 = infinite_chai()

for _ in range(3):
    print(next(user1))

for _ in range(6):
    print(next(user2))
```

Output

```
Refill 1
Refill 2
Refill 3

Refill 1
Refill 2
Refill 3
Refill 4
Refill 5
Refill 6
```

Explanation:

* `user1` has its own counter
* `user2` has a separate counter
* Both use the **same generator function**

---

## 10. How Infinite Generators Work Internally

Flow:

```
Generator starts
↓
yield value
↓
pause
↓
next() called
↓
resume execution
↓
yield next value
```

Because of `while True`, this continues forever.

---

## 11. Real-World Example (Log Stream)

Example of streaming logs:

```python
def log_stream():
    count = 1
    while True:
        yield f"Log entry {count}"
        count += 1
```

Usage:

```python
logs = log_stream()

for _ in range(5):
    print(next(logs))
```

Output

```
Log entry 1
Log entry 2
Log entry 3
Log entry 4
Log entry 5
```

---

## 12. Important Points to Remember

1️⃣ Infinite generators produce **unlimited values**
2️⃣ Usually implemented with **`while True` loop**
3️⃣ They use **`yield` instead of return**
4️⃣ Values are generated **one at a time**
5️⃣ They must be **controlled externally**
6️⃣ Each generator instance **keeps its own state**
7️⃣ Often used in **streams, AI pipelines, logging systems**

---

## 13. Quick Summary

Normal generator:

```
Produces limited values
Stops automatically
```

Example:

```python
yield 1
yield 2
yield 3
```

---

Infinite generator:

```
Produces unlimited values
Runs forever unless controlled
```

Example:

```python
while True:
    yield value
```

---

✅ **Final Simple Explanation**

An **infinite generator** is a generator function that **never stops generating values** because it uses an infinite loop (`while True`).
We control it using loops or `next()` so that it does not run forever.

---

## 54. Send Value to Generators (07:45)

## 1. Idea Behind This Lesson

So far we learned:

* Generators **produce values using `yield`**
* We get values using **`next()`**

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

But Python generators can also **receive values from outside**.

That is done using:

```python
generator.send(value)
```

This means:

```text
Generators can both SEND and RECEIVE data
```

---

## 2. Key Concept

Normally:

```text
Generator → sends data to caller
```

With `send()`:

```text
Caller → sends data to generator
```

So the communication becomes **two-way**.

---

## 3. Important Keywords

### `yield`

* pauses the generator
* returns a value
* waits for the next instruction

### `next()`

* resumes generator execution
* used when no value is sent

### `send(value)`

* resumes generator
* **passes a value into the generator**

---

## 4. Basic Generator with `send()`

Example generator:

```python
def chai_customer():
    print("Welcome!")
    print("What chai would you like?")

    order = yield

    while True:
        print(f"Preparing {order}")
        order = yield
```

---

## 5. How It Works

Create the generator:

```python
stall = chai_customer()
```

Start the generator:

```python
next(stall)
```

Output:

```
Welcome!
What chai would you like?
```

Now the generator **pauses at `yield`** waiting for input.

---

## 6. Sending Data to Generator

Now send a chai order:

```python
stall.send("Masala Chai")
```

Output:

```
Preparing Masala Chai
```

Send another order:

```python
stall.send("Lemon Chai")
```

Output:

```
Preparing Lemon Chai
```

So the generator **keeps receiving new orders**.

---

## 7. Step-by-Step Execution

Generator code:

```python
order = yield
```

Execution flow:

### Step 1

```python
stall = chai_customer()
```

Generator is created but **not executed yet**.

---

### Step 2

```python
next(stall)
```

Runs until first `yield`.

Output:

```
Welcome!
What chai would you like?
```

Now generator pauses at:

```python
order = yield
```

---

### Step 3

```python
stall.send("Masala Chai")
```

The value `"Masala Chai"` becomes:

```python
order = "Masala Chai"
```

Then generator continues.

Output:

```
Preparing Masala Chai
```

---

### Step 4

Generator pauses again at:

```python
order = yield
```

Waiting for the next order.

---

### Step 5

```python
stall.send("Lemon Chai")
```

Output:

```
Preparing Lemon Chai
```

---

## 8. Why Second `yield` is Necessary

This part is important.

Inside the loop:

```python
order = yield
```

This **pauses the generator again**.

If this line is removed:

```python
while True:
    print(f"Preparing {order}")
```

Then the loop becomes:

```text
Infinite loop
```

It keeps printing forever because **nothing pauses the generator**.

---

## 9. Why the Program Went Infinite

Without this line:

```python
order = yield
```

The code becomes:

```python
while True:
    print(order)
```

Which means:

```
print
print
print
print
print
...
```

So the program **never pauses**.

That’s why it runs infinitely.

---

## 10. Why Generators Pause

Generators pause at `yield`.

Example flow:

```
start
↓
yield
↓ pause
↓
send(value)
↓
resume
↓
yield
↓ pause
```

This pause-resume behavior is what makes generators powerful.

---

## 11. Real World Use Cases

This type of generator is used in:

### 1️⃣ Web frameworks

Example:

* streaming responses

### 2️⃣ FastAPI

Used for:

* async processing
* event streams

### 3️⃣ Pipelines

Data pipelines where:

```
input → process → output
```

---

## 12. Simple Example (Calculator Generator)

```python
def calculator():
    result = 0

    while True:
        number = yield result
        result += number
```

Usage:

```python
calc = calculator()

next(calc)

print(calc.send(5))
print(calc.send(10))
print(calc.send(3))
```

Output:

```
5
15
18
```

The generator **keeps receiving numbers and updating the result**.

---

## 13. Important Points to Remember

1️⃣ Generators normally **send values using `yield`**

2️⃣ With `send()` we can **send data into generators**

3️⃣ `next()` is required to **start the generator**

4️⃣ `yield` pauses the generator

5️⃣ `send(value)` resumes generator and **passes value to yield**

6️⃣ Generators allow **two-way communication**

7️⃣ Used in **frameworks, streaming, and pipelines**

---

## 14. Quick Summary

Normal generator:

```python
yield value
```

Caller receives values.

---

Advanced generator:

```python
value = yield
```

Generator **receives values from caller**.

---

### Communication Flow

```
Generator → yield → caller
Caller → send() → generator
```

---

✅ **Final Simple Explanation**

Generators can do more than just produce values.
Using `send()`, they can **receive data from the caller**, making them useful for **interactive systems, pipelines, and frameworks**.

---

## 55. Yield From and Close the Generators (08:55)

This tutorial explains **two more advanced generator features in Python**:

1. **`yield from`** – getting values from another generator
2. **`close()`** – stopping and cleaning up a generator

Below is a **simple summary, important points, and clear code examples**.

---

## 1. Quick Recap of Generators

Generators are functions that **produce values one at a time** using:

```python
yield
```

Instead of returning everything at once.

Example:

```python
def chai_menu():
    yield "Masala Chai"
    yield "Ginger Chai"
```

Usage:

```python
for chai in chai_menu():
    print(chai)
```

Output

```
Masala Chai
Ginger Chai
```

---

## 2. Concept 1: `yield from`

Sometimes a generator **does not produce values itself**.

Instead, it **gets values from another generator**.

Python provides a special syntax for this:

```python
yield from generator_function()
```

This is called **delegation**.

It means:

```
Take values from another generator and yield them here.
```

---

## 3. Example: Multiple Generators

Suppose we have **local chai options**.

```python
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
```

And **imported chai options**.

```python
def imported_chai():
    yield "Matcha"
    yield "Oolong"
```

---

## 4. Combining Generators Using `yield from`

Now we combine them into one menu.

```python
def full_menu():
    yield from local_chai()
    yield from imported_chai()
```

Usage:

```python
for chai in full_menu():
    print(chai)
```

Output

```
Masala Chai
Ginger Chai
Matcha
Oolong
```

### What happened?

`yield from` automatically:

* calls another generator
* gets its values
* yields them to the caller

---

## 5. Without `yield from`

The same thing could be written manually:

```python
def full_menu():
    for chai in local_chai():
        yield chai
        
    for chai in imported_chai():
        yield chai
```

But `yield from` is **shorter and cleaner**.

---

## 6. Concept 2: Closing a Generator

Sometimes generators:

* run **infinite loops**
* stay in **memory**
* wait for more data

So we may want to **stop them manually**.

Python provides:

```python
generator.close()
```

This **stops the generator and frees memory**.

---

## 7. Example: Chai Stall Generator

Generator waiting for orders.

```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order..."
    except GeneratorExit:
        print("Stall closed. No more chai.")
```

---

## 8. Using the Generator

Create generator:

```python
stall = chai_stall()
```

Start generator:

```python
print(next(stall))
```

Output:

```
Waiting for chai order...
```

---

## 9. Closing the Generator

Now close it.

```python
stall.close()
```

Output:

```
Stall closed. No more chai.
```

The generator stops and memory is cleaned.

---

## 10. Why `close()` is Important

Generators can remain active in memory.

Example situations:

* database connections
* infinite generators
* streaming systems

Closing them ensures:

* **no memory leaks**
* **better performance**
* **clean resource handling**

---

## 11. GeneratorExit Exception

When we call:

```python
generator.close()
```

Python raises an internal exception:

```
GeneratorExit
```

That is why we often use:

```python
try:
    ...
except GeneratorExit:
    cleanup code
```

This allows us to **clean resources properly**.

---

## 12. Real-World Example (Database Connection)

Generators are often used like this:

```python
def database_connection():
    connection = "DB Connected"
    try:
        yield connection
    finally:
        print("Closing database connection")
```

Usage:

```python
conn = database_connection()

print(next(conn))

conn.close()
```

Output

```
DB Connected
Closing database connection
```

---

## 13. Important Generator Features Learned

### 1️⃣ `yield`

Pauses and resumes function execution.

```python
yield value
```

---

### 2️⃣ `next()`

Gets the next value from generator.

```python
next(generator)
```

---

### 3️⃣ `send(value)`

Sends data **into the generator**.

```python
generator.send(value)
```

---

### 4️⃣ `yield from`

Gets values **from another generator**.

```python
yield from another_generator()
```

---

### 5️⃣ `close()`

Stops the generator and cleans memory.

```python
generator.close()
```

---

## 14. Simple Visual Flow

Generator lifecycle:

```
start generator
      ↓
yield value
      ↓
pause
      ↓
next() / send()
      ↓
resume
      ↓
close()
      ↓
cleanup
```

---

## 15. Final Simple Summary

Generators in Python can:

1. **Generate values** → `yield`
2. **Provide next value** → `next()`
3. **Receive data** → `send()`
4. **Use other generators** → `yield from`
5. **Stop execution** → `close()`

They are widely used for:

* **data streaming**
* **frameworks like FastAPI**
* **database connections**
* **large data processing**

---

## 55. Decorators in python (09:13)

## Python Decorators – Simple Notes & Explanation

## 1. What is a Decorator?

A **decorator** in Python is a **function that wraps another function to add extra behavior without modifying the original function**.

Think of it like **decoration on coffee ☕**:

* Coffee = original function
* Chocolate powder on top = decorator
* Coffee still works the same, but something extra is added.

So decorators allow you to:

* add extra functionality
* run code **before or after a function**
* keep the original function unchanged

---

## 2. Basic Idea of Decorators

Suppose you have many functions and you want to **log whenever a function runs**.

Instead of editing every function, you can create **one decorator** that wraps them.

Conceptual flow:

```
Decorator
   |
   v
Extra code before function
Original function runs
Extra code after function
```

---

## 3. Basic Decorator Syntax

A decorator is just a **function that takes another function as argument**.

### Example

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")

        func()   # calling original function

        print("After function runs")

    return wrapper
```

### What happens here?

* `func` = original function
* `wrapper` = new function that adds extra behavior
* wrapper runs:

  * before code
  * original function
  * after code

---

## 4. Using a Decorator

Python provides special syntax using **@**

### Example

```python
@my_decorator
def greet():
    print("Hello from Chai Code")
```

Calling the function:

```python
greet()
```

### Output

```
Before function runs
Hello from Chai Code
After function runs
```

### What actually happens internally?

This line:

```
@my_decorator
def greet():
```

is equivalent to:

```python
def greet():
    print("Hello from Chai Code")

greet = my_decorator(greet)
```

So the original function gets **replaced with the wrapper function**.

---

## 5. Why Decorators Are Useful

Decorators help avoid **repeating the same code**.

Common real-world uses:

* Logging
* Authentication
* Timing functions
* Access control
* Caching
* Validation

Example idea:

```
Check login
Run function
Log result
```

---

## 6. Problem with Basic Decorators

If you check the function name:

```python
print(greet.__name__)
```

You may get:

```
wrapper
```

Instead of:

```
greet
```

Why?

Because the decorator **returns the wrapper function**, so Python thinks the function name is `wrapper`.

This also affects other **metadata** like:

* function name
* documentation
* annotations

---

## 7. What is Metadata?

**Metadata = data about data**

Example:

For a song file:

| Type        | Example                     |
| ----------- | --------------------------- |
| Actual Data | Music                       |
| Metadata    | song length, format, artist |

For functions:

| Data           | Metadata                     |
| -------------- | ---------------------------- |
| Function logic | name, docstring, annotations |

Decorators can accidentally overwrite this metadata.

---

## 8. Solution: functools.wraps

Python provides **`wraps`** to preserve metadata.

Import it like this:

```python
from functools import wraps
```

---

## 9. Correct Decorator Using wraps

```python
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Before function runs")

        func()

        print("After function runs")

    return wrapper
```

Now:

```python
@my_decorator
def greet():
    print("Hello")
```

Checking name:

```python
print(greet.__name__)
```

Output:

```
greet
```

Metadata is preserved.

---

## 10. Full Working Example

```python
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Before function runs")

        func()

        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print("Hello from decorator example")


greet()
```

### Output

```
Before function runs
Hello from decorator example
After function runs
```

---

## 11. Decorator Flow (Step-by-Step)

1. Python reads decorator

```
@my_decorator
```

2. Function is passed to decorator

```
my_decorator(greet)
```

3. Decorator returns `wrapper`

4. `greet` now becomes `wrapper`

5. Calling `greet()` runs wrapper

---

## 12. Key Points to Remember

Important things from this tutorial:

1️⃣ Decorators **wrap a function** to add extra behavior.

2️⃣ A decorator is just a **function that takes another function as input**.

3️⃣ It usually contains a **wrapper function**.

4️⃣ Wrapper runs:

* code before
* original function
* code after

5️⃣ Use **@decorator_name** to apply decorators.

6️⃣ Decorators **replace the original function with wrapper**.

7️⃣ Metadata like function name may change.

8️⃣ Use **`functools.wraps`** to preserve metadata.

---

## 13. Simple Mental Model

Think like this:

```
Original function
      ↓
Decorator wraps it
      ↓
New function with extra behavior
```

---

✅ **One-line definition**

A **decorator is a function that modifies or extends another function without changing its source code.**

---

## 55. Build a Logger with Decorators (05:56)

## Python Logging Decorator – Simple Notes

## 1. What is a Logging Decorator?

A **logging decorator** is a decorator that **prints or records information whenever a function runs**.

It usually logs things like:

* when a function starts
* when it finishes
* which function is running
* what parameters were passed

Example log:

```
Calling brew_chai
Brewing masala chai
Finished calling brew_chai
```

This helps in:

* debugging
* tracking program flow
* monitoring applications

---

## 2. Structure of a Decorator (Always Same Pattern)

Most decorators follow this structure:

```python
from functools import wraps

def decorator_name(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # code before

        result = func(*args, **kwargs)

        # code after

        return result

    return wrapper
```

### Key parts

| Part        | Purpose              |
| ----------- | -------------------- |
| `func`      | original function    |
| `wrapper()` | wraps the function   |
| `*args`     | positional arguments |
| `**kwargs`  | keyword arguments    |
| `wraps`     | preserves metadata   |

---

## 3. Importing `wraps`

Always import `wraps` to preserve function metadata.

```python
from functools import wraps
```

Without `wraps`, Python may change:

* function name
* docstring
* metadata

---

## 4. Creating a Logging Decorator

Example logging decorator:

```python
from functools import wraps

def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished calling {func.__name__}")

        return result

    return wrapper
```

---

## 5. Why Use `*args` and `**kwargs`?

Decorators must work with **any function**.

Functions may have:

* no parameters
* one parameter
* multiple parameters
* keyword parameters

So we use:

| Syntax     | Meaning                                    |
| ---------- | ------------------------------------------ |
| `*args`    | accepts any number of positional arguments |
| `**kwargs` | accepts any number of keyword arguments    |

Example:

```python
def example(a, b, c=10):
```

Decorator can handle this using:

```python
wrapper(*args, **kwargs)
```

---

## 6. Calling the Original Function

Inside wrapper:

```python
result = func(*args, **kwargs)
```

This means:

* call the original function
* pass all arguments
* store the returned result

---

## 7. Returning the Result

Always return the result:

```python
return result
```

Otherwise the decorated function may return **None**.

---

## 8. Using the Logging Decorator

Use `@decorator_name` above a function.

Example:

```python
@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")
```

Calling function:

```python
brew_chai("masala")
```

### Output

```
Calling brew_chai
Brewing masala chai
Finished calling brew_chai
```

---

## 9. Example with Multiple Parameters

Functions can have multiple parameters.

```python
@log_activity
def brew_chai(type, milk="No"):
    print(f"Brewing {type} chai with milk: {milk}")
```

Calling function:

```python
brew_chai("Masala", milk="Yes")
```

Output:

```
Calling brew_chai
Brewing Masala chai with milk: Yes
Finished calling brew_chai
```

Notice:

* decorator **still works**
* because we used `*args` and `**kwargs`

---

## 10. Accessing Function Name

Decorators can get the function name using:

```python
func.__name__
```

Example:

```python
print(func.__name__)
```

Output:

```
brew_chai
```

This helps for **logging and debugging**.

---

## 11. Full Example Code

Complete working example:

```python
from functools import wraps

def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished calling {func.__name__}")

        return result

    return wrapper


@log_activity
def brew_chai(type, milk="No"):
    print(f"Brewing {type} chai with milk: {milk}")


brew_chai("Masala", milk="Yes")
```

Output:

```
Calling brew_chai
Brewing Masala chai with milk: Yes
Finished calling brew_chai
```

---

## 12. Advantages of Logging Decorators

Decorators help you **separate logic**.

Instead of writing logging inside every function:

Bad approach:

```python
def brew_chai():
    print("Starting function")
    print("Brewing chai")
    print("Ending function")
```

Better approach using decorator:

```python
@log_activity
def brew_chai():
    print("Brewing chai")
```

Cleaner and reusable.

---

## 13. Real World Use Cases

Decorators are widely used in frameworks like:

* **Django**
* **FastAPI**
* **Flask**

Examples include:

| Use            | Example                |
| -------------- | ---------------------- |
| Authentication | check login            |
| Logging        | track function calls   |
| Performance    | measure execution time |
| Caching        | store results          |
| Permissions    | restrict access        |

---

## 14. Key Takeaways

Important things to remember:

1️⃣ Decorators wrap functions.

2️⃣ Logging decorators track function execution.

3️⃣ Always use:

```python
*args
**kwargs
```

4️⃣ Use `wraps` from `functools`.

5️⃣ Use:

```python
func.__name__
```

to access function name.

6️⃣ Always return result.

---

## 15. One Line Definition

A **logging decorator** is a decorator that **prints or records when a function starts and finishes executing**.

---

## 56. Build an Authorization Decorator (05:45)

## 🔐 Python Authentication Decorator – Simple Notes

## 1. What is this Decorator?

This is a **custom decorator** that:

👉 **Allows only admin users to run a function**
👉 Blocks others with an "Access Denied" message

This is very common in real-world apps like:

* dashboards
* admin panels
* APIs (especially in Django, FastAPI)

---

## 2. Basic Idea

We wrap a function and check:

```id="z3k38d"
IF user is admin → allow function execution  
ELSE → deny access
```

---

## 3. Basic Structure of This Decorator

```python id="z0c2g3"
from functools import wraps

def require_admin(func):

    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
        else:
            return func(user_role)

    return wrapper
```

---

## 4. How It Works

Step-by-step:

1. Function is passed into decorator → `func`
2. Wrapper receives argument → `user_role`
3. Condition checks:

   * if NOT admin → deny access
   * if admin → call original function

---

## 5. Using the Decorator

```python id="v4s7m5"
@require_admin
def access_inventory(user_role):
    print("Access granted to tea inventory")
```

---

## 6. Calling the Function

```python id="5v6jgr"
access_inventory("user")
access_inventory("admin")
```

---

## 7. Output

```id="smgg29"
Access denied: Admins only
Access granted to tea inventory
```

---

## 8. Important Concept: Wrapper Arguments

In this example:

```python id="n3l4a0"
def wrapper(user_role):
```

We only accept **one argument** because we know the function needs only that.

But in general, safer way is:

```python id="38lg2j"
def wrapper(*args, **kwargs):
```

👉 Use this when:

* you don’t know number of arguments
* making reusable decorators

---

## 9. Important Concept: Return Statement

Inside decorator:

```python id="u6k5lh"
return func(user_role)
```

This ensures:

* original function runs
* its result is returned

---

## 10. Important Edge Case (VERY IMPORTANT)

In this part:

```python id="ydx6cr"
if user_role != "admin":
    print("Access denied")
```

We are **not returning anything**.

Python may:

* silently return `None`
* or sometimes cause issues in strict codebases

---

## 11. Safe Practice (Recommended)

Always return something explicitly:

```python id="4u9k9x"
if user_role != "admin":
    print("Access denied")
    return None
```

👉 Why?

* avoids unexpected bugs
* makes code predictable
* useful in production systems

---

## 12. Full Correct Version

```python id="t2gqv0"
from functools import wraps

def require_admin(func):

    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)

    return wrapper


@require_admin
def access_inventory(user_role):
    print("Access granted to tea inventory")


access_inventory("user")
access_inventory("admin")
```

---

## 13. Key Concepts Learned

### 1️⃣ Decorator for Access Control

* Restrict function execution

---

### 2️⃣ Wrapper Function

* Controls execution flow

---

### 3️⃣ Conditional Logic in Decorator

```python id="akqbb9"
if condition:
    block
else:
    allow
```

---

### 4️⃣ Always Return Value

```python id="i6pwhb"
return None
```

Important for:

* stability
* production code

---

### 5️⃣ Use `@wraps`

```python id="rsh3to"
@wraps(func)
```

Preserves:

* function name
* metadata

---

## 14. Real-World Example

This is how it's used in real apps:

```python id="gksf45"
@require_admin
def delete_user(user_role):
    print("User deleted")
```

Only admin can delete users.

---

## 15. Mental Model

Think like this:

```id="bt60ts"
User → Decorator → Check Role → Allow / Deny → Function
```

---

## 16. Key Takeaways

✔ Decorators can enforce rules (like authentication)
✔ You can control function execution
✔ Always handle all cases properly (return values)
✔ Use precise arguments if known
✔ Use `*args, **kwargs` for flexibility

---

## 17. One-Line Definition

👉 **An authentication decorator controls access to a function based on user roles.**

---

## Sec 9 - OOPs in Python

## 60. Building your 1st Class and Object in python (9:05)

## 🧠 Python OOP – Simple Notes

## 1. What is OOP?

👉 **OOP (Object-Oriented Programming)** is a **way (style) of writing code**

* This “way” is called a **paradigm**
* Other paradigms also exist (like **functional programming**)

👉 In real-world code:

* You’ll often see a **mix of OOP + functional programming**

---

## 2. Core Idea (Very Important)

Think like this:

```
Class → Blueprint  
Object → Real item created from blueprint
```

---

## 3. Real-Life Example

* Class = Car design
* Objects = Individual cars made from that design

Each car:

* can have different color
* can have different features
  But all come from the same blueprint

---

## 4. Key Terminology

## ✅ Class

👉 Blueprint/template

## ✅ Object

👉 Instance created from class

---

## 5. Creating a Class in Python

```python
class Chai:
    pass
```

### Explanation:

* `class` → keyword
* `Chai` → class name (should start with Capital letter)
* `pass` → empty class (no logic yet)

---

## 6. Important Concept

👉 In Python:

```
Everything is an object (even classes!)
```

---

## 7. Checking Type of Class

```python
class Chai:
    pass

print(type(Chai))
```

### Output:

```
<class 'type'>
```

👉 Meaning:

* Class itself is also an object of type `type`

---

## 8. Creating an Object

```python
ginger_tea = Chai()
```

👉 This creates an object from class `Chai`

---

## 9. Checking Object Type

```python
print(type(ginger_tea))
```

### Output:

```
<class '__main__.Chai'>
```

👉 Meaning:

* This is an object of class `Chai`

---

## 10. Checking Object Belongs to Class

Using `isinstance()`:

```python
print(isinstance(ginger_tea, Chai))
```

### Output:

```
True
```

---

## 11. Checking Against Another Class

```python
class ChaiTime:
    pass

print(isinstance(ginger_tea, ChaiTime))
```

### Output:

```
False
```

👉 Because:

* Object belongs to `Chai`
* Not to `ChaiTime`

---

## 12. Full Example (Clean Code)

```python
class Chai:
    pass

class ChaiTime:
    pass

# create object
ginger_tea = Chai()

# check types
print(type(Chai))           # class type
print(type(ginger_tea))    # object type

# check instance
print(isinstance(ginger_tea, Chai))      # True
print(isinstance(ginger_tea, ChaiTime))  # False
```

---

## 13. Key Concepts to Remember

### 🔹 1. Class = Blueprint

* Defines structure

---

### 🔹 2. Object = Instance

* Created using class

---

### 🔹 3. Syntax

```python
class ClassName:
    pass

obj = ClassName()
```

---

### 🔹 4. Everything is Object in Python

* even classes

---

### 🔹 5. `type()` vs `isinstance()`

| Function       | Purpose             |
| -------------- | ------------------- |
| `type()`       | shows type          |
| `isinstance()` | checks relationship |

---

## 14. Mental Model

```
Class → Create → Object → Use
```

Example:

```
Chai (class) → ginger_tea (object)
```

---

## 15. One-Line Definition

👉 **OOP is a way of writing code using classes (blueprints) and objects (instances).**

---

## 16. What’s Coming Next (Important for You)

Since you already work with:

* Node.js
* Backend systems

Next OOP topics will be very useful:

* constructors (`__init__`)
* attributes
* methods
* encapsulation
* inheritance

---

## 61. Class and Object Namespace (08:19)

- Each object has its own entity, that's called as namespace that doesn't bother other ones.

## 62. Attribute Shadowing in python (06:14)

## 🧠 Python OOP – Namespaces (Simple Notes)

## 1. What is Namespace?

👉 **Namespace = a container where variables live**

In simple words:

```text
Each object has its own space to store data
```

---

## 2. Core Idea

👉 Every object created from a class:

* has its **own data (properties)**
* does **not affect other objects**
* does **not affect the class**

---

## 3. Class with Properties

```python
class SimpleChai:
    origin = "India"
```

👉 Here:

* `origin` is a **property (variable inside class)**

---

## 4. Accessing Class Property

```python
print(SimpleChai.origin)
```

### Output:

```
India
```

---

## 5. Adding Property to Class

```python
SimpleChai.is_hot = True
```

Now class has:

* origin = India
* is_hot = True

---

## 6. Creating Object

```python
masala = SimpleChai()
```

---

## 7. Accessing Properties via Object

```python
print(masala.origin)
print(masala.is_hot)
```

### Output:

```
India
True
```

👉 Object can access class properties

---

## 8. Important Concept: Object Namespace

Now change value in object:

```python
masala.is_hot = False
```

---

## 9. Check Values Again

```python
print(SimpleChai.is_hot)  # class
print(masala.is_hot)      # object
```

### Output:

```
True
False
```

---

## 🔥 Key Insight

```text
Changing object value DOES NOT change class value
```

👉 Because:

* Object has its **own namespace**

---

## 10. Adding New Property to Object

```python
masala.flavor = "Masala"
```

Now:

```python
print(masala.flavor)
```

### Output:

```
Masala
```

---

## ⚠️ Important

👉 This property exists only in object:

```text
masala → has flavor  
class → does NOT have flavor
```

---

## 11. Full Example

```python
class SimpleChai:
    origin = "India"

# add class property
SimpleChai.is_hot = True

# create object
masala = SimpleChai()

# access properties
print(masala.origin)   # India
print(masala.is_hot)   # True

# change object property
masala.is_hot = False

# compare
print(SimpleChai.is_hot)  # True
print(masala.is_hot)      # False

# add new property to object
masala.flavor = "Masala"
print(masala.flavor)      # Masala
```

---

## 12. Key Concepts to Remember

### 🔹 1. Class Namespace

* shared by all objects (initially)

---

### 🔹 2. Object Namespace

* unique to each object
* overrides class values if changed

---

### 🔹 3. Property (Important Term)

```text
Variable inside class = Property
```

---

### 🔹 4. Object Independence

```text
Object changes → do NOT affect class
Object changes → do NOT affect other objects
```

---

## 13. Mental Model

Think like this:

```text
Class = Blueprint

Object 1 → own data
Object 2 → own data
Object 3 → own data
```

Even if they come from same class:

* they behave independently

---

## 14. Real-Life Analogy

T-shirt example:

* Class → T-shirt design
* Object → actual T-shirts

Each T-shirt:

* can have different size
* different color
* different fit

But all came from same design

---

## 15. One-Line Definition

👉 **Namespace means each object has its own separate storage for data.**

---

## 16. Why This Matters (Important for You)

Since you're into **backend development (Node/Express)**:

👉 This concept is used in:

* user objects
* API data handling
* request/response objects
* database models

---

## 17. Quick Summary

✔ Class defines properties
✔ Object gets properties
✔ Object can override them
✔ Object can add new ones
✔ No effect on class or other objects

---

## 62. Attribute Shadowing in python (06:14)

## 🧠 What is Attribute Shadowing?

**In simple words:**

Attribute shadowing happens when an **object overrides (hides)** a variable (attribute) that is defined in its class.

* Class has a default value
* Object creates its own value
* Object value **shadows (hides)** the class value

---

## 🔑 Key Idea

👉 Python looks for attributes in this order:

1. **Object (instance)**
2. **Class**

So:

* If object has the attribute → use it
* If not → fallback to class

---

## 📌 Basic Example

```python
class Chai:
    temperature = "hot"

cutting = Chai()

print(cutting.temperature)  # hot (from class)
```

---

## ⚡ Shadowing Example

```python
class Chai:
    temperature = "hot"

cutting = Chai()

# Shadowing happens here
cutting.temperature = "mild"

print(cutting.temperature)  # mild (object value)
print(Chai.temperature)     # hot (class value)
```

### ✔ Explanation

* `cutting.temperature` → uses object value
* `Chai.temperature` → still unchanged

👉 Object value **shadows** class value

---

## 🔄 Fallback Behavior (Important)

If you remove the object’s attribute:

```python
class Chai:
    temperature = "hot"

cutting = Chai()
cutting.temperature = "mild"

del cutting.temperature  # remove object attribute

print(cutting.temperature)  # hot
```

### ✔ Why?

* Object no longer has `temperature`
* Python falls back to class

👉 This is **shadow removed → fallback to class**

---

## ❌ No Fallback Case

If attribute exists only in object:

```python
class Chai:
    pass

cutting = Chai()
cutting.cup = "small"

print(cutting.cup)  # small

del cutting.cup

print(cutting.cup)  # ERROR
```

### ✔ Why?

* Attribute not in object anymore
* Also not in class
* So Python throws error

---

## 📊 Summary Table

| Situation                            | Result            |
| ------------------------------------ | ----------------- |
| Attribute in object                  | Object value used |
| Attribute not in object but in class | Class value used  |
| Attribute not in both                | ❌ Error           |

---

## 🧩 Important Concepts

## 1. Attribute = Variable in class/object

```python
class Chai:
    strength = "strong"
```

---

## 2. Shadowing = Overriding at object level

```python
obj.strength = "light"
```

---

## 3. Fallback mechanism

* Object → Class lookup chain

---

## 4. Deleting attributes

```python
del obj.attribute
```

---

## 🎯 Real-Life Analogy

Think of:

* **Class = Template (default settings)**
* **Object = Custom version**

Example:

* Default chai = hot
* Your chai = mild

If you remove your customization → back to default (hot)

---

## 🚀 Final Takeaways

* Attribute shadowing = object overrides class attribute
* Python always checks object first
* If not found → fallback to class
* If nowhere found → error
* Deleting object attribute reveals class value again

---

## 63. Self argument in python (07:31)

## 🧠 What is `self`?

**In simple words:**

👉 `self` is a reference to the **current object (instance)**.

* It lets you access **variables (attributes)** and **methods** inside a class.
* It connects the method to the specific object calling it.

---

## 🔑 Key Idea

When you call a method like:

```python
obj.method()
```

Python internally converts it to:

```python
Class.method(obj)
```

👉 That `obj` is passed as **`self`**

---

## 📌 Basic Class with Method

```python
class ChaiCup:
    size = 150  # in ml

    def describe(self):
        return f"{self.size} ml chai cup"
```

---

## ✅ Using the Method (Correct Way)

```python
cup = ChaiCup()
print(cup.describe())
```

### Output:

```
150 ml chai cup
```

### ✔ Explanation

* `cup` is passed automatically as `self`
* So `self.size` = `cup.size`

---

## ⚠️ Important Rule

👉 Inside class methods, always use:

```python
self.variable_name
```

❌ Wrong:

```python
return size   # ERROR
```

✅ Correct:

```python
return self.size
```

---

## 🚨 Calling Method from Class (Common Confusion)

```python
ChaiCup.describe()
```

### ❌ Error:

```
missing 1 required positional argument: 'self'
```

### ✔ Why?

* Class doesn’t know **which object** to use
* No `self` is passed

---

## ✅ Fix: Pass Object Manually

```python
cup = ChaiCup()
print(ChaiCup.describe(cup))
```

### ✔ Explanation

* You manually pass `cup` as `self`

---

## 🔄 Multiple Objects Example

```python
class ChaiCup:
    size = 150

    def describe(self):
        return f"{self.size} ml chai cup"


cup1 = ChaiCup()
cup2 = ChaiCup()

cup2.size = 100  # override for this object

print(cup1.describe())  # 150 ml
print(cup2.describe())  # 100 ml
```

---

## 🧩 What’s Happening Here?

* `cup1` and `cup2` are different objects
* Each object has its **own data**
* `self` ensures correct object is used

---

## 🔍 Internal Working

When you do:

```python
cup1.describe()
```

Python does:

```python
ChaiCup.describe(cup1)
```

When you do:

```python
cup2.describe()
```

Python does:

```python
ChaiCup.describe(cup2)
```

👉 That’s why results differ

---

## 📊 Summary Table

| Concept          | Meaning                     |
| ---------------- | --------------------------- |
| `self`           | Reference to current object |
| Method           | Function inside class       |
| `self.attribute` | Access object data          |
| Object call      | Automatically passes `self` |
| Class call       | Must pass object manually   |

---

## 🎯 Key Takeaways

* `self` = current object reference
* Always write `self` as first parameter in methods
* Use `self` to access variables and methods
* Object automatically passes `self`
* Class does NOT → you must pass it manually

---

## 🚀 Simple Analogy

Think of `self` like:

👉 “**This object**”

Example:

* cup1 says: “this cup is 150ml”
* cup2 says: “this cup is 100ml”

---

## 64. Constructors and Init in python classes (08:20)

## 🧠 What is `__init__`?

**In simple words:**

👉 `__init__` is a special method that runs **automatically when you create an object**.

It is used to:

* Initialize (set up) object data
* Assign values to attributes

---

## 🔑 Key Idea

When you create an object:

```python
obj = ClassName(...)
```

👉 Python automatically calls:

```python
ClassName.__init__(obj, ...)
```

---

## 📌 Basic Syntax

```python
class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
```

---

## ✅ Example Usage

```python
order1 = ChaiOrder("masala", 200)
order2 = ChaiOrder("ginger", 220)
```

---

## 🧩 Adding a Method

```python
class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} chai"
```

---

## ▶️ Running the Code

```python
order1 = ChaiOrder("masala", 200)
print(order1.summary())

order2 = ChaiOrder("ginger", 220)
print(order2.summary())
```

### Output:

```
200 ml of masala chai
220 ml of ginger chai
```

---

## ⚠️ Important Concepts

## 1. `__init__` is a constructor

* Special method
* Runs automatically on object creation

---

## 2. Always use `self`

```python
def __init__(self, ...):
```

👉 `self` refers to the current object

---

## 3. Assign values using `self`

```python
self.type = type_
self.size = size
```

👉 Creates object-specific attributes

---

## 4. You don’t pass `self` manually

```python
ChaiOrder("masala", 200)  # correct
```

❌ Wrong:

```python
ChaiOrder(self, "masala", 200)
```

---

## 🤔 Why Use `__init__`?

Without `__init__`:

```python
class Chai:
    pass

c = Chai()
c.type = "masala"
c.size = 200
```

👉 Manual and messy

---

With `__init__`:

```python
c = ChaiOrder("masala", 200)
```

👉 Clean and automatic

---

## ⚡ Special Case: Using Reserved Names

In the tutorial, this was used:

```python
def __init__(self, type_, size):
```

### ✔ Why `type_` instead of `type`?

👉 Because `type` is a built-in function in Python

```python
type(10)  # returns <class 'int'>
```

So we avoid conflict by using:

* `type_` (common practice)

---

## 📊 Summary Table

| Concept    | Meaning                              |
| ---------- | ------------------------------------ |
| `__init__` | Constructor method                   |
| Runs when  | Object is created                    |
| Purpose    | Initialize object data               |
| `self`     | Current object reference             |
| `type_`    | Avoids conflict with built-in `type` |

---

## 🎯 Key Takeaways

* `__init__` runs automatically
* Used to initialize object properties
* Always include `self`
* Makes object creation clean and structured
* Avoid using reserved keywords → use `type_`

---

## 🚀 Simple Analogy

Think of `__init__` like:

👉 “Setup instructions when a new object is born”

Example:

* You order chai → system sets type & size automatically

## 65. Inheritance and Composition in python classes (18:03)

## 🧠 1. Big Picture

This lecture explains two important OOP concepts:

### ✅ Inheritance

* One class **reuses** another class’s code
* Like: child inherits from parent

### ✅ Composition

* One class **uses another class inside it**
* Like: “has-a” relationship

👉 In real projects, both are used together.

---

## 🧾 2. Inheritance (Easy Concept)

### 🔹 Idea

If a class already has functionality, you don’t rewrite it.

You just **inherit it**.

---

### 🧩 Example

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")
```

Now create another class:

```python
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves")
```

---

### ▶️ Usage

```python
chai = MasalaChai("Masala")
chai.prepare()       # inherited
chai.add_spices()    # own method
```

---

### 🔑 Important Points

* Syntax:

  ```python
  class ChildClass(ParentClass):
  ```
* Child gets:

  * variables
  * methods
* No need to rewrite code

---

## 🧠 3. Composition (Important for Real Projects)

### 🔹 Idea

Instead of inheriting, a class **contains another class**

👉 “has-a” relationship

---

### 🧩 Example

```python
class ChaiShop:
    def __init__(self):
        self.chai = BaseChai("Regular")  # object inside class

    def serve(self):
        print(f"Serving {self.chai.type} chai")
        self.chai.prepare()
```

---

### ▶️ Usage

```python
shop = ChaiShop()
shop.serve()
```

---

### 🔑 Important Points

* Uses object of another class
* More flexible than inheritance
* Common in production code

---

## ⚔️ 4. Inheritance vs Composition

| Feature      | Inheritance          | Composition       |
| ------------ | -------------------- | ----------------- |
| Relationship | “is-a”               | “has-a”           |
| Example      | MasalaChai is a Chai | Shop has a Chai   |
| Flexibility  | Less                 | More              |
| Usage        | Simple reuse         | Real-world design |

---

## 🧠 5. Combining Both

You can use **both together**

```python
class FancyChaiShop(ChaiShop):
    def __init__(self):
        super().__init__()   # use parent constructor
```

---

## ⚠️ 6. Common Error (Important)

### ❌ Calling method without object

```python
MasalaChai.add_spices()   # ❌ error
```

### ✅ Correct way

```python
chai = MasalaChai("Masala")
chai.add_spices()
```

👉 Because methods need `self` (context)

---

## 🧠 7. Key Learnings

* Inheritance = reuse code
* Composition = use objects inside class
* Methods need object context (`self`)
* Constructor (`__init__`) always runs when object is created
* Production code often uses **composition more**

---

## 🧪 8. Simple Combined Example

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai")


class ChaiShop:
    def __init__(self):
        self.chai = BaseChai("Regular")

    def serve(self):
        print(f"Serving {self.chai.type}")
        self.chai.prepare()


shop = ChaiShop()
shop.serve()
```

---

## 🚀 Final Understanding

* **Inheritance → reuse**
* **Composition → flexibility**
* Real-world systems = mix of both

---

## What is Composition and why it is used if there is inheritance already in python?

---

## 🧠 What is Composition?

**Composition means putting one object inside another object.**

👉 In simple terms:
A class **uses another class as a part of it**

---

### 🔹 Example

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def drive(self):
        self.engine.start()
        print("Car is moving")
```

👉 Here:

* `Car` **has an Engine**
* Not “Car is Engine”

---

## 🧾 Inheritance vs Composition (Core Idea)

### 🔸 Inheritance → “IS-A” relationship

```python
class Animal:
    pass

class Dog(Animal):   # Dog IS-A Animal
    pass
```

---

### 🔸 Composition → “HAS-A” relationship

```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS-A Engine
```

---

## 🤔 Why do we need Composition if Inheritance exists?

Because inheritance is **not always the right design**.

---

## 🚫 Problem with Inheritance

Inheritance creates **tight coupling**

Example:

```python
class ElectricCar(Car):
    pass
```

Now:

* ElectricCar is forced to behave like Car
* Hard to change parts independently
* Can become messy in large systems

---

## ✅ Why Composition is Preferred

### 1. More Flexible

You can swap parts easily

```python
class PetrolEngine:
    def start(self):
        print("Petrol engine")

class ElectricEngine:
    def start(self):
        print("Electric engine")


class Car:
    def __init__(self, engine):
        self.engine = engine
```

👉 Now:

```python
car1 = Car(PetrolEngine())
car2 = Car(ElectricEngine())
```

✔ Same Car class
✔ Different behavior

---

### 2. Loose Coupling

* Classes don’t depend too tightly on each other
* Easier to modify without breaking code

---

### 3. Better for Real-World Modeling

Real world is mostly “has-a”, not “is-a”

* Car **has** engine ✅
* Car **is** engine ❌

---

### 4. Easier Testing & Maintenance

You can test components separately

---

## 🔥 Simple Rule (Very Important)

👉 Use this rule:

* If relationship is **IS-A → use inheritance**
* If relationship is **HAS-A → use composition**

---

## ⚖️ Quick Comparison

| Feature        | Inheritance | Composition |
| -------------- | ----------- | ----------- |
| Relationship   | IS-A        | HAS-A       |
| Flexibility    | Less        | More        |
| Coupling       | Tight       | Loose       |
| Real-world use | Limited     | Very common |

---

## 🧠 Final Understanding

* Inheritance is good for **code reuse**
* Composition is better for **design and flexibility**
* That’s why in real production code:
  👉 Composition is used more

---

## 66. 3 Ways to Acess Base Class (07:19)

## 📘 Accessing Base Class in Python (Simple Notes)

## 🔑 Core Idea

When using **inheritance**, a child class may need to use properties or methods from the **parent (base) class**.

There are **3 ways** to access the base class:

1. ❌ Code Duplication
2. ⚠️ Explicit Call
3. ✅ `super()` (Best & most used)

---

## 1️⃣ Code Duplication (Not Recommended)

### 💡 Idea

You rewrite the parent class code inside the child class.

### ❌ Problem

* Repeats code
* Hard to maintain
* Violates DRY (Don’t Repeat Yourself)

### 🧑‍💻 Example

```python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # ❌ Code duplication
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level
```

👉 Works fine, but **bad practice**

---

## 2️⃣ Explicit Call (Direct Parent Call)

### 💡 Idea

Call parent class constructor manually using its name.

### 👍 Pros

* Avoids duplication
* Clear what's happening

### ⚠️ Cons

* Not flexible in complex inheritance (like multiple inheritance)

### 🧑‍💻 Example

```python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # ⚠️ Explicit call
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level
```

👉 You're directly calling:

```python
Chai.__init__(self, ...)
```

---

## 3️⃣ Using `super()` (Best Practice ✅)

### 💡 Idea

Use `super()` to automatically call the parent class.

### 👍 Pros

* Clean & readable
* Works well with multiple inheritance
* Most commonly used

### 🧑‍💻 Example

```python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # ✅ Using super()
        super().__init__(type_, strength)
        self.spice_level = spice_level
```

---

## 🧠 Key Concepts Explained

## 🔹 Base Class (Parent Class)

The class being inherited from.

```python
class Chai:   # Base class
```

---

## 🔹 Derived Class (Child Class)

The class that inherits from another class.

```python
class GingerChai(Chai):   # Child class
```

---

## 🔹 Constructor (`__init__`)

Special method used to initialize object properties.

```python
def __init__(self, type_, strength):
```

---

## 🔹 `super()` Function

### ✔ What it does:

Calls methods from the parent class.

```python
super().__init__(type_, strength)
```

👉 Meaning:

> “Call the parent class constructor automatically”

---

## ⚖️ Comparison Table

| Method        | Code Duplication | Readability | Best Practice |
| ------------- | ---------------- | ----------- | ------------- |
| Duplication   | ❌ High           | ❌ Poor      | ❌ No          |
| Explicit Call | ⚠️ Medium        | ⚠️ Okay     | ⚠️ Sometimes  |
| `super()`     | ✅ None           | ✅ Clean     | ✅ Yes         |

---

## 🚀 Final Takeaways

* Avoid repeating code → ❌ Duplication
* Explicit calls work but are less flexible → ⚠️
* Use `super()` in real projects → ✅ BEST

---

## 🎯 One-Line Summary

👉 **Use `super()` to access parent class functionality cleanly and efficiently in Python inheritance.**

---

## 67. Method Resolution Order (MRO) (08:03)


summaries this python tutorial transcript in simple words, make note of all important pointers and also explain each important concepts with basic code examples