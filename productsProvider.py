from typing import Protocol
from products import BIL, BOK, DRYCK, ELEKTRONIK, FRUKT, KLÄDER, PRODUCT_NAME_AND_TYPE
import random

PRODUKT_TYPE = {'Bil':1,
              'Bok':2,
              'Elektronik':3,
              'Frukt':4,
              'Kläder':5,
              'Dryck':6}


class Product(Protocol):
    Produkt_typ = None

    def namn(self) -> str:
        pass

    def antal(self) -> int:
        pass

    def pris(self) -> int:
        pass


class Bil:
    Produkt_typ = 'Bil'
    BILAR = BIL

    def __init__(self) -> None:
        self.bil = random.choice(self.BILAR)
        
    def namn(self) -> str:
        return self.bil['namn']

    def antal(self) -> int:
        antal = random.gauss(mu=2, sigma=1)
        return 1 if antal < 1 else int(antal)

    def pris(self) -> int:
        return self.bil['pris']

class Bok:
    Produkt_typ = 'Bok'
    BÖCKER = BOK

    def __init__(self) -> None:
        self.bok = random.choice(self.BÖCKER)

    def namn(self) -> str:
        return self.bok['namn']

    def antal(self) -> int:
        antal = random.gauss(mu=2, sigma=1)
        return 1 if antal < 1 else int(antal)

    def pris(self) -> int:
        return self.bok['pris']

class Elektronik:
    Produkt_typ = 'Elektronik'
    ELEKTRONIK = ELEKTRONIK

    def __init__(self) -> None:
        self.elektronikpryl = random.choice(self.ELEKTRONIK)

    def namn(self) -> str:
        return self.elektronikpryl['namn']

    def antal(self) -> int:
        antal = random.gauss(mu=2, sigma=1)
        return 1 if antal < 1 else int(antal)

    def pris(self) -> int:
        return self.elektronikpryl['pris']

class Frukt:
    Produkt_typ = 'Frukt'
    FRUKTER = FRUKT

    def __init__(self) -> None:
        self.frukt = random.choice(self.FRUKTER)

    def namn(self) -> str:
        return self.frukt['namn']

    def antal(self) -> int:
        antal = random.gauss(mu=8, sigma=5)
        return 1 if antal < 1 else int(antal)

    def pris(self) -> int:
        return self.frukt['pris']
        
class Kläder:
    Produkt_typ = 'Kläder'
    KLÄDER = KLÄDER

    def __init__(self) -> None:
        self.klädesplagg = random.choice(self.KLÄDER)

    def namn(self) -> str:
        return self.klädesplagg['namn']

    def antal(self) -> int:
        antal = random.gauss(mu=3, sigma=2)
        return 1 if antal < 1 else int(antal)

    def pris(self) -> int:
        return self.klädesplagg['pris']

class Dryck:
    Produkt_typ = 'Dryck'
    DRYCKER = DRYCK

    def __init__(self) -> None:
        self.dryck = random.choice(self.DRYCKER)

    def namn(self) -> str:
        return self.dryck['namn']

    def antal(self) -> int:
        antal = random.gauss(mu=10, sigma=5)
        return 1 if antal < 1 else int(antal)

    def pris(self) -> int:
        return self.dryck['pris']
    

class Products:
    
    def car(self) -> Bil:
        return Bil()
    
    def book(self) -> Bok:
        return Bok()
    
    def beverage(self) -> Dryck:
        return Dryck()
    
    def electronics(self) -> Elektronik:
        return Elektronik()

    def fruit(self) -> Frukt:
        return Frukt()
    
    def cloths(self) -> Kläder:
        return Kläder()
    
products = Products()
products_methods = [
    products.car, 
    products.book, 
    products.beverage, 
    products.electronics, 
    products.fruit,
    products.cloths]

def RandomProduct() -> Product:
    prod = random.choice(products_methods)
    return prod()