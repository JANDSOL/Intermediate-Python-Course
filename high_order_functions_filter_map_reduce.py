"""Example of high order functions"""

def saludo(func):
	func()

def hola():
	print('Hola!!!')

def adios():
	print('Adios!!!')


if __name__ == '__main__':
	saludo(hola)
	saludo(adios)
