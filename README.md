# Projeto de Sistema de Fidelidade

Este projeto implementa um sistema de programa de fidelidade com diferentes níveis de clientes (Padrão, Premium e VIP).

## Requisitos

-   Python 3.8+
-   pip (gerenciador de pacotes Python)

## Instalação

### 1. Clonar o repositório

```bash
cd projeto_teste
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## Executando os Testes

### Rodar todos os testes

```bash
pytest
```

### Rodar testes com relatório de cobertura

```bash
pytest --cov=src --cov-report=html
```

Este comando irá gerar um relatório HTML detalhado na pasta `htmlcov/`. Abra o arquivo `htmlcov/index.html` em um navegador para visualizar a cobertura de testes.

### Rodar testes com mais verbosidade

```bash
pytest -v
```

### Rodar um arquivo de testes específico

```bash
pytest tests/test_loyalty_system.py
```

### Rodar um teste específico

```bash
pytest tests/test_loyalty_system.py::test_calcular_pontos_compra_cliente_padrao
```

## Estrutura do Projeto

```
projeto_teste/
├── src/                      # Código-fonte principal
│   ├── __init__.py
│   ├── customer.py           # Definição da classe Cliente
│   ├── loyalty_system.py     # Sistema de fidelidade
│   └── main.py               # Ponto de entrada
├── tests/                    # Testes automatizados
│   ├── __init__.py
│   └── test_loyalty_system.py
├── htmlcov/                  # Relatório de cobertura (gerado)
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

## Dependências

O projeto utiliza as seguintes bibliotecas:

-   **pytest**: Framework para testes
-   **pytest-cov**: Plugin para relatório de cobertura de testes
-   **coverage**: Ferramenta para análise de cobertura de código
