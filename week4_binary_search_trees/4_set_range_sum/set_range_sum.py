# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  left.parent = right
  update(right)
  return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)
  
def erase_1(x): 
  global root
  
  # base case: there is only x in the BST
  if root.key == x and not root.left and not root.right:
    root = None
    return root 

  result = find(root, x)
  found = result[0]
  
  # x is not in the tree
  if not found:
    return

  # x is not in the tree
  if found.key != x:
    return
  
  # finds successor and splays to the top
  result = find(root, x+1)
  successor = result[0]
  root = result[1]

  # splays predecssor to the root, such that its right child is its successor
  root = splay(found)
  # print('successor',successor)

  # promote successor to root
  l = found.left 
  r = found.right
  # print('l', found.left)
  # print('r', found.right)

  if not successor:
    # removing largest element -> does not have any right children
    l.parent = None 
    root = l
    
  else:
    # there exists a larger element -> promote it (the right child)
    r.left = l
    root = r 
    if r:
      r.parent = None
    if l:
      l.parent = r
    
  return x

def erase(x):
  global root

  # split the tree such that left subtree is < x, and right subtree is >= x
  (left, middle) = split(root, x)

  # make another split such that left subtree <= x, right subtree > x
  (middle, right) = split(root, x+1)
  
  # merge the left subtree of first split with right subtree of second split
  # this leaves out x if x was in the tree
  # update the root of the new tree
  root = merge(left, right)
  

def search(x): 
  global root
  
  # find(x) which also splays the node to the root
  (result, root) = find(root, x)

  # if x > all elements in the tree, find returns None
  if not result:
    return False

  # found x
  if result.key == x:
    return True
  
  # if x is not in the tree and x is not the largest, find(x) returns its predecessor i.e next(x)
  return False
  
def sum(fr, to): 
  global root

  # split tree such that left subtree < fr, right subtree >= fr
  (left, middle) = split(root, fr)
  update(middle)
  if middle:
    print('mid', middle.key, middle.sum)#, middle.right.key, middle.left)
  else:
    print('mid', middle)
  if left:
    print('left', left.key, left.sum)
  else:
    print('left', left)
  # split tree again, this time by the root of the right subtree from our first split
  # This splits such that left subtree >= fr and <= to, while the right subtree > to. The sum of the left subtree gives us our range sum
  (middle, right) = split(middle, to + 1)
  if middle:
    print('mid', middle.key, middle.sum,middle.right)
  else:
    print('mid', middle)
  if right:
    print('right', right.key, right.sum)
  else:
    print('right', right)
  # now merge the trees back. You have to respect the order, so first merge left and middle, then the result with right.
  res = 0 if not middle else middle.sum
  root = merge(merge(left, middle), right)
  
  return res



MODULO = 1000000001

n = int(f.readline())
last_sum_result = 0

for i in range(n):
  line = f.readline().split()
  
  if line[0] == '+':
    x = (int(line[1]) + last_sum_result) % MODULO
    insert(x)
    

  elif line[0] == '-':
    x = (int(line[1]) + last_sum_result) % MODULO
    erase(x)
   

  elif line[0] == '?':
    x = (int(line[1]) + last_sum_result) % MODULO
    print('Found' if search(x) else 'Not found')

  elif line[0] == 's':
    l = (int(line[1]) + last_sum_result) % MODULO
    r = (int(line[2]) + last_sum_result) % MODULO
    res = sum(l, r)
    last_sum_result = res % MODULO
    print(res)
  



  

# MODULO = 1000000001
# fn = r'week4_binary_search_trees\4_set_range_sum\tests\36'
# answer = fn + '.a'

# wrong_ans = []
# with open(fn, 'r') as f:
#   with open(answer, 'r') as a:

#     n = int(f.readline())
#     last_sum_result = 0

#     for i in range(n):
#       line = f.readline().split()
     
#       if line[0] == '+':
#         x = (int(line[1]) + last_sum_result) % MODULO
#         insert(x)
#         print('QUERY', i, line[0], x)

#       elif line[0] == '-':
#         x = (int(line[1]) + last_sum_result) % MODULO
#         erase(x)
#         print('QUERY', i, line[0], x)

#       elif line[0] == '?':
#         x = (int(line[1]) + last_sum_result) % MODULO
#         res = 'Found' if search(x) else 'Not found'
#         ans = a.readline().strip()
    
#         print('QUERY', i, line[0], x)
#         print(ans)
#         print(res, '\n')
       
#         if ans != str(res):
#           print("INCORRECT")
#           wrong_ans.append(i)
#           break
          

#       elif line[0] == 's':
#         l = (int(line[1]) + last_sum_result) % MODULO
#         r = (int(line[2]) + last_sum_result) % MODULO
#         res = sum(l, r)
#         last_sum_result = res % MODULO
      
#         ans = a.readline().strip()
      
#         print('QUERY', i, line[0], l, r)
#         print(ans)
#         print(res, '\n')
#         if ans != str(res):
#           print("INCORRECT")
#           wrong_ans.append(i)
#           while True:
            
#             print(root.left)
#             root = root.left
#             if not root.left:
#               break
#           while True:
#           break

#       if root:
#         print('\nroot:', root.key, '\n')
#       else:
#         print('\nempty tree\n')        
# print(wrong_ans)   
  
