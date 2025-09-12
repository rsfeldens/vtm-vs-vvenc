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

header = ["Profile", "Video", "QP", "Inter", "Intra", "IME", "FME", "AME"]

with open("D:/results_trace.csv", mode='w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    writer.writerow(header)

for video in VIDEOS:
    for qp in QPs:
        for config in CONFIGS:
            filename = f"{TRACEFILES_FOLDER}/{video[0]}_{qp}_{config[0]}.csv"

            intra = inter =  0
            ime = fme = ame = 0


            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    line = line.split(";")
                    if line[0] != "BlockStat":
                        continue
                    if int(line[1]) > 32:
                        break
                    if "PredMode" in line:
                        if line[7] == '0':
                            inter += int(line[4]) * int(line[5])
                        if line[7] == '1':
                            intra += int(line[4]) * int(line[5])

                    if line[6] == "MVL0" or line[6] == "MVL1":
                        mv_x = int(line[7]) & 0b11
                        mv_y = int(line[8]) & 0b11
                        if mv_x == 0 and mv_y == 0:
                            ime += int(line[4]) * int(line[5])
                        else:
                            fme += int(line[4]) * int(line[5])

                    if line[6] == "AffineMVL0" or line[6] == "AffineMVL1":
                        ame += int(line[4]) * int(line[5])
                total = inter + intra
                inter_modes = ime + fme + ame
                inter = int(inter / total * 100)
                intra = int(intra / total * 100)
                ime = int(ime / inter_modes * 100)
                fme = int(fme / inter_modes * 100)
                ame = int(ame / inter_modes * 100)
                actual_line = [config[0], video[0], qp, inter, intra, ime, fme, ame]
                with open("D:/results_trace.csv", mode='a', newline='') as saida:
                    writer = csv.writer(saida, delimiter=';')
                    writer.writerow(actual_line)