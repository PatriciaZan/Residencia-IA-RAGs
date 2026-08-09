
def distancia_euclidiana(vetor1, vetor2):
    soma_quadrados = sum((a - b) ** 2 for a, b in zip(vetor1, vetor2))
    return math.sqrt(soma_quadrados)

