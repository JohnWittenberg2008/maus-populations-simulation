generationen = int(input('Anzahl an Generationen: '))
jung = 6
erwachsen = 9
alt = 12
while generationen > 0:
    #Population Berechnen
    hilf = erwachsen * 4 + alt * 2
    alt = erwachsen // 3
    erwachsen = jung // 2
    jung = hilf
    generationen = generationen - 1
GesamtZahl = alt + erwachsen + jung
#Ausgabe
print('Anzahl Junger Mäuse:',jung)
print('Anzahl Erwachsener Mäuse:',erwachsen)
print('Anzahl ALter Mäuse:',alt)
print('Anzahl der Population' ,GesamtZahl)