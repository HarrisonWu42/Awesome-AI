# -*- coding: utf-8 -*-
# @Description : 该代码用于LeNet的训练数据集MNIST的载入
# @File : data.py
# @Time : 2022/3/26 16:21
# @Author : HarrisonWu42
# @Email: hangzhouwh@gmail.com
# @Software: PyCharm

from torchvision.datasets import MNIST
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

data_train = MNIST('D:/Workspace/data',
                   download=False,
                   transform=transforms.Compose([
                       transforms.Resize((32, 32)),
                       transforms.ToTensor()]))
data_test = MNIST('D:/Workspace/data',
                  train=False,
                  download=False,
                  transform=transforms.Compose([
                       transforms.Resize((32, 32)),
                       transforms.ToTensor()]))
# data_train_loader = DataLoader(data_train, batch_size=256, shuffle=True, num_workers=8) # default:num_workers=0
data_train_loader = DataLoader(data_train, batch_size=256, shuffle=True)
# data_test_loader = DataLoader(data_test, batch_size=1024, num_workers=8)
data_test_loader = DataLoader(data_test, batch_size=1024)

# MNIST数据集的展示
# if __name__ == '__main__':
#     figure = plt.figure()
#     num_of_images = 60
#     print(len(data_train_loader))
#     x = enumerate(data_train_loader)
#     y = list(x)
#     for imgs, targets in data_train_loader:
#         break
#     for idx, (a, b) in enumerate(data_train_loader):
#         print("idx: ", idx)
#         print("a:   ", a)
#         print("b:   ", b)
#         break
#
#     for idx in range(num_of_images):
#         plt.subplot(6, 10, idx + 1)
#         plt.axis('off')
#         img = imgs[idx, ...]
#         plt.imshow(img.numpy().squeeze(), cmap='gray_r')
#
#     plt.show()