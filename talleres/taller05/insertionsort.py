# -*- coding: utf-8 -*-
"""insertionsort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qi23Ez80ITGMk1G0Ktar0Qb7saUh2TRn
"""

def Insertion_sort(Vector):
    for i in range(1,len(Vector)):
        actual = Vector[i]
        j = i
        while j>0 and Vector[j-1]>actual:
            Vector[j]=Vector[j-1]
            j = j-1
        Vector[j]=actual
    print(Vector)

arr = ['ahj', 'aa', 'z', 'f', 'p'] 
Insertion_sort(arr)