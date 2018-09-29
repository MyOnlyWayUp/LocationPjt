#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:35:30 2018

@author: nlp
"""

import difflib
import sys
sys.setrecursionlimit(1000)


def Merge(F_list, T_list, F_i, T_i):
    if F_i>=len(F_list) or T_i>=len(T_list):
        return F_list
    else:
        if F_list[F_i] != T_list[T_i]:
            F_list.insert(F_i, T_list[T_i])
            #F_i += 1
            print("F_list: ", F_list)
            if T_i + 1 < len(T_list):
                T_i += 1
                while(T_list[T_i] != F_list[F_i]):
                    F_i += 1
                return Merge(F_list, T_list,F_i+1, T_i+1)
        else:
            return Merge(F_list, T_list,F_i+1, T_i+1)
    
def Del(F_list, T_list, F_i):
    if F_i == len(T_list):
        return F_list
    else:
        maxSim = difflib.SequenceMatcher(None, F_list, T_list).quick_ratio()
        print(maxSim)
        if(difflib.SequenceMatcher(None, F_list[:F_i]+F_list[F_i+1:], T_list).quick_ratio()>maxSim):
            del(F_list[F_i])
            print("F_list: ", F_list)
            F_i -= 1
        return Del(F_list, T_list, F_i+1)
        
        
if __name__ == '__main__':
    F_list = '上海市浦东我饿区'
    T_list = '上海市浦东新区'
    F_list = list(F_list)
    T_list = list(T_list)
    
    resMerge = Merge(F_list, T_list, 0, 0)
    resDel = Del(resMerge, T_list, 0)
    print("result: ", resDel)
    