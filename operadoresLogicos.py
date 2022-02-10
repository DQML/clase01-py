from turtle import color
from unicodedata import numeric


number = 50

#print(number == 50 and number > 60)
#print(color == "red" or color == "blue")

color = "yellow"

def comprar():
  if color == "red" or color == "blue":
     return "compralo"
  else:
     return "no comprar"

#print(comprar())

print(not number == 40)