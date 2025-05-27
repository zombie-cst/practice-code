from database_ar.db_automobiles_rental import get_connection

class Clients:
    def __init__(self, id=None, first_name=None, last_name=None,
                 patronymic=None, addres=None, phone_number=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.addres = addres
        self.phone_number = phone_number

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''INSERT INTO Clients(first_name, last_name,
                        patronymic, addres, phone_number)
                        VALUES(?, ?, ?, ?, ?)''',
                        (self.first_name, self.last_name, self.patronymic,
                         self.addres, self.phone_number))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Clients SET first_name = ?, last_name = ?,
                        patronymic = ?, addres = ?, phone_number = ?''',
                        (self.first_name, self.last_name, self.patronymic,
                         self.addres, self.phone_number))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Clients WHERE id = ?''', (self.id,))
            conn.commit()
            conn.close()

def get_all_clients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, first_name, last_name, patronymic,
                addres, phone_number FROM Clients''')
    rows = cur.fetchall()
    conn.close()
    return [Clients(id=row[0], first_name=row[1], last_name=row[2],
                    patronymic=row[3], addres=row[4], phone_number=row[5])
            for row in rows]