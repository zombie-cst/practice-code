import sqlite3
def initialize_db():
    conn = sqlite3.connect('system_of_events.db')
    cur = conn.cursor()
    
    #Создание таблицы "Тип кузова"
    cur.execute('''CREATE TABLE IF NOT EXISTS BodyType(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT)''')
    
    #Создание таблицы "Автомобили"
    cur.execute('''CREATE TABLE IF NOT EXISTS Automobiles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Brand TEXT,
                Model TEXT,
                YearRelease INTEGER,
                Fuel TEXT,
                Speed REAL,
                TransmissionBox TEXT,
                Drive TEXT,
                Color TEXT,
                Price REAL,
                BodyType_id INTEGER,
                FOREIGN KEY (BodyType_id) REFERENCES BodyType(id))''')
    
    #Создание таблицы "Клиенты"
    cur.execute('''CREATE TABLE IF NOT EXISTS Customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName TEXT,
                LastName TEXT,
                Patronymic TEXT,
                Addres TEXT,
                PhoneNumber TEXT,
                Email TEXT)''')
    
    #Создание таблицы "Сотрудники"
    cur.execute('''CREATE TABLE IF NOT EXISTS Employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName TEXT,
                LastName TEXT,
                Patronymic TEXT,
                PhoneNumber TEXT,
                Email TEXT)''')

    #Создание таблицы "Бронирование"
    cur.execute('''CREATE TABLE IF NOT EXISTS Booking(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                DateIssue TEXT,
                ReturnDate TEXT,
                Addres TEXT,
                Automobiles_id INTEGER,
                Customers_id INTEGER,
                Employees_id INTEGER,
                FOREIGN KEY (Automobiles_id) REFERENCES Automobiles(id),
                FOREIGN KEY (Customers_id) REFERENCES Customers(id),
                FOREIGN KEY (Employees_id) REFERENCES Employees(id))''')
    
    #Создание таблицы "Договор"
    cur.execute('''CREATE TABLE IF NOT EXISTS Contract(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Date TEXT,
                Rules TEXT,
                Discounts TEXT,
                FinalPrice REAL,
                Booking_id INTEGER,
                FOREIGN KEY (Booking_id) REFERENCES Booking(id))''')
    conn.commit()
    conn.close()