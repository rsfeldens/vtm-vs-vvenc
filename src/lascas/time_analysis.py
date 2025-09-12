import csv
import pandas as pd
TIMEFILES_FOLDER = 'D:/pred-time-profiles'
REPORTFILE_FOLDER = 'D:/vvenc-reports-time'
VIDEOS = [
    ('Tango2','Tango2_3840x2160_60fps_10bit_420.yuv'),
    ('FoodMarket4','FoodMarket4_3840x2160_60fps_10bit_420.yuv'),
    ('Campfire','Campfire_3840x2160_30fps_bt709_420_videoRange.yuv'),
    ('CatRobot','CatRobot_3840x2160_60fps_10bit_420_jvet.yuv'), 
    ('DaylightRoad2','DaylightRoad2_3840x2160_60fps_10bit_420.yuv'),
    ('ParkRunning3','ParkRunning3_3840x2160_50fps_10bit_420.yuv'),
    ('MarketPlace','MarketPlace_1920x1080_60fps_10bit_420.yuv'),
    #('RitualDance','RitualDance_1920x1080_60fps_10bit_420.yuv'),
    ('BasketballDrive','BasketballDrive_1920x1080_50.yuv'),
    ('Cactus','Cactus_1920x1080_50.yuv'),
    ('BQTerrace','BQTerrace_1920x1080_60.yuv'),
    ('RaceHorsesC','RaceHorsesC_832x480_30.yuv'),
    ('BQMall','BQMall_832x480_60.yuv'),
    ('PartyScene','PartyScene_832x480_50.yuv'),
    ('BasketballDrill','BasketballDrill_832x480_50.yuv'),
]

QPs = [22,27,32,37]

CONFIGS = [
    ('faster', 'randomaccess_faster.cfg'),
    ('fast', 'randomaccess_fast.cfg'),
    ('medium', 'randomaccess_medium.cfg'),
    ('slow', 'randomaccess_slow.cfg'),
    ('slower', 'randomaccess_slower.cfg')
]

header = ["Profile", "Video", "QP", "Inter", "Intra", "IME", "FME", "AME"]

with open("D:/results_times.csv", mode='w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    writer.writerow(header)

for video in VIDEOS:
    for qp in QPs:
        for config in CONFIGS:
            intra = inter =  0
            ime = fme = ame = 0
            total = 0
            for i in range(5):
                filename = f"{TIMEFILES_FOLDER}/{video[0]}_{qp}_{config[0]}_{i}.csv"
                filename2 = f"{REPORTFILE_FOLDER}/{video[0]}_{qp}_{config[0]}_{i}.report"
                df = pd.read_csv(filename, sep=';')
                inter += df.loc[df['Stage'] == 'INTER', 'Time(ms)'].values[0]
                intra += df.loc[df['Stage'] == 'INTRA', 'Time(ms)'].values[0]
                ime += df.loc[df['Stage'] == 'INTER_IME', 'Time(ms)'].values[0]
                fme += df.loc[df['Stage'] == 'INTER_FME', 'Time(ms)'].values[0]
                ame += df.loc[df['Stage'] == 'INTER_AME', 'Time(ms)'].values[0]
                
                with open(filename2, 'r') as arquivo:
                    for linha in arquivo:
                        if 'Total Time:' in linha:
                            partes = linha.split()
                            indice = partes.index('Time:')
                            valor_tempo = partes[indice + 1]
                            total += float(valor_tempo) * 1000
                        else:   
                            continue
            inter /= 5
            intra /= 5
            ime /= 5
            fme /= 5
            ame /= 5
            total /= 5
            inter_modes = ime + fme + ame
            inter = int(inter / total * 100)
            intra = int(intra / total * 100)
            ime = int(ime / inter_modes * 100)
            fme = int(fme / inter_modes * 100)
            ame = int(ame / inter_modes * 100)
            actual_line = [config[0], video[0], qp, inter, intra, ime, fme, ame]
            with open("D:/results_times.csv", mode='a', newline='') as saida:
                writer = csv.writer(saida, delimiter=';')
                writer.writerow(actual_line)