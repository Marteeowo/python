#Harjutus07 MJ ITS25 11.10.25

#Näide.
#     #loendid
#     nimed = ["Alice", "Bober", "Carol", "Dave", "Eve"]
# 
#     nimed.append("Kass")
#     nimed.insert(0,"Jaanus")
# 
#     for i in nimed:
#         print(i)

# Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
# "jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# 
#     Kuva mõõdetava kuu nimetus
#     Kuva viimase mõõtmise tulemus
#     Kuva ainult temperatuurid
#     Leia kuu maksimaalne ja minimaalne temperatuur
#     Leia kuu keskmine temperatuur
#     Mitu korda esines -20 kraadi
#     Eemalda element nr 5
#     Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
#     Sorteeri temperatuurid nimekirjas kasvavas järjekorras

mootmed = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"Mõõdetav kuu: {mootmed[0]}")
print(f"Viimane mõõtmine: {mootmed[-1]}")
print(f"Mõõtmed: {mootmed[1:]}")
mootmed.pop(0)
print(f"min: {min(mootmed)}, max:{max(mootmed)}")
print(f"Keskmine temp: {round(sum(mootmed)/len(mootmed),2)}")
print(f"-20 kraadi esineb {mootmed.count(-20)} korda ")
mootmed.pop(4)
mootmed.insert(4,23)
mootmed.sort()
print(f"Mõõtmed minu vanusega: ",mootmed)



# albumid = ['1. ALIKA – "Bridges"','2. Anett x Fredi – "Read Between The Lines"','3. villemdrillem – "leekiv armastus"','4. Clicherik & Mäx – "PAKSUD"','5. nublu – "ära ärata"','6. NOËP – "Move Your Feet"','7. Trad.Attack! – "Bring It On"','8. Bedwetters – "It Is What It Is"','9. Reket – "Panama paberid"','10. Grete Paia – "Võluväel"']
# 
# print("-----------------KÕIK LOOD-----------------")
# for i in albumid:
#     print(i)
#     
# lugu = int(input("Millist lugu mängid: "))
# print(f"Mängin: {albumid[lugu-1]}")


