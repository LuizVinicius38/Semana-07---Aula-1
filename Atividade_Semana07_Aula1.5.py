peso = float(input(""))
altura = float(input(""))
IMC = peso // (altura ** 2)
print(format(IMC, ".2f"))
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 35:
    print("Obeso leve")
elif IMC < 40:
    print("Obeso moderado")
elif IMC >= 40:
    print("Obeso mórbido")



