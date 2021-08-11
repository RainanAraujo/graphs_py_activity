def matrizGenerate(size, matriz):
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matriz.append(row)

def addEdges(matriz):
    while True:
        answer = input("Adicionar uma aresta na matriz: [y/n]")
        if answer == "n":
            break
        elif answer == "y":
            row = int(input('Digite a linha: '))
            column = int(input('Digite a coluna: '))
            matriz[row - 1][column - 1] += 1
            if row != column:
                matriz[column - 1][row - 1] += 1
        
def printMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end = "  ")
        print("")

def printDegrees(matriz):
    for index,line in enumerate(matriz):
        print(f"{index + 1}º vértice = {sum(line)} Graus")

    

def maxDegrees(matriz):
    degreesList = [sum(line) for line in matriz] 
    print(f"Maior grau = {max(degreesList)}")

def minDegress(matriz):
    degreesList = [sum(line) for line in matriz] 
    print(f"Menor grau = {min(degreesList)}")
    

matriz = []
size = int(input("TAMANHO DA MATRIZ QUADRADA: "))

matrizGenerate(size, matriz)
printMatriz(matriz)
addEdges(matriz)
printMatriz(matriz)
printDegrees(matriz)
maxDegrees(matriz)
minDegress(matriz)

