# Калькуль

from colorama import Fore, Back
from colorama import init

init()

print( Fore.BLACK )
print( Back.RED )

what = input ( "Что выберешь? (+, -, *, /, ^): " )

print( Back.WHITE )

a = float( input( "Введи первое число: " ) )
b = float ( input( "Введи второе число: " ) )

print( Back.GREEN )

if what == "+":
	c = a + b
	print( "Результат: " + str(c))
elif what == "-":
	c = a - b
	print( "Результат: " + str(c))
elif what == "/":
	c = a / b
	print( "Результат: " + str(c))
elif what == "*":
	c = a * b
	print( "Результат: " + str(c))
elif what == "^":
	c = a ** b
	print( "Результат: " + str(c))

else: print( "Выбрана неверная операция!" )

input()