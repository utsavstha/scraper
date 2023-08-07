import mysql.connector
from share_model import ShareModel
class DatabaseConnector:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="nepalinvestx-db.c6jzsecgskjq.us-east-1.rds.amazonaws.com",
            user="nepalinvestx",
            password="RnaEa3uTt7aTxaCk"
        )
        self.cursor = self.db.cursor()


    def insert(self, share_model: [tuple]):
        query = '''INSERT INTO nepalinvestx.db_shareprice 
        (db_shareprice_date, db_shareprice_symbol, 
        db_shareprice_ltp, db_shareprice_change, 
        db_shareprice_high, db_shareprice_low, 
        db_shareprice_open, db_shareprice_qty, db_shareprice_turnover) 
        VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)'''
        self.cursor.executemany(query, share_model)
        self.db.commit()