#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree():

  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right
    self.in_order = []
    self.flag = False


  def inOrder(self, tree=0):

    if tree == -1:
      return
    
    if self.left[tree] != -1:
      if self.key[tree] == self.key[self.left[tree]]:
        self.flag = True
        return

    self.inOrder(self.left[tree])
    self.in_order.append(self.key[tree])
    self.inOrder(self.right[tree])
  
  def isBST(self):
    # if the tree is empty, don't bother
    if not self.key:
      return True

    # traverse in order and check if the resulting list is sorted
    # if it is, the tree has to be a binary search tree by definition (assuming no duplicates)
    self.inOrder()
  
    if self.flag:
      return False

    return all(self.in_order[i] <= self.in_order[i + 1] for i in range(len(self.in_order)-1))


def main():
  nodes = int(sys.stdin.readline().strip())
 
  key = []
  left = []
  right = []

  for i in range(nodes):
   
    [a, b, c] = map(int, sys.stdin.readline().strip().split())
    key.append(a)
    left.append(b)
    right.append(c)

  tree = Tree(key, left, right)

  if tree.isBST():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
