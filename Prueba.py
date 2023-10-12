from datetime import datetime
import random
import math

#Definir cuantos cupos tiene el parqueadero en motos y carros

print('////BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS////')
print("----------------------------------------------------")
camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))

#Definir los campos del parqueadero
name_camp_cars = []
name_camp_moto = []

while int(len(name_camp_cars)) < camp_cars:
name_camp_cars.append({‘place’: str(input('Ingresa el nombre del campo del parqueadero de carro: ')),‘avalible’:True})
#print(name_camp_cars)

while int(len(name_camp_moto)) < camp_motorcycles:
name_camp_moto.append({‘place’: str(input('Ingresa el nombre del campo del parqueadero de moto: ')),‘avalible’:True})
#print(name_camp_moto)

#Definir tarifa de cobro por tiempo
cost_frac_car = 2000
cost_frac_moto = 1000

#Registrar entrada de vehicula o cobrar parqueadero
register_car = []
register_motorcycle =[]

while True:
#recorrer un for dentro de una lista para consultar los diccionarios que hay
place_free_moto = [x[‘place’] for x in name_camp_moto if x[‘avalible’] == True]
place_free_car = [x[‘place’] for x in name_camp_cars if x[‘avalible’] == True]
print(‘lugares disponibles:’,place_free_car,place_free_moto)

print(‘QUE OPCION DESEAS REALIZAR?’)
options = input(‘1. Registrar nuevo vehiculo \n2. Registrar salida de vehiculo:\n opcion >:’)
#Validar que el dato no sean letras
if options.isdigit() and options !=‘1’ and options !=‘2’:
print(‘NO SE ADMITEN LETRAS SOLO LAS OPCIONES 1 o 2’)
#Opcion para registrar Moto
elif options == ‘1’:
if len(place_free_moto) > 0 or len(place_free_car) > 0:

type_vehicule= input('QUE TIPO DE VEHICULO DESEAS REGISTRAR?\n1.Moto\n2.Carro\nopcion >:')

 iftype_vehicule.isdigit() and type_vehicule !='1' and type_vehicule !='2':
   print('NO SE ADMITEN LETRAS SOLO LAS OPCIONES 1 o 2')

  #registrar Moto
 elif (type_vehicule =='1' and len(place_free_moto) > 0):

  #print('ingreso a registrar moto')
  placa= str(input('POR FAVOR INGRESA LA PLACA DEL VEHICULO >:'))
  hour_inside= datetime.now().strftime('%Y-%m-%d %H:%M')
  place_random = random.choice(place_free_moto)
  #print(place_random)
  register_motorcycle.append({'place':place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action':'Entro'})

  for x in name_camp_moto:
    if x['place'] == place_random:
      x['avalible'] = False
  print('El registro de vehiculos es el siguiente: ', register_motorcycle)

  #Registrar Carro
 eliftype_vehicule =='2' and len(place_free_car) > 0:

  #print('ingreso a registrar carro')
  placa= str(input('POR FAVOR INGRESA LA PLACA DEL VEHICULO >:'))
  hour_inside= datetime.now().strftime('%Y-%m-%d %H:%M')
  place_random = random.choice(place_free_car)
  #print(place_random)
  register_car.append({'place':place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action':'Entro'})

  for x in name_camp_cars:
    if x['place'] == place_random:
      x['avalible'] = False
  print('El registro de vehiculos es el siguiente: ', register_car)

 elif len(place_free_moto) == 0:
   print('PARQUEADERO DE MOTOS LLENO')
 elif len(place_free_car) == 0:
   print('PARQUEADERO DE CARROS LLENO')    
 #print('final',type_vehicule, placa,hour_inside)

 else:
  print('POR FAVOR INTRODUZCA UNA SELECCION VALIDA')
  print('##############################################################################')

else :
  print('PARQUEADERO LLENO, ESPERE QUE SALGA UN VEHICULO')

#option de retirar un vehiculo, aqui se dira cuanto se cobra y cuanto
elif options == ‘2’:
#juntar las dos listas para buscar el registro en una sola lista
option_cash = input('POR FAVOR DIGITE EL TIPO DE VEHICULO A COBRAR\n 1.Moto.\n 2.Carro.\n Opcion: ')

if option_cash.isdigit() and option_cash !=‘1’ and option_cash !=‘2’:
print(‘NO SE ADMITEN LETRAS SOLO LAS OPCIONES 1 o 2’)

#Registrar salida de una moto ##############################
if option_cash == ‘1’:
placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))

#se valida que se encuentre la placa consultada
if str([x['Action'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro']) == '[]':
  print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
  continue

hour_inside = [x['hour_inside'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro']
place_out = [x['place'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro']

#calcular tiempo de cobro

hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
total = datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(str(hour_inside[0]), '%Y-%m-%d %H:%M')
total = total.total_seconds()
total = total / 3600
#Convertir el tiempo de parqueo a un entero para poderlo multiplicar por el costo
total = math.ceil(total)
total = total * cost_frac_moto
print('Tu valor a pagar de parqueo es => ',total)

#liberar parqueadero
for x in name_camp_moto:
 if x['place'] == str(place_out[0]):
  x['avalible'] = True    
print('for', name_camp_moto, place_out)
#Actualizar volante de salida con hora de salida y pago total para llevar un registro
for x in register_motorcycle:
 if x['placa'] == placa_pay:
  x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
  x['pay_all'] = total
  x['Action'] = 'salio'

print('los vehiculos motorizados registrados son los siguientes: ', register_motorcycle)

#Registrar salida de un carro######################
elif option_cash == ‘2’:
placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))

#se valida que se encuentre la placa consultada
if str([x['Action'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro']) == '[]':
  print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
  continue

hour_inside = [x['hour_inside'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro']
place_out = [x['place'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro']

#calcular tiempo de cobro

hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
total = datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(str(hour_inside[0]), '%Y-%m-%d %H:%M')
total = total.total_seconds() 
total = total / 3600

#Convertir el tiempo de parqueo a un entero para poderlo multiplicar por el costo
total = math.ceil(total)
total = total * cost_frac_car
print('Tu valor a pagar de parqueo es => ',total)

#liberar parqueadero
for x in name_camp_cars:
 if x['place'] == str(place_out[0]):
  x['avalible'] = True 

print('for', name_camp_cars,place_out)

#Actualizar volante de salida con hora de salida y 
for x in register_car:
 if x['placa'] == placa_pay:
  x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
  x['pay_all'] = total
  x['Action'] = 'salio'

print('los vehiculos registrados son los siguientes: ', register_car)

else:
print(‘POR FAVOR INTRODUZCA UNA SELECCION VALIDA’)
else:
print(‘POR FAVOR INTRODUZCA UNA SELECCION VALIDA’)