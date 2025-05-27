from database_ar.db_automobiles_rental import get_connection

class Automobiles:
    def __init__(self, id=None, brand=None, model=None, year_release=None,
                 fuel=None, color=None, price=None, body_type_id=None):
        self.id = id
        self.brand = brand
        self.model = model
        self.year_release = year_release
        self.fuel = fuel
        self.color = color
        self.price = price
        self.body_type_id = body_type_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is not None:
            cur.execute('''INSERT INTO Automobiles(brand, model,
                        year_release, fuel, color, price, body_type_id)
                        VALUES(?, ?, ?, ?, ?, ?, ?)''',
                        (self.brand, self.model, self.year_release,
                         self.fuel, self.color, self.price, self.body_type_id))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Automobiles SET brand = ?, model = ?,
                        year_release = ?, fuel = ?, color = ?, price = ?,
                        body_type_id = ?''',
                        (self.brand, self.model, self.year_release,
                         self.fuel, self.color, self.price, self.body_type_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Automobiles WHERE id = ?''',
                        (self.id,))
            conn.commit()
            conn.close()

def get_all_automobiles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, brand, model, year_release, fuel,
                color, price, body_type_id FROM Automobiles''')
    rows = cur.fetchall()
    conn.close()
    return [Automobiles(id=row[0], brand=row[1], model=row[2],
                        year_release=row[3], fuel=row[4], color=row[5],
                        price=row[6], body_type_id=row[7])
            for row in rows]