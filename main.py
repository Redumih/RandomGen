import string
import random

longitud = int(input("Introduza el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.punctuation + string.digits

password = "".join(random.choice(caracteres) for i in range (longitud))

print ("La contraseña es: " + password)