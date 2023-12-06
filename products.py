
BIL = []
BIL_FIL = f'.\\produkter\\Bilar.txt'

BOK = []
BOK_FIL = f'.\\produkter\\Böcker.txt'

DRYCK = []
DRYCKES_FIL = f'.\\produkter\\Dryck.txt'

ELEKTRONIK = []
ELEKTRONIK_FIL = f'.\\produkter\\Elektronik.txt'

FRUKT = []
FRUKT_FIL = f'.\\produkter\\Frukt.txt'

KLÄDER = []
KLÄDERS_FIL = f'.\\produkter\\Kläder.txt'


PRODUCT_NAME_AND_TYPE = {}

def ladda_produkter(path:str, produkt_lista:list,typ:str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        for row in f:
            namn, pris = row.strip().split(',')
            produkt_lista.append({'namn':namn,'pris':int(pris)})
            PRODUCT_NAME_AND_TYPE[namn] = typ


ladda_produkter(BIL_FIL, BIL,'Bil')
ladda_produkter(BOK_FIL, BOK,'Bok')
ladda_produkter(DRYCKES_FIL, DRYCK,'Dryck')
ladda_produkter(ELEKTRONIK_FIL, ELEKTRONIK, 'Elektronik')
ladda_produkter(FRUKT_FIL, FRUKT,'Frukt')
ladda_produkter(KLÄDERS_FIL, KLÄDER,'Kläder')


