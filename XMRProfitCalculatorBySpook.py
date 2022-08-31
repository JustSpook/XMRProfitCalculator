# Arte de consola + introducción
import pyfiglet
import colorama
colorama.init(autoreset=True)
T = str("Spook \n XMR Profit calculator")
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
print(
    "Bienvenidos a mi calculador de profit de XMR, para usarlo solo introduzca los datos pedidos en el formato"
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
while True:
    comando = input("Que quiere hacer? {}[C]alcular profit , {}[A]yuda , {}[F]órmulas, {}[P]ro Mode, {}[E]xit: "
                    .format(colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.LIGHTGREEN_EX,
                            colorama.Fore.LIGHTRED_EX)+colorama.Fore.CYAN)

    if comando == "C":
        # Variables
        elec_cost = float(input("Coste de la electricidad (en €/Wh):"))
        pow_cost = float(input("Consumo de energía (en vatios):"))
        hashrate = float(input("Mining Hashrate (en kH/s):"))
        horasminando = float(input("Horas minando al día:"))
        profit1keur = float(0.024 / 24 * horasminando)
        profit1kxmr = float(0.0001619 / 24 * horasminando)
        gananciadiaeur = hashrate * profit1keur
        gananciadiaxmr = hashrate * profit1kxmr
        # Fórmulas
        costedia = elec_cost * horasminando * pow_cost
        profitdiaeur = gananciadiaeur - costedia
        profitdiaper = gananciadiaeur - costedia * 100
        # Info
        print("Ganado por día {}XMR o {}EUR.".format(gananciadiaxmr, gananciadiaeur))
        print("Coste por dia {}.".format(costedia))
        print("Profit al día {}€ o un {}%.".format(profitdiaeur, profitdiaper))
        print("\n Tenga en cuenta que debido a que no ha seleccionado la opción pro y al constante cambio en los "
              "precios de "
              "luz, de la propia moneda y de la network difficulty/hashrate o pool share los valores son muy "
              "estimados.")

    if comando == "P":
        # Variables
        elec_costact = float(input("Coste de la electricidad (en €/Wh):"))
        pow_costact = float(input("Consumo de energía (en vatios):"))
        hashrateact = float(input("Mining Hashrate (en kH/s): "))
        horasminandoact = float(input("Horas minando al día: "))
        profit1keuract = float(input("Profit/Día/1kH/s en euros: "))
        profit1kxmract = float(input("Profit/Día/1kH/s en XMR: "))
        profit1keuract2 = profit1keuract / 24 * horasminandoact
        profit1kxmract2 = profit1kxmract / 24 * horasminandoact
        gananciadiaeuract = hashrateact * profit1keuract2
        gananciadiaxmract = hashrateact * profit1kxmract2
        # Fórmulas
        costediaact = elec_costact * horasminandoact * pow_costact
        profitdiaeuract = gananciadiaeuract - costediaact
        profitdiaperact = gananciadiaeuract - costediaact * 100
        # Info
        print("Ganado por día {}XMR o {}EUR.".format(gananciadiaxmract, gananciadiaeuract))
        print("Coste por dia {}.".format(costediaact))
        print("Profit al día {}€ o un {}%.".format(profitdiaeuract, profitdiaperact))
        print("\n Tenga en cuenta que debido a que los shares de la pool, y el precio de la luz no es constante"
              "este valor es una buena aproximación pero no es el valor exacto del profit.")

    if comando == "F":
        print("Las fórmulas usadas son las siguientes:\n"
              "{}profit1k {}(es una variable que depende del H/s de la network, la network difficulty y el share de la "
              "pool "
              "en este caso calculada a día 28/08/2022 para 1kH/s por lo tanto el mayor error de la calucladora se "
              "encuentra "
              "en este valor que puede ser ajustado en el modo Pro para mas precisión)\n "
              "{}profit1k {}= {}Ganancias estimadas en 24h por cada 1kH/s en euros o xmr {}/ {}24 {}* {}Horas minando "
              "\n"
              "{}Ganancia/Dia = {}Hash/s {}* {}profit1k\n"
              "{}Coste/Dia = {}Precio electricidad {}* {}Horas minando {}* {}Voltaje del equipo\n"
              "{}Profit/Dia (en euros) = {}Ganancia/Dia {}- {}Coste/Dia\n"
              "{}Profit/Dia (en porcentaje) = {}Ganancia/Dia {}- {}Coste/Dia {}* {}100\n".format(
                                                                                     colorama.Fore.LIGHTBLUE_EX,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.LIGHTBLUE_EX,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.RESET,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.BLUE,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.LIGHTWHITE_EX,
                                                                                     colorama.Fore.LIGHTGREEN_EX,
                                                                                     colorama.Fore.RED,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.LIGHTBLUE_EX,
                                                                                     colorama.Fore.LIGHTRED_EX,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.LIGHTYELLOW_EX,
                                                                                     colorama.Fore.LIGHTWHITE_EX,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.CYAN,
                                                                                     colorama.Fore.GREEN,
                                                                                     colorama.Fore.LIGHTGREEN_EX,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.LIGHTRED_EX,
                                                                                     colorama.Fore.GREEN,
                                                                                     colorama.Fore.LIGHTGREEN_EX,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.LIGHTRED_EX,
                                                                                     colorama.Fore.YELLOW,
                                                                                     colorama.Fore.BLUE))

    if comando == "A":
        print("\n\nSi necesita cualquier tipo de ayuda siempre puede encontrarla en mi página de github.\n"
              "  -No obstante le escribo los motivos de consulta más frecuentes resueltos:\n"
              "  -Dónde puedo encontrar todos los datos que la calculadora me pide?:\n"
              "  -Hashrate en H/s: Puede encontrarlo en su software de minería\n"
              "  -Coste de la electricidad: Debe buscarlo en una página web, tenga en cuenta que este precio varía a lo"
              "largo del día\n"
              "  -Consumo de energía en vatios: recomiendo el uso de software externo tal como HWMonitor\n"
              "  link no sponsorizado: https://www.cpuid.com/softwares/hwmonitor.html\n"
              "  -Si está en modo PRO puede que le interese buscar el valor de profit1k actual\n"
              "personalmente uso la página https://bitinfocharts.com/monero/ (de nuevo mención no sponsorizada)\n"
              "aunque puede calcularlo usted mismo.\n")

    if comando == "E":
        quit()

    else:
        print("Asegúrate de usar el formato correcto: [C]alcular profit , [A]yuda , [F]órmulas, [P]ro Mode, [E]xit.\n ")
