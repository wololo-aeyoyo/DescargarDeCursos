import json
import aiohttp
import os
from urllib.request import Request, urlopen
import re
from pathlib import Path


class conseguirlink:
	corto="esto no me hace falta kek"
	def escrapear(enlace_plat,dir):

		#los mariguanos de platzi joden y se cambia el headers
		html_content =Request(str(enlace_plat),  headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(html_content).read().decode()
		#print(webpage)
		#with open("epa.txt","w",encoding="utf-8") as file:
		#	file.write(webpage)
		os.system("cls")
		print("\nSe consiguio la pagina sin peo")


		#aqui se busca el window.initialData y se selecciona hasta el ;
		vainaparsed=re.search("(window.initialData = )(.*)",webpage).group(2)
		#print(vainaparsed)
		#with open("jsonmaybe.txt","w",encoding="utf-8") as file:
		#	file.write(vainaparsed)
		print("\nSe parseo el json a los golpes")

		#aqui se busca el url tabulado de las clases 
		url_uni=re.search("(\"video\", \"url\": \"\/clases\/)(.*?)/",vainaparsed).group(2)
		print("\nEl url de las clases e platzi con id gay es :"+url_uni)

		#aqui se buscan los url de todas las clases pero el guevo peluo iba a aprender regex bien sin internet
		#busco todas las que salen con url y el url universal tabulado
		lista=re.findall("(\"url\": \"/clases/"+ url_uni +"/)(.*?)/",vainaparsed)
		print("\nYa tengo las listas mas o menos")
		#print(lista)

		#aqui se limpia el beta
		i=0
		links=[]
		savefile=[]
		while i <len(lista):
			limpia=str(lista[i])
			limpia=limpia.replace("('\"url\": \"/clases/"+url_uni+"/', ","")
			limpia=limpia.replace("'","")
			limpia=limpia.replace(")","")
			limpia="https://platzi.com/clases/{}/{}".format(url_uni,limpia)
			guarda=limpia
			limpia="youtube-dl -cwi"+" -o "+'"'+dir+"\\%(title)s-%(id)s.%(ext)s"+'"'+" --cookies=cookies.txt "+limpia
			guarda="youtube-dl -cwi"+" -o "+'"'+dir+"\\%%(title)s-%%(id)s.%%(ext)s"+'"'+" --cookies=cookies.txt "+guarda
			savefile.append(guarda)
			links.append(limpia)
			i=1+i

#el otro array es para ahorrarse el peo del %% y % en el .bat que es distinto de como se ejecuta y si se manda desde un bat o 
#de la terminal la vaina se rompe
		del links[0]
		del savefile[0]
		with open ("ejecutame.bat","w") as f:
			f.writelines("%s\n" % place for place in savefile)
		print("\n\nel programa ya te guardo el beta en ejecutame.bat e igual se va a bajar esa vaina porque\n yo soy es malandro \n \n ")
		return links

	def leer(nombre_archivo):
		listicalacra=[]
		with open(nombre_archivo,"r") as f:
			vainasbajar = f.readlines()
			for i in vainasbajar:
				aux=i[:-1]
				listicalacra.append(aux)
		return listicalacra

	def directorio_mariguanero(Nombreahi):
		Nombreahi = Nombreahi.replace("https://platzi.com/clases/","")
		Nombreahi = Nombreahi.replace("/","")
		Path(Nombreahi).mkdir(parents=True, exist_ok=True)
		Nombreahi=str(Path().absolute())+"\\"+Nombreahi

		return Nombreahi




