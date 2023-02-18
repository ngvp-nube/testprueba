from django.shortcuts import render
from urllib.request import urlopen
import json 
from selenium import webdriver
from .models import Nombres
import time
from selenium.webdriver.common.by import By
# Create your views here.
def index(request):
    global lista
    test_paginaç()
    #consumimos api
    url = "http://api.citybik.es/v2/networks/bikesantiago"
    response = urlopen(url)
    data = json.loads(response.read())
    info = data["network"]["stations"]
    #print(data["network"]["stations"])
    #recorremos datat
    for i in info:
        nombre= i["name"]
        #si se encuentra la guardamos en postgres y la mostramos en el citio
        if "P60 - Suecia / Carmen Sylva" in nombre:
            names = i["name"]
            print("se encontro",names)
            nom = Nombres(
                name = names
            )
            nom.save()
            break

        else:
            print("no lo encontro")

    
    nombres = Nombres.objects.all() 
    return render(request,'core/index.html',{'lista_nombre':nombres})

def test_paginaç():
    driver = webdriver.Edge(executable_path=r"C:\Users\Haka\Downloads\msedgedriver.exe")
    driver.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php")  
    time.sleep(6)
    #xpat //table[@class='tabla_datos']//tbody//tr
    data = driver.find_elements(By.XPATH, "//table[@class='tabla_datos']//tbody//tr")
    print("data",data)
    for i in range(len(data)):
        data = data[i].text
        print(data)