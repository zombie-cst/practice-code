from database.db_automobiles_rental import initialize_db
class Contract:
    def __init__(self, id, date, rules, discounts, finalPrice, booking_id):
        self.__id = id
        self.__date = date
        self.__rules = rules
        self.__discounts = discounts
        self.__finalPrice = finalPrice
        self.__booking_id = booking_id
    
    def save(self):
        conn = initialize_db()
        cur = conn.cursot()
        if self.__id is None:
            cur.execute('''INSERT INTO Contract(date, rules,
                        discounts, finalPrice, booking_id)
                        VALUES(?, ?, ?, ?, ?)''',
                        (self.__date, self.__rules, self.__discounts,
                         self.__finalPrice, self.__booking_id))
            self.__id = cur.lastrowid
        else:
            cur.execute('''UPDATE Contract SET date = ?, rules = ?,
                        discounts = ?, finalPrice = ?, booking_id = ?''',
                        (self.__date, self.__rules, self.__discounts,
                         self.__finalPrice, self.__booking_id))
            conn.commit()
            conn.close()

    def delete(self):
        if self.__id is None:
            conn = initialize_db()
            cur = conn.cursot()
            cur.execute('''DELETE FROM Contract WHERE id = ?''', (self.__id,))
            conn.commit()
            conn.close()

    def get_all_contract():
        conn = initialize_db()
        cur = conn.cursor()
        cur.execute('''SELECT id, date, rules, discounts, finalPrice,
                    booking_id FROM Contract''')
        rows = cur.fetchall()
        conn.close()
        return [Contract(id=row[0], date=row[1], rules=row[2],
                            discounts=row[3], finalPrice=row[4], booking_id=row[5])
                for row in rows ]
    
    def get_contract_by_id(contract_id):
        conn = initialize_db()
        cur = conn.cursor()
        cur.execute('''SELECT id, date, rules, discounts, finalPrice,
                    booking_id FROM Contract WHERE id = ?''', (contract_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            Contract(id=row[0], date=row[1], rules=row[2],
                        discounts=row[3], finalPrice=row[4], booking_id=row[5])
        return None