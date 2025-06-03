# README em Português (pt-BR) 🇧🇷

## ChemicalPy

ChemicalPy é uma biblioteca Python projetada para facilitar cálculos e operações relacionadas à química. Ela fornece ferramentas úteis para trabalhar com fórmulas químicas, balanceamento de equações, cálculos estequiométricos e muito mais.

### Instalação

Para instalar a biblioteca ChemicalPy, execute o seguinte comando:

```bash
pip install chemicalpy
```

### Funcionalidades

- Cálculos estequiométricos
- Balanceamento de equações químicas
- Conversão entre unidades químicas
- Cálculo de massas molares
- Geração de fórmulas químicas

### Exemplo de Uso

```python
import chemicalpy as chem

# Calcular massa molar
massa_molar = chem.calcular_massa_molar("H2O")
print(f"Massa molar da água: {massa_molar} g/mol")

# Balancear equação química
equacao = "H2 + O2 -> H2O"
equacao_balanceada = chem.balancear_equacao(equacao)
print(f"Equação balanceada: {equacao_balanceada}")
```

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

### Licença

Este projeto está licenciado sob a licença MIT.

---

# README in English 🇺🇸

## ChemicalPy

ChemicalPy is a Python library designed to facilitate chemistry-related calculations and operations. It provides useful tools for working with chemical formulas, equation balancing, stoichiometric calculations, and more.

### Installation

To install the ChemicalPy library, run the following command:

```bash
pip install chemicalpy
```

### Features

- Stoichiometric calculations
- Chemical equation balancing
- Conversion between chemical units
- Molar mass calculations
- Chemical formula generation

### Usage Example

```python
import chemicalpy as chem

# Calculate molar mass
molar_mass = chem.calculate_molar_mass("H2O")
print(f"Molar mass of water: {molar_mass} g/mol")

# Balance chemical equation
equation = "H2 + O2 -> H2O"
balanced_equation = chem.balance_equation(equation)
print(f"Balanced equation: {balanced_equation}")
```

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
