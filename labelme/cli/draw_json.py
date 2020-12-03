#!/usr/bin/env python

import argparse
<<<<<<< HEAD
import base64
import json
import os
import sys

import matplotlib.pyplot as plt

=======
import sys

import imgviz
import matplotlib.pyplot as plt

from labelme.label_file import LabelFile
>>>>>>> upstream/master
from labelme import utils


PY2 = sys.version_info[0] == 2


def main():
    parser = argparse.ArgumentParser()
<<<<<<< HEAD
    parser.add_argument('json_file')
    args = parser.parse_args()

    json_file = args.json_file

    data = json.load(open(json_file))

    if data['imageData']:
        imageData = data['imageData']
    else:
        imagePath = os.path.join(os.path.dirname(json_file), data['imagePath'])
        with open(imagePath, 'rb') as f:
            imageData = f.read()
            imageData = base64.b64encode(imageData).decode('utf-8')
    img = utils.img_b64_to_arr(imageData)

    label_name_to_value = {'_background_': 0}
    for shape in sorted(data['shapes'], key=lambda x: x['label']):
        label_name = shape['label']
=======
    parser.add_argument("json_file")
    args = parser.parse_args()

    label_file = LabelFile(args.json_file)
    img = utils.img_data_to_arr(label_file.imageData)

    label_name_to_value = {"_background_": 0}
    for shape in sorted(label_file.shapes, key=lambda x: x["label"]):
        label_name = shape["label"]
>>>>>>> upstream/master
        if label_name in label_name_to_value:
            label_value = label_name_to_value[label_name]
        else:
            label_value = len(label_name_to_value)
            label_name_to_value[label_name] = label_value
<<<<<<< HEAD
    lbl = utils.shapes_to_label(img.shape, data['shapes'], label_name_to_value)
=======
    lbl, _ = utils.shapes_to_label(
        img.shape, label_file.shapes, label_name_to_value
    )
>>>>>>> upstream/master

    label_names = [None] * (max(label_name_to_value.values()) + 1)
    for name, value in label_name_to_value.items():
        label_names[value] = name
<<<<<<< HEAD
    lbl_viz = utils.draw_label(lbl, img, label_names)
=======
    lbl_viz = imgviz.label2rgb(
        label=lbl,
        img=imgviz.asgray(img),
        label_names=label_names,
        font_size=30,
        loc="rb",
    )
>>>>>>> upstream/master

    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(lbl_viz)
    plt.show()


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> upstream/master
    main()
