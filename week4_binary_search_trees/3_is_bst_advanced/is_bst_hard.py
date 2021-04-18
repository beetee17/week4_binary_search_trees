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





  
### FAILED ATTEMPTS

def IsBinarySearchTree(tree):
  
  # if the tree is empty, don't bother
  if not tree:
    return True

  # traverse in order and check if the resulting list is sorted
  # if it is, the tree has to be a binary search tree by definition (assuming no duplicates)
  traversal = inOrderTraversal(tree)
 
  if not traversal:
    return False

  return all(traversal[i] <= traversal[i + 1] for i in range(len(traversal)-1))

def inOrderTraversal(tree, node=0, result=[]):
  # tree is a list of lists, each inner list is a node in the form
  # (key, left_child_index, right_child_index)
  # tree[0] is the root

  if node == -1:
      return

  KEY = tree[node][0]
  LEFT_INDEX = tree[node][1]
  RIGHT_INDEX = tree[node][2]

  # check if duplicate is on wrong side of the parent node (must be on right side as per problem statement)
  if LEFT_INDEX != -1:
    if KEY == tree[LEFT_INDEX][0]:
      return []

  inOrderTraversal(tree, LEFT_INDEX, result)
  result.append(KEY)
  inOrderTraversal(tree, RIGHT_INDEX, result)

  return result


from queue import Queue

def breadthFirstTraversal(tree, node=0):
  # tree is a list of lists, each inner list is a node in the form
  # (key, left_child_index, right_child_index)
  # tree[0] is the root
  
  KEY = 0
  LEFT_INDEX = 1
  RIGHT_INDEX = 2

  result = []
  q = Queue(maxsize=len(tree))
  
  q.put_nowait(tree[node][KEY])
  

  while not q.empty():
    for i in range(q.qsize()):
      result.append(q.get_nowait())

    
    left_child_index = tree[node][LEFT_INDEX]
    if left_child_index != -1:
      q.put_nowait(tree[left_child_index][KEY])

    right_child_index = tree[node][RIGHT_INDEX]
    if right_child_index != -1:
      q.put_nowait(tree[right_child_index][KEY])
  
    node = left_child_index

  return result