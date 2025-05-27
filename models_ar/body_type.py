from database_ar.db_automobiles_rental import get_connection

class BodyType:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def save(self):
        if self.id is None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''INSERT INTO BodyType(name) VALUES(?)''',
                        (self.name,))
            conn.commit()
            conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM BodyType WHERE id = ?''',
                        (self.id,))
            conn.commit()
            conn.close()

def get_all_body_type():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, name FROM BodyType''')
    rows = cur.fetchall()
    conn.close()
    return [BodyType(id=row[0], name=row[1]) for row in rows]