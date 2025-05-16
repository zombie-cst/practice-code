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
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                yearRelease INTEGER NOT NULL,
                fuel TEXT NOT NULL,
                speed REAL NOT NULL,
                color TEXT NOT NULL,
                price REAL NOT NULL,
                bodyType_id INTEGER,
                FOREIGN KEY (bodyType_id) REFERENCES BodyType(id))''')
    #Создание таблицы "Клиенты"
    cur.execute('''CREATE TABLE IF NOT EXISTS Clients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT NOT NULL,
                lastName TEXT NOT NULL,
                patronymic TEXT NOT NULL,
                addres TEXT NOT NULL,
                phoneNumber TEXT NOT NULL)''')
    #Создание таблицы "Бронирование"
    cur.execute('''CREATE TABLE IF NOT EXISTS Booking(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dateIssue TEXT NOT NULL,
                returnDate TEXT NOT NULL,
                addres TEXT NOT NULL,
                automobiles_id INTEGER,
                clients_id INTEGER,
                FOREIGN KEY (automobiles_id) REFERENCES Automobiles(id),
                FOREIGN KEY (clients_id) REFERENCES Clients(id))''')
    #Создание таблицы "Договор"
    cur.execute('''CREATE TABLE IF NOT EXISTS Contract(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                rules TEXT NOT NULL,
                discounts TEXT NOT NULL,
                finalPrice REAL NOT NULL,
                booking_id INTEGER,
                FOREIGN KEY (booking_id) REFERENCES Booking(id))''')
    conn.commit()
    conn.close()