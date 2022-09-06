import math
#print(math.pi)


kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

#kanta_n = float(kanta)
#korkeus_n = float(korkeus)

piiri = kanta * 2 + korkeus * 2
print(f'Suorakulmion piiri on: {piiri:.2f}')

pinta_ala = kanta * korkeus
print(f'Suorakulmion pinta-ala on: {pinta_ala:.2f}')