import sqlite3
import datetime


def create_table():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = '''
            CREATE TABLE IF NOT EXISTS history(
                id INTEGER PRIMARY KEY, 
                date TEXT, 
                title TEXT,
                links TEXT
            )
        '''

        cursor.execute(query)

        if cursor.rowcount < 1:
               print("Database existing table initialized.")
        else:
               print("Successfully database table created.")
               
        conn.commit()
        conn.close()


def add_history(date,title,links):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = '''
            INSERT INTO history( date, title, links )
                        VALUES ( ?,?,? )
        '''
        cursor.execute(query,(date,title,links))
        if cursor.rowcount < 1:
               return 1
        conn.commit()
        conn.close()


def get_histories():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = '''
            SELECT date, title, links
            FROM history
        '''
        cursor.execute(query)
        all_rows = cursor.fetchall()

        conn.commit()
        conn.close()

        return all_rows

def get_history_by_data(data):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = '''
            SELECT date, title, links
            FROM history
            WHERE title LIKE '%{}%'
        ''' .format(data)
        cursor.execute(query)
        all_rows = cursor.fetchall()

        conn.commit()
        conn.close()

        return all_rows

def update_history(date,title,links):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = '''
            UPDATE history
            SET title = ?, links = ?
            WHERE date = ?
        '''
        cursor.execute(query,(date,title,links))
        conn.commit()
        conn.close()

def delete_history(date):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = '''
            DELETE
            FROM history
            WHERE date = {}
        ''' .format(date)
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()

        return all_rows

def deleteAllHistory():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = '''
            DELETE
            FROM history
        ''' 
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()

        if cursor.rowcount < 1:
               return  "History is emptry."
        else:
               return "Histories deleted successfully."


def add_data(date,title,links):
        add_history(date,title,links)
	
def get_data():
        return get_histories()

def deleteAll():
        deleteAllHistory()

def show_data():
        histories = get_data()
        return histories

def show_data_by_data(data):
        histories = get_history_by_data(data)
        if not histories:
                return "No data found"
        else:
                return histories
