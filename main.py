from testing_loco import conseguirlink
import json
import aiohttp
import os
from urllib.request import Request, urlopen
import re
from pathlib import Path


os.system("cls")

print("Epale mi pana como ta la vaina \n")
opcion=input("dime  un solo link  (1) o un tienes un archivo (2)\n")
vaina =0
if opcion == "1":
	link_indi=input("epale convive tron  \nmeteme el fucking link e platzi: \n")
	path = conseguirlink.directorio_mariguanero(link_indi)
	d=conseguirlink.escrapear(link_indi,path)
	for x in range(len(d)):
		nada=os.system(d[x])





elif opcion =="2":
	archivito_link=	conseguirlink.leer(input("dame el name ahi del archivo completo con extension y todo \n"))
	for i in range(len(archivito_link)):
		path = conseguirlink.directorio_mariguanero(str(archivito_link[i]))
		d= conseguirlink.escrapear(archivito_link[i],path)
		print("el path donde se bajara ahi: "+path)
		for x in range(len(d)):
			nada=os.system(d[x])
	os.system("cls")
	print("se debio haber bajado el curso numero: "+str(i)+"\n \n")


else:
	print("viste que eres marico")



print("Done")
