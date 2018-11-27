import os
import glob
import pandas as pd
import csv
import shutil

final_dest = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/images/animal/new2/'

def file_move(path,csv_path):
    file_csv = open(csv_path,"r")
    reader = csv.reader(file_csv, delimiter=',')
    i=0
    k=0
    for row in reader:
        if k==0:
            k+=1
            continue
        else:
            file_name = row[0] + ".JPEG" 
            #print(file_name)
            try:
                image_path = os.path.join(path,'{}'.format(file_name))
                shutil.move(image_path, final_dest)
                
            except:
                pass
            i+=1
    print("Successfully moved %d files",i-1)

def num_files(path):
    directory = os.fsencode(path)
    k=0
    for files in os.listdir(directory):
        k+=1
    print("Number of files : ",k)

def main():
    data_dir = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/images/animal/n02152740/'
    csv_path = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation/animal_labels2_new.csv'
    file_move(data_dir,csv_path) 
    #num_files(final_dest)

main()