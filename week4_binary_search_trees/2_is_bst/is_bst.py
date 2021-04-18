#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  
  # if the tree is empty, don't bother
  if not tree:
    return True

  # traverse in order and check if the resulting list is sorted
  # if it is, the tree has to be a binary search tree by definition (assuming no duplicates)
  traversal = inOrderTraversal(tree)

  return all(traversal[i] <= traversal[i + 1] for i in range(len(traversal)-1))

def inOrderTraversal(tree, node=0, result=[]):
  # tree is a list of lists, each inner list is a node in the form
  # (key, left_child_index, right_child_index)
  # tree[0] is the root
  KEY = 0
  LEFT = 1
  RIGHT = 2

  if node == -1:
      return
  
  inOrderTraversal(tree, tree[node][LEFT], result)
  result.append(tree[node][KEY])
  inOrderTraversal(tree, tree[node][RIGHT], result)

  return result



def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
