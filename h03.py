#Harjutus03.1 MJ ITS25 09.10.25
import turtle

nimi = "joonas"
vanus = 118
pikkus = 2.10

print(nimi,",", vanus,"aastat vana ja pikkus on", pikkus,"m")
print(nimi+", "+str(vanus)+" aastat vana ja pikkus on "+str(pikkus)+"m")

# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)

sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100.50
kokku = paevade_arv * oobimise_hind
print(sihtkoht,"reis kestab", paevade_arv,"päeva ja maksab kokku",kokku,"€")

# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
# Kasutades Turtle’i, joonista kõrvuti 3 värvilist ruutu, mis kasutab loodud muutujaid
# Iga ruut on järgmisest 1,5 korda eemal
# Testi: muuda külje pikkust ning ruudud on kenasti teineteisest eemal

kylje_pikkus = 100
nurk = 90
kujundi_varv = "red"
x = 110
kordaja = x * 2

turtle.pencolor(kujundi_varv)
for j in range(3):
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x = x * 2
    
    
turtle.done()