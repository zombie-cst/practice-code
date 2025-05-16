from database_ar.db_automobiles_rental import get_connection
class Clients:
    def __init__(self, id, firstName, lastName, patronymic, addres, phoneNumber):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__patronymic = patronymic
        self.__addres = addres
        self.__phoneNumber = phoneNumber
    
    def save(self):
        conn = get_connection()
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
            conn = get_connection()
            cur = conn.cursot()
            cur.execute('''DELETE FROM Clients WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_clients():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT id, firstName, lastName, patronymic, addres,
                    phoneNumber FROM Clients''')
        rows = cur.fetchall()
        conn.close()
        return [Clients(id=row[0], firstName=row[1], lastName=row[2],
                            patronymic=row[3], addres=row[4], phoneNumber=row[5])
                for row in rows ]