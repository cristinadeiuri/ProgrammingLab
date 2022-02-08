#definisco la classe
class CSVTimeSeriesFile():

    def __init__(self, name):
       
        #setto il nome del file
        self.name = name

        #alzo un'eccezione per assicurarmi che il file esista provando a leggere la prima riga del file
        self.can_read = True
        try:
            time_series_file = open(self.name, 'r')
            time_series_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}".'.format(e))
        

    def get_data(self):

        #se c'è un problema di lettura del file stampo a schermo l'avviso e faccio in modo che la funzione non restituisca nulla, altrimenti procedo con la creazione di una lista di liste
        if not self.can_read:
            print('Errore, file non aperto o illegibile')
            return None

        else:
            #creo una lista su cui salverò tutte le liste
            time_series = []
            
            #apro il file
            time_series_file = open(self.name, 'r')

            #leggo il file linea per linea
            for line in time_series_file:
                
                #faccio lo split ad ogni linea del file 
                #ogni riga la divido in due stringhe (della stessa lista), la prima corrisponde alla data e la seconda al numero di passeggeri
                elements = line.split(',')

                #pulisco il carattere newline ed eventuali spazi ad inizio o a fine stringa con la funzione strip
                elements[-1] = elements[-1].strip()

                #se non sto processando l'intestazione...
                if elements[0] != 'date':
                    #...associo gli elementi
                    date = elements[0]

                    #converto la stringa corrispondente al numero di passeggeri in floating point e la associo al suo valore
                    elements[1] = float(elements[1])
                    passengers = elements[1]

                    #aggiungo alla lista gli elementi della linea
                    time_series.append(elements)
   

            #chiudo il file
            time_series_file.close()

            #ritorno la lista dopo aver considerato tutte le righe
            return time_series
                

#assegno la classe al file
time_series_file = CSVTimeSeriesFile(name = 'datap.csv')

#assegno il file alla lista
time_series = time_series_file.get_data()

#opzionale, se voglio stampare l'indirizzo in memeoria dell'oggetto creato: print(time_series_file)

#stampo il nome del file, dato dalla funzione __init__
print('Nome del file: "{}"'.format(time_series_file.name))

#stampo il contenuto del file, dato dalla funzione get_data
print('Dati contenuti nel file: "{}"'.format(time_series))


#creo una funzione per poter calcolare la differenza media del numero di passeggeri mensile tra anni consecutivi
def compute_avg_monthly_difference(time_series, first_year, last_year):

    