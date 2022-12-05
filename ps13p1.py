#define the object
class Employee:
  #use pass to leave empty for now 
  def __init__(self, first, last, pay):
    self.first=first
    self.last=last
    self.pay=pay
    self.email=first+ '.' +last+ '@company.com'

  def bonus(self, rate):
    bo=float(rate)*float(self.pay)
    return bo
#main - execution begins here 
#instantiate the object
empi1=Employee('Munkhjin', 'Galdandorj', 98000.00)

#use the object 
#object syntax is object method
print(empi1.email)
print(empi1.first)
print(empi1.last)
print(empi1.pay)
print(empi1.bonus(0.10))
print(empi1.bonus(0.20))