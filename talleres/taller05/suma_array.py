# -*- coding: utf-8 -*-
"""Suma_array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bmmkG8t0nDmN2sOX9-zpJSFOgaud9msw
"""

def suma(arr):
  sum = 0
  for i in range(0,len(arr)):
    if arr[i] != None :
      sum += arr[i]
  print(sum)

arr = [12, 11, 13, 5, 6] 
suma(arr)