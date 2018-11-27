import os
import glob
import pandas as pd
import csv
import shutil

csv_from = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation/animal_labels2.csv'
csv_to = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation/animal_labels2_new.csv'

'''
with open(csv_from,'r') as in_file, open(csv_to,'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    i=0
    for line in in_file:
        if line in seen: 
            continue # skip duplicate
        seen.add(line)
        out_file.write(line)
        i+=1
    print("Written %d records",i)
'''
def count_pairs(csv_from):
    file_csv_from = open(csv_from,"r")
    file_csv_to = open(csv_to,"w")
    reader = csv.reader(file_csv_from, delimiter=',')
    writer = csv.writer(file_csv_to)
    row_prev = []
    row_curr = []
    k=0
    i=0
    for row in reader:
        if len(row_prev)== 0:
            row_prev.append(str(row[0]))
            writer.writerow(row)
        else:
            row_curr.append(str(row[0]))
            if row_prev[0] != row_curr[0]:
                i+=1
                writer.writerow(row)
            row_prev = []
            row_prev.append(str(row[0]))
            row_curr = []
    file_csv_from.close()
    file_csv_to.close()
    print("We have found moved ",i," rows")

count_pairs(csv_from)

    