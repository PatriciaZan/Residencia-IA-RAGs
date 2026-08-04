# 📃 Aula 01

## 🛠 Para rodar em sua máquina:

1. Nescessário a instalação do ambiente:
```
    # No Windows
      python -m venv venv
    
    # No Linux/macOS
      python3 -m venv venv

```

2. A inicialização do ambente por meio do comando:
```
    # No Linux/macOS
        source venv/bin/activate
    
    # No Windows
        venv\Scripts\activate
```

3. Nescessário a instalação dos pacotes por meio do comando: <br>
```
    pip install -r requirements.txt  
 ```

4. Nescessario a criação do arquivo e suas variáveis de ambiente:

- ``.env `` crie este arquivo na raiz do projeto
- Adicione as chaves nescessárias para testes e funcionamento, tais como no arquivo ``.envExemple`` ou:
```
    API_KEY=sua_chave_de_api_aqui
    OPENROUTER_API_KEY=gpt-4o-mini
```

## 🔧 Melhorias futuras (finalizado)
- [X] Connectar com outra LLM
- [X] Testar com mais inputs 