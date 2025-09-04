import pandas as pd
import matplotlib.pyplot as plt


PATH = 'D:/qtdepths.csv'
video_order = [
    'BasketballDrill',
    'BQMall',
    'PartyScene',
    'RaceHorsesC',
    'BasketballDrive',
    'BQTerrace',
    'Cactus',
    'MarketPlace',
    'CatRobot',
    'DaylightRoad2',
    'ParkRunning3',
    'Campfire',
    'FoodMarket4',
    'Tango2'
]
# Ler CSV (troque para o nome do seu arquivo)
df = pd.read_csv(PATH, sep=";")

df["Inter_ratio"] = df["Inter"] / df["Total"]

mean_df = df.groupby(["Config", "Video"], as_index=False)["Inter_ratio"].mean()
mean_df["Video"] = pd.Categorical(mean_df["Video"], categories=video_order, ordered=True)
mean_df = mean_df.sort_values("Video")

configs_ordem = ["slower", "slow", "medium", "fast", "faster"]

for config in configs_ordem:
    dados_config = mean_df[mean_df["Config"] == config]
    plt.figure(figsize=(10, 5))
    plt.bar(dados_config["Video"], dados_config["Inter_ratio"], edgecolor="black", linewidth=1.2)
    plt.ylim(0, 1)  # pois é uma proporção
    plt.title(f"Inter/Total médio - {config}")
    plt.ylabel("Inter/Total")
    plt.xlabel("Vídeo")
    plt.xticks(rotation=90, ha="right")
    plt.tight_layout()
    plt.savefig(f"grafico_{config}.png", dpi=300)
    plt.close()

print("Gráficos salvos!")