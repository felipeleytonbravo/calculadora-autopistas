def calcular_tarifa(tipo_vehiculo):
    tarifas = {
        "auto": 500,
        "moto": 300,
        "camion": 1000,
        "bus": 800
    }
    return tarifas.get(tipo_vehiculo.lower(), 0)

def main():
    print("=== Calculadora de Tarifa de Autopista ===")
    tipo = input("Ingrese tipo de vehiculo (auto / moto / camion / bus): ")
    tarifa = calcular_tarifa(tipo)
    if tarifa == 0:
        print("Tipo de vehiculo no valido.")
    else:
        print(f"La tarifa para '{tipo}' es: $ {tarifa}")

if __name__ == "__main__":
    main()
