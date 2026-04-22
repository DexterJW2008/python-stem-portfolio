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
    
    
    
    
    
    