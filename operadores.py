from audioop import mul
from re import sub


numero1 = 2
numero2 = 4

mul = numero1 * numero2
sum = numero1 + numero2
sub = numero2 - numero1
div = numero2 / numero1

print(mul)
print(sum)
print(sub)
print(div)

edad = 25
edadLegal=18

resultado = 'Eres mayor de edad' if edad >= edadLegal else 'eres menor de edad'

print(resultado)