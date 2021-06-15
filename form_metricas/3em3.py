#lista = ["Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Medio", "Alto"]

path_linha = "linha_resp.txt"
file_linha = open(path_linha, "r")
lista = file_linha.read().split()

size = len(lista)

print("Quantidade de itens: ", size)

path_resp_final = "resp.txt"
file_resp_final = open(path_resp_final, "w")
passo = 3
final = ""

for i in range(size):
    final += lista[i]
    ordem_resp = i + 1
    if ((ordem_resp % passo) == 0):
        final += "\n"
    if (i < size and ((ordem_resp % passo) != 0)):
        final += "\t"

file_resp_final.write(final)

print(final)
