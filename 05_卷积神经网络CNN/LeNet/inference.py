# -*- coding: utf-8 -*-
# @Description : 该代码定义了LeNet模型的推断过程
# @File : inference.py
# @Time : 2022/3/26 16:21
# @Author : HarrisonWu42
# @Email: hangzhouwh@gmail.com
# @Software: PyCharm


import torch
import torch.nn as nn

from data import data_test_loader
from model import LeNet


# save_info = { # 保存的信息
#    "iter_num": iter_num,  # 迭代步数
#    "optimizer": optimizer.state_dict(), # 优化器的状态字典
#    "model": model.state_dict(), # 模型的状态字典
# }

model_path = "models/model.pth"  # 假设模型保存在model.pth文件中
save_info = torch.load(model_path)  # 载入模型
model = LeNet()  # 定义LeNet模型
criterion = nn.CrossEntropyLoss()  # 定义损失函数
model.load_state_dict(save_info["model"])  # 载入模型参数
model.eval()  # 切换模型到测试状态

test_loss = 0
correct = 0
total = 0
with torch.no_grad():  # 关闭计算图
    for batch_idx, (inputs, targets) in enumerate(data_test_loader):
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        test_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

        print(batch_idx, len(data_test_loader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
              % (test_loss / (batch_idx + 1), 100. * correct / total, correct, total))