#Harjutus06 MJ ITS25 11.10.25
import turtle
import random
import math

# Kasuta Python Turtles’i, et joonistada stseen, kus redel toetub majale 53° nurga all. Redeli ülemine ots peaks ulatuma 4,4 meetri kõrgusele maja seinal virtuaalses mõõtkavas.
# 
#     Muuda nurgad radiaanideks (radian)
#     Redeli kaugus seinast: kasuta tangensfunktsiooni (tan) ja antud nurka, et leida, kui kaugele redeli alumine ots on seinast. Valem:
#     Kaugus=Kõrgus seinaltan⁡(Nurk) 
#     Redeli pikkus: kasuta Pythagorase teoreemi, et leida redeli pikkus, kui tead redeli kõrgust seinal ja kaugust seinast. Valem:
#     Pikkus=(Kõrgus seinal)2+(Kaugus seinast)2 
#     Ümarda vastus 2 komakohta
#     Kuva vastused konsoolid

nurk = 53
h = 4.4
radiaan = math.radians(nurk)
kaugus = h / math.tan(radiaan)
c = math.hypot(h,kaugus)
print(h, kaugus, c)

koef = 50
turtle.fd(kaugus*koef)
turtle.lt(90)
turtle.fd(h*koef)
turtle.lt(143)
turtle.fd(c*koef)


turtle.done()