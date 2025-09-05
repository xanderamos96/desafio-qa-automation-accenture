# QA Automation Challenge — API (DemoQA Book Store)

Este projeto implementa o fluxo completo do desafio de API usando **Python + pytest + requests**.

## 🔧 Stack
- Python 3.10+
- pytest
- requests

## 🚀 Como rodar
```bash
# 1) (Opcional) criar um ambiente virtual
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 2) Instalar dependências
pip install -r requirements.txt

# 3) Executar os testes (modo verboso)
pytest -v

# ou modo enxuto
pytest -q
```

## ℹ️ O que o teste faz
1. **Cria um usuário**  
2. **Gera um token**  
3. **Confirma autorização**  
4. **Lista livros** e escolhe dois ISBNs  
5. **Adiciona** (aluga) os dois livros ao usuário  
6. **Consulta os detalhes** do usuário e valida os livros  
7. (Bônus) **Limpa** o usuário criado ao final do teste

Toda a execução ocorre em **um único comando** (`pytest`), com **validações de status code e contrato mínimo**.

## 📁 Estrutura
```
qa-automation-challenge-api/
 ├── README.md
 ├── requirements.txt
 └── tests/
     └── test_bookstore_api_flow.py
```

## ✅ Notas de avaliação
- Código organizado e claro
- Reuso de funções utilitárias
- Asserts descritivos em falhas
- Fluxo encadeado ponta-a-ponta
- (Opcional) Fácil integração com CI/CD

> Dica: para a etapa de **UI**, podemos reaproveitar a mesma estrutura de pastas em outro repositório ou criar `tests/ui` num mono-repo.
