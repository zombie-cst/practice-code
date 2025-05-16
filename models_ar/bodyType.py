from database_ar.db_automobiles_rental import get_connection
class BodyType:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def save(self):
        if self.__id is None:
            conn = get_connection()
            cur = conn.cursot()
            cur.execute('''INSERT INTO BodyType(name) VALUES(?)''', (self.__name,))
            conn.commit()
            conn.close()

    def delete(self):
        if self.__id is None:
            conn = get_connection()
            cur = conn.cursot()
            cur.execute('''DELETE FROM BodyType WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_bodytype():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT id, name, FROM BodyType''')
        rows = cur.fetchall()
        conn.close()
        return [BodyType(id=row[0], name=row[1])
                for row in rows ]