#define the object
class student:
  #use pass to leave empty for now
  def __init__(self, first, last,dcode,credits):
    self.first=first
    self.last=last
    self.dcode=dcode
    self.credits=credits

  def tuition(self,dcode,credits):
    if dcode=="I":
      t=250.00*int(self.credits)
    else:
      t=500.00*int(self.credits)
    return t
#main-execution begins here 
#instantiate the object
stu1=student('Galdandorj', 'Munkhjin','I',120)

#use the object
#object syntax is object method
print(stu1.first)
print(stu1.last)
print(stu1.tuition("I",120))
