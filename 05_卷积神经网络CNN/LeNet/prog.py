# -*- coding: utf-8 -*-
# @Description : 通过命令行的方式来传递超参数，方便对网络进行超参数的调优
# @File : prog.py
# @Time : 2022/3/26 22:49
# @Author : HarrisonWu42
# @Email: hangzhouwh@gmail.com
# @Software: PyCharm


import argparse

# parser测试
# parser = argparse.ArgumentParser(description='Process some integer.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

# 在train.py 和 inference.py中加入各种超参数的选项来满足工程调参的需要
parser = argparse.ArgumentParser(description='PyTorch LeNet Training.')
parser.add_argument('--lr', default=0.01, type=float, help='Learning rate')
parser.add_argument('--batch-size', '-b', default=256, type=int, help='Batchsize')
args = parser.parse_args()
print(args)