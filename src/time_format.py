import matplotlib as plt
import numpy as np
import pandas as pd 
import os
import csv

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

header = ["Video", "QP", "Config", "QT_Depth=0", "QT_Depth=1", "QT_Depth=2", "QT_Depth=3", "QT_Depth=4", "Inter", "Total"]

with open("D:/times.csv", mode='w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    writer.writerow(header) 

for video in VIDEOS:
    for qp in QPs:
        for config in CONFIGS:
            encoder_time = 0
            inter_time = 0
            qt0 = 0
            qt1 = 0
            qt2 = 0
            qt3 = 0
            qt4 = 0
            for i in range(5):
                filename = f"{TIMEFILES_FOLDER}/{video[0]}_{qp}_{config[0]}_{i}.csv"
                if filename == f"{TIMEFILES_FOLDER}/Tango2_22_faster_2.csv":
                    continue
                df = pd.read_csv(filename, sep=';')
                encoder_time += df.loc[df['Stage'] == 'ENCODER', 'Time(ms)'].values[0]
                inter_time += df.loc[df['Stage'] == 'INTER', 'Time(ms)'].values[0]
                qt0 += df.loc[df['Stage'] == 'QT_0', 'Time(ms)'].values[0]
                qt1 += df.loc[df['Stage'] == 'QT_1', 'Time(ms)'].values[0]
                qt2 += df.loc[df['Stage'] == 'QT_2', 'Time(ms)'].values[0]
                qt3 += df.loc[df['Stage'] == 'QT_3', 'Time(ms)'].values[0]
                qt4 += df.loc[df['Stage'] == 'QT_4', 'Time(ms)'].values[0]
            if video[0] == "Tango2" and qp == 22 and config[0] == 'faster':
                encoder_time /= 4
                inter_time /= 4
                qt0 /= 4
                qt1 /= 4
                qt2 /= 4
                qt3 /= 4
                qt4 /= 4
            else:
                encoder_time /= 5  
                inter_time /= 5
                qt0 /= 5
                qt1 /= 5
                qt2 /= 5
                qt3 /= 5
                qt4 /= 5
            actual_line = [video[0], qp, config[0], qt0, qt1, qt2, qt3, qt4, inter_time, encoder_time]
            with open("D:/times.csv", mode='a', newline='') as saida:
                writer = csv.writer(saida, delimiter=';')
                writer.writerow(actual_line)