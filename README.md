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

## Project 2: Number Guessing Game

``` python
import random

def play_game():
    """Play one round of the guessing game."""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break  # Exit the loop

play_game()

```

## Project 3: To do list

``` python

def show_tasks(tasks):
    """Display all tasks with their numbers."""
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    
    print("\n=== Your Tasks ===")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    """Add a new task to the list."""
    new_task = input("Enter task: ")
    tasks.append(new_task)
    print(f"Added: '{new_task}'")

def remove_task(tasks):
    """Remove a task by number."""
    show_tasks(tasks)
    number = int(input("Enter task number to remove: "))
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Removed: '{removed}'")
    else:
        print("Invalid number.")

def main():
    tasks = []
    
    while True:
        print("=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break

main()

```

## Project 4: PED calculator - Economics 

``` python
def ped():

    num1 = float(input("Enter origional value for quantity demanded"))
    num2 = float(input("Enter second value for quantity demanded"))
    num3 = float(input("Enter origional value for quantity demanded"))
    num4 = float(input("Enter original value for price"))
    num5 = float(input("Enter second value for price"))
    num6 = float(input("Enter origional value for price"))

    difference = num1 - num2
    percentagedif = difference/num3

    difference = num4 - num5
    percentagediff = difference/num6

    print(f"PED: {(percentagedif/percentagediff)}")
    
def percentageChange():
  
     num1 = float(input("Enter original value"))
     num2 = float(input("Enter second value"))
     num3 = float(input("Enter original value"))
     
     difference = num1 - num2
     percentagedif = difference/num3
     
     print(f"Percentage change: {(percentagedif*100)}")

```

## Project 5: Calculator

``` python


        

def main():
    menu = """
1. Volume of a cube
2. PED calculation
3. Percentage change
4. Quit"""
    while True:
        print(menu)
        while True:
            try:
                menuChoice = int(input('Enter a menu choice:'))
                break
            except:
                print("Please enter a number from the menu:")
        if menuChoice ==4:
            break
        elif menuChoice ==1:
            volumeCube()
        elif menuChoice ==2:
            ped()
        elif menuChoice ==3:
            percentageChange()
            

def volumeCube():
    while True:
        try:
            length = float(input('length: '))
            width = float(input('width: '))
            height = float(input('height: '))
            
            volume = length*height*width
            print(f'Volume is {volume} cubic units')
            break
        except ValueError:
            print('only numbers may be entered')
            

def ped():

    num1 = float(input("Enter origional value for quantity demanded"))
    num2 = float(input("Enter second value for quantity demanded"))
    num3 = float(input("Enter origional value for quantity demanded"))
    num4 = float(input("Enter original value for price"))
    num5 = float(input("Enter second value for price"))
    num6 = float(input("Enter origional value for price"))

    difference = num1 - num2
    percentagedif = difference/num3

    difference = num4 - num5
    percentagediff = difference/num6

    print(f"PED: {(percentagedif/percentagediff)}")
    
def percentageChange():
  
     num1 = float(input("Enter original value"))
     num2 = float(input("Enter second value"))
     num3 = float(input("Enter original value"))
     
     difference = num1 - num2
     percentagedif = difference/num3
     
     print(f"Percentage change: {(percentagedif*100)}")

```

## Prpject 6: Multiplication table 

``` python

# Ask the user for a number
number = int(input("Enter a number to generate its multiplication table: "))

# Generate and display the multiplication table from 1 to 10
print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")

```

## Project 7: Databse 

``` python
import sqlite3
def dbConnection():
     #Create connection to database
    conn = sqlite3.connect('movie_list.db')
    cursor = conn.cursor()
    
    #Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movielist (
              item_id INTEGER PRIMARY KEY AUTOINCREMENT,
              item_name TEXT NOT NULL,
              year INTEGER NOT NULL,
              director TEXT, 
              genre TEXT NOT NULL,
              rating INTEGER
        )
    ''')
    #Save changes and close
    return conn, cursor
    conn.commit(), cursor
    conn.close()
    

def insertDatawithParameters():
    '''add data to the database table'''
    query = '''INSERT INTO movielist (item_name, year, director, genre, rating)
VALUES (?, ?, ?, ?, ?);'''
    item_name = input('Enter the item name;')
    year = int(input('Enter the year;'))
    director = input('Enter the directors name;')
    genre = input('Enter the genre:')
    rating = int(input('Enter your rating:'))
    conn, cursor = dbConnection()
    cursor.execute(query,(item_name, year, director, genre, rating))
    conn.commit()
    conn.close()
    print("Record was succesfully saved")
    
def readDataBase():
    '''read from a table'''
    query = """SELECT * from movielist"""
    conn, cursor = dbConnection()
    cursor.execute(query,)
    results = cursor.fetchall()
    print(f'Item name	Year	Director	Genre	Rating')
    for i in range(len(results)):
        print(f'{results[i][2]}		{results[i][3]}		{results[i][4]}')
    conn.close()
    
    
#MAIN
def menu():
    title = 'Film List ratings'
    line = '-'
    menu = '''1. Add item(s)
2. Show items
3. Remove item
4. Update itme
5. Quit
'''
    print(f'{title}\n{line*len(title)}')
    print(menu)
def main():
    '''Main user interface'''
    while True:
        menu()
        userChoice = int(input('Choose an option:'))
        if userChoice == 5:
            print('------------- End programme ---------')
            break
        elif userChoice ==1:
            insertDatawithParameters()

```
