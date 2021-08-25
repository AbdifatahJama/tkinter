'''Module creates weightDatabase that adds and tracks user inputs of their weights'''

import sqlite3

class Database:
  def __init__(self):
    self.conn = sqlite3.connect('WeightDatabase.db') # Creates database if not exists and if exists the database is connected
    self.c = self.conn.cursor()
    # print('Connected to database')
    
  def create_table(self):
    '''Create table within database called Users'''
    self.c.execute('''CREATE TABLE WeightTable(current_date Text, user_weight Integer)''')
    self.conn.commit()
    self.conn.close()
    print('Table created within database')
    
  def add_user(self,date,weight):
    '''Add user to database'''
    self.c.execute('''INSERT INTO WeightTable Values(?,?)''',(date,weight))
    self.conn.commit()
    self.conn.close()
    print('Weight added')
    
  def get_all_rows(self):
    self.c.execute('''SELECT * FROM WeightTable''')
    return self.c.fetchall() # Returns all rows in list
  
  def delete_row(self,row):
    self.c.execute('DELETE FROM WeightTable WHERE rowid = ?',(row,))
    self.conn.commit()
    self.conn.close()
  
  def drop_table(self):
    '''drops table from database'''
    self.c.execute('''DROP TABLE WeightTable''')  
    print('Drop table')

d = Database()
# d.create_table() # Creates table within database called WeightTable 
# d.drop_table()

# list = d.get_all_rows()
# print(type(list))
# for a,b in list:
#   print(a)
#   print(b)



  





