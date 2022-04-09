# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:40:13 2022

@author: yus
"""

'''
Goal: To calcuate the score for the owner below and rank them accordingly
'''

owner = {
    'Jack': ['A','I','G','I'],
    'Mary': ['W','P','J','T'],
    'Tom': ['Q','R','M','D'],
    'Jade': ['Z','Z','Z','Z']
    }

letter_type = {
      'Type 1': ['A','B','C','D','E','F','G'],
      'Type 2': ['H','I','J','K','L','M','N'],
      'Type 3': ['O','P','Q','R','S','T'],
      'Type 4': ['U','V','W','X','Y','Z']
    }

Type_score = {
    'Type 1': 1,
    'Type 2': 2,
    'Type 3': 3,
    'Type 4': 4
    }

#Need to regroup the owner dictionary so similar group could be together



def regroup_owner(dic):
    res = {}
    for key, value in dic.items():
        for i in range(len(value)):   
            if key not in res:
                res[key] = {}
                res[key][value[i]] = 1
            elif value[i] not in  res[key].keys():
                #res[key] = {}
                res[key][value[i]] = 1
            else:
                res[key][value[i]] = res[key][value[i]] + 1
    return res


def letter_type_regroup():
    holder_dic = {}
    res = regroup_owner(dic)
    for key, value in letter_type.items():
        for key1, value1 in res.items():
            for inn_key, inn_value in value1.items():
                if key1 not in holder_dic and inn_key in value:
                    holder_dic[key1] = {}
                    holder_dic[key1][key] = inn_value
                elif key1 in holder_dic and inn_key in value and key not in holder_dic[key1].keys():
                    holder_dic[key1][key] = inn_value
                elif key1 in holder_dic and inn_key in value and key in holder_dic[key1].keys():
                    holder_dic[key1][key] = holder_dic[key1][key] + inn_value
    return holder_dic


def final_score():
    final_res = {}
    holder_dic = letter_type_regroup()
    for key, value in holder_dic.items():
        for inn_key, inn_value in value.items():
            if key not in final_res:
               final_res[key] =  Type_score[inn_key] * inn_value
            else:
               final_res[key] =  final_res[key] + Type_score[inn_key] * inn_value
               
    data_sorted = {k: v for k, v in sorted(final_res.items(), key=lambda x: x[1], reverse = True)}         
                
    return data_sorted