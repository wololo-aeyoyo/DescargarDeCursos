import json
import aiohttp
import os
from urllib.request import Request, urlopen
import re
enlace_plat=input("epale convive tron  \nmeteme el fucking link e platzi: \n")


#los mariguanos de platzi joden y se cambia el headers
html_content =Request(str(enlace_plat),  headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(html_content).read().decode()
#print(webpage)
#with open("epa.txt","w",encoding="utf-8") as file:
#	file.write(webpage)
print("\n se consiguio la pagina sin peo")


#aqui se busca el window.initialData y se selecciona hasta el ;
vainaparsed=re.search("(window.initialData = )(.*)",webpage).group(2)
#print(vainaparsed)
#with open("jsonmaybe.txt","w",encoding="utf-8") as file:
#	file.write(vainaparsed)
print("\nse parseo el json a los golpes")

#aqui se busca el url tabulado de las clases 
url_uni=re.search("(\"video\", \"url\": \"\/clases\/)(.*?)/",vainaparsed).group(2)
print("\nel url de las clases e platzi con id gay es :"+url_uni+"\n \n")

#aqui se buscan los url de todas las clases pero el guevo peluo iba a aprender regex bien sin internet
#busco todas las que salen con url y el url universal tabulado
lista=re.findall("(\"url\": \"/clases/"+ url_uni +"/)(.*?)/",vainaparsed)
print("\nya tengo las listas mas o menos")
#print(lista)

#aqui se limpia el beta
i=0
links=[]
while i <len(lista):
	limpia=str(lista[i])
	limpia=limpia.replace("('\"url\": \"/clases/"+url_uni+"/', ","")
	limpia=limpia.replace("'","")
	limpia=limpia.replace(")","")
	limpia="https://platzi.com/clases/{}/{}".format(url_uni,limpia)
	limpia="youtube-dl -cwi --cookies=cookies.txt "+limpia
	links.append(limpia)
	i=1+i

del links[0]
with open ("ejecutame.bat","w") as f:
	f.writelines("%s\n" % place for place in links)
print("\n\nel programa ya te guardo el beta en ejecutame.bat")