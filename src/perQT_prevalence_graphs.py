import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
PATH = 'D:/qtdepths.csv'
videos = [
    ["BasketballDrill", "BQMall", "PartyScene", "RaceHorsesC"],
    ["BasketballDrive", "BQTerrace", "Cactus", "MarketPlace"],
    ["CatRobot", "DaylightRoad2", "ParkRunning3"],
    ["Campfire", "FoodMarket4", "Tango2"]
]
qps = [22, 27, 32, 37]
qt_cols = ["QT_Depth=0", "QT_Depth=1", "QT_Depth=2", "QT_Depth=3", "QT_Depth=4"]

df = pd.read_csv(PATH, sep=";")
df = df[(df["Video"].isin(videos[3])) & (df["Config"] == "medium")]

df_grouped = df.groupby("QP")[qt_cols + ["Inter"]].mean()

df_percent = df_grouped[qt_cols].div(df_grouped["Inter"], axis=0) * 100

qt_0 = df_percent["QT_Depth=0"].values
qt_1 = df_percent["QT_Depth=1"].values
qt_2 = df_percent["QT_Depth=2"].values
qt_3 = df_percent["QT_Depth=3"].values
qt_4 = df_percent["QT_Depth=4"].values

bottom2 = np.add(qt_4, qt_3)
bottom3 = np.add(bottom2, qt_2)
bottom4 = np.add(bottom3, qt_1)

plt.figure(figsize=(8, 6))  
plt.bar(qps, qt_4, width=2, color='#0A2040', edgecolor='black', linewidth=0.9)
plt.bar(qps, qt_3, width=2, bottom=qt_4, color='#114470', edgecolor='black', linewidth=0.9)
plt.bar(qps, qt_2, width=2, bottom=bottom2, color='#1B5D92', edgecolor='black', linewidth=0.9)
plt.bar(qps, qt_1, width=2, bottom=bottom3, color='#71ACD9', edgecolor='black', linewidth=0.9)
plt.bar(qps, qt_0, width=2, bottom=bottom4, color='#BFD7EA', edgecolor='black', linewidth=0.9)
plt.xticks(qps)
plt.title("Distribuição QT (%) - class_A1")
plt.xlabel("QP")
plt.ylabel("% da Inter")
plt.legend()
plt.show()