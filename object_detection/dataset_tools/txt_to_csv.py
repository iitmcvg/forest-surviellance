import csv
import os
import glob

txt_path = '/home/keerthan/Documents/CVI/Experiments/object_detection/dataset/00001/groundTruth.txt'
txt_path2 = '/home/keerthan/Documents/CVI/Experiments/object_detection/dataset/00001/groundTruth2.txt'
csv_path = ''

"""
txt = open(txt_path,"r")
txt_w = open(txt_path2,"w")

reader = csv.reader(txt, delimiter='\n')

file_names = []
num_box = []
box_size = []

i=0
for row in reader:
    if(i>3):
        for k in range(len(row)):
            if(row[0][k]==" "):
                row[0][k] = ','
        txt_w.write(str(row[0][:]))
        txt_w.write('\n')
        #file_names.append(row[0][:13])
        #num_box.append(row[0][14])
    else:
        i+=1
"""
with open(txt_path,"r") as f:
    data = f.readlines()
words = []
for line in data:
    words.append(line.split())
print(words)