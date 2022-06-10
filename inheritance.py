from typing_extensions import Self
from unicodedata import name


class person:
 def _init_(self,fname,lname):
  self.firstname = fname
  Self.lastname = lname

  def printname(self):
      print(self.firstname , self.lastname)

 
x = person("Nyawera", "Tut")
x.printname()