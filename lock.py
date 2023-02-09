from cryptography.fernet import Fernet
import os 

#FUNCION PARA GENERAR CLAVE 
def genera_clave(name):
	clave = Fernet.generate_key()
	with open(name +'.key',"wb") as archivo_clave:
		archivo_clave.write(clave)

#FUNCION PARA CARGAR LA CLAVE 
def cargar_clave(key):
	return open(key,"rb").read()


#FUNCION PARA ENCRIPTAR ARCHIVOS 
def encript(nom_archivo,clave):
	f = Fernet(clave)
	with open(nom_archivo, "rb")as file:
		archivo_info = file.read()
	encrypted_date =f.encrypt(archivo_info)
	with open(nom_archivo, "wb") as file:
		file.write(encrypted_date)

#FUNCION PARA DESENCRIPTAR ARCHIVOS 
def desencript(nom_archivo,clave):
	f = Fernet(clave)
	with open(nom_archivo, "rb") as file:
		encrypted_data = file.read()
	decrypted_data = f.decrypt(encrypted_data)
	with open(nom_archivo, "wb") as file:
		file.write(decrypted_data)

#FUNCION PARA LIMPIAR LA TERMINAL
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

i = 1
while (i !=0):
	clear()
	print(" _                  _      ______   _   _        ")
	print("| |                | |    |  ____| (_) | |       ")
	print("| |   ___     ___  | | __ | |__     _  | |   ___ ")
	print("| |  / _ \   / __| | |/ / |  __|   | | | |  / _  ")
	print("| | | (_) | | (__  |   <  | |      | | | | |  __/")
	print("|_|  \___/   \___| |_|\_\ |_|      |_| |_|  \___|")
	print("                                                    v1.1")
	print("---------------------------------------------------------")
	print("Que desea hacer")
	print("---------------------------------------------------------")
	print("1.Encriptar archivo")
	print("2.Desencriptar archivo")
	print("3.Generar Hash")
	print("----------------------------------------------------------")
	print("                                   [Control + c] -> Cerrar")
	print("----------------------------------------------------------")
	op = int(input())
	if op == 1:
		print("Elija el archivo con la clave de encryptacion")
		key= input()
		clave = cargar_clave(key)
		print("Que archivo va a encryptar")
		nom_archivo = input()
		encript(nom_archivo,clave)
	elif op == 2:
		print("Elija el archivo con la clave de encryptacion")
		key= input()
		clave = cargar_clave(key)
		print("Que archivo va a desencriptar")
		nom_archivo = input()
		desencript(nom_archivo,clave)
	else:
		print("Nombre para la clave")
		name = input()
		genera_clave(name)
	