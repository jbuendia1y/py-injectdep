# Probando injection dependency

Librareria para la injección de dependencias para python

## Porqué usarlo ?

Pues esta librería está hecha para proyectos pequeños que no necesiten testear la applicación o que quieran probar la injección de dependencias


## Cómo usarlo ?

Aquí es un ejemplo de inyección de forma global con la librería

```py
import injectdep


@injectdep.register
class MyDB:
    def find_all():
        return ["Jhon", "Pepe", "Carlos"]

def main(db: MyDB):
    results = db.find_all()
    print(results) # ["Jhon", "Pepe", "Carlos"]


if __name__ == "__main__":
    injected = injectdep.inject(main)
    injected()
```

## Puede construir su propio módulo

```py
import injectdep
from injectdep import Module

database_module = Module()

@database_module.register
class MyDB:
    def find_all():
        return ["Jhon", "Pepe", "Carlos"]

def main(db: MyDB):
    results = db.find_all()
    print(results) # ["Jhon", "Pepe", "Carlos"]


if __name__ == "__main__":
    injected = database_module.inject(main)
    injected()
```

<p align="center">Inspirado en AngularModules</p>