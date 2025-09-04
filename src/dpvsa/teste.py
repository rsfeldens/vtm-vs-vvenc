import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

velocidades = ["VTM","Slower", "Slow", "Medium", "Fast", "Faster"]
classes = ["A1", "A2", "B", "C"]
vtm = [83.70, 93.41, 93.625, 92.375] #qtdepths
#vtm = [27.25, 27.79, 26.375, 20.53] #times
slower = [0] * 4
slow = [0] * 4  
medium = [0] * 4
fast = [0] * 4
faster = [0] * 4

PATH = 'D:'
for i in range(4):
    df = pd.read_csv(f'{PATH}/qtdepths{classes[i]}.csv', sep=";")
    #df = pd.read_csv(f'{PATH}/times{classes[i]}.csv', sep=";")
    df["Inter_ratio"] = df["Inter"] / df["Total"] * 100
    slower[i] = df.loc[df["Config"] == "slower", "Inter_ratio"].mean()
    slow[i] = df.loc[df["Config"] == "slow", "Inter_ratio"].mean()
    medium[i] = df.loc[df["Config"] == "medium", "Inter_ratio"].mean()
    fast[i] = df.loc[df["Config"] == "fast", "Inter_ratio"].mean()
    faster[i] = df.loc[df["Config"] == "faster", "Inter_ratio"].mean()

values = np.array([
    vtm,
    slower,
    slow,
    medium,
    fast,
    faster
])
print(values)
colors = {"A1":"cornflowerblue", "A2":"goldenrod", "B":"mediumseagreen", "C":"indianred"}

# Posição das barras
x = np.arange(len(velocidades))  
bar_width = 0.2  

fig, ax = plt.subplots(figsize=(10,5))

for i, cls in enumerate(classes):
    ax.bar(
        x + i*bar_width,
        values[:, i],
        width=bar_width,
        label=cls,
        color=colors[cls],
        edgecolor="black",  # cor da borda
        linewidth=0.7        # espessura da borda
    )

# --- ADICIONE ESTE CÓDIGO ---
def to_percent(y, position):
    return f'{y:.0f}%'

formatter = FuncFormatter(to_percent)
ax.yaxis.set_major_formatter(formatter)
# --- FIM DO CÓDIGO A SER ADICIONADO ---


# Ajustes
ax.set_xticks(x + bar_width*1.5)
ax.set_xticklabels(velocidades)
##ax.set_ylabel("Valor")
#ax.set_ylabel("Porcentagem (%)") # Altere o rótulo do eixo Y para refletir a mudança
##ax.set_xlabel("Velocidade")
ax.legend(title="Class")
plt.savefig("overall_depths.png", dpi=300)
plt.close()
plt.show()