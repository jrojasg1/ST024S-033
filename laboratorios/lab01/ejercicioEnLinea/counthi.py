# -*- coding: utf-8 -*-
"""counthi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mx6Tk6tL4w3y_vg5BblZ4i3SOtXBidXu
"""

def counthi(str1):    
  cont = 0
  i = 0
  if len(str1)==0:
    return cont
  else:
    if str1[i:i+3] != "xhi" and str1[i+1:i+3] == "hi"  or str1[i:i+2] == "hi":
        cont +=1
  return cont + counthi(str1[i+2:])


counthi("ahibhi")