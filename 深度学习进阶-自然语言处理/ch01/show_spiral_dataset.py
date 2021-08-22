# coding: utf-8
import sys
sys.path.append('..')  # 为了引入父目录的文件而进行的设定

import os
root_path = os.path.dirname(os.path.abspath(__file__))
previous_path = os.path.dirname(root_path)
sys.path.append(root_path)
sys.path.append(previous_path)

from dataset import spiral
import matplotlib.pyplot as plt


x, t = spiral.load_data()
print('x', x.shape)  # (300, 2)
print('t', t.shape)  # (300, 3)

# 绘制数据点
N = 100
CLS_NUM = 3
markers = ['o', 'x', '^']
for i in range(CLS_NUM):
    plt.scatter(x[i*N:(i+1)*N, 0], x[i*N:(i+1)*N, 1], s=40, marker=markers[i])
plt.show()
