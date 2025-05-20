from database_ar.db_automobiles_rental import get_connection
class Automobiles:
    def __init__(self, id=None, brand=None, model=None, yearRelease=None, fuel=None, color=None, price=None, bodyType_id=None):
        self.id = id
        self.brand = brand
        self.model = model
        self.yearRelease = yearRelease
        self.fuel = fuel
        self.color = color
        self.price = price
        self.bodyType_id = bodyType_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''INSERT INTO Automobiles(brand, model, yearRelease, fuel, color, price, bodyType_id)
                        VALUES(?, ?, ?, ?, ?, ?, ?)''',
                        (self.brand, self.model, self.yearRelease, self.fuel, self.color, self.price, self.bodyType_id))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Automobiles SET brand = ?, model = ?, yearRelease = ?, fuel = ?, color = ?, price = ?, bodyType_id = ?''',
                        (self.brand, self.model, self.yearRelease, self.fuel, self.color, self.price, self.bodyType_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Automobiles WHERE id = ?''', (self.id,))
            conn.commit()
            conn.close()

def get_all_automobiles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, brand, model, yearRelease, fuel, color, price, bodyType_id FROM Automobiles''')
    rows = cur.fetchall()
    conn.close()
    return [Automobiles(id=row[0], brand=row[1], model=row[2], yearRelease=row[3], fuel=row[4], color=row[5], price=row[6], bodyType_id=row[7])
            for row in rows ]

def get_automobiles_by_id(automobiles_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT id, brand, model, yearRelease, fuel, color, price, bodyType_id FROM Automobiles WHERE id = ?''', (automobiles_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Automobiles(id=row[0], brand=row[1], model=row[2], yearRelease=row[3], fuel=row[4], color=row[5], price=row[6], bodyType_id=row[7])
    return None