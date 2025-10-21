#Kodutoo01 MJ ITS25 21.10.25


# 1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# 	kood mis teavitab paaris või paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

print("1.1. Paaris või paaritu")			  # see on koodi tiitel
print("palun sisesta number mis ei ole null") # siin ytleb kasutajala et sisestada arvu mis ei ole null
a = str(input()) 								# input on string sest et valtida vigasi kui kasutaja sisestab teksti
if a == "0" or not (a.isnumeric()): 			# siin kontrollib kaks input on 0 voi ei ole number
    print("jama") 								# kasutaja saab teada kas nad tegid vea
else: 											# see osa kontrollib kas arv on paaris voi paaritu
    b = int(a) 									# kasutaja sisestatud input on muudetud integeriks et teha arvutamine lihtsamaks
    paaris = b % 2 								# mod 2 sisestatud arvu jargi, sest on ainult kaks valikut, paaritu ja paaris
    if paaris == 0: 							# see kontrollib kas arv jagub kahega ja lopuks jaab nulli, ehk paaris
        print(f"{a} on paaris") 				# annab kasutajale teada kas arv on paaris
    else:
        print(f"{a} on paaritu") 				# annab kasutajale teada kas arv on paaritu

# 2. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# 	küsitakse valuuta kogust ja tehakse arvutused - 2p
# 	kood kommenteeritud - 1p

import math # sisestame matemaatika raamatukogu

print("1.2. Eurokalkulaator")

try:
    print(f"Sisestage kogus")
    kogus = float(input())
    print(f"kui soovid EUR->EEK siis kirjuta 1, v6i 2 et EEK->EUR: ")
    
    valik = int(input())
    eureek = float(15.6466)
    eekeur = float(1/eureek)

    if valik == 1:
        loppkogus = kogus*eureek
        print(f"{kogus} eurot on {loppkogus:.5f} krooni")
    elif valik == 2:
        loppkogus = kogus*eekeur
        print(f"{kogus} krooni on {loppkogus:.5f} eurot")
    else:
        print(f"valik pole voimalik")
except:
    print(f"Proovi uuesti")

# 3. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p

import random
print(f"1.3 T2ringud")

arvuti_taring1 = random.randint(1,6)
arvuti_taring2 = random.randint(1,6)
arvuti_summa = arvuti_taring1 + arvuti_taring2

kasutaja_taring1 = random.randint(1,6)
kasutaja_taring2 = random.randint(1,6)
kasutaja_summa = kasutaja_taring1 + kasutaja_taring2

print(f"sa voitled vastu arvutit taringu veeremisega")
print(f"kui soovid veereta esimesena vajuta 1, kui teisena vajuta 2 ")

try:
    esimene_veereja = int(input())
    if esimene_veereja == 1:
        print(f"sa veeretasid {kasutaja_summa}")
    elif	esimene_veereja == 2:
        print(f"arvuti veeretas {arvuti_summa}")
    else:
        print(f"valesti sisestasid")
        exit
    print(f"kui sa arvad et sa veeretasid rohkem kui arvuti vajuta 1, kui vahem, vajuta 2")
    pakkumine = int(input())
    if pakkumine == 1:
        if kasutaja_summa > arvuti_summa:
            print(f"sina veeretasid {kasutaja_summa} ja arvuti veeretas {arvuti_summa}, tubli, veeretasid rohkem")
        elif kasutaja_summa < arvuti_summa:
            print(f"sina veeretasid {kasutaja_summa} ja arvuti veeretas {arvuti_summa}, kaotasid. veeretasid vahem")
        else:
            print(f"sina ja arvuti veeretasite vordselt {arvuti_summa}, keegi ei voitnud")
    elif pakkumine == 2:
        if kasutaja_summa > arvuti_summa:
            print(f"sina veeretasid {kasutaja_summa} ja arvuti veeretas {arvuti_summa}, kaotasid, veeretasid rohkem")
        elif kasutaja_summa < arvuti_summa:
            print(f"sina veeretasid {kasutaja_summa} ja arvuti veeretas {arvuti_summa}, tubli. veeretasid vahem")
        else:
            print(f"sina ja arvuti veeretasite vordselt {arvuti_summa}, keegi ei voitnud")
    else:
        print(f"pakkumise valik oli vigane")

except:
    print(f"error")
    


















