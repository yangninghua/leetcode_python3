#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#  File: /Users/king/Python初级算法/code/2/mergeSort.py
#  Project: /Users/king/Python初级算法/code/2
#  Created Date: 2018/10/26
#  Author: hstking hst_king@hotmail.com


from randomList import randomList
import timeit

iList = randomList(20)

def mergeSort(iList):
    if len(iList) <= 1:
        return iList
    middle = len(iList)//2
    left, right = iList[0:middle], iList[middle:]
    return mergeList(mergeSort(left), mergeSort(right))

def mergeList(left, right):
    mList = []
    while left and right:
        if left[0] >= right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))
    while left:
        mList.append(left.pop(0))
    while right:
        mList.append(right.pop(0))
    return mList


if __name__ == "__main__":
    print(iList)
    print(mergeSort(iList))
    print(timeit.timeit("mergeSort(iList)", "from __main__ import mergeSort,iList", number=100))