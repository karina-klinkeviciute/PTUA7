# tuple
geles = ("Ramunė", "Rožė", "Lobelija", "Rožė")


# is tuple darom sarasa
geliu_sarasas = list(geles)

# is tuple darom aibe
geliu_aibe = set(geles)

print(geles)

print(geliu_sarasas)

print(geliu_aibe)

# sujungiam tuple elementus į eilutę
geles_string = " - ".join(geles)

print(geles_string)

print(geles)

# eiluciu skaidymas
print('Žalgiris, Rytas, Neptūnas, Liverpulis'.split(", "))

komandos = 'Žalgiris, Rytas, Neptūnas, Liverpulis'

print(type(komandos))

kintamasis = (1, )

print(kintamasis)

tekstas = ("LKL yra pagrindine krepsinio lyga", )

tekstas = tekstas.replace("pagrindine", "didziausia")

print(tekstas)
# print(naujas_tekstas)
