def distancia_cosseno(vetor1, vetor2):
    # 1. Produto escalar (dot product)
    produto_escalar = sum(a * b for a, b in zip(vetor1, vetor2))

    # 2. Magnitudes dos vetores
    magnitude1 = math.sqrt(sum(a ** 2 for a in vetor1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vetor2))

    # Prevenção contra divisão por zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 1.0

    # 3. Retorna a distância (1 - similaridade)
    similaridade = produto_escalar / (magnitude1 * magnitude2)
    return 1.0 - similaridade










