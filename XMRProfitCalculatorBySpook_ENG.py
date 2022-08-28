# Arte de consola + introducción
import pyfiglet
import colorama
colorama.init(autoreset=True)
T = str("Spook \n XMR Profit calculator")
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
print(
    "Welcome to my XMR profit calculator, to use it just enter the requested data in the correct"
    "format.\n\nTo search for this data I recommend the use of external websites and the use of external software for "
    "data such as the voltage of your equipment.\n")
print(
    "If this tool has helped you and you consider it appropriate, I accept donations in the following monero wallet:\n "
    "45ySHwq1dyxdiktXCPiJrkQRZaQZNrVDgcJ5nrycrYyN9nWji9FTLG9KJAhbzPvydZV6kgjjEbhjkJETm4jrGCxj11xD7ys"
    "\n")
print("Disclaimer:\n"
      "Please note that the values provided by this tool are never going to be exact,\n"
      "perhaps there is a web page that calculates this data with greater precision (or not) but the idea\n"
      "of this tool is to eliminate the need to install or open a browser on your mining rig\n"
      "simplifying the calculation of profits. Thanks again for using the tool and good luck mining.\n")

# Comienzo del código
while True:
    comando = input("What do you want to do? {}[C]alculate profit , {}[H]elp , {}[F]ormulas, {}[P]ro Mode, {}[E]xit: "
                    .format(colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.LIGHTGREEN_EX,
                            colorama.Fore.LIGHTRED_EX)+colorama.Fore.CYAN)

    if comando == "C":
        # Variables
        elec_cost = float(input("Cost of electricity (in €/Wh):"))
        pow_cost = float(input("Power consumption (in watts):"))
        hashrate = float(input("Mining Hashrate (in kH/s):"))
        horasminando = float(input("Hours mining per day:"))
        profit1keur = float(0.024 / 24 * horasminando)
        profit1kxmr = float(0.0001619 / 24 * horasminando)
        gananciadiaeur = hashrate * profit1keur
        gananciadiaxmr = hashrate * profit1kxmr
        # Fórmulas
        costedia = elec_cost * horasminando * pow_cost
        profitdiaeur = gananciadiaeur - costedia
        profitdiaper = gananciadiaeur - costedia * 100
        # Info
        print("Earned per day {}XMR or {}EUR.".format(gananciadiaxmr, gananciadiaeur))
        print("Cost per day {}.".format(costedia))
        print("Profit per day {}€ or {}%.".format(profitdiaeur, profitdiaper))
        print("\n Please note that due to the fact that you have not selected the pro option and the constant change "
              "in electricity prices,"
              "of the coin itself and of the network difficulty/hashrate or pool share the values are highly estimated.")

    if comando == "P":
        # Variables
        elec_costact = float(input("Cost of electricity (in €/Wh):"))
        pow_costact = float(input("Power consumption (in watts):"))
        hashrateact = float(input("Mining Hashrate (in kH/s): "))
        horasminandoact = float(input("Hours mining per day: "))
        profit1keuract = float(input("Profit/Day/1kH/s in euros: "))
        profit1kxmract = float(input("Profit/Day/1kH/s in XMR: "))
        profit1keuract2 = profit1keuract / 24 * horasminandoact
        profit1kxmract2 = profit1kxmract / 24 * horasminandoact
        gananciadiaeuract = hashrateact * profit1keuract2
        gananciadiaxmract = hashrateact * profit1kxmract2
        # Fórmulas
        costediaact = elec_costact * horasminandoact * pow_costact
        profitdiaeuract = gananciadiaeuract - costediaact
        profitdiaperact = gananciadiaeuract - costediaact * 100
        # Info
        print("Earned per day {}XMR or {}EUR.".format(gananciadiaxmract, gananciadiaeuract))
        print("Cost per day {}.".format(costediaact))
        print("Profit per day {}€ or {}%.".format(profitdiaeuract, profitdiaperact))
        print("\n Keep in mind that because the shares of the pool, and the price of electricity is not constant"
              "this value is a good approximation but it is not the exact value of the profit.")

    if comando == "F":
        print("The formulas used are the following:\n"
              "profit1k (it is a variable that depends on the H/s of the network, the network difficulty and the share of the "
              "pool "
              "in this case calculated on 08/28/2022 for 1kH/s, therefore the largest error of the calculator is "
              "is found in this value "
              "which can be adjusted in Pro mode for more precision)\n "
              "profit1k = Estimated earnings in 24h for every 1kH/s in euros or xmr / 24 * hours mining \n"
              "Earning/Day = Hash/s * profit1k\n"
              "Cost/Day = Electricity price * Mining hours * Equipment voltage\n"
              "Profit/Day (in euros) = Earning/Day - Cost/Day\n"
              "Profit/Day (in percentage) = Earning/Day - Cost/Day * 100\n")

    if comando == "H":
        print("\n\nIf you need any kind of help you can always find it on my github page.\n"
              "  -However, I write the most frequent reasons for consultation resolved:\n"
              "  -Where can I find all the data that the calculator asks me for?:\n"
              "  -Hashrate in H/s: You can find it in your mining software\n"
              "  -Cost of electricity: You must look it up on a web page, keep in mind that this price varies throughout the day\n"
              "  -Power consumption in watts: I recommend the use of external software such as HWMonitor\n"
              "  non-sponsored link: https://www.cpuid.com/softwares/hwmonitor.html\n"
              "  -If you are in PRO mode you may want to look up the current profit1k value\n"
              "I personally use the page https://bitinfocharts.com/monero/ (again non-sponsored mention)\n"
              "although you can calculate it yourself.\n")

    if comando == "E":
        quit()

    else:
        print("Make sure you use the correct format: [C]alculate profit , [H]elp , [F]formulas, [P]ro Mode, [E]xit.\n ")
