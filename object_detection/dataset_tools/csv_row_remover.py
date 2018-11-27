import os
import csv

def row_remover(from_path,to_path):
    file_csv = open(from_path,"r")
    to_csv = open(to_path,"w")
    reader = csv.reader(file_csv, delimiter=',')
    writer = csv.writer(to_csv, delimiter=',')
    i=0
    k=0
    for row in reader:
        if i<3:
            i+=1
            continue
        else:
            writer.writerow(row)
    print("Successfully moved %d files",i-1)

def main():
    data_dir = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation'
    csv_path = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation/final_detection_labels (copy).csv'
    dest_path =  '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation/final_detection_labels2.csv'
    row_remover(csv_path,dest_path) 
    #num_files(final_dest)

main()