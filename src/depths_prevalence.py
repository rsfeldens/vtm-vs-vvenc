import matplotlib as plt
import numpy as np
import pandas as pd 
import os
import csv

TRACEFILES_FOLDER = 'D:/tracefiles'

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

with open("D:/qtdepths.csv", mode='w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    writer.writerow(header) 

for video in VIDEOS:
    for qp in QPs:
        for config in CONFIGS:
            filename = f"{TRACEFILES_FOLDER}/{video[0]}_{qp}_{config[0]}.csv"
            count_qtdepths = [0] * 5  # initialize counts for QT_Depth 0 to 4
            count_inter = 0
            count_total = 0
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    line = line.split(";")
                    if line[0] == "BlockStat" and "QT_Depth" in line:
                        actual_level = int(line[7])
                        for next_line in file:
                            next_line = next_line.strip()
                            next_line = next_line.split(";")
                            if "PredMode" in next_line:
                                count_total += int(next_line[4]) * int(next_line[5])
                                if next_line[7] == '0':
                                    if actual_level == 0:
                                        count_qtdepths[0] += int(next_line[4]) * int(next_line[5])
                                    elif actual_level == 1:
                                        count_qtdepths[1] += int(next_line[4]) * int(next_line[5])
                                    elif actual_level == 2:
                                        count_qtdepths[2] += int(next_line[4]) * int(next_line[5])
                                    elif actual_level == 3:
                                        count_qtdepths[3] += int(next_line[4]) * int(next_line[5])
                                    elif actual_level == 4:
                                        count_qtdepths[4] += int(next_line[4]) * int(next_line[5])
                                    break
                            else:
                                continue
                count_inter = sum(count_qtdepths)
                actual_line = [video[0], qp, config[0], count_qtdepths[0], count_qtdepths[1], count_qtdepths[2], count_qtdepths[3], count_qtdepths[4], count_inter, count_total]
                with open("D:/qtdepths.csv", mode='a', newline='') as saida:
                    writer = csv.writer(saida, delimiter=';')
                    writer.writerow(actual_line)