import xml.etree.ElementTree as ET 
import csv
from itertools import chain
k = 5 #解析したいcsvデータ番号。長時間
px_list = []



# with open ('.\\model2_SUS\\csv_data\\' + str(k) + 'x.csv', 'w', newline='') as f0:
with open ('.\\raw_data\\b5x.csv', 'w', newline='') as f0:
    writer = csv.writer(f0)
    # with open ('.\\model2_SUS\\csv_data\\' + str(k) + '.csv', 'r') as f2: #何さんから貰った方 y, x, h
    with open ('.\\raw_data\\b5.csv', 'r') as f2: #何さんから貰った方 y, x, h
        line2 = csv.reader(f2)
        for row2 in line2:
    
            with open ('pixel_xml.csv', 'r') as f1: #提供したデータ y,x,X,Y
                line1 = csv.reader(f1)
                
                for row1 in line1:
                    if row2[0:2] == row1[0:2]:
                        # px_list.append(row1[2:4])
                        # px_list = list(chain(row2[0:2], row1[2:4], row2[2:3])) #一致確認
                        px_list = list(chain(row1[2:4], row2[2:3])) #X, Y, h
                        writer.writerow(px_list)
                        print(px_list)
                        
                
                    # print(a_list)
            
        
                # l1 = [row for row in reader[1]]
                # for row in line:
                # l = [row for row in line]
