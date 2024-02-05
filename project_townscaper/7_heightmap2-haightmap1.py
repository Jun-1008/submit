import csv

list_XY = []
heightmap_array = []

with open ('fig7a_vs.csv', 'w', newline='') as f0: #書き込み用csv
    writer = csv.writer(f0)

    with open ('fig7a_s2.csv', 'r') as f1: # x,y
        line1 = csv.reader(f1)
        for row1 in line1:

            with open ('fig7a.csv', 'r') as f2: # x,y
                line2 = csv.reader(f2)
                for row2 in line2:

                    if row1[0:2] == row2[0:2]:
                        heightmap_array = [row1[0], row1[1], row1[2], row2[2]] # シンハイトマップのx, y, h とそれに対応するハイトマップのh
                        writer.writerow(heightmap_array)
                        print(heightmap_array)