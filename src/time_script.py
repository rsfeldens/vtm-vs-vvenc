import matplotlib as plt
import numpy as np
import pandas as pd 

TIMEFILES_FOLDER = 'C:/Users/Rodrigo/Documents/time-profiles'

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

inter_per_total = []

for video in VIDEOS:
    for qp in QPs:
        for config in CONFIGS:
            encoder_time = 0
            inter_time = 0
            for i in range(5):
                filename = f"{TIMEFILES_FOLDER}/{video[0]}_{qp}_{config[0]}_{i}.csv"
                if filename == f"{TIMEFILES_FOLDER}/Tango2_22_faster_2.csv":
                    continue
                df = pd.read_csv(filename, sep=';')
                encoder_time += df.loc[df['Stage'] == 'ENCODER', 'Time(ms)'].values[0]
                inter_time += df.loc[df['Stage'] == 'INTER', 'Time(ms)'].values[0]
            if video[0] == "Tango2" and qp == 22 and config[0] == 'faster':
                encoder_time /= 4
                inter_time /= 4
            else:
                encoder_time /= 5  
                inter_time /= 5
            print(f"{video[0]},{qp},{config[0]},{encoder_time},{inter_time}")
            inter_per_total.append(inter_time / encoder_time * 100)

print(f"Average inter per total: {np.mean(inter_per_total)}%")