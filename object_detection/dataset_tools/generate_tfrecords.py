from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

'''
flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS
'''
output_path = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/train.record'

# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'n02472293':
        return 1
    elif row_label == 'n00015388' or row_label == 'n02152740':
        return 2
    else:
        None


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group,image_path):
    image_path_new = os.path.join(image_path, '{}'.format(group.filename)) + ".JPEG"
    with tf.gfile.GFile(image_path_new, 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'JPEG'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        #width = row['width']
        #height = row['height']
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    output_path = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/train.record'
    writer = tf.python_io.TFRecordWriter(output_path)
    '''
    Note :
        There are 3 image_path
        
        image_path1 = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/images/animal_train/n0015388_train'
        image_path2 = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/images/animal_train/n02152740_train'
        image_path3 = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/images/human_train'

        you might need to make a list of these image_paths
        image_path = [image_path3, image_path1, image_path2]

        or you can 'copy' all the training images that you have into a single directory(images_train)
    '''
    image_path = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/images_train'
    csv_input = '/home/keerthan/Documents/CVI/Experiments/object_detection/train_data/Annotation/final_detection_labels.csv'

    examples = pd.read_csv(csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group,image_path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = output_path
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()