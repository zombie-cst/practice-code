from database.db_automobiles_rental import initialize_db
class BodyType:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def save(self):
        conn = initialize_db()
        cur = conn.cursot()
        if self.__id is None:
            cur.execute('''INSERT INTO BodyType(name) VALUES(?)''', (self.__name,))
            self.__id = cur.lastrowid
        else:
            cur.execute('''UPDATE BodyType SET name = ?''', (self.__name,))
            conn.commit()
            conn.close()

    def delete(self):
        if self.__id is None:
            conn = initialize_db()
            cur = conn.cursot()
            cur.execute('''DELETE FROM BodyType WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_bodytype():
        conn = initialize_db()
        cur = conn.cursor()
        cur.execute('''SELECT id, name, FROM BodyType''')
        rows = cur.fetchall()
        conn.close()
        return [BodyType(id=row[0], name=row[1])
                for row in rows ]