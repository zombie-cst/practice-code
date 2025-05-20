from database_ar.db_automobiles_rental import get_connection
class Booking:
    def __init__(self, id=None, dateIssue=None, returnDate=None, addres=None, automobiles_id=None, clients_id=None):
        self.id = id
        self.dateIssue = dateIssue
        self.returnDate = returnDate
        self.addres = addres
        self.automobiles_id = automobiles_id
        self.clients_id = clients_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''INSERT INTO Booking(dateIssue, returnDate, addres, automobiles_id, clients_id)
                        VALUES(?, ?, ?, ?, ?)''',
                        (self.dateIssue, self.returnDate, self.addres, self.automobiles_id, self.clients_id))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Booking SET dateIssue = ?, returnDate = ?, addres = ?, automobiles_id = ?, clients_id = ?''',
                        (self.dateIssue, self.returnDate, self.addres, self.automobiles_id, self.clients_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Booking WHERE id = ?''', (self.id,))
            conn.commit()
            conn.close()

def get_all_booking():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, dateIssue, returnDate, addres, automobiles_id, clients_id FROM Booking''')
    rows = cur.fetchall()
    conn.close()
    return [Booking(id=row[0], dateIssue=row[1], returnDate=row[2], addres=row[3], automobiles_id=row[4], clients_id=row[5])
            for row in rows ]
    
def get_booking_by_id(booking_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT id, dateIssue, returnDate, addres, automobiles_id, clients_id FROM Booking WHERE id = ?''', (booking_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Booking(id=row[0], dateIssue=row[1], returnDate=row[2], addres=row[3], automobiles_id=row[4], clients_id=row[5])
    return None