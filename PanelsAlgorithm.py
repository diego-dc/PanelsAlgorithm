
while True:
    techo = input("Por favor ingrese las dimensiones del techo.\n(Ejemplo: 10x10)\nIngresa dimensiones: ")
    paneles = input("Por favor ingrese las dimensiones de los paneles. \n(Ejemplo: 2x2)\nIngresa dimensiones: ")

    techo = techo.split("x")
    paneles = paneles.split("x")

    AreaTecho = int(techo[0]) * int(techo[1])
    AreaPanel = int(paneles[0]) * int(paneles[1])

    panelesNecesarios = AreaTecho / AreaPanel
    cabenPaneles = (techo[0] >= paneles[0] and techo[1] >= paneles[1] ) or (techo[0] >= paneles[1] and techo[1] >= paneles[0])
    if panelesNecesarios > 0 and cabenPaneles:
        print("> Caben ", int(panelesNecesarios), "paneles" + "\n")
    else:
        print("> No caben los paneles de esas dimensiones en el techo indicado." + "\n")