#modificare l'oggetto CSVFile dell'esercizio precedente in modo che stampi a schermo un messaggio di errore se si cerca di aprire un file non esistente 

class CSVFile():

    def __init__(self, name):
       
        #setto il nome
        self.name = name

        #provo ad aprirlo e a leggere una riga
        self.can_read = True
        try:
            file = open(self.name, 'r')
            file.readline()
        except Exception as e:
            self.can_read = False
            print('Non posso leggere il file perché: "{}".'.format(e))

    def get_data(self):

        if not self.can_read:
            return None

        else:    
            file = open(self.name, 'r')    
            data = []
            for line in file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                data.append(elements)     
            file.close()
            return data
                       


#dò il nome al file e lo stampo
file = CSVFile('shampoo_sales.csv')
print(file)
print('Il nome del file è:',format(file.name))
print('Dati contenuti nel mio file: "{}”.'.format(file.get_data()))
