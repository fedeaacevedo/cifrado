from random import randint, uniform,random
import os

while True:
	abc_MAYUSCULA = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	abc_MINUSCULA = "abcdefghijklmnñopqrstuvwxyz"
	print("|==========================================|")
	print("|          Angel  y  Federico              |")
	print("|                                          |")
	print("|      Encriptacion y Desencriptacio       |")
	print("|==========================================|")
	print("|1-Encriptar                               |")
	print("|2-Desencriptar                            |")
	print("|3-Salir                                   |")
	print("|==========================================|")
	eleccion = int(input('|Introduce un numero: '))
	print("|==========================================|")
	if eleccion == 1:
		texto = input("|Mensaje a encriptar: ")
		print("|******************************************|")
		# Abecedario a utilizar en el cifrado
		# Variable para guardar mensaje cifrado
		cifrado = ""
		# Iteramos por cara letra del mensaje
		for l in texto:
			if l in abc_MAYUSCULA:
				pos_letra = abc_MAYUSCULA.index(l)
				nueva_pos = (pos_letra + 26) % len(abc_MAYUSCULA)
				cifrado+= abc_MAYUSCULA[nueva_pos]
			else:
				pos_letra = abc_MINUSCULA.index(l)
				nueva_pos = (pos_letra + 26) % len(abc_MINUSCULA)
				cifrado+= abc_MINUSCULA[nueva_pos]
		file = open("cifrafo.txt", "w")
		file.write(cifrado)
		file.close()
		print("|Mensaje cifrado:                          |")
		print("|", cifrado)
		print("|******************************************|")
	elif eleccion == 2:
	# abre el archivo cifrado.txt y lo guarda en en la variable texto2
		f = open ('cifrafo.txt')
		texto2 = f.read()
		f.close()
		descifrado = ""
		for a in str(texto2):
			if a in abc_MAYUSCULA:
				pos_letra = abc_MAYUSCULA.index(a)
				nueva_pos = (pos_letra + 28) % len(abc_MAYUSCULA)
				descifrado+= abc_MAYUSCULA[nueva_pos]
			else:
				pos_letra = abc_MINUSCULA.index(a)
				nueva_pos = (pos_letra + 28) % len(abc_MINUSCULA)
				descifrado+= abc_MINUSCULA[nueva_pos]
		print("|==========================================|")
		print('|Mensaje Desifrado:                        |')
		print('|', descifrado)
		print("|==========================================|")
	elif eleccion == 3:
		break
	else:
		print("Numero invalido")
	print("\n\n")


