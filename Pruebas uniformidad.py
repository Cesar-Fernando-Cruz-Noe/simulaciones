# PRUEBAS UNIFORMIDAD SIMULACION ESTOCASTICA
def generador_congruencial_lineal(n, semilla=6):
    a = 1664525
    c = 1013904223
    m = 2**32  # Esto asegura que los números estén en un rango grande
    
    X = semilla    
    numeros = []
    
    for _ in range(n):
        X = (a * X + c) % m
        numero_aleatorio = X / m
        numeros.append(numero_aleatorio)
    
    return numeros

n = 1000
numeros_generados = generador_congruencial_lineal(n)

print(numeros_generados[:10])
################################################################################
print('########################## PRUEBA DE LA MEDIA ##################################')

def prueba_media(numeros):
    media_observada = sum(numeros)/len(numeros) #Calculamos la media

    media_esperada = 0.5 #Media esperada para la distribución uniforme [0, 1]

    print(f"Media observada: {media_observada}")
    print(f"Media esperada: {media_esperada}")

    if abs(media_observada - media_esperada) < 0.05:
        print("Los datos tienen una media cercana a la distribución")
    else:
        print("Los datos no tienen una media cercana a la distribución")
        
# numeros = [0.67, 0.678, 0.567, 0.87, 0.123, 0.567]

print(prueba_media(numeros_generados))

################################################################################
print ('########################### PRUEBA DE LA VARIANZA ##############################')
def prueba_varianza(numeros):
    media = sum(numeros) / len(numeros) # Calculamos la media

    varianza_observada = sum((x - media)**2 for x in numeros)/len(numeros)

    varianza_esperada = 1/(108 * n)

    print(f'Varianza observada: {varianza_observada}')
    print(f'Varianza esperada: {varianza_esperada}')

    if abs(varianza_observada - varianza_esperada) < 0.01:

        print('Los datos parecen tener una varianza cercana a la distribución uniforme')
    else:
        print('Los datos no tienen una varianza cercana a la distribución')

prueba_varianza(numeros_generados)

################################################################################
print('########################### PRUEBA DE CHI-CUADRADA #############################')
def prueba_chi_cuadrada(numeros, k = 100):
    intervalos = [0] * k #Dividimos los intervalos "k"
    
    n = len(numeros)

    for numero in numeros:
        index = int(numero * k)
        if index == k:
            index = k - 1
        intervalos[index] += 1

    frecuencia_esperada = n/k

    chi_cuadrado = sum((obs - frecuencia_esperada) ** 2 / frecuencia_esperada for obs in intervalos)

    print(f'Estadística de Chi-Cuadrado: {chi_cuadrado}')

    valor_critico = 16.92

    if chi_cuadrado < valor_critico:
        print('No se rechaza la hipótesis de que los numeros siguen una distribución uniforme')
    else:
        print('Se rechaza la hipótesis de que los números siguen una distribución uniforme')

prueba_chi_cuadrada(numeros_generados)












