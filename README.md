# Breit-Wigner
Esta equação é usada para modelar como nêutrons interagem com núcleos no combustível nuclear

# 📊 Tabela Convoluída da Integral \( \psi(x, t) \)

Este projeto fornece uma implementação em Python da integral convoluída associada à fórmula de Breit–Wigner de ressonância nuclear, convoluída com uma distribuição de velocidades de espalhadores térmicos de Maxwell. A função \( \psi(x, t) \) representa a base para o cálculo da **seção de choque efetiva** \( \sigma_{\text{efetiva}} \), essencial na modelagem de reatores nucleares térmicos.

## 🧮 A Integral

A função \( \psi(x, t) \) é definida por:

\[
\psi(x,t) = \frac{1}{2\sqrt{\pi t}} \int_{-\infty}^{\infty} \frac{e^{-\frac{(x - y)^2}{4t}}}{1 + y^2} \, dy
\]

Ela representa a convolução da seção de choque de ressonância com a distribuição de velocidades dos nêutrons térmicos. Os parâmetros envolvidos são:

- **x**: diferença adimensional entre a energia do nêutron e a energia de ressonância;
- **t**: parâmetro relacionado à temperatura do espalhador, razão de massas e largura de ressonância.

## 📚 Base de Dados

O projeto inclui dados digitalizados do relatório técnico [WAPD-SR-506](https://www.osti.gov/biblio/4364484), volume I, que contém valores tabelados de \( \psi(x,t) \) para múltiplas combinações de x e t:

- \( t \in [0.000, 2.000] \)
- \( x \in [0.0, 19.5] \)
- Resoluções variáveis: \( \Delta t = 0.005 \) até \( 0.0625 \), \( \Delta x = 0.05 \) até \( 0.5 \)

## 📦 Estrutura do Projeto

```bash
├── tabela_psi_volume_I.csv     # Tabela extraída com valores de ψ(x, t)
├── consultar_psi.py            # Script Python interativo para consulta
├── README.md                   # Este arquivo

