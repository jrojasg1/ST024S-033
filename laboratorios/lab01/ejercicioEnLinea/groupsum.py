# -*- coding: utf-8 -*-
"""groupsum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1thJhTTDg-6nICXbxwf7kkBJdwZhIbBT8
"""

def groupSum(start,nums,target):
  numsarray = []
  longitud = len(nums)
  for i in range(0,longitud):
    numsarray.append(int(nums[i:i+1]))
    
    groupSumAux(start,numsarray,target)

def groupSumAux(start,nums,target):

  if start >= len(nums):
    return False
  if groupSumAux(start + 1, nums, target - nums[start]):
    return True
  if groupSumAux(start + 1, nums, target):
    return True

print(groupSum(0,"245",10))