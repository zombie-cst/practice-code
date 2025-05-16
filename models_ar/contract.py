from database_ar.db_automobiles_rental import get_connection
class Contract:
    def __init__(self, id, rules, discounts, finalPrice, booking_id):
        self.__id = id
        self.__rules = rules
        self.__discounts = discounts
        self.__finalPrice = finalPrice
        self.__booking_id = booking_id
    
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.__id is None:
            cur.execute('''INSERT INTO Contract(rules,
                        discounts, finalPrice, booking_id)
                        VALUES(?, ?, ?, ?)''',
                        (self.__rules, self.__discounts,
                         self.__finalPrice, self.__booking_id))
            self.__id = cur.lastrowid
        else:
            cur.execute('''UPDATE Contract SET rules = ?,
                        discounts = ?, finalPrice = ?, booking_id = ?''',
                        (self.__rules, self.__discounts,
                         self.__finalPrice, self.__booking_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.__id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('''DELETE FROM Contract WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_contract():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT id, rules, discounts, finalPrice,
                    booking_id FROM Contract''')
        rows = cur.fetchall()
        conn.close()
        return [Contract(id=row[0], rules=row[1], discounts=row[2], 
                            finalPrice=row[3], booking_id=row[4])
                for row in rows ]
    
    def get_contract_by_id(contract_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, rules, discounts, finalPrice,
                    booking_id FROM Contract WHERE id = ? """, (contract_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Contract(id=row[0], rules=row[2], discounts=row[3],
                            finalPrice=row[4], booking_id=row[5])
        return None