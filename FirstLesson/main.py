import requests
from bs4 import BeautifulSoup

f = open('csv.txt')
massiv=[]
for line in f:
    splitted=line.split(',')
    massiv.append(splitted)
f.close()
html=[]
html.append("<table>")
print(massiv)
counterB=0

for b in range(0,len(massiv)):
    html.append("<tr>")
    counterA = 0
    for a in range(0,len(massiv[0])):
        html.append("<th>")
        print(counterA,counterB)
        html.append(massiv[counterB][counterA])
        html.append("</th>")
        counterA+=1
    counterB += 1
    html.append("</tr>")
html.append("</table>")
f = open('table.html', 'w')
for index in html:
     f.write(index)
f.close()