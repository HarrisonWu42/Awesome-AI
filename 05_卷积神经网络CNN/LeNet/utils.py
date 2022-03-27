# -*- coding: utf-8 -*-
# @Description : 该代码定义了一些工程使用的工具脚本
# @File : utils.py
# @Time : 2022/3/26 16:21
# @Author : HarrisonWu42
# @Email: hangzhouwh@gmail.com
# @Software: PyCharm
from data import data_train_loader


def plot_mnist():
    import matplotlib.pyplot as plt
    figure = plt.figure()
    num_of_images = 60

    for imgs, targets in data_train_loader:
        break

    for index in range(num_of_images):
        plt.subplot(6, 10, index+1)
        plt.axis('off')
        img = imgs[index, ...]
        plt.imshow(img.numpy().squeeze(), cmap='gray_r')
    plt.show()