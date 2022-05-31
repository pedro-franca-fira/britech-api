import pyodbc
class Database():
  def __init__(self, driver, server, database, user, password):
    self.driver = driver
    self.server = server
    self.database = database
    self.user = user
    self.password = password
    self.conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(self.driver, self.server, self.database, self.user,self.password))
    self.cursor = self.conn.cursor()


  def execute(self, query, parameters):
    self.cursor.execute(query, parameters)
    #self.cursor.commit()
    #self.cursor.close()
  def commit(self):
    self.conn.commit()

  def rollback(self):
    self.conn.rollback()
  
  def close(self):
    self.conn.close()