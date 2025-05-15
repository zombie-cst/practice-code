import sqlite3
def initialize_db():
    conn = sqlite3.connect('system_of_events.db')
    cur = conn.cursor()
    
    #Создание таблицы "Тип кузова"
    cur.execute('''CREATE TABLE IF NOT EXISTS BodyType(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)''')
    
    #Создание таблицы "Автомобили"
    cur.execute('''CREATE TABLE IF NOT EXISTS Automobiles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Brand TEXT NOT NULL,
                Model TEXT NOT NULL,
                YearRelease INTEGER NOT NULL,
                Fuel TEXT NOT NULL,
                Speed REAL NOT NULL,
                TransmissionBox TEXT NOT NULL,
                Drive TEXT NOT NULL,
                Color TEXT NOT NULL,
                Price REAL NOT NULL,
                BodyType_id INTEGER,
                FOREIGN KEY (BodyType_id) REFERENCES BodyType(id))''')
    
    #Создание таблицы "Клиенты"
    cur.execute('''CREATE TABLE IF NOT EXISTS Customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Patronymic TEXT NOT NULL,
                Addres TEXT NOT NULL,
                PhoneNumber TEXT NOT NULL,
                Email TEXT NOT NULL)''')
    
    #Создание таблицы "Сотрудники"
    cur.execute('''CREATE TABLE IF NOT EXISTS Employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Patronymic TEXT NOT NULL,
                PhoneNumber TEXT NOT NULL,
                Email TEXT NOT NULL)''')

    #Создание таблицы "Бронирование"
    cur.execute('''CREATE TABLE IF NOT EXISTS Booking(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                DateIssue TEXT NOT NULL,
                ReturnDate TEXT NOT NULL,
                Addres TEXT NOT NULL,
                Automobiles_id INTEGER,
                Customers_id INTEGER,
                Employees_id INTEGER,
                FOREIGN KEY (Automobiles_id) REFERENCES Automobiles(id),
                FOREIGN KEY (Customers_id) REFERENCES Customers(id),
                FOREIGN KEY (Employees_id) REFERENCES Employees(id))''')
    
    #Создание таблицы "Договор"
    cur.execute('''CREATE TABLE IF NOT EXISTS Contract(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Date TEXT NOT NULL,
                Rules TEXT NOT NULL,
                Discounts TEXT NOT NULL,
                FinalPrice REAL NOT NULL,
                Booking_id INTEGER,
                FOREIGN KEY (Booking_id) REFERENCES Booking(id))''')
    conn.commit()
    conn.close()