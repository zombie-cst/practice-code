from database_ar.db_automobiles_rental import get_connection

class Booking:
    def __init__(self, id=None, date_issue=None, return_date=None,
                 addres=None, automobiles_id=None, clients_id=None):
        self.id = id
        self.date_issue = date_issue
        self.return_date = return_date
        self.addres = addres
        self.automobiles_id = automobiles_id
        self.clients_id = clients_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is not None:
            cur.execute('''INSERT INTO Booking(date_issue, return_date,
                        addres, automobiles_id, clients_id)
                        VALUES(?, ?, ?, ?, ?)''',
                        (self.date_issue, self.return_date, self.addres,
                         self.automobiles_id, self.clients_id))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Booking SET date_issue = ?, return_date = ?,
                        addres = ?, automobiles_id = ?, clients_id = ?''',
                        (self.date_issue, self.return_date, self.addres,
                         self.automobiles_id, self.clients_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Booking WHERE id = ?''',
                        (self.id,))
            conn.commit()
            conn.close()

def get_all_booking():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, date_issue, return_date, addres,
                automobiles_id, clients_id FROM Booking''')
    rows = cur.fetchall()
    conn.close()
    return [Booking(id=row[0], date_issue=row[1], return_date=row[2],
                    addres=row[3], automobiles_id=row[4], clients_id=row[5])
            for row in rows]