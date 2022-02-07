#esempio di codice minimale: trovare i numeri in una lista minori di 5 e stamparli

number_list = [13,12,34,4,51,3,8,27,18]

for item in number_list:
    if item < 5:
        print(item)


#stampo a schermo due variarbili

my_var_1 = 134
my_var_2 = 57382

print('Valore 1: {}, valore 2: {}'.format(my_var_1, my_var_2))


#dizionari:

my_dict_1 = {'Trieste': 34100, 'Padova': 35100}#dizionario di numeri 
my_dict_2 = {'Trieste': 'TS', 'Padova': 'PD'}#dizionario di stringhe
print('CAP di Trieste: {}'.format(my_dict_1['Trieste']))


#istruzioni condizionali

if(my_var_1 > my_var_2):
    print("my_var_1 è maggiore di my_var_2")

    if(my_var_1 - my_var_2) <= 1:
        print("...ma non di molto")

    elif(my_var_1 - my_var_2) <= 100:
        print("...abbastanza")

    else:
        print("...di molto")

else:
    print("my_var_1 è minore di my_var_2")

    if(my_var_2 - my_var_1) <= 1:
        print("...ma non di molto")

    elif(my_var_2 - my_var_1) <= 100:
        print("...abbastanza")

    else:
        print("...di molto")                       


#cicli iterativi
#1° esempio

i = 0
while i < 10:
    print(i)
    i = i + 1

#2° esempio (migliore del primo)    
for i in range(10):
    print(i)

#3° esempio stampa la posizione dei valori e i valori stessi della prima lista creata in questo file 
for i, item in enumerate(number_list):
    print("Posizione {}: {}".format(i, item))


#funzioni

def my_funcion(argomento1, argomento2):
    print("Argomenti: {} e {}".format(argomento1, argomento2))

my_funcion("Pippo", "Pluto")


#return

def eleva_al_quadrato(numero):
    return numero * numero
    
eleva_al_quadrato(4)

risultato = eleva_al_quadrato(4)
print('Risultato: {}'.format(risultato))


#come scrivere una buona funzione (uso variabili locali non enclosing)

def eleva(numero):
    risultato = numero * numero
    return risultato

eleva(2)

risultato = eleva(2)
print('Quadrato: {}'.format(risultato))


#moduli (contengono funzionalità della libreria standard, ma non sono built-in)

from math import sqrt
#qua potrei scrivere: sqrt(600)
print('sqrt: {}'.format(sqrt(600)))

#oppure
import math
math.sqrt #opzionale (anche con valore tra parentesi)
print('sqrt_2: {}'.format(math.sqrt(300)))



#iterazione pythonica (migliore) sugli elementi di una lista

mia_lista = ["marco", "irene", "paolo"]

for item in mia_lista:
    print(item)

if "elena" in mia_lista:
    print('Ho trovato Elena!')

else:
    print('Elena non fa parte della lista :(')