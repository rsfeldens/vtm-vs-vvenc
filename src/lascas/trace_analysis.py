import csv

TRACEFILES_FOLDER = 'D:/tracefiles'

VIDEOS = [
    #('BasketballDrive','BasketballDrive_1920x1080_50.yuv'),
    ('BQMall','BQMall_832x480_60.yuv'),
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

with open("D:/results_table.csv", mode='w', newline='') as output_file:
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
                    #if int(line[1]) > 32:
                    #    break
                    if "PredMode" in line:
                        if line[7] == '0':
                            inter += int(line[4]) * int(line[5])
                        if line[7] == '1':
                            intra += int(line[4]) * int(line[5])

                    if line[6] == "MVL0": #or line[6] == "MVL1":
                        mv_x = int(line[7]) & 0b11
                        mv_y = int(line[8]) & 0b11
                        if mv_x == 0 and mv_y == 0:
                            ime += int(line[4]) * int(line[5])
                        else:
                            fme += int(line[4]) * int(line[5])

                    if line[6] == "AffineMVL0":# or line[6] == "AffineMVL1":
                        ame += int(line[4]) * int(line[5])

                actual_line = [config[0], video[0], qp, inter, intra, ime, fme, ame]
                with open("D:/results_table.csv", mode='a', newline='') as saida:
                    writer = csv.writer(saida, delimiter=';')
                    writer.writerow(actual_line)