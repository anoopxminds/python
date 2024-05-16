#Define an abstarct class Dbconnection with two abstarct methods connetToDb and diconnect
#Create 2 subclasses MySQL and Postgres which will implement these abstract methods

from abc import *

class Dbconnection:
    
    @abstractmethod
    def connetToDb(self):
        pass
    @abstractmethod
    def discunnect(self):
        pass
    
class MySQL(Dbconnection):
    def connetToDb(self):
        print("Connecting to mysql database.")
    def discunnect(self):
        print("Disconnecting mysql database.")
        
class Postgres(Dbconnection):
    def connetToDb(self):
        print("Connecting to Postgres database.")
        
    def discunnect(self):
        print("Disconnecting to Postgres database.")
        
database = input('Enter Database Name either MySQL or Postgres:')
sub_classname = globals()[database]
main = sub_classname()
main.connetToDb()
main.discunnect()
        
    
    