class Person:
   '''
   name str
   register str - cpf/cnpj
   birth date
   '''
   def __init__(self, name, register, birth):
      self.name = name
      self.register = register
      self.birth = birth
   def __str__(self):
      return "name='%s', register='%s', birth='%s'" % (self.name, self.register, self.birth)

class Costumer:
   '''
   address dict - key = str description, value = object Address
   phones dict - key = str description, value = str phone number
   '''
   def __init__(self, name, register, birth, address, phones):
      Person.__init__(self, name, register, birth)
      self.address = address
      self.phones = phones

   def __str__(self):
      return "%s, address=%s, phones=%s" % (Person.__str__(self), self.address, self.phones)

class Address:
   def __init__(self, street, neighb, city, state, zipcode):
      self.street = street
      self.neighb = neighb
      self.city = city
      self.state = state
      self.zipcode = zipcode

   def __str__(self):
      return "street='%s', neighb='%s', city='%s', state='%s', zipcode='%s'"\
             %(self.street, self.neighb, self.city, self.state, self.zipcode)
