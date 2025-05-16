from database_ar.db_automobiles_rental import get_connection
class Booking:
    def __init__(self, id, dateIssue, returnDate, addres, 
                 automobiles_id, clients_id, employees_id):
        self.__id = id
        self.__dateIssue = dateIssue
        self.__returnDate = returnDate
        self.__addres = addres
        self.__automobiles_id = automobiles_id
        self.__clients_id = clients_id
        self.__employees_id = employees_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.__id is None:
            cur.execute('''INSERT INTO Booking(dateIssue, returnDate, addres,
                        automobiles_id, clients_id, employees_id)
                        VALUES(?, ?, ?, ?, ?, ?)''',
                        (self.__dateIssue, self.__returnDate, self.__addres, self.__automobiles_id,
                         self.__clients_id, self.__employees_id))
            self.__id = cur.lastrowid
        else:
            cur.execute('''UPDATE Booking SET dateIssue = ?, returnDate = ?, addres = ?,
                        automobiles_id = ?, clients_id = ?, employees_id = ?''',
                        (self.__dateIssue, self.__returnDate, self.__addres, self.__automobiles_id,
                         self.__clients_id, self.__employees_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.__id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Booking WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_booking():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT id, dateIssue, returnDate, addres, automobiles_id,
                    clients_id, employees_id FROM Booking''')
        rows = cur.fetchall()
        conn.close()
        return [Booking(id=row[0], dateIssue=row[1], returnDate=row[2], addres=row[3],
                        automobiles_id=row[4], clients_id=row[5], employees_id=row[6])
                for row in rows ]
    
    def get_booking_by_id(booking_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, dateIssue, returnDate, addres, automobiles_id,
                    clients_id, employees_id FROM Booking WHERE id = ? """, (booking_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Booking(id=row[0], dateIssue=row[1], returnDate=row[2], addres=row[3],
                           automobiles_id=row[4], clients_id=row[5], employees_id=row[6])
        return None