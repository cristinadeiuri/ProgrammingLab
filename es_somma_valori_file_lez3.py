#scrivere uno script che sommi tutti i valori delle vendite degli shampoo del file "shampoo_sales.csv"


#inizializzo una lista vuota per salvare i valori del file
valori = []

#apro il mio file csv, linea per linea
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    
    #faccio lo split di ogni riga sulla virgola
    elementi = line.split(',')
   
    #se non sto processando l'intestazione..
    if elementi[0] != 'Date':
       
        #setto la data ed il valore
        date = elementi[0]
        valore = elementi[1]
       
        #aggiungo alla lista il valore
        valori.append(float(valore))

#stampo la lista dei valori, che ora sarà composta dai valori delle vendite di shampoo appartenenti al file (è una cosa completamente facoltativa)
print(valori)


#sommo i valori appartenenti alla lista su cui ho salvato i valori delle vendite del file

#prima creo una variabile somma su cui salverò il risultato
somma = 0

#ogni valore della lista lo sommo
for item in valori:
    somma = somma + item #oppure somma += item

#stampo il risultato
print('Somma valori vendite dello shampoo: {}'.format(somma))    




