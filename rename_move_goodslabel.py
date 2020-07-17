# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET
import shutil
import random

def listdir(path):
    jpg_name = []
    xml_name = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.jpg':
            jpg_name.append(file)
        elif os.path.splitext(file)[1] == '.xml':
            xml_name.append(file)
    if len(jpg_name) == len(xml_name):
        return jpg_name, xml_name
    else:
        print("there is empty image with no xml file")
        print(len(jpg_name))
        print(len(xml_name))


def move_change_label(path ,jpg_name, xml_name):
    i = 100000
    j = 100000
    for file in jpg_name:
        shutil.copy(path + "/" + file, "JPEGImages/" + str(i) + ".jpg")
        i += 1
    for file in xml_name:
        tree = ET.parse(path + "/" + file)
        root = tree.getroot()
        for object1 in root.findall('object'):
            for labels in object1.findall('name'):
                if (labels.text == "8019") or (labels.text == "8020"):
                    labels.text = "drinks"
                else:
                    labels.text = "goods"
                tree.write(path + "/" + file, encoding='utf-8')

        shutil.copy(path + "/" + file, "Annotation/" + str(j) + ".xml")
        j += 1

def txt_maker():
    num_list = []
    jpg_name = []
    for file in os.listdir("JPEGImages"):
        if os.path.splitext(file)[1] == '.jpg':
            jpg_name.append(file)
    picture_num = len(jpg_name)
    for i in range(100000, 100000 + picture_num):
        num_list.append(i)
    random.shuffle(num_list)
    train_rate = 0.7
    train_num = int(picture_num*train_rate)
    # val_num = picture_num - train_num
    # write train.txt
    f1 = open('Imagesets/Main/train.txt', 'w')
    for i in range(0, train_num):
        f1.write(str(num_list[i]) + "\n")
    f1.close()
    # write val
    f2 = open('Imagesets/Main/val.txt', 'w')
    for i in range(train_num, picture_num):
        f2.write(str(num_list[i]) + "\n")
    f2.close()
    # write test.txt
    f3 = open('Imagesets/Main/test.txt', 'w')
    for i in range(0, picture_num):
        f3.write(str(num_list[i]) + "\n")
    f3.close()




if __name__ == '__main__':
    path = "goodsphoto"
    jpg_name, xml_name = listdir(path)
    move_change_label(path, jpg_name, xml_name)
    txt_maker()