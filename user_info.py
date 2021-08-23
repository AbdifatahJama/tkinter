import sqlite3
from cryptography.fernet import Fernet
import hashlib

key = Fernet.generate_key() # Genarates unique key
f  = Fernet(key) # uses key to instantiate Fernet object

'''Password is in database should all be hashed or encrpyted'''

class Database:
  def __init__(self):
    self.conn = sqlite3.connect('AppDatabase.db')
    self.c = self.conn.cursor()
    # print('Connected to database')
    
  def create_table(self):
    '''Create table within database called Users'''
    self.c.execute('''CREATE TABLE Users(Email_address Text,Username Text, User_password Text)''')
    self.conn.commit()
    self.conn.close()
    print('Table created within database')
    
  def add_user(self,email_address = '',username = '',password = ''):
    '''Add user to database'''
    self.c.execute('''INSERT INTO Users Values(?,?,?)''',(email_address,username,password))
    self.conn.commit()
    self.conn.close()
    
  def get_all_rows(self):
    self.c.execute('''SELECT rowid,* FROM Users''')
    return self.c.fetchall() # Returns all rows in list
  
  def delete_row(self,row):
    self.c.execute('DELETE FROM Users WHERE rowid = ?',(row,))
    self.conn.commit()
    self.conn.close()
  
  def find_if_data_exist(self):
    '''Finds if username and password exist in database'''
    pass
    
d = Database()
# d.add_user('JamesManning1@gmail.com','CaliforniaDreamer1','Ronaldo81.')

  
  