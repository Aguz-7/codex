# Programa de checklist para pruebas de celular


def obtener_respuesta(pregunta):
    while True:
        resp = input(pregunta + " (s/n): ").strip().lower()
        if resp in ('s', 'n'):
            return resp == 's'
        print("Por favor ingrese 's' para si o 'n' para no.")

def main():
    pruebas = [
        "Pantalla",
        "Botones",
        "Camara",
        "Microfono",
        "Altavoz",
        "Vibracion",
        "Conectividad WiFi",
        "Bluetooth"
    ]

    resultados = {}
    print("Prueba basica de funciones del celular\n")
    for prueba in pruebas:
        resultados[prueba] = obtener_respuesta(f"¿Funciona {prueba}?")

    print("\nResumen de pruebas:")
    for prueba, exito in resultados.items():
        estado = "OK" if exito else "FALLA"
        print(f"- {prueba}: {estado}")

    guardar = obtener_respuesta("¿Desea guardar el reporte en un archivo?")
    if guardar:
        nombre_archivo = "reporte_pruebas.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            for prueba, exito in resultados.items():
                estado = "OK" if exito else "FALLA"
                f.write(f"{prueba}: {estado}\n")
        print(f"Reporte guardado en {nombre_archivo}")

if __name__ == "__main__":
    main()
