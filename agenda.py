# holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ahora lo pude modificar!!!!


agenda = {'base':{'Nombre':'', 'Apellido':'', 'Edad':''}, 'RASTI': {'Nombre': 'Ale', 'Apellido': 'Fer', 'Edad': 33}, 'TUCRO': {'Nombre': 'Asado', 'Apellido': 'Asad', 'Edad': 55}}
print ("Aca boludeando con Ale")
lista_de_elementos = list(agenda['base'].keys())
#print(lista_de_elementos)
#print(lista_de_elementos[0])

def Cargar_datos():
	nick = input('Nick: ').upper()
	for elemento in lista_de_elementos:
		dato = input(f'ingrese el {elemento}: ').capitalize()
		#dato = {'Nombre' : nombre, 'Apellido': apellido, 'Edad' : edad}
		
		agenda[nick] = {elemento:dato}
		
	'''nick = input('Nick: ').upper()
	nombre = input('Nombre: ').capitalize()
	apellido = input('Apellido: ').capitalize()
	while True:
		try:
			edad = int(input('Edad: '))
			break
		except:
			print('Ingrese solo números')
	datos = {'Nombre' : nombre, 'Apellido': apellido, 'Edad' : edad}
	agenda[nick] = datos
'''
def Leer():
	for nicks in agenda:
		print(nicks, end=' ')
	while True:
		buscado = input ('ingrese el nick buscado (Z para salir): ').upper()
		if buscado in agenda:
			for datos in agenda[buscado]:
				print (f"{agenda[buscado]['Nombre']:<10}\t{agenda[buscado]['Apellido']:<10}\t{agenda[buscado]['Edad']:<10}")
				#print(f'nombre: {agenda[buscado]['nombre']}') 
				#print(f'agenda: {agenda[buscado]['Apellido']}') 
				#print(f'agenda: {agenda[buscado]['edad']}') 
				return (buscado, agenda[buscado])
				break
		elif buscado == 'Z':
			break
		else:
			print('Dato no agendado')

def Modificar():
	recepcionNick, Dic = Leer()
	print(recepcionNick, Dic)
	#opcion = input('Que desea modificar? 1:Nombre, 2:Apellido, 3:Edad')
	contador = 0
	
	for llaves in Dic:
		lista.append(llaves)
		print(f'{contador+1}-{lista[contador]}')
		contador += 1
	while True:
		try:
			opcion = int(input('ingrese que opcion quiere modificar'))
			if not(0 < opcion < len(lista)+1):
				n=8/0
			else:
				agenda[recepcionNick][lista[opcion-1]] = input(f'ingrese el nuevo {lista[opcion-1]}')
				break
		except:
			print(f'Ingrese opciones entre 1 y {len(lista)+1}')
			

while True:
	# crud (Create, Read, Update, Delete)
	print('Presione C para crear un nuevo cliente') 
	print('Presione R para leer la lista de clientes')
	print('Presione U para Actualizar')
	print('Presione D para borrar un registro')
	print('Presione Z para salir')
	ingreso = input('opcion: ').upper()
	if ingreso == 'C':
		Cargar_datos()
	elif ingreso == 'R':
		Leer()
	elif ingreso == 'U':
		Modificar()
	elif ingreso == 'D':
		pass
	elif ingreso == 'Z':
		print('chau')
		break
	else:
		print('Ingrese una opcion válida')
	

