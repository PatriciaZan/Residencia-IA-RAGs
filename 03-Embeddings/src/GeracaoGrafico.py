
labels = list(banco_embeddings.keys())
vetores = list(banco_embeddings.values())

# Reduz a dimensão dos embeddings usando PCA
pca = PCA(n_components=2)
vetores_2d = pca.fit_transform(vetores)

plt.figure(figsize=(10, 7))


plt.scatter(vetores_2d[:, 0], vetores_2d[:, 1], color='dodgerblue', edgecolors='k', s=120)


for i, palavra in enumerate(labels):
    plt.annotate(
        palavra,
        (vetores_2d[i, 0], vetores_2d[i, 1]),
        textcoords="offset points",
        xytext=(8, 5),
        ha='center',
        fontsize=10,
        fontweight='bold'
    )


plt.title("Visualização Espacial das similaridades", fontsize=14, fontweight='bold')
plt.xlabel("Componente 1", fontsize=11)
plt.ylabel("Componente 2", fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# OUTPUT OBTIDO COLAB ________________________________________________
# Arquivo grafico.png contido no src do projeto