import csv
from Email import Email

class ManejadorEmails:
    __listaEmails=[]

    def __init__(self):
        self.__listaEmails = []           #####Defino una LISTA

    def agregarEmail(self, unEmail):
        self.__listaEmails.append(unEmail)  ####Agrego con ".append" un "email" a la lista (un elemento dentro de lista)

    def buscarEmailDominio(self, dominio):
        i=0                                 ###########inicializo i (CONTADOR)
        for email in self.__listaEmails:    ###########Recorro cada OBJETO dentro de la Lista
            if email.getdominio() == dominio:   #########PARA CADA OBJETO QUE COINCIDA incremento el contador
                i= i+1
        return i

    def getEmail (self, numero):
        return self.__listaEmails[numero]

    def __str__(self):
        s = ''
        for email in self.__listaEmails:
            s += str(email) + '\n'
        return s

    def testEmails(self):
        archivo = open('Emails.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            lista = fila[0].split('@')
            lista2 = lista[1].split('.')
            unEmail = Email(lista[0], lista2[0], lista2[1])
            self.agregarEmail(unEmail)




