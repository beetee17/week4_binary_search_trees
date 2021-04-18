# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

    self.in_order = []
    self.pre_order = []
    self.post_order = []

  def inOrder(self, tree=0):

    if tree == -1:
      return
    
    self.inOrder(self.left[tree])
    self.in_order.append(self.key[tree])
    self.inOrder(self.right[tree])

   

  def preOrder(self, tree=0):
    if tree == -1:
      return
    
    self.pre_order.append(self.key[tree])
    self.preOrder(self.left[tree])
    self.preOrder(self.right[tree])
   

  def postOrder(self, tree=0):
    if tree == -1:
      return
    
    self.postOrder(self.left[tree])
    self.postOrder(self.right[tree])
    self.post_order.append(self.key[tree])

def main():
  
  tree = TreeOrders()
  tree.read()
  tree.inOrder()
  tree.preOrder()
  tree.postOrder()
    
  print(" ".join(str(x) for x in tree.in_order))
  print(" ".join(str(x) for x in tree.pre_order))
  print(" ".join(str(x) for x in tree.post_order))

threading.Thread(target=main).start()

# 5
# 4 1 2
# 2 3 4
# 5 -1 -1
# 1 -1 -1
# 3 -1 -1