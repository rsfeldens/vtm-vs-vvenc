import matplotlib as plt
import numpy as np
import pandas as pd 

TRACEFILES_FOLDER = 'C:/Users/Rodrigo/Documents/tracefiles'

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

for video in VIDEOS:
    for qp in QPs:
        for config in CONFIGS:
            filename = f"./{video[0]}_{qp}_{config[0]}.csv"
