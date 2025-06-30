class ind():
    def capital(self):
       print ("New Delhi is the capital")
    def lan(self):
       print ("Hindi is India's most spoken language")
    def type(self):
       print ("India is a developing country")

class usa():
   def capital(self):
      print ("Washington D.C. is America's capital")
   def lan(self):
      print ("English is America's most spoken language")
   def type(self):
      print ("America is a developed country")

obj_i = ind()
obj_usa = usa()
for country in (obj_i, obj_usa):
   country.capital()
   country.lan()
   country.type()
