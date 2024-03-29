import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.c = self.con.cursor()
        # self.c.execute("""
        # DROP TABLE IF EXISTS subscription_management_system;
        # """)
        self.c.execute("""
                        CREATE TABLE IF NOT EXISTS subscription_management_system(
                        pid INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        registration_number TEXT NOT NULL,
                        start_of_subscription TEXT NOT NULL,
                        duration TEXT NOT NULL,
                        end_of_subscription TEXT NOT NULL,
                        city TEXT NOT NULL,
                        districts TEXT NOT NULL,
                        state TEXT NOT NULL,
                        address TEXT NOT NULL,
                        address_two TEXT NOT NULL,
                        mobile_number TEXT NOT NULL,
                        whatsapp_number TEXT NOT NULL,
                        email_address TEXT NOT NULL                    
                        )
                        """)
        self.con.commit()

    def insert(self, title, name, gender, registration_number, start_of_subscription, duration, end_of_subscription, city, districts, state, address, address_two, mobile_number, whatsapp_number, email_address):
        sql = """
            INSERT INTO subscription_management_system VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        print("SQL", sql)
        self.c.execute(sql, (title, name, gender, registration_number, start_of_subscription, duration, end_of_subscription, city, districts, state, address, address_two, mobile_number, whatsapp_number, email_address))
        self.con.commit()

    def fetch_record(self):
        self.c.execute("SELECT * FROM subscription_management_system")
        data = self.c.fetchall()
        return data

    def update_record(self, title, name, gender, registration_number, start_of_subscription, duration, end_of_subscription, city, districts, state, address, address_two, mobile_number, whatsapp_number, email_address, pid):
        sql = """
            UPDATE subscription_management_system SET title=?, name=?, gender=?, registration_number=?, start_of_subscription=?, duration=?, end_of_subscription=?, city=?, districts=?, state=?, address=?, address_two=?, mobile_number=?, whatsapp_number=?, email_address=? WHERE pid=?
        """
        self.c.execute(sql, (title, name, gender, registration_number, start_of_subscription, duration, end_of_subscription, city, districts, state, address, address_two, mobile_number, whatsapp_number, email_address, pid))
        self.con.commit()

    def remove_record(self, pid):
        sql = "DELETE FROM subscription_management_system WHERE pid=?"
        self.c.execute(sql, (pid,))
        self.con.commit()
