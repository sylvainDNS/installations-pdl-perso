import sqlite3

CreateDataBase = sqlite3.connect('/db/MyDataBase.db')

QueryCurs = CreateDataBase.cursor()

def CreateTable():
    QueryCurs.execute('''CREATE TABLE Clients
    (id INTEGER PRIMARY KEY, Nom TEXT,Rue TEXT,Ville TEXT, Region TEXT, Note REAL)''')

def AddEntry(Nom,Rue,Ville,Region,Note):
    QueryCurs.execute('''INSERT INTO Clients (Nom,Rue,Ville,Region,Note)
    VALUES (?,?,?,?,?)''',(Nom,Rue,Ville,Region,Note))

CreateTable()

AddEntry('Toto','Rue 1','Lille','Nord',105.2)
AddEntry('Bill','Rue 2','Fourmies','Nord',105.2)
AddEntry('Ben','Rue 3','Lille','Nord',105.2)
AddEntry('Paul','Rue 4','Lille','Nord',105.2)

CreateDataBase.commit()

QueryCurs.execute('SELECT * FROM Clients')

for i in QueryCurs:
    print ("\n")
    for j in i:
        print (j)

QueryCurs.close()
