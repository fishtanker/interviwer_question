# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:42:44 2022

@author: yus
"""

sample = [['A', 1.00 ,'upload photo'],
        ['A',1.04, 'tag friends on photos'],
        ['A',1.05, 'upload photo'],
        ['A',1.07, 'add messages'],
        ['A',1.09, 'post photos'],
        ['B',2.02, 'upload photo'],
        ['B',2.04, 'tag friends on photos'],
        ['B',2.07, 'upload photo'],
        ['B',2.11, 'add messages'],
        ['B',2.15, 'post photos'],
        ]

sample_dic_list = [['A','upload photo', 2.99 ]]
sample_dic = {
            'upload photo': {
                             'A': [1.1, 1.02,1.15],
                             'B': [1.12,1.23,1.9]
                            },
            'tag friends on photos': {
                             'A': [1.3, 1.32,1.35],
                             'B': [1.42,1.43,1.49]
                            },
            'post photos': {
                             'A': [1.52, 1.79,1.95],
                             'B': [1.64,1.73,1.89]
                            }
    }

dic = {}

for i in range(len(sample)):
    if sample[i][2] not in dic:
        dic[sample[i][2]] = {}
        dic[sample[i][2]][sample[i][0]] = [sample[i][1]]
    elif  sample[i][0] in dic[sample[i][2]]:
        dic[sample[i][2]][sample[i][0]].append(sample[i][1])
    elif  sample[i][0] not in dic[sample[i][2]]:
        dic[sample[i][2]][sample[i][0]] = [sample[i][1]]