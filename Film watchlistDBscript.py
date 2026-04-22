import sqlite3
def dbConnection():
      # Create connection to database
    conn = sqlite3.connect('film_watchlist.db')
    cursor = conn.cursor()
        
    # Create Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmwatchlist (
            Item_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Item_name Text NOT NULL, 
            Director Text NOT NULL,
            Genre Text NOT NULL ,
            Watched status Text NOT NULL,
            Rating INTEGER NOT NULL
        )
    ''')
    # Save changes and close
    conn.commit()
    conn.close()
    return conn, cursor
