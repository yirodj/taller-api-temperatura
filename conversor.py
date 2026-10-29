"""Lógica del taller: convertir grados Celsius a Fahrenheit."""


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte °C a °F y redondea el resultado a dos decimales."""
    return round((celsius * 9 / 5) + 32, 2)


if __name__ == "__main__":
    temperatura = 25
    print(f"{temperatura} °C = {celsius_a_fahrenheit(temperatura):.2f} °F")
