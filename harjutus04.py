#Harjutus04 MJ ITS25 09.10.25
import turtle
# Ringi pindala ja Turtle
# 
#     Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis ringi pindala ja ümbermõõdu.
#     Programm küsib kasutajalt ringi raadiuse.
#     Kasuta ** operaatorit raadiuse ruudu arvutamiseks ja π väärtusena 3.14.
#     Lisa veakontroll, et kontrollida kasutaja sisestatud raadiuse korrektsust.
#     Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
#     Näide:
#     Kasutaja sisestab: 5
#     Programm väljastab konsoolis: Ringi pindala on 78.5 ja ümbermõõt on 31.4
#     Turtle graafika joonistab vastava ringi
try:
    r = float(input("Ringi raadius r="))
    s = 3.14 * r ** 2
    p = 2 * 3.14 * r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r)
except:
    print("Kontrolli sisestust")
    
turtle.done()

#     Sa töötad kingipoes ja sinu ülesanne on pakkida kingitusi.
#     Igasse kinkekarpi mahub täpselt 5 kingitust.
#     Sinu ülesandeks on arvutada, mitu täis kinkekasti saad teha ja mitu kingitust jääb üle, kui need kõik ei mahu karpidesse.
#     Loo programm, mis küsib kasutajalt, mitu kingitust on vaja pakkida.
#     Programm peaks seejärel arvutama, mitu täis kinkekasti saab teha ja mitu kingitust jääb üle. Kasuta täisarvulist jagamist (//) kinkekarpide arvu leidmiseks ja jäägi (%) operaatorit ülejäävate kingituste arvu leidmiseks.
#     Kasuta veakontrolli ja vastuse vormindamist
#     Näide:
#     Kasutaja sisestab: 23
#     Programm väljastab: Saad teha 4 täis kinkekasti. Üle jääb 3 kingitust.

#Kontroll
try:
    kingitused = int(input("lisa kingituste arv: "))
    maht = 5

    kingitusi_kokku = kingitused // maht #täisarv
    ylejaak = kingitused % maht #jäääääk

    print(f"Saad teha {kingitusi_kokku} täis kinkekasti. Üle jääb {ylejaak} kingitust.")
except:
    print("Kontrolli sisestust")
    


#     Raamatupoes on 30% soodusmüük.
#     Kirjuta programm, mis küsib kasutajalt soovitud raamatute arvu ja arvutab nende kogumaksumuse, kui iga raamatu tavahind on 12,53€.
#     Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
#     Näide:
#     Kasutaja sisestab: 3
#     Programm väljastab: 3 raamatu hind soodustusega on 26.25€.

ale = 0.3
hind = 12.53
kogus = int(input("Raamatute kogus: "))
summa = (hind-hind*ale)*kogus
print(f"{kogus} raamatu hind soodustusega on {summa:.2f}€. ja ilma soodustusega on {kogus*hind:.2f}€.") #.2f ümardab 2 kohaga

#     Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
#     Aed on ristküliku kujuline. (a+b)*2 = P
#     Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
#     Väljasta lause, kasutades f-string vormindamist.
#     Näide:
#     Kasutaja sisestab: 4 ja 5
#     Programm väljastab: Aia kogupikkus on 18 meetrit.

a = int(input("Lisa külg 1: "))
b = int(input("Lisa külg 2: "))
p = (a+b)*2
print(f"aia pikkus külgedega {a} ja {b} on {p} meetrit.")

