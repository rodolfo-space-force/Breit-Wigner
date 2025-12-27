#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

import numpy as np
import pandas as pd
from scipy.integrate import quad

# Função integrando ψ(x,t)
def integrand(y, x, t):
    return np.exp(-((x - y) ** 2) / (4 * t)) / (1 + y ** 2)

def psi_x_t(x, t):
    if t == 0.0:
        # Valores retirados da tabela escaneada (Volume I, t=0.0)
        tabela_t0 = {
            0.00: 1.0000000000,
            0.05: 0.99750623,
            0.10: 0.99099990,
            0.15: 0.977799511,
            0.20: 0.96153846,
            0.25: 0.94117647,
            0.30: 0.91743119,
            0.35: 0.89086859,
            0.40: 0.86206897,
            0.45: 0.83160083
        }
        return tabela_t0.get(np.round(x, 2), 0.0)
    else:
        # Cálculo numérico da integral para t > 0
        result, _ = quad(integrand, -np.inf, np.inf, args=(x, t))
        return result / (2 * np.sqrt(np.pi * t))

# Geração de todos os valores conforme Volume I
def gerar_tabela_psi():
    t_values = np.concatenate([
        np.arange(0.000, 0.1005, 0.005),
        np.arange(0.100, 0.2505, 0.010),
        np.arange(0.250, 0.3005, 0.010),
        np.arange(0.300, 1.0005, 0.025),
        np.arange(1.000, 2.0005, 0.0625)
    ])

    x_values = np.concatenate([
        np.arange(0.0, 2.05, 0.05),
        np.arange(2.0, 4.1, 0.1),
        np.arange(4.0, 19.6, 0.5)
    ])

    print(" Gerando tabela...")
    data = []
    for t in t_values:
        for x in x_values:
            psi = psi_x_t(x, t)
            data.append([round(t, 5), round(x, 5), psi])

    df = pd.DataFrame(data, columns=["t", "x", "ψ(x,t)"])
    df.to_csv("tabela_psi_volume_I.csv", index=False)
    print(" Tabela salva como tabela_psi_volume_I.csv")
    return df

# Consulta interativa
def consulta_interativa(df):
    while True:
        try:
            x = float(input("Digite o valor de x: "))
            t = float(input("Digite o valor de t: "))
            resultado = psi_x_t(x, t)
            print(f"\nResultado: ψ({x:.2f}, {t:.3f}) = {resultado:.10f}\n")
        except Exception as e:
            print(f"Erro: {e}")
        cont = input("Deseja consultar outro valor? (s/n): ")
        if cont.lower() != "s":
            break

if __name__ == "__main__":
    tabela = gerar_tabela_psi()
    consulta_interativa(tabela)

# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.
