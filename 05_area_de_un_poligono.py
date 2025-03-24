# Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  La función recibirá por parámetro sólo UN polígono a la vez.
#  Los polígonos soportados serán Triángulo (b x h / 2), Cuadrado (l x l) y Rectángulo (b x h).
#  Imprime el cálculo del área de un polígono de cada tipo.


def calcular_area(tipo_poligono, base=None, altura=None, lado=None):
    if tipo_poligono == "triángulo":
        return (base * altura) / 2
    elif tipo_poligono == "cuadrado":
        return lado * lado
    elif tipo_poligono == "rectángulo":
        return base * altura
    else:
        return "Tipo de polígono no soportado"

# Ejemplo de uso para cada tipo de polígono
print(f"El área del triángulo es: {calcular_area('triángulo', base=5, altura=10)}")
print(f"El área del cuadrado es: {calcular_area('cuadrado', lado=4)}")
print(f"El área del rectángulo es: {calcular_area('rectángulo', base=6, altura=8)}")