import sqlite3
from database_ar.config import BD_NAME

def get_connection():
    return sqlite3.connect(BD_NAME)

def initialize_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS BodyType(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Automobiles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year_release INTEGER NOT NULL,
                fuel TEXT NOT NULL,
                color TEXT NOT NULL,
                price REAL NOT NULL,
                body_type_id INTEGER,
                FOREIGN KEY (body_type_id) REFERENCES BodyType(id))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Clients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                patronymic TEXT NOT NULL,
                addres TEXT NOT NULL,
                phone_number TEXT NOT NULL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Booking(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_issue TEXT NOT NULL,
                return_date TEXT NOT NULL,
                addres TEXT NOT NULL,
                automobiles_id INTEGER,
                clients_id INTEGER,
                FOREIGN KEY (automobiles_id) REFERENCES Automobiles(id),
                FOREIGN KEY (clients_id) REFERENCES Clients(id))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Contract(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rules TEXT NOT NULL,
                discounts TEXT NOT NULL,
                booking_id INTEGER,
                FOREIGN KEY (booking_id) REFERENCES Booking(id))''')
    conn.commit()
    conn.close()