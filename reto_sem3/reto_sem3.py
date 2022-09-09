#Reto semana3 Desarrollo de aplicaciones web avanzado - 2022 - 2
#Grupo: Caceres Serna Nicole Jane y Turin Scharff Dario Jose
a=[19,20,21]
b=[15,32,18]
contA=0
contB=0
for i in range(3):
    if a[i] > b[i]:
        contA = contA + 1
    if a[i] < b[i]:
        contB = contB +1
    else:
        continue

print("Alice",contA)
print("Bob",contB)

