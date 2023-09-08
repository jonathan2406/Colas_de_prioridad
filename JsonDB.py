import json

def cargue(info):
    with open("db.json","w") as archivo:
        json.dump(info,archivo)

def descargue():
    with open("db.json","w") as archivo:
        datos = json.loads(archivo)
        return datos
    

hola = {1:"1",2:"2"}




print(descargue())

