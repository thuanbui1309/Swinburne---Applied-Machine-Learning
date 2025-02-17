import os
import shutil

type = "train"
with open(f"data/{type}.txt", "r") as file:
    dat = file.readlines()

    for line in dat:
        line = line.strip().split(" ")
        if not os.path.exists(f"data/{type}/{line[1]}"):
            os.mkdir(f"data/{type}/{line[1]}")

        # print(f"data/test/{line[0]}")
        shutil.move(f"data/{type}/{line[0]}", f"data/{type}/{line[1]}")