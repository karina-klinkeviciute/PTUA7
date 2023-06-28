# zodiako zenklu sarasas
zodiakai = (("avinas", "balandis", (3, 1)), ("jautis", "kovas", (2, 8)))

print("Galimi zodiako zenklai: ")

# spausdinam po viena zodiako zenklu numerius ir pavadinimus
for zodiakas in zodiakai:
    print(zodiakai.index(zodiakas), zodiakas[0])

zenklas = int(input("pasirinkite zodiako zenkla pagal numeri: "))

zenklo_info = zodiakai[zenklas]

print(zodiakai[zenklas])

# for zodiakas in zodiakai:
#     if zenklas == zodiakas[0]:
#         print(zodiakas[2])
