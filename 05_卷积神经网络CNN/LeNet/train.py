# -*- coding: utf-8 -*-
# @Description : 该代码定义了LeNet模型的训练过程
# @File : train.py
# @Time : 2022/3/26 16:21
# @Author : HarrisonWu42
# @Email: hangzhouwh@gmail.com
# @Software: PyCharm


import torch
import torch.nn as nn
from torch import optim

from data import data_train_loader
from model import LeNet


model = LeNet()  # 定义LeNet模型
model.train()  # 切换模型到训练状态
lr = 0.01  # 定义学习率
criterion = nn.CrossEntropyLoss()   # 定义损失函数
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=5e-4)  # 定义随机梯度下降优化器

train_loss = 0
correct = 0
total = 0
epochs = 2

for iter_num in range(epochs):
    for batch_idx, (inputs, targets) in enumerate(data_train_loader):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, preedicted = outputs.max(1)
        total += targets.size(0)
        correct += preedicted.eq(targets).sum().item()

        print(batch_idx, len(data_train_loader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)' % (train_loss / (batch_idx + 1), 100. * correct / total, correct, total))

save_info = {   # 保存的信息
   "iter_num": iter_num,  # 迭代步数
   "optimizer": optimizer.state_dict(),  # 优化器的状态字典
   "model": model.state_dict(),  # 模型的状态字典
}
save_path = "models/model.pth"
torch.save(save_info, save_path)
