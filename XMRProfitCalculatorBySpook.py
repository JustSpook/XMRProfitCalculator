# Arte de consola + introducción
import pyfiglet
import colorama
import requests
from bs4 import BeautifulSoup
colorama.init(autoreset=True)
ART = str("Spook \n XMR Profit calculator")
ASCII_art_1 = pyfiglet.figlet_format(ART)
print(ASCII_art_1)
print(
    "Bienvenidos a mi calculador de profit de XMR, para usarlo solo introduzca los datos pedidos en el formato "
    "correcto.\n\nPara buscar estos datos recomiendo el uso de páginas webs externas y el uso de software externo para "
    "datos como el voltaje de su equipo.\n")
print(
    "Si esta herramienta le ha ayudado y lo considera oportuno acepto donaciones en la siguiente cartera de monero:\n "
    "45ySHwq1dyxdiktXCPiJrkQRZaQZNrVDgcJ5nrycrYyN9nWji9FTLG9KJAhbzPvydZV6kgjjEbhjkJETm4jrGCxj11xD7ys"
    "\n")
print("Disclaimer:\n"
      "Tenga en cuenta que los valores proporcionados por esta herramienta nunca van a ser exactos,\n"
      "quizá haya alguna página web que calcule estos datos con mayor precisión (o no) pero la idea\n"
      "de esta herramienta es eliminar la necesidad de instalar o abrir un navegador en su equipo de minería\n"
      "simplificando el calculo de las ganancias. Gracias de nuevo por usar la herramienta y suerte con la minería.\n")

# Comienzo del código

#Profit estimado
URL = "https://bitinfocharts.com/monero/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
profit1k = str(soup.find(id="tdid32"))
profit1k = profit1k[16:len(profit1k)]
profit1k = profit1k.split(" ")
profit1k = float(profit1k[0])

#Precio luz
URL2 = "https://preciosdelaluz.es/"
page2 = requests.get(URL2)
soup2 = BeautifulSoup(page2.content, "html.parser")
precioluz = str(soup2.find_all("div", class_="preciomed")).split("span")[1]
precioluz = precioluz[1:len(precioluz)]
precioluz = float(precioluz[:len(precioluz)-2]) / 1000

#Loop del programa
while True:
    comando = input("Que quiere hacer? {}[C]alcular profit , {}[P]ro Mode, {}[A]yuda , {}[F]órmulas, {}[E]xit: "
                    .format(colorama.Fore.GREEN, colorama.Fore.MAGENTA, colorama.Fore.YELLOW, colorama.Fore.BLUE,
                            colorama.Fore.LIGHTRED_EX)+colorama.Fore.CYAN)

    if comando == "C":
        # Variables
        pow_cost = float(input("Consumo de energía (en vatios):"))
        hashrate = float(input("Mining Hashrate (en kH/s):"))
        horasminando = float(input("Horas minando al día:"))
        profit1keur = float(profit1k / 24 * horasminando)
        gananciadiaeur = hashrate * profit1keur
        # Fórmulas
        costedia = precioluz * horasminando * pow_cost
        profitdiaeur = gananciadiaeur - costedia
        profitdiaper = gananciadiaeur - costedia * 100
        # Info
        print("Ganado por día {}EUR.".format(gananciadiaeur))
        print("Coste por dia {}.".format(costedia))
        print("Profit al día {}€ o un {}%.".format(profitdiaeur, profitdiaper))
        print("\n Tenga en cuenta que debido al constante cambio en los precios de luz, de la propia moneda y de la "
              "network difficulty/hashrate o pool share los valores son muy estimados.")
    if comando == "P":
        # Variables
        elec_cost = float(input("Coste de la electricidad (en kW/h)"))
        pow_cost = float(input("Consumo de energía (en vatios):"))
        hashrate = float(input("Mining Hashrate (en kH/s):"))
        horasminando = float(input("Horas minando al día:"))
        profit1keur = float(profit1k / 24 * horasminando)
        gananciadiaeur = hashrate * profit1keur
        # Fórmulas
        costedia = (elec_cost * (horasminando * pow_cost) / 1000)
        profitdiaeur = gananciadiaeur - costedia
        profitdiaper = gananciadiaeur - costedia * 100
        # Info
        print("Ganado por día {}EUR.".format(gananciadiaeur))
        print("Coste por dia {}.".format(costedia))
        print("Profit al día {}€ o un {}%.".format(profitdiaeur, profitdiaper))
        print("\n Tenga en cuenta que debido al constante cambio en los precios de luz, de la propia moneda y de la"
              " network difficulty/hashrate o pool share los valores son muy estimados.")

    if comando == "F":
        #Fórmulas explicadas
        print("Las fórmulas usadas son las siguientes:\n"
              "{}profit1k {}(es una variable que depende del H/s de la network, la network difficulty y el share de la "
              "pool "
              "por lo tanto el mayor error de la calucladora se encuentra "
              "en este valor\n"
              "{}profit1k {}= {}(Ganancias estimadas en 24h por cada 1kH/s en euros) {}/ {}24 {}* {}Horas minando "
              "\n"
              "{}Ganancia/Dia {}= {}Hash/s {}* {}profit1k\n"
              "{}Coste/Dia {}= {}Precio electricidad {}* {}Horas minando {}* {}Voltaje del equipo\n"
              "{}Profit/Dia {}(en euros) {}= {}Ganancia/Dia {}- {}Coste/Dia\n"
              "{}Profit/Dia {}(en porcentaje) {}= {}Ganancia/Dia {}- {}Coste/Dia {}* {}100\n".format(
                                                                                     colorama.Fore.LIGHTBLUE_EX,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.LIGHTBLUE_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.BLUE,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTWHITE_EX,
                                                                                     colorama.Fore.LIGHTGREEN_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.RED,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTBLUE_EX,
                                                                                     colorama.Fore.LIGHTRED_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.LIGHTWHITE_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.CYAN,
                                                                                     colorama.Fore.GREEN,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTGREEN_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTRED_EX,
                                                                                     colorama.Fore.GREEN,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTGREEN_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTRED_EX,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.BLUE))

    if comando == "A":
        #Tab de ayuda sobre el uso del programa
        print("\n\nSi necesita cualquier tipo de ayuda siempre puede encontrarla en mi página de github.\n"
              "  -No obstante le escribo los motivos de consulta más frecuentes resueltos:\n"
              "  -Dónde puedo encontrar todos los datos que la calculadora me pide?:\n"
              "  -Hashrate en H/s: Puede encontrarlo en su software de minería\n"
              "  -Coste de la electricidad: SOLO SI ESTA EN MODO PRO, debe buscarlo en una página web, tenga en cuenta "
              "que este precio varía a lo largo del día\n"
              "  -Consumo de energía en vatios: recomiendo el uso de software externo tal como HWMonitor\n"
              "  link no sponsorizado: https://www.cpuid.com/softwares/hwmonitor.html\n")

    if comando == "E":
        quit()

    else:
        print("Asegúrate de usar el formato correcto: [C]alcular profit , [A]yuda , [F]órmulas, [P]ro Mode, [E]xit.\n ")
