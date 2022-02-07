#apriamo e leggiamo un file

my_file = open('shampoo_sales.csv', 'r')

print(my_file.read())

my_file.close()

#stampare solo un pezzo di file (slicing)

my_file = open('shampoo_sales.csv', 'r')

print (my_file.read()[0:50])

my_file.close()


#slicing in versione più sofisticata

my_file = open('shampoo_sales.csv', 'r')

my_file_contents = my_file.read()

if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + 'solo le prime 50 stringhe')
else:
    print(my_file_contents)

my_file.close()

#leggere il file riga per riga, una alla volta

my_file = open('shampoo_sales.csv', 'r')

print(my_file.readline())

print(my_file.readline())

my_file.close()



#leggere il file riga per riga in modo migliore:

my_file = open('shampoo_sales.csv', 'r')

for line in my_file:
    print(line)

my_file.close()


#metodo .split per separare le stringhe su uno specifico carattere

my_string = 'Ciao, come va?'
string_elements = my_string.split(',')
print(string_elements)


#conversione di una stringa a valore numerico

mia_stringa = '5.5'
mio_numero = float(mia_stringa)
print(mio_numero)


#aggiungere un elemento ad una lista

mia_lista = [1, 2, 3]
mia_lista.append(4)
print(mia_lista)


#leggere i valori di un file csv

values = []

my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    
    elements = line.split(',')
   
    if elements [0] != 'Date':
        date = elements[0]
        value = elements[1]

        values.append(float(value))

print(values)

print(my_file.read())

my_file.close()
