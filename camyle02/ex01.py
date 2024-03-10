def substituir_valores(vetor):
    for x in range(len(vetor)):
        if vetor[x] > 0:
            vetor[x] = 1
        else:
            vetor[x] = 0

def main():
    vetor = []
    for x in range(30):
        num = float(input(f"Digite o número {x+1}: "))
        vetor.append(num)

    print("Vetor original:", vetor)

    substituir_valores(vetor)

    print("Vetor após substituição:", vetor)

if __name__ == "__main__":
    main()