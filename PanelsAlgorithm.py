def calcular_paneles(techo, panel):
    ancho_techo, alto_techo = techo
    ancho_panel, alto_panel = panel

    max_paneles = [0, 0, 0]  # [cantidad_paneles, ancho_ocupado, alto_ocupado]

    # Intentamos las dos orientaciones de los paneles
    for panel_w, panel_h in [(ancho_panel, alto_panel), (alto_panel, ancho_panel)]:
        total_paneles = 0
        resto_ancho = ancho_techo
        resto_altura = alto_techo
        paneles_por_fila = 0
        paneles_por_columna = 0

        # Calculamos paneles en filas y columnas
        paneles_por_fila = resto_ancho // panel_w
        paneles_por_columna = resto_altura // panel_h
        total_paneles = paneles_por_fila * paneles_por_columna

        # Calculamos las dimensiones ocupadas
        ancho_ocupado = paneles_por_fila * panel_w
        alto_ocupado = paneles_por_columna * panel_h

        # Si encontramos más paneles, actualizamos el máximo
        if total_paneles > max_paneles[0]:
            max_paneles = [total_paneles, ancho_ocupado, alto_ocupado]

    return max_paneles


# Ejemplo de uso
while True:
    techo = input("Por favor ingrese las dimensiones del techo.\n(Ejemplo: 10x10)\nIngresa dimensiones: ")
    panel = input("Por favor ingrese las dimensiones de los paneles.\n(Ejemplo: 2x2)\nIngresa dimensiones: ")

    # Parseamos las dimensiones
    techo = list(map(int, techo.split("x")))
    panel = list(map(int, panel.split("x")))

    cant_paneles = 0
    regiones_por_probar = [techo]  # Inicializamos con la región completa

    # Iterativamente probamos todas las regiones disponibles
    while regiones_por_probar:
        region_actual = regiones_por_probar.pop(0)  # Sacamos una región para procesar
        resultado = calcular_paneles(region_actual, panel)
        if resultado[0] > 0:
            # Agregamos paneles encontrados
            cant_paneles += resultado[0]

            # Calculamos subregiones restantes y las agregamos para probarlas
            ancho_restante = region_actual[0] - resultado[1]
            alto_restante = region_actual[1] - resultado[2]

            # Subregión horizontal (a la derecha del espacio ocupado)
            if ancho_restante > 0:
                regiones_por_probar.append([ancho_restante, region_actual[1]])

            # Subregión vertical (debajo del espacio ocupado)
            if alto_restante > 0:
                regiones_por_probar.append([region_actual[0], alto_restante])

    if cant_paneles > 0:
        print(f"\n> Caben {cant_paneles} paneles en el techo.\n")
    else:
        print("\n> No caben los paneles de esas dimensiones en el techo indicado.\n")