# Tarea #1 de Robótica NRC: 22116
# Estudiante: Erick Encalada
# Creación de mi porpia función mi_antan2(x,y)

# Usamos la librería math para usar las funciones matemáticas, en este caso el de la arcotangente normal
import math
# Usabmos la esta libraria para graficar en el plano cartesiano:
import matplotlib.pyplot as plt

#----------------------------------Celda 1: Creación de la funcion atan2----------------------------------------------#
# Función con la que creamo nuestro propio antan2
    # Esta función devolverá el ángulo en radianes entre el eje X positivo y el vector (x, y).
def mi_atan2(y, x):
    # Condicionamos el Primer y Cuarto cuadrante (x > 0); 
        # Si x es positivo, se puede usar directamente atan(y/x), ya que el ángulo estará entre -π/2 y π/2 (se comprende el primer y cuarto cuadrante)
    if x > 0:
        return math.atan(y / x)
    # Condicionamos el Segundo cuadrante (x < 0, y ≥ 0); 
        # Cuando x es negativo e y positivo o cero, el ángulo está en el segundo cuadrante.
        # math.atan(y/x) por sí solo devolvería un valor negativo; al sumar π (180°), se corrige el ángulo al cuadrante adecuado.
    elif x < 0 and y >= 0:  
        return math.atan(y / x) + math.pi
    # Condicionamos el Tercer cuadrante (x < 0, y < 0);
        # Si ambos x y y son negativos, el ángulo cae en el tercer cuadrante.
        # Se le resta π para colocarlo en el rango correcto de (-π, -π/2).
    elif x < 0 and y < 0:
        return math.atan(y / x) - math.pi
    # Casos Extras:
        # Si x es cero y y positivo, el vector apunta directamente hacia arriba. El ángulo es π/2 (90°).
    elif x == 0 and y > 0:
        return math.pi / 2
        # Si x es cero y y negativo, apunta directamente hacia abajo. El ángulo es -π/2 (-90°).
    elif x == 0 and y < 0:
        return -math.pi / 2
        # Origen (0, 0); Este es un caso especial. El ángulo no está definido matemáticamente, pero aquí se devuelve 0.0 para evitar errores o excepciones.
    elif x == 0 and y == 0:
        return 0.0  # o podrías lanzar una excepción si prefieres
        # si algo raro ocurre (como un tipo de dato inválido), lanza una excepción para advertir de un posible error de lógica o entrada.
    else:
        raise ValueError("Caso inesperado en mi_atan2.")


#----------------------------------Celda 2: Determinar el cudrante en que el punto esta ubicado----------------------------------------------#
# Función para determinar en que cuadrante esta ubicado el punto.
def determinar_cuadrante(x, y):
    if x > 0 and y > 0:
        return "Primer cuadrante"
    elif x < 0 and y > 0:
        return "Segundo cuadrante"
    elif x < 0 and y < 0:
        return "Tercer cuadrante"
    elif x > 0 and y < 0:
        return "Cuarto cuadrante"
    elif x == 0 and y != 0:
        return "Eje Y"
    elif y == 0 and x != 0:
        return "Eje X"
    elif x == 0 and y == 0:
        return "Origen"
    else:
        return "Indeterminado"
    
# Función auxiliar para comparar ángulos (considerando saltos en ±π)
def ang_diff(a, b):
    return abs((a - b + math.pi) % (2 * math.pi) - math.pi)
# Pruebas automáticas
valores_prueba = [
    (2, 2),
    (3, -3),
    (-4, -4),
    (-5, 9),
    (0, 8),
    (0, -4),
    (9, 0),
    (-10, 0),
    (0, 0),
]
print("Evaluando puntos:\n")
#----------------------------------Celda 3: Comparacion de resultados entre atan2 y mi_atan2, grafica de los resultados en el palno cartesiano----------------------------------------------#
# Visualización y resultados, se programa para poder visulaizar los puentos de prueba en un plano cartesiano (en los 4 cuadrantes)
plt.figure(figsize=(8, 8))
plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)
plt.grid(True)
plt.title("Visualización de puntos y ángulos con mi_atan2")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# iniciamos un bucle para poder comparar los resultados entre nuestra mi_atan2 y el atan2 original de la librearia import math
for y, x in valores_prueba:
    ang_math = math.atan2(y, x)
    ang_mi = mi_atan2(y, x)
    cuadrante = determinar_cuadrante(x, y)
    print(f"Punto (x={x}, y={y}) → {cuadrante}")
    print(f"  math.atan2(y, x)  = {ang_math:.6f} rad")
    print(f"  mi_atan2(y, x)    = {ang_mi:.6f} rad")

    #Verificación con tolerancia numérica (1e-6)
        # Se hace uso de try y except para evitar que el programa se detenga.
    try:
        assert ang_diff(ang_math, ang_mi) < 1e-6
        print("  ✅ Resultado correcto")
    except AssertionError:
        print("  ❌ Diferencia detectada")
    print("-" * 40)


    # Se dibuja flecha desde el origen
    plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue')
    # Se añade etiqueta con el ángulo
    plt.text(x * 1.05, y * 1.05, f"{ang_mi:.2f} rad", fontsize=9, color='darkred')
    # Configuramos la magnitud de los ejes
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal')
    plt.show()
print("Pruebas completadas.")