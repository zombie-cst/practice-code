from database_ar.db_automobiles_rental import get_connection
class Automobiles:
    def __init__(self, id, brand, model, yearRelease, fuel, 
                 speed, color, price, bodyType_id):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__yearRelease = yearRelease
        self.__fuel = fuel
        self.__speed = speed
        self.__color = color
        self.__price = price
        self.__bodyType_id = bodyType_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursot()
        if self.__id is None:
            cur.execute('''INSERT INTO Automobiles(brand, model, yearRelease,
                        fuel, speed, color, price, bodyType_id)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (self.__brand, self.__model, self.__yearRelease, self.__fuel,
                         self.__speed, self.__color, self.__price, self.__bodyType_id))
            self.__id = cur.lastrowid
        else:
            cur.execute('''UPDATE Automobiles SET brand = ?, model = ?, yearRelease = ?,
                        fuel = ?, speed = ?, color = ?, price = ?, bodyType_id = ?''',
                        (self.__brand, self.__model, self.__yearRelease, self.__fuel,
                         self.__speed, self.__color, self.__price, self.__bodyType_id))
            conn.commit()
            conn.close()

    def delete(self):
        if self.__id is None:
            conn = get_connection()
            cur = conn.cursot()
            cur.execute('''DELETE FROM Automobiles WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_automobiles():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT id, brand, model, yearRelease, fuel, speed, 
                       color, price, bodyType_id FROM Automobiles''')
        rows = cur.fetchall()
        conn.close()
        return [Automobiles(id=row[0], brand=row[1], model=row[2], yearRelease=row[3], fuel=row[4], 
                            speed=row[5], color=row[6], price=row[7], bodyType_id=row[8])
                for row in rows ]