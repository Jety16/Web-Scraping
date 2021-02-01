from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq 

my_url= "https://listado.mercadolibre.com.ar/vinilos-disco#D[A:vinilos%20disco]"

#abre la conexion y despues la cierra 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#json 
page_soup = soup(page_html, "html.parser")
contenedores = page_soup.findAll("div", {"class": "ui-search-result__content-wrapper"})


for contenedor in contenedores:
	#obtengo el titulo del producto
    nombre = contenedor.div.a["title"]
    #obtengo el precio del producto
    precio_conteiner = contenedor.findAll("span",{"class":"price-tag ui-search-price__part"})
    precio = precio_conteiner[0].text
    #los imprimo
    print ("Producto:  " + nombre + "  \nPrecio: " +  precio)


while True:
    pass
