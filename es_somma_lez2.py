#scrivere una funzione che sommi tutti gli elementi di una lista e commitare il file i cui è stata scritta

my_list = [1, 4, 7, 8]    
somma = 0

for item in my_list:
    somma += item

print('Somma: {}'.format(somma))    
#guardando da internet, ma io voglio creare una funzione!


def sum(lista):
    pass 
    return sum
    
lista = [3, 4, 8]

risultato = sum(lista)
print('Somma: {}'.format(risultato))
#non so, dubito sia giusto


#riprovo

def sum_list(the_list):
    risultato = sum(the_list)
    return risultato

the_list = [4, 5, 8]

risultato = sum_list(the_list)
print('Somma: {}'.format(risultato))
#dà sempre un risultato non numerico, bu