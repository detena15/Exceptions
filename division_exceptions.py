"""
Error handling. The def is a division.
The code analise some exceptions and save the data in a log file called error.txt.
"""
import traceback
from datetime import datetime


def division(x, y):
    try:
        z = x/y
        return z
    except ZeroDivisionError:
        with open("error.txt", "a") as f:
            f.write(f'{datetime.today()}\n')
            traceback.print_exc(file=f)
            f.write("\n")
            f.close()
    except TypeError:
        with open("error.txt", "a") as f:
            f.write(f'{datetime.today()}\n')
            traceback.print_exc(file=f)
            f.write("\n")
            f.close()
    except:
        with open("error.txt", "a") as f:
            f.write(f'{datetime.today()}\n')
            traceback.print_exc(file=f)
            f.write("\n")
            f.close()


while True:
    try:
        divisor = float(input("Divisor: "))
        break
    except ValueError:
        print("Debes introducir un número!")

while True:
    try:
        dividendo = float(input("Dividendo: "))
        break
    except ValueError:
        print("Debes introducir un número!")


resultado = division(x=divisor, y=dividendo)

if type(resultado) == float:
    print("El resultado es: ", resultado)
else:
    print("Hubo un error! Revisar el fichero error.txt")

