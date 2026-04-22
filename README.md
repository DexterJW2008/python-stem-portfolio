# Python-Stem-Portfolio
Python programming portfolio - Bishop's Stortford College STEM course
**Dexter Williamson**
**Bishop's Stortford College**
**Python for STEM**
**Year 12**

---

##About me 
[I am Dexter, i am in year 12 at the school of Bishop's Stortford College. I was born in the year of 2008 on october 10th. I love to play football and go to the gym. I study economics, geography and DT. My favourite subject is DT because i love making stuff, however personally i find a lot of interest in geography because i find it very enjoyable. ]

---

##Course Overview 
[During this course I have learnt the python fundamentals such as variables, input/output and data types. As well: 
- Control structures (Loops and conditions)
- Functions and modular code
- Data Structures(lists, dictionaires, tuples, sets)
- Validation and error handling
- File handling
- Object-orientinal programming(OOP)
- Versions control with Git and Github
- Working with Juypter Notebooks]

---

##Portfolio Projects 
| # | Project | Key Skills | Status |
|---|---|---|---|
| 1 | [Unit Converter](#) | Variables, funcitons, input/output| ✅Complete |
| 2 | [Number Guessing Game](#) | Loops, Conditional, Random | ✅Complete |
| 3 | [To-Do List](#) | Lists, Functions, Data structures | ✅Complete |
| 4 | [Student Grade Calculator](#) | Dictionairies, validation, error handling | ✅Complete |
| 5 | [OOP Bank Account](#) | Classes, OOP principles | ✅Complete |
| 6 | [Data Analysis Notebook](#) | Juypter Notebooks, data exploration | ✅Complete |

---

##Skills I Have Developed

**Programming Concepts**
- Writing clean, well-commented Python code
- Using functions to organise and reuse code 
- Handling user input safely with validation 

**Tools and Technologies** 
- Python 3 (Thonny IDE)
- Juypter Notebooks
- Git version control 
- Github for code sharing and portfolio management 
- Markdown for documentation

--- 

## Contact 

- **GitHub:** [DexterJW2008]
- **Email:** [26willid@bscmail.org]

## Project 1: Unit Converter 

``` python
def km_to_miles(km):
    """Convert kilometres to miles."""
    miles = km * 0.621371
    return miles

def miles_to_km(miles):
    """Convert miles to kilometres."""
    km = miles / 0.621371
    return km


def show_menu():
    print("=== Unit Converter ===")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

def main():
    show_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        km = float(input("Enter kilometres: "))
        result = km_to_miles(km)
        print(f"{km} km = {result:.2f} miles")
```
