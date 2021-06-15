import random

valores = ["Baixo", "Medio", "Alto"]
linhas = 29
final = ""
passo = 3

for i in range(linhas * 3):
    rand = random.randrange(0, 3, 1)
    final += valores[rand]
    #final += "\t"
   
    ordem_resp = i + 1
    if ((ordem_resp % passo) == 0):
        final += "\n"
    if ((ordem_resp % passo) != 0):
        final += "\t"

print(final)

path_massa = "massa_linhas.txt"
file_massa = open(path_massa, "w")
file_massa.write(final)
