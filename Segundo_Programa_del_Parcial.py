# Solicitar al usuario que ingrese un número entero positivo
num = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if num <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Inicializamos la secuencia y el resultado
    resultado = 0
    secuencia = ""

    # Generamos la secuencia y calculamos el resultado
    for i in range(1, num + 1):
        valor_operar = 1 / i
        if i % 2 == 0: # Si i es par
            resultado -= valor_operar # Restamos valor_operar del resultado
            secuencia += f" - (1/{i})" # Actualizamos la cadena "Secuencia" agregandole el sogno - para restar
        else: # Si i es impar
            resultado += valor_operar # Sumamos valor_operar del resultado
            if i == 1: # Si i es 1 omitimos el signo +
                secuencia += f"(1/{i})" 
            else: # Si es cualquier otro valor impar actualizamos la cadena con el signo + para sumar
                secuencia += f" + (1/{i})"
    
    # Mostramos la secuencia y el resultado
    print(f"Secuencia: {secuencia}")
    print(f"Resultado: {resultado}")



