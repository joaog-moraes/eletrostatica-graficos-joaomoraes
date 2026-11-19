import matplotlib.pyplot as plt

# Constantes físicas (mesmos valores do relatório em LaTeX)
k = 8.99e9   # N·m²/C²
q1 = 1e-6    # 1 µC
q2 = 1e-6    # 1 µC
Q = 1     # 1 C

# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
distancias = [0.10 + i * 0.01 for i in range(91)]
intensidade = [k * abs(Q) / (r ** 2) for r in distancias]


plt.figure(figsize=(6, 4))
plt.plot(distancias, intensidade, color="tab:blue", linewidth=2)
plt.title("Campo Elétrico vs. Distância (Lei de Coulomb)")
plt.xlabel("Distância r (m)")
plt.ylabel("Intensidade do Campo Elétrico E (N/C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("campo_eletrico.png", dpi=150)
print("Gráfico salvo em campo_eletrico.png!")
