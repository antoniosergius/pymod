class Person:
   '''pid int, name str, register str, birth date'''
   def __init__(self, pid, name, register, birth):
      self.pid = pid
      self.name = name
      self.register = register
      self.birth = birth
   def __str__(self):
      return "pid='%d', name='%s', register='%s', birth='%s'" %
             (self.pid, self.name, self.register, self.birth)

class Costumer:
   '''
   address dict - key = str description, value = object Address
   phones dict - key = str description, value = str phone number
   '''
   def __init__(self, pid, name, register, birth, address, phones):
      Person.__init__(self, pid, name, register, birth)
      self.address = address
      self.phones = phones

   def __str__(self):
      return "%s, address=%s, phones=%s" %
             (Person.__str__(self), self.address, self.phones)

class Address:
   '''street str, neighb str, city str, state str, zipcode str'''
   def __init__(self, street, neighb, city, state, zipcode):
      self.street = street
      self.neighb = neighb
      self.city = city
      self.state = state
      self.zipcode = zipcode

   def __str__(self):
      return "street='%s', neighb='%s', city='%s', state='%s', zipcode='%s'" %
             (self.street, self.neighb, self.city, self.state, self.zipcode)
