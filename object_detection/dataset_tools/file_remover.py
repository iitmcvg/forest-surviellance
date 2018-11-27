import os
import glob

def file_remove(path):
    for gif_file in glob.glob(path + '/*.gif'):
        os.remove(gif_file)

def main():
    data_dir = '/home/keerthan/Documents/CVI/google-images-download/google_images_download/fire_pics2/forest fire/'
    file_remove(data_dir)
    print("Successfully removed gifs")

main()