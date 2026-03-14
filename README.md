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




summaries this python tutorial transcript in simple words, make note of all important pointers and also explain each important concepts with basic code examples