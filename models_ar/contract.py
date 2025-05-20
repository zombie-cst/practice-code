from database_ar.db_automobiles_rental import get_connection
class Contract:
    def __init__(self, id=None, rules=None, discounts=None, booking_id=None):
        self.id = id
        self.rules = rules
        self.discounts = discounts
        self.booking_id = booking_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''INSERT INTO Contract(rules, discounts, booking_id)
                        VALUES(?, ?, ?)''',
                        (self.rules, self.discounts, self.booking_id))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE Contract SET rules = ?, discounts = ?, booking_id = ?''',
                        (self.rules, self.discounts, self.booking_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Contract WHERE id = ?''', (self.id,))
            conn.commit()
            conn.close()

def get_all_contract():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT id, rules, discounts, booking_id FROM Contract''')
    rows = cur.fetchall()
    conn.close()
    return [Contract(id=row[0], rules=row[1], discounts=row[2], booking_id=row[3])
            for row in rows ]
    
def get_contract_by_id(contract_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT id, rules, discounts, booking_id FROM Contract WHERE id = ?''', (contract_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Contract(id=row[0], rules=row[1], discounts=row[2], booking_id=row[3])
    return None