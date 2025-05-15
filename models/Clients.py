from database.db_automobiles_rental import initialize_db
class Clients:
    def __init__(self, id, firstName, lastName, patronymic, addres, phoneNumber):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__patronymic = patronymic
        self.__addres = addres
        self.__phoneNumber = phoneNumber
    
    def save(self):
        conn = initialize_db()
        cur = conn.cursot()
        if self.__id is None:
            cur.execute('''INSERT INTO Clients(firstName, lastName,
                        patronymic, addres, phoneNumber)
                        VALUES(?, ?, ?, ?, ?)''',
                        (self.__firstName, self.__lastName, self.__patronymic,
                         self.__addres, self.__phoneNumber))
            self.__id = cur.lastrowid
        else:
            cur.execute('''UPDATE Clients SET firstName = ?, lastName = ?,
                        patronymic = ?, addres = ?, phoneNumber = ?''',
                        (self.__firstName, self.__lastName, self.__patronymic,
                         self.__addres, self.__phoneNumber))
            conn.commit()
            conn.close()

    def delete(self):
        if self.__id is None:
            conn = initialize_db()
            cur = conn.cursot()
            cur.execute('''DELETE FROM Clients WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_clients():
        conn = initialize_db()
        cur = conn.cursor()
        cur.execute('''SELECT id, firstName, lastName, patronymic, addres,
                    phoneNumber FROM Clients''')
        rows = cur.fetchall()
        conn.close()
        return [Clients(id=row[0], firstName=row[1], lastName=row[2],
                            patronymic=row[3], addres=row[4], phoneNumber=row[5])
                for row in rows ]
    
    def get_clients_by_id(clients_id):
        conn = initialize_db()
        cur = conn.cursor()
        cur.execute('''SELECT id, firstName, lastName, patronymic, addres,
                    phoneNumber FROM Clients WHERE id = ?''', (clients_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            Clients(id=row[0], firstName=row[1], lastName=row[2],
                        patronymic=row[3], addres=row[4], phoneNumber=row[5])
        return None