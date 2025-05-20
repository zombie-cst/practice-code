from database_ar.db_automobiles_rental import get_connection
class Clients:
    def __init__(self, id=None, firstName=None, lastName=None, patronymic=None, addres=None, phoneNumber=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.patronymic = patronymic
        self.addres = addres
        self.phoneNumber = phoneNumber
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''INSERT INTO Clients(firstName, lastName, patronymic, addres, phoneNumber)
                        VALUES(?, ?, ?, ?, ?)''',
                        (self.firstName, self.lastName, self.patronymic, self.addres, self.phoneNumber))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Clients SET firstName = ?, lastName = ?, patronymic = ?, addres = ?, phoneNumber = ?''',
                        (self.firstName, self.lastName, self.patronymic, self.addres, self.phoneNumber))
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
    cur.execute('''SELECT id, firstName, lastName, patronymic, addres, phoneNumber FROM Clients''')
    rows = cur.fetchall()
    conn.close()
    return [Clients(id=row[0], firstName=row[1], lastName=row[2], patronymic=row[3], addres=row[4], phoneNumber=row[5])
            for row in rows ]

def get_clients_by_id(clients_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT id, firstName, lastName, patronymic, addres, phoneNumber FROM Clients WHERE id = ?''', (clients_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Clients(id=row[0], firstName=row[1], lastName=row[2], patronymic=row[3], addres=row[4], phoneNumber=row[5])
    return None