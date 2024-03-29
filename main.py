"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024/1/3 22:04
 @Author  : Ivan Mao
 @File    : main.py
 @Description : 
"""
import torch
from itertools import product

from model.DigitRecognizerNN import DigitRecognizerNN
from pipeline import process_data, trainer, validater

# Instantiate the model and move it to the device (CPU or GPU)
# device = torch.device(torch.device("cuda") if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")

"""Train the model"""
# train_dataloader, train_labels_tensor = process_data(type='train', argument=False, trans=False)
# trainer(train_dataloader, 'drnn', device, mark='origin')

# for model, mark in product(['cnn', 'drnn'], ['origin', 'augment','normal']):
#     print(model, mark)
#     if mark== 'origin':
#         train_dataloader, train_labels_tensor = process_data(type='train', augment=False, trans=False)
#     elif mark=='augment':
#         train_dataloader, train_labels_tensor = process_data(type='train', augment=True, trans=True)
#     else:
#         train_dataloader, train_labels_tensor = process_data(type='train', augment=False, trans=True)
#     trainer(train_dataloader, model, device, mark=mark)

"""Test the model"""
# test_dataloader, test_labels_tensor = process_data(type='test', augment=False, trans=True)
# validater(device, test_dataloader)
for model in ['CNN', 'DigitRecognizerNN']:
    model = torch.load(f'./checkpoint/{model}_cuda_augment.pth')
    print(model)



