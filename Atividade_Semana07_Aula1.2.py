# primeira Data
dia = int(input(""))
mes = int(input(""))
ano = int(input(""))
# Segunda Data
dias = int(input(""))
meses = int(input(""))
anos = int(input(""))
if ano > anos or dia > dias or mes > meses:
    print(f"{dia}/{mes}/{ano}")
elif anos > ano or dias > dia or meses > mes:
    print(f"{dias}/{meses}/{anos}")
else:
    print(f"{dia}/{mes}/{ano}")
