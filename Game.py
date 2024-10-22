palabra = list("casa")
n = len(palabra)
letra = ""
entrada = ['-'for _ in range(n)] #Concepto de Listas de comprensión
vidas = 6
encontrado = False

#print(entrada)

#for (int i = 0; i <= 3; i++)
print("Bienvenido al juego del ahorcado")
print(f"Cuentas con {vidas} vidas")
print(f"Estado actual: {entrada}")
while(entrada != palabra):
    letra = input("Ingresa una letra: ")
    for i in range(n):
        if palabra[i] == letra:
            print(f"Si existe {letra} en la posición {i}")
            entrada[i] = letra
            encontrado = True
    if encontrado == False:
        print(f"La letra {letra} no existe, bu!")
        vidas -= 1
        
    
    print(f"Estado actual: {entrada}")
    print(f"Vidas restantes: {vidas}")

    if vidas == 0:
        print("Perdiste todas tus vidas")
        break
   
    
    encontrado = False
    print()

if entrada  == palabra:
    print("Felicidades ganaste!")
print("Game Over")
