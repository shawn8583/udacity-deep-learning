import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
      exp_of_L = np.exp(L)
      sumExp_of_L = sum(exp_of_L)
      list = []
      for i in exp_of_L:
            list.append(i*1.0/sumExp_of_L)
      return list