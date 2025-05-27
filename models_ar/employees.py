from database_ar.db_automobiles_rental import get_connection

class Employees: 
    def __init__(self, id=None, first_name=None, last_name=None,
                 patronymic=None, phone_number=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is not None:
            cur.execute('''INSERT INTO Employees(first_name, last_name,
                        patronymic, phone_number)
                        VALUES(?, ?, ?, ?)''',
                        (self.first_name, self.last_name, self.patronymic,
                         self.phone_number))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Employees SET first_name = ?, last_name = ?,
                        patronymic = ?, phone_number = ?''',
                        (self.first_name, self.last_name, self.patronymic,
                         self.phone_number))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Employees WHERE id = ?''', (self.id,))
            conn.commit()
            conn.close()

def get_all_employees():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, first_name, last_name, patronymic,
                phone_number FROM Employees''')
    rows = cur.fetchall()
    conn.close()
    return [Employees(id=row[0], first_name=row[1], last_name=row[2],
                    patronymic=row[3], phone_number=row[4])
            for row in rows]