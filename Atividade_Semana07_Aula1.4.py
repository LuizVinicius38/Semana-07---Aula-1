primeiroValor = int(input(""))
segundoValor = int(input(""))
terceiroValor = int(input(""))
quartoValor = int(input(""))
quintoValor = int(input(""))
media = (primeiroValor + segundoValor + terceiroValor +
         quartoValor + quintoValor) / 5
print(format(media, '.2f'))
if primeiroValor > media:
    print(format(primeiroValor, '.2f'))
if segundoValor > media:
    print(format(segundoValor, '.2f'))
if terceiroValor > media:
    print(format(terceiroValor, '.2f'))
if quartoValor > media:
    print(format(quartoValor, '.2f'))
if quintoValor > media:
    print(format(quintoValor, '.2f'))
         

